import numpy
import mpmath

from syngular import Field
from lips import Particles

# Pseudo random FF point natively from lips
field = Field("finite field", 2 ** 31 - 19, 1)
oPs8pt_FFKCheck = Particles(8, field=field, seed=0, internal_masses={'m_t'})
oPs8pt_FFKCheck.m_t = field.random()
oPs8pt_FFKCheck.m_h = "sqrt(s_34)"
oPs8pt_FFKCheck._singular_variety(("s_34-s_56", "s_56-s_78", ), (1, 1, ), seed=0)
oPsFFKCheck = oPs8pt_FFKCheck.cluster([[1, ], [2, ], [3, 4], [5, 6], [7, 8]])


# Hardcoded KCheck point imported from MCFM
momenta = numpy.vectorize(mpmath.mpc)(numpy.array([
    [-2.4355786006558882, 1.4898301874122055, 0.74775195662750948, 1.7757579069253617],
    [-0.32971463788504002, -0.27367176832349427, 1.8549133627351725E-002, -0.18295200272210582],
    [2.5000000000000000, 0.0000000000000000, 0.0000000000000000, 2.4206145913796355],
    [2.5000000000000000, 0.0000000000000000, 0.0000000000000000, -2.4206145913796355],
    [-2.2347067614590719, -1.2161584190887111, -0.76630109025486126, -1.5928059042032559]
]))

oPsKCheck = Particles(5, field=Field("mpc", 0, 64))
oPsKCheck[1].four_mom = momenta[0]
oPsKCheck[2].four_mom = momenta[1]
oPsKCheck[3].four_mom = momenta[2]
oPsKCheck[4].four_mom = momenta[3]
oPsKCheck[5].four_mom = momenta[4]

oPsKCheck.m_t2 = 0.748225
oPsKCheck.m_h2 = 0.390625

oPsKCheck.m_t = oPsKCheck.field.sqrt(oPsKCheck.m_t2)
oPsKCheck.m_h = oPsKCheck.field.sqrt(oPsKCheck.m_h2)
