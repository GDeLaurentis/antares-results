from antares.terms.lterms import TermsList
from pathlib import Path

this_script_path = Path(__file__).resolve().parent

lTerms = TermsList(this_script_path, 6)
