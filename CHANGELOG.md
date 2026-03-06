# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]

### Added

### Changed

### Fixed

### Deprecated


## [0.1.0] - 2026-03-06 - Vjj massive spinor-helicity update

### Added

- one- and two-loop Vjj remainders in the massive spinor helicity formalism in `Vjj.qQQqV` and `Vjj.qggqV`
- tests for all polarizations of the massive vector boson

### Changed

- ttH results now require `lips.conjugation_acts_on_spin_indices` set to `True`  (to be reviewd)
- new processes are at least minor versions (to leave room for patches)


## [0.0.4] - 2025-07-28 - ggHHH update

### Added

- ggHHH one-loop coefficients: `from antares_results.HHH.ggHHH.pp/pm import coeffs`

### Changed

- Maintenance on other results: spinor indices for ttH are tuple (index position, index value), 4j results are loaded with multiplicity set to 6.
- Tests use git version of antares instead of pypi version.


## [0.0.3] - 2025-04-24

### Added

- ttH one-loop coefficients.
- `__init__.py` to most folders of computed processes, to allow import in python (see README.md).
- Example usage in `Quick Start` on README.

### Changed

- Renamed package to 'antares_results' to avoid problems with python imports.


## [0.0.2]

### Added

- jjjj one-loop coefficients


## [0.0.1]

### Added

- Vjj remainders up to two loops
- jjj remainders up to two loops


[unreleased]: https://github.com/GDeLaurentis/antares-results/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/GDeLaurentis/antares-results/compare/v0.0.4...v0.1.0
[0.0.4]: https://github.com/GDeLaurentis/antares-results/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/GDeLaurentis/antares-results/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/GDeLaurentis/antares-results/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/GDeLaurentis/antares-results/releases/tag/v0.0.1
