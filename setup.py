from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='control-tx-pi',  # Required
    version='0.0.1',  # Required
    description='Control transmitters',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional
    url='https://github.com/GaborSzabo7/control-tx-pi',  # Optional
    author=[  # Optional
        'Gabor Pap',
        'Gabor Szabo'
    ],
    author_email=[ # Optional
        'mcganyer@gmail.com',
        'gaszabo7@gmail.com'
    ],  
    keywords='tx, pi, ardf',  # Optional
    packages=['src'],  # Required
    python_requires='>=3.8, <4',
    
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    entry_points={  # Optional
        'console_scripts': [
            'ctrl-tx-pi=src.main:start_application',
        ],
    },

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/GaborSzabo7/control-tx-pi/issues',
        'Source': 'https://github.com/GaborSzabo7/control-tx-pi',
    },
)