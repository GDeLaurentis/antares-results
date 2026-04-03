import numpy
import pytest
from importlib import import_module

from pathlib import Path

from pentagon_functions import evaluate_pentagon_functions, PentagonMonomial
from linac.sparse_matrix_tools import matrix_from_plain_txt_coo

from .momenta import oPs, oPs5pt
from .target_values import target_values


this_script_path = Path(__file__).resolve().parent

test_cases = [
    pytest.param(channel, partial, id=f"{channel}-{partial}")
    for channel, entries in target_values.items()
    for partial in entries
]


@pytest.mark.parametrize("channel, partial", test_cases)
def test_Hjj_HTL_helicity_remainder(channel, partial):
    """Test the numerical evaluation of the Hjj HTL remainders against cached values, run with pytest."""
    target = target_values[channel][partial]
    helicity = partial.split("_")[0]

    representative_helicity = helicity
    if channel == 'ggggH' and helicity == 'pmpm':
        representative_helicity = 'ppmm'
    elif channel == 'uubggH' and helicity == 'pmmp':
        representative_helicity = 'pmpm'
    elif channel == 'uubddbH' and helicity == 'pmmp':
        representative_helicity = 'pmpm'

    module = import_module(f".HTL.{channel}.{representative_helicity}", package=__package__)
    lTerms = module.lTerms

    with open(this_script_path / "HTL" / channel / "basis_transcendental.txt", "r") as f:
        basis_transcendental = f.readlines()
    basis_transcendental = [PentagonMonomial(entry.replace("\n", "")) for entry in basis_transcendental]

    pentagon_functions = basis_transcendental
    pentagon_monomials = list(set([pentagon for pentagon_monomial in pentagon_functions
                                   for pentagon in pentagon_monomial.distinct_elements()]))

    evaluated_pentagon_monomials = evaluate_pentagon_functions(
        pentagon_monomials, oPs.image(("654321", False)),
        pentagon_function_set='m1', precision="d", number_of_cores=4)

    pentagon_basis = basis_transcendental
    numerical_pentagon_basis = [entry.subs(evaluated_pentagon_monomials) for entry in pentagon_basis]

    rref = matrix_from_plain_txt_coo(this_script_path / "HTL" / channel / representative_helicity / f"matrix_{partial}")

    permutation = ('12345', False)
    if channel == 'ggggH' and helicity == 'pmpm':
        permutation = ('13245', False)
    elif channel == 'uubggH' and helicity == 'pmmp':
        permutation = ('12435', False)
    elif channel == 'uubddbH' and helicity == 'pmmp':
        permutation = ('12435', False)

    oPs5ptPerm = oPs5pt.image(permutation)
    num_eval = lTerms(oPs5ptPerm) @ rref @ numpy.array(numerical_pentagon_basis)
    assert numpy.isclose(target, complex(num_eval)), f"Failed, target: {target}, got: {complex(num_eval)}."
