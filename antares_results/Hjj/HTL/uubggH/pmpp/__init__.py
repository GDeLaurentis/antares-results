from antares.terms.lterms import TermsList
from .md_0 import lTerms as lTerms_md_0
from .md_2 import lTerms as lTerms_md_2
from .md_m4 import lTerms as lTerms_md_m4

lTerms = TermsList(lTerms_md_0 + lTerms_md_2 + lTerms_md_m4, 6)
