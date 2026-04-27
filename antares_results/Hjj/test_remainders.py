import numpy
import pytest
import re
from multiset import Multiset
from importlib import import_module

from pathlib import Path

from pentagon_functions import PentagonMonomial

from .momenta import oPs, oPsFFCheck5pt
from .target_values import target_values
from .remainders import remainder


this_script_path = Path(__file__).resolve().parent

test_cases = [
    pytest.param(channel, partial, id=f"{channel}-{partial}")
    for channel, entries in target_values.items()
    for partial in entries
]

LOOP_PATTERN = re.compile(r"_(\d)L_")


@pytest.mark.parametrize("channel, partial", test_cases)
def test_Hjj_HTL_helicity_remainder(channel, partial):
    """Test the numerical evaluation of the Hjj HTL remainders against cached values, run with pytest."""
    target = target_values[channel][partial]
    match = LOOP_PATTERN.search(partial)
    loops = int(match.group(1))
    num_eval = remainder(channel, partial, oPs)
    assert numpy.isclose(target / 2 ** loops, complex(num_eval)), f"Failed, target: {target}, got: {complex(num_eval)}."


@pytest.mark.parametrize("channel, partial", test_cases)
def test_Hjj_HTL_FF_semi_numerical(channel, partial):
    """Test the numerical evaluation of the Hjj HTL remainders against cached values, run with pytest."""
    match = LOOP_PATTERN.search(partial)
    loops = int(match.group(1))

    module = import_module(f".FF_targets.HTL.{channel}.{partial}", package=__package__)
    doriginal = module.target_values
    dreloaded = remainder(channel, partial, oPsFFCheck5pt, semi_numerical=True, as_dict=True)
    # remove roots: targets were generated from Caravel while the roots were re-added afterwards
    dreloaded = {
        PentagonMonomial(dict([(key, val) for key, val in Multiset(pent).items() if not any(e in key for e in ['over', 'str', 'Sigma'])])): val
        for pent, val in dreloaded.items()
    }

    assert doriginal.keys() == dreloaded.keys(), f"Keys do not match, original: {doriginal.keys()}, reloaded: {dreloaded.keys()}"
    assert all([doriginal[key] == dreloaded[key] * 2 ** loops for key in doriginal.keys()]), f"Values do not match, original: {doriginal.values()}, reloaded: {dreloaded.values()}"
