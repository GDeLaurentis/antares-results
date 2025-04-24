# antares-results
This is a repository for spinor-helicity amplitudes reconstructed from numerical evaluations.

[![CI Lint](https://github.com/GDeLaurentis/antares-results/actions/workflows/ci_lint.yml/badge.svg)](https://github.com/GDeLaurentis/antares-results/actions/workflows/ci_lint.yml)
[![CI Test](https://github.com/GDeLaurentis/antares-results/actions/workflows/ci_test.yml/badge.svg)](https://github.com/GDeLaurentis/antares-results/actions/workflows/ci_test.yml)
[![Docs](https://github.com/GDeLaurentis/antares-results/actions/workflows/cd_docs.yml/badge.svg?label=Docs)](https://gdelaurentis.github.io/antares-results/)
[![PyPI](https://img.shields.io/pypi/v/antares-results?label=PyPI)](https://pypi.org/project/antares-results/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/antares-results.svg?label=PyPI%20downloads)](https://pypi.org/project/antares-results/)
[![DOI](https://zenodo.org/badge/905853539.svg)](https://doi.org/10.5281/zenodo.14536697)
<!-- [![Coverage](https://img.shields.io/badge/Coverage-81%25-greenyellow?labelColor=2a2f35)](https://github.com/GDeLaurentis/antares-results/actions) -->


## Quick Start

### Vjj (two-loops planar)

Load all $qggqV$ coefficients and evaluate them (for exmaple at a $\mathbb{F}_p$ phase space point). These are a basis of the vector space of pentagon-function coefficients.

```python
In [1]: from antares_results.Vjj.qggqll.mhv import lTerms
In [2]: from lips import Particles
In [3]: from syngular import Field

# print analytic expressions for the first 5 rational functions in the basis of the vector space of pentagon-function coefficients
In [4]: print(lTerms[:5])
Out [4]: [Terms("""+(+1⟨4|6⟩²)/(⟨1|2⟩⟨2|3⟩⟨3|4⟩⟨5|6⟩)"""), Terms("""+(+1⟨4|6⟩⟨1|4⟩[1|5])/(⟨1|2⟩⟨2|3⟩⟨3|4⟩⟨1|5+6|1])"""), Terms("""+(-1⟨1|6⟩[2|3]⟨4|6⟩)/(⟨1|3⟩⟨2|3⟩⟨5|6⟩⟨1|2+4|3])"""), Terms("""+(+1[2|3]⟨4|6⟩⟨2|6⟩)/(⟨1|2⟩⟨2|3⟩⟨5|6⟩⟨2|3+4|2])"""), Terms("""+(+1⟨3|6⟩[2|3]⟨4|6⟩)/(⟨1|3⟩⟨2|3⟩⟨5|6⟩⟨3|2+4|3])""")]

# generate a random phase space point (in this case over finite fields) and evaluate the basis
In [5]: oPs = Particles(6, field=Field("finite field", 2 ** 31 - 1, 1), seed=0)
In [6]: lTerms(oPs)
Out [4]: [1162389822 % 2147483647, 1610387318 % 2147483647, 173910601 % 2147483647, 1377129258 % 2147483647, 2082634606 % 2147483647, ...]
```

Floating point (real or complex) and $p$-adic phase space points work much in the same way.

### ttH (one-loop)

Load all $qqttH$ coefficients. These are directly coefficients of the respective Feynman integrals (labeld by external legs and internal mass routings).

```python
In [1]: from antares_results.ttH.qqttH.pm import coeffs as qqttH_pm_coeffs
In [2]: qqttH_pm_coeffs.keys()
Out [2]:  dict_keys(['tree', 'bub12x00', 'tri12x3x00m', 'box3x12x4xm00m', 'tri13x24xm0m', 'box3x4x12xm0mm', 'box3x1x24xm00m', 'bub13xm0', 'bub34xmm', 'tri124x3xm0m', 'bub1234xmm', 'tri12x3xmm0', 'bub123xm0', 'box4x2x1xm000', 'tri12x34xmmm', 'bub12xmm'])
In [3]: from antares_results.ttH.momenta import oPsKCheck  # load a phase space point
In [4]: {key: val(oPsKCheck) for key, val in qqttH_pm_coeffs.items()}
Out[4]: 
{'tree': mpc(real='0.4998512132360710056', imag='0.1143902001899784471'),
 'bub12x00': mpc(real='0.08890670891584541782', imag='3.486530065803925438'),
 'tri12x3x00m': mpc(real='48.35977263849211738', imag='53.33641975568919236'),
 'box3x12x4xm00m': mpc(real='-47.46308257461350877', imag='-45.87188967765678171'),
 'tri13x24xm0m': mpc(real='-12.70147396497987757', imag='2.465657548592817883'),
 'box3x4x12xm0mm': mpc(real='-0.8736344184540660862', imag='-9.246218431210708744'),
 'box3x1x24xm00m': mpc(real='25.39062949179914419', imag='-8.492255173857109485'),
 'bub13xm0': mpc(real='0.07829108262369600946', imag='-0.1842325910625640072'),
 'bub34xmm': mpc(real='0.1032547846538197367', imag='0.3591837975251150339'),
 'tri124x3xm0m': mpc(real='5.625101060149315213', imag='1.58915938402978163'),
 'bub1234xmm': mpc(real='-0.820858500734524571', imag='-0.03028493471636876586'),
 'tri12x3xmm0': mpc(real='-6.615318666263966363', imag='-8.927541807153011488'),
 'bub123xm0': mpc(real='0.6853493549121706108', imag='-1.404274244486850426'),
 'box4x2x1xm000': mpc(real='-90.29617792252767927', imag='6.479713760815963397'),
 'tri12x34xmmm': mpc(real='-4.354721966504684239', imag='-3.285466744291004104'),
 'bub12xmm': mpc(real='-0.3362765929597263115', imag='-0.4684054239865742472')}
```

### jjj (two-loops full-color)

Analogous to $Vjj$.

### jjjj (one-loop)

Analogous to $ttH$.
