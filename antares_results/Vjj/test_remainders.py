import mpmath
import numpy
import pytest

from pathlib import Path
from fractions import Fraction

from lips import Particles
from lips.tools import LeviCivita
from syngular import Field
from pyadic.primes import primes
from antares import Terms
from pentagon_functions import evaluate_pentagon_functions, PentagonMonomial
from antares.terms.lterms import TermsList

# from linac.sparse_matrix_tools import matrix_from_plain_txt_coo

from .momenta import oPs, oPsAllUp
from .target_values import target_values, polarized_target_values


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
    """Test the numerical evaluation of the Vjj remainders against cached values, run with pytest."""

    if amppart in ["quarkspm", "quarksmp"]:
        merged_vs = "qQQqll/nmhv/"
    elif amppart in ["gluonspp"]:
        merged_vs = "qggqll/mhv/"
    elif amppart in ["gluonspm", "gluonsmp"]:
        merged_vs = "qggqll/nmhv/"

    rational_basis = TermsList(this_script_path / merged_vs, 6, verbose=True)
    rational_matrix_tree = matrix_from_plain_txt_coo(this_script_path / merged_vs / f"{amppart}_tree")

    mpmath.mp.dps = 16

    if "pp" in amppart or "pm" in amppart:
        numerical_rational_basis = numpy.array(rational_basis(oPs))
    elif "mp" in amppart:
        numerical_rational_basis = numpy.array(rational_basis(oPs.image(("132456", False))))
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


@pytest.mark.parametrize(
    "amppart", ampparts
)
def test_Vjj_helicity_vs_spin_spinor_basis_functions(amppart):
    if amppart in ["quarkspm", "quarksmp"]:
        merged_vs = "qQQqll/nmhv/"
    elif amppart in ["gluonspp"]:
        merged_vs = "qggqll/mhv/"
    elif amppart in ["gluonspm", "gluonsmp"]:
        merged_vs = "qggqll/nmhv/"

    lTerms6pt = TermsList(this_script_path / merged_vs, 6, verbose=True)
    lTerms5pt = TermsList(this_script_path / merged_vs.replace('ll', 'V'), 6, verbose=True)

    oPsCheck6pt = Particles(6, field=Field("finite field", primes[-1], 1), seed=0)
    oPsCheck5pt = oPsCheck6pt.cluster([[1, ], [2, ], [3, ], [4, ], [5, 6], ], massive_spins=((5, ('d', 1), ('u', 2), ),))
    oPsCheck5ptAllUpDown = oPsCheck6pt.cluster([[1, ], [2, ], [3, ], [4, ], [5, 6], ], massive_spins=((5, ('u', all), ('d', all), ),))
    oPsCheck5ptAllDownUp = oPsCheck6pt.cluster([[1, ], [2, ], [3, ], [4, ], [5, 6], ], massive_spins=((5, ('d', all), ('u', all), ),))
    oPsCheck5ptAllUp = oPsCheck6pt.cluster([[1, ], [2, ], [3, ], [4, ], [5, 6], ], massive_spins=((5, ('u', all), ('u', all), ),))

    assert numpy.all(numpy.array(lTerms6pt(oPsCheck6pt)) * oPsCheck6pt("s_56") == lTerms5pt(oPsCheck5pt)), "Failed to match scalar evaluation back to six point result."

    # move this transpose to realign indices across the basis in the definition of TermsList.__call__ ?
    res = [entry if isinstance(lTerms5pt[i], Terms) or lTerms5pt[i][1] is False else entry.T for i, entry in enumerate(lTerms5pt(oPsCheck5ptAllDownUp))]
    res = [entry[0, 1] for entry in res]
    assert res == lTerms5pt(oPsCheck5pt), "Failed to match A_I=0^J=1 component back to scalar evaluation."

    resDownUp = [entry if isinstance(lTerms5pt[i], Terms) or lTerms5pt[i][1] is False else entry.T for i, entry in enumerate(lTerms5pt(oPsCheck5ptAllDownUp))]
    resAllUp = [entry if isinstance(lTerms5pt[i], Terms) or lTerms5pt[i][1] is False else entry.T for i, entry in enumerate(lTerms5pt(oPsCheck5ptAllUp))]
    assert all([numpy.all(-LeviCivita @ a == b) for a, b in zip(resDownUp, resAllUp)]), "Failed covariance check, raise left index."

    resUpDown = [entry if isinstance(lTerms5pt[i], Terms) or lTerms5pt[i][1] is False else entry.T for i, entry in enumerate(lTerms5pt(oPsCheck5ptAllUpDown))]
    resAllUp = [entry if isinstance(lTerms5pt[i], Terms) or lTerms5pt[i][1] is False else entry.T for i, entry in enumerate(lTerms5pt(oPsCheck5ptAllUp))]
    assert all([numpy.all(a @ LeviCivita == b) for a, b in zip(resUpDown, resAllUp)]), "Failed covariance check, raise right index."


@pytest.mark.parametrize(
    "amppart, loop, nf", partial_amplitudes
)
def test_Vjj_spin_spinor_remainder(amppart, loop, nf):
    if amppart in ["quarkspm", "quarksmp"]:
        merged_vs = "qQQqll/nmhv/"
    elif amppart in ["gluonspp"]:
        merged_vs = "qggqll/mhv/"
    elif amppart in ["gluonspm", "gluonsmp"]:
        merged_vs = "qggqll/nmhv/"

    rational_basis_6pt = TermsList(this_script_path / merged_vs, 6, verbose=True)
    rational_basis_5pt = TermsList(this_script_path / merged_vs.replace('ll', 'V'), 6, verbose=True)
    rational_matrix_tree = matrix_from_plain_txt_coo(this_script_path / merged_vs / f"{amppart}_tree")

    mpmath.mp.dps = 16

    if "pp" in amppart or "pm" in amppart:
        numerical_rational_basis_6pt = numpy.array(rational_basis_6pt(oPs))
        numerical_rational_basis_6pt_swapped_current = numpy.array(rational_basis_6pt(oPs.image(("123465", False))))
        numerical_rational_basis_5pt = numpy.array(rational_basis_5pt(oPsAllUp))
    elif "mp" in amppart:
        numerical_rational_basis_6pt = numpy.array(rational_basis_6pt(oPs.image(("132456", False))))
        numerical_rational_basis_6pt_swapped_current = numpy.array(rational_basis_6pt(oPs.image(("132456", False)).image(("123465", False))))
        numerical_rational_basis_5pt = numpy.array(rational_basis_5pt(oPsAllUp.image(("132456", False))))
    else:
        raise Exception(f"amppart {amppart} not undersood")

    with open(this_script_path / merged_vs / "basis_transcendental", "rb") as f:
        content = f.readlines()

    numerical_tree_6pt = (numerical_rational_basis_6pt @ rational_matrix_tree)[0]
    numerical_tree_5pt = numpy.einsum('xIJ,xy->IJ', numerical_rational_basis_5pt, rational_matrix_tree)
    assert numpy.isclose(complex(numerical_tree_6pt * oPs("s56")), numerical_tree_5pt.astype(complex)[1, 1]), "Failed to match tree."

    if loop == 0:

        numerical_finite_remainder_5pt = numerical_tree_5pt

    else:

        pentagon_functions = [PentagonMonomial(entry) for entry in content]
        pentagon_monomials = list(set([pentagon for pentagon_monomial in pentagon_functions
                                       for pentagon in pentagon_monomial.distinct_elements()]))

        evaluated_pentagon_monomials = evaluate_pentagon_functions(pentagon_monomials, oPs.image(("654321", False)),
                                                                   pentagon_function_set='m1', precision="d", number_of_cores=4)

        rational_matrix = matrix_from_plain_txt_coo(this_script_path / merged_vs / f"{amppart}_{loop}L_Nf{nf}")

        pentagon_basis = [PentagonMonomial(entry) for entry in pentagon_functions]
        numerical_pentagon_basis = [entry.subs(evaluated_pentagon_monomials) for entry in pentagon_basis]

        numerical_finite_remainder_5pt = numpy.einsum('xIJ,xy,y->IJ', numerical_rational_basis_5pt, rational_matrix, numpy.array(numerical_pentagon_basis))

    assert numpy.all(numpy.isclose(numerical_rational_basis_6pt.astype(complex), (numerical_rational_basis_5pt / oPs("s56")).astype(complex)[:, 1, 1])), \
        "Failed to match ε+ coeffs to 6pt"
    assert numpy.all(numpy.isclose(numerical_rational_basis_6pt_swapped_current.astype(complex), -(numerical_rational_basis_5pt / oPs("s56")).astype(complex)[:, 0, 0])), \
        "Failed to match ε- coeffs to 6pt"
    if loop != 0:  # match ε+ component (normalized by its tree) to the original target values in Table 5 of 2110.07541
        assert numpy.isclose(complex(numerical_finite_remainder_5pt[1, 1] / numerical_tree_5pt[1, 1]), target_values[(amppart, loop, nf)]), \
            "Failed to match A+ back to original"
    assert numpy.isclose(complex(numerical_finite_remainder_5pt[1, 1] / oPs("s56")), polarized_target_values[(amppart, loop, nf)]['ε+']), \
        "Failed to match A+ to target"
    assert numpy.isclose(complex(numerical_finite_remainder_5pt[0, 0] / oPs("s56")), polarized_target_values[(amppart, loop, nf)]['ε-']), \
        "Failed to match A- to target"
    assert numpy.isclose(complex((numerical_finite_remainder_5pt[0, 1] + numerical_finite_remainder_5pt[1, 0]) / oPs("s56")), polarized_target_values[(amppart, loop, nf)]['εL']), \
        "Failed to match AL to target"


# Function from linac (coming soon)

def matrix_from_coo(coo):
    """Converts a COO dictionary back to a numpy array."""
    rows = max([row for row, column in coo.keys()]) + 1
    columns = max([column for row, column in coo.keys()]) + 1
    matrix = numpy.zeros((rows, columns), dtype=object)
    for key in coo.keys():
        matrix[key] = coo[key]
    return matrix


def coo_from_plain_txt_coo(file_name, dtype=Fraction):
    """Loads coo from json containing coo dictionary."""
    with open(file_name, 'r') as f:
        lines = f.readlines()
    coo = {}
    for line in lines:
        key0, key1, val = line.split(" ")
        coo[(eval(key0), eval(key1))] = dtype(val)
    return coo


def matrix_from_plain_txt_coo(file_name, dtype=Fraction):
    """Loads coo from json containing coo dictionary."""
    coo = coo_from_plain_txt_coo(file_name, dtype=dtype)
    matrix = matrix_from_coo(coo)
    return matrix

# end of function from linac
