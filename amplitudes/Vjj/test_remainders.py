import mpmath
import numpy
import pytest

from pathlib import Path

from pentagon_functions import evaluate_pentagon_functions, PentagonMonomial

from antares.terms.vs_basis import load_basis, evaluate_basis

from linac.sparse_matrix_tools import matrix_from_plain_txt_coo

from .momenta import oPs
from .target_values import target_values


this_script_path = Path(__file__).resolve().parent

ampparts = ['quarkspm', 'quarksmp', 'gluonspp', 'gluonspm', 'gluonsmp']
loops = [0, 1, 2]

partial_amplitudes = [
    (amppart, loop, nf)
    for amppart in ampparts
    for loop in loops
    for nf in range(loop + 1)
]


@pytest.mark.parametrize(
    "amppart, loop, nf", partial_amplitudes
)
def test_Vjj_helicity_remainder(amppart, loop, nf):

    if amppart in ["quarkspm", "quarksmp"]:
        merged_vs = "qQQqll/nmhv/"
    elif amppart in ["gluonspp"]:
        merged_vs = "qggqll/mhv/"
    elif amppart in ["gluonspm", "gluonsmp"]:
        merged_vs = "qggqll/nmhv/"

    rational_basis = load_basis(this_script_path / merged_vs, 6, verbose=True)
    rational_matrix_tree = matrix_from_plain_txt_coo(this_script_path / merged_vs / f"{amppart}_tree")

    mpmath.mp.dps = 16

    if "pp" in amppart or "pm" in amppart:
        numerical_rational_basis = numpy.array(evaluate_basis(rational_basis, oPs))
    elif "mp" in amppart:
        numerical_rational_basis = numpy.array(evaluate_basis(rational_basis, oPs.image(("132456", False))))
    else:
        raise Exception(f"amppart {amppart} not undersood")

    with open(this_script_path / merged_vs / "basis_transcendental", "rb") as f:
        content = f.readlines()

    numerical_tree = (numerical_rational_basis @ rational_matrix_tree)[0]

    if loop == 0:

        numerical_finite_remainder = numerical_tree

    else:

        pentagon_functions = [PentagonMonomial(entry) for entry in content]
        pentagon_monomials = list(set([pentagon for pentagon_monomial in pentagon_functions
                                       for pentagon in pentagon_monomial.distinct_elements()]))

        evaluated_pentagon_monomials = evaluate_pentagon_functions(pentagon_monomials, oPs.image(("654321", False)),
                                                                   pentagon_function_set='m1', precision="d", number_of_cores=4)

        rational_matrix = matrix_from_plain_txt_coo(this_script_path / merged_vs / f"{amppart}_{loop}L_Nf{nf}")

        pentagon_basis = [PentagonMonomial(entry) for entry in pentagon_functions]
        numerical_pentagon_basis = [entry.subs(evaluated_pentagon_monomials) for entry in pentagon_basis]

        numerical_finite_remainder = (numerical_rational_basis @ rational_matrix @ numerical_pentagon_basis) / numerical_tree

    error = abs(target_values[(amppart, loop, nf)] - complex(numerical_finite_remainder))

    assert numpy.isclose(target_values[(amppart, loop, nf)], complex(numerical_finite_remainder)), f"Error: {error}"