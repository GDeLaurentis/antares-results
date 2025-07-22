import numpy
import pytest

from pathlib import Path
from termcolor import colored

from antares.terms.terms import LoadResults

from .momenta import oPsKCheck, oPsFFKCheck
from .target_values import target_values_red_C, target_values_red_FF, \
    target_values_pp_C, target_values_pp_FF, target_values_pm_C, target_values_pm_FF


do_assertions = True
this_script_path = Path(__file__).resolve().parent


@pytest.mark.parametrize(
    "coeff, target", target_values_red_C.items()
)
def test_ggHHH_reduction_coefficients_in_C(coeff, target):
    print(coeff)
    oTerms = LoadResults(f"{this_script_path}/ggHHH/{coeff}")[0]
    actual = 0 if oTerms == 0 else complex(oTerms[0](oPsKCheck))
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


@pytest.mark.parametrize(
    "coeff, target", target_values_red_FF.items()
)
def test_ggHHH_reduction_coefficients_in_FF(coeff, target):
    print(coeff)
    oTerms = LoadResults(f"{this_script_path}/ggHHH/{coeff}")[0]
    actual = 0 if oTerms == 0 else oTerms[0](oPsFFKCheck)
    print("actual: ", actual)
    print("target: ", target)
    assert actual == target


@pytest.mark.parametrize(
    "coeff, target", target_values_pp_C.items()
)
def test_ggHHH_pp_coefficients_in_C(coeff, target):
    print(coeff)
    oTerms = LoadResults(f"{this_script_path}/ggHHH/pp/{coeff}")[0]
    actual = 0 if oTerms == 0 else complex(oTerms[0](oPsKCheck))
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


@pytest.mark.parametrize(
    "coeff, target", target_values_pp_FF.items()
)
def test_ggHHH_pp_coefficients_in_FF(coeff, target):
    print(coeff)
    oTerms = LoadResults(f"{this_script_path}/ggHHH/pp/{coeff}")[0]
    actual = 0 if oTerms == 0 else oTerms[0](oPsFFKCheck)
    print("actual: ", actual)
    print("target: ", target)
    assert actual == target


@pytest.mark.parametrize(
    "coeff, target", target_values_pm_C.items()
)
def test_ggHHH_pm_coefficients_in_C(coeff, target):
    print(coeff)
    oTerms = LoadResults(f"{this_script_path}/ggHHH/pm/{coeff}")[0]
    actual = 0 if oTerms == 0 else complex(oTerms[0](oPsKCheck))
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


@pytest.mark.parametrize(
    "coeff, target", target_values_pm_FF.items()
)
def test_ggHHH_pm_coefficients_in_FF(coeff, target):
    print(coeff)
    oTerms = LoadResults(f"{this_script_path}/ggHHH/pm/{coeff}")[0]
    actual = 0 if oTerms == 0 else oTerms[0](oPsFFKCheck)
    print("actual: ", actual)
    print("target: ", target)
    assert actual == target
