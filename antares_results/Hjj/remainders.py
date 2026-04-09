import numpy
from importlib import import_module
from pathlib import Path

from pentagon_functions import evaluate_pentagon_functions, PentagonMonomial
from linac.sparse_matrix_tools import matrix_from_plain_txt_coo

this_script_path = Path(__file__).resolve().parent


def remainder(channel, partial, phase_space_point, semi_numerical=False, as_dict=False, mu2=1):
    oPs = phase_space_point
    helicity = partial.split("_")[0]

    if len(oPs) == 6:
        oPs5pt = oPs.cluster([[1, ], [2, ], [3, ], [4, ], [5, 6]])
        oPs5pt[5]._r_sp_d = oPs5pt[5]._l_sp_d = oPs5pt[5]._r_sp_u = oPs5pt[5]._l_sp_u = None
    else:
        oPs5pt = oPs
    if oPs.field in ['finite field', 'padic', 'Fp', 'Qp']:
        semi_numerical = True

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

    if not semi_numerical:
        pentagon_functions = basis_transcendental
        pentagon_monomials = list(set([pentagon for pentagon_monomial in pentagon_functions
                                       for pentagon in pentagon_monomial.distinct_elements()]))

        evaluated_pentagon_monomials = evaluate_pentagon_functions(
            pentagon_monomials, oPs.image(("654321", False)), mu2=mu2,
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

    if not semi_numerical:
        num_eval = lTerms(oPs5ptPerm) @ rref @ numpy.array(numerical_pentagon_basis)
        return num_eval

    semi_num_result = [(a, b) for a, b in zip(lTerms(oPs5ptPerm) @ rref, basis_transcendental) if a != 0]
    if as_dict:
        return dict([(b, a) for a, b in semi_num_result])
    else:
        return semi_num_result
