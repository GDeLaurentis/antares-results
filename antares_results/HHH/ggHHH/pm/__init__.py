from pathlib import Path
from antares.terms.terms import LoadResults

here = Path(__file__).parent

coeffs = {}
for file in here.glob("*.tex"):
    res = LoadResults(f"{here}/{file.stem}")[0]
    coeffs[file.stem] = (res[0] if res != 0 else res)
