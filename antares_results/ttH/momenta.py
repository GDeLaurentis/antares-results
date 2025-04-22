import numpy
import mpmath

from syngular import Field
from lips import Particles
from pyadic import FieldExtension

# Pseudo random FF point natively from lips
prime = 2 ** 31 - 19
field = Field("finite field", prime, 1)
seed = 0
oPs = Particles(8, field=field, seed=seed)
oPs._singular_variety(("⟨34⟩+[34]", "⟨34⟩-⟨56⟩", "⟨56⟩+[56]"), (1, 1, 1, ), seed=seed)
oPs.m_t = - oPs("⟨34⟩")
oPs.m_h = oPs.field.sqrt(oPs("s_78"))

assert oPs("⟨34⟩") == oPs("[43]") == oPs("⟨56⟩") == oPs("[65]")
assert not isinstance(oPs("<34>"), FieldExtension)

oPsFFKCheck = oPs.cluster([[1, ], [2, ], [3, 4], [5, 6], [7, 8]], massive_fermions=((3, 'u', 1), (4, 'd', 1)))


# Hardcoded KCheck point imported from MCFM
momenta = numpy.vectorize(mpmath.mpc)(numpy.array([
    [-0.3551079346745915E+01, -0.3551079346745915E+01, -0.0000000000000000E+00, 0.0000000000000000E+00],
    [-0.1224172214110815E+01, 0.1224172214110815E+01, -0.0000000000000000E+00, 0.0000000000000000E+00],
    [0.1673741180698765E+01, 0.1063984431702150E+01, 0.6966206550046100E+00, 0.6582127939225301E+00],
    [0.1928885468219350E+01, 0.5474475911732299E+00, -0.1068246753750290E+01, -0.1236497839678005E+01],
    [0.1172624911938610E+01, 0.7154751097597249E+00, 0.3716260987456795E+00, 0.5782850457554750E+00]
]))

oPsKCheck = Particles(5, field=Field("mpc", 0, 16))
oPsKCheck[1].four_mom = momenta[0]
oPsKCheck[2].four_mom = momenta[1]
oPsKCheck[3].four_mom = momenta[2]
oPsKCheck[4].four_mom = momenta[3]
oPsKCheck[5].four_mom = momenta[4]

# top states
oPsKCheck[3]._r_sp_u = numpy.vectorize(mpmath.mpc)(numpy.array([[(0.15754139214464724 + 0.19798867440882467j), (0.32572088288936740 - 0.64719402886667221j)]]))
oPsKCheck[3]._l_sp_d = numpy.vectorize(mpmath.mpc)(numpy.array([[(1.3442469155889438), (0.73436052092409343 - 0.64204688820310396j)]]))
oPsKCheck[3]._r_sp_u_to_r_sp_d()
oPsKCheck[3]._l_sp_d_to_l_sp_u()
oPsKCheck[3].spin_index = "u"
oPsKCheck[4]._r_sp_d = numpy.vectorize(mpmath.mpc)(numpy.array([[(1.01625936813760885E-002 - 0.22054306530403212j)],
                                                                [(0.67179178959347197 - 0.19005528425990376j)]]))
oPsKCheck[4]._l_sp_u = numpy.vectorize(mpmath.mpc)(numpy.array([[(0.62161365611385844 + 1.5137881459404428j)],
                                                                [(-0.80227495696756812)]]))
oPsKCheck[4]._r_sp_d_to_r_sp_u()
oPsKCheck[4]._l_sp_u_to_l_sp_d()
oPsKCheck[4].spin_index = "d"

oPsKCheck.m_t = oPsKCheck.field.sqrt(oPsKCheck("s_3"))
oPsKCheck.m_h = oPsKCheck.field.sqrt(oPsKCheck("s_5"))
