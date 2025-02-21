# antares-results
This is a repository for spinor-helicity amplitudes reconstructed from numerical evaluations.

[![CI Lint](https://github.com/GDeLaurentis/antares-results-dev/actions/workflows/ci_lint.yml/badge.svg)](https://github.com/GDeLaurentis/antares-results-dev/actions/workflows/ci_lint.yml)
[![CI Test](https://github.com/GDeLaurentis/antares-results-dev/actions/workflows/ci_test.yml/badge.svg)](https://github.com/GDeLaurentis/antares-results-dev/actions/workflows/ci_test.yml)
[![Docs](https://github.com/GDeLaurentis/antares-results-dev/actions/workflows/cd_docs.yml/badge.svg?label=Docs)](https://gdelaurentis.github.io/antares-results-dev/)
[![PyPI](https://img.shields.io/pypi/v/antares-results?label=PyPI)](https://pypi.org/project/antares-results/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/antares-results.svg?label=PyPI%20downloads)](https://pypi.org/project/antares-results/)
[![DOI](https://zenodo.org/badge/905853539.svg)](https://doi.org/10.5281/zenodo.14536697)
<!-- [![Coverage](https://img.shields.io/badge/Coverage-81%25-greenyellow?labelColor=2a2f35)](https://github.com/GDeLaurentis/antares-results-dev/actions) -->



## Quick Start

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