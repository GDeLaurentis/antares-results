from pathlib import Path
from antares.terms.terms import LoadResults

here = Path(__file__).parent

qqttH_pm_coeffs = {}
for file in here.glob("*.tex"):
    qqttH_pm_coeffs[file.stem] = LoadResults(f"/media/gdl/scratch/Programs/antares-dev-nbs/Jupyter/mcfm/ttH/results/{file.stem}")[0][0]
