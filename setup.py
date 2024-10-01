from setuptools import setup, find_packages
from pathlib import Path
from version import __version__ as version

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='spinor-helicity-amplitudes',
    version=version,
    license='GNU General Public License v3.0',
    description='Spinor Helicity Amplitudes',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Giuseppe De Laurentis',
    author_email='g.dl@hotmail.it',
    url='https://github.com/GDeLaurentis/lips',
    download_url=f'https://github.com/GDeLaurentis/spinor-helicity-amplitudes/archive/v{version}.tar.gz',
    project_urls={
        'Documentation': 'https://gdelaurentis.github.io/spinor-helicity-amplitudes/',
        'Issues': 'https://github.com/GDeLaurentis/spinor-helicity-amplitudes/issues',
    },
    keywords=['Spinor Helicity', 'Scattering Amplitudes'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=['lips',
                      ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)