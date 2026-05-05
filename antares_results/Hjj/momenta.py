"""
Phase space point of arXiv:2503.10595 written in terms of four momenta.

.. code-block:: python

    from amplitudes.Hjj.HTL.momenta import oPs

"""


import mpmath
import numpy

from syngular import Field
from pyadic.primes import primes
from lips import Particles


mpmath.mp.dps = 300

oPs = Particles(6)

momenta = numpy.array([
    [mpmath.mpf('-88'), 0, 0, mpmath.mpf('88')],
    [mpmath.mpf('-88'), 0, 0, mpmath.mpf('-88')],
    [mpmath.mpf('2181/176'), mpmath.mpf('85281/16') / mpmath.sqrt(mpmath.mpf('1477139')),
     mpmath.mpf('3/176') * mpmath.sqrt(mpmath.mpf('349651897847/1477139')), mpmath.mpf('-1425/176')],
    [mpmath.mpf('9527/176'), mpmath.mpf('7924743/176') / mpmath.sqrt(mpmath.mpf('1477139')),
     mpmath.mpf('-3/176') * mpmath.sqrt(mpmath.mpf('349651897847/1477139')), mpmath.mpf('6791/176')],
    [mpmath.mpf('205458/4817'), 0, mpmath.mpf('205458/4817'), 0],
    [mpmath.mpf('14163337/211948'), mpmath.mpf('-3/88') * mpmath.sqrt(mpmath.mpf('1477139')),
     mpmath.mpf('-205458/4817'), mpmath.mpf('-2683/88')]
])

for i, oP in enumerate(oPs):
    oP.four_mom = momenta[i][[0, 2, 3, 1]]

assert numpy.all(abs(oPs.total_mom).astype(float) < oPs.field.tollerance)
assert numpy.all(abs(numpy.array(oPs.m2s)) < oPs.field.tollerance)

oPs5pt = oPs.cluster([[1, ], [2, ], [3, ], [4, ], [5, 6]])
oPs5pt[5]._r_sp_d = oPs5pt[5]._l_sp_d = oPs5pt[5]._r_sp_u = oPs5pt[5]._l_sp_u = None

oPsFFCheck = Particles(6, field=Field("finite field", primes[-1], 1), seed=0)
oPsFFCheck5pt = oPsFFCheck.cluster([[1, ], [2, ], [3, ], [4, ], [5, 6]])
oPsFFCheck5pt[5]._r_sp_d = oPsFFCheck5pt[5]._l_sp_d = oPsFFCheck5pt[5]._r_sp_u = oPsFFCheck5pt[5]._l_sp_u = None
