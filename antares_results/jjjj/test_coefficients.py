import numpy
import pytest

from pathlib import Path
from termcolor import colored

from antares.terms.terms import LoadResults

from .momenta import oPs
from .target_values import target_values


do_assertions = True
this_script_path = Path(__file__).resolve().parent


@pytest.mark.parametrize(
    "helicity, coeff_targets", target_values.items()
)
def test_independent_coefficients(helicity, coeff_targets):
    for coeff, target in coeff_targets.items():
        print(helicity, coeff)
        oTerms = LoadResults(f"{this_script_path}/gggggg/{helicity}/{coeff}")[0]
        actual = 0 if oTerms == 0 else complex(oTerms[0](oPs))
        print("actual: ", actual)
        print("target: ", target)
        if do_assertions:
            assert numpy.isclose(actual, target)
        else:
            if numpy.isclose(actual, target):
                print(colored("PASSED", "green"))
            else:
                print(colored("FAILED", "red"))
        print()
