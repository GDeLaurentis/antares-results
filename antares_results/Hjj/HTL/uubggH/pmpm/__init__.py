from antares.terms.lterms import TermsList
from .md0 import lTerms as lTerms_md0
from .md2 import lTerms as lTerms_md2
from .md4 import lTerms as lTerms_md4

lTerms = TermsList(lTerms_md0 + lTerms_md2 + lTerms_md4, 6)
