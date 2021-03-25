import io
import re 
from setuptools import find_packages
from setuptools import setup

# parse_requirements() 
with io.open('requirements.txt') as fp:
    install_requires = fp.read()

with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("dummy_gen/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)


CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Environment :: Plugins",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Framework :: Flask",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
setup(
    name="dummy_gen",
    version=version,
    author="Hendri Karisma",
    author_email="situkangsayur@gmail.com",
    maintainer="Hendri Karisma",
    maintainer_email="situkangsayur@gmail.com",
    url="https://github.com/situkangsayur/dummy_gen",
    download_url="https://github.com/situkangsayur/dummy_gen",
    license="MIT",
    include_package_data=True,
    description= "",
    long_description_content_type="text/x-rst",
    long_description=readme,
    platforms=["any"],
    classifiers=CLASSIFIERS,
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=install_requires,
    tests_require=["coverage==4.2", 
                   "pyyaml==5.4"],
    extras_require={
        "dev": [
            "coverage",
            "sphinx",
            "pallets-sphinx-themes",
            "sphinxcontrib-log-cabinet",
            "sphinx-issues",
        ],
        "docs": [
            "sphinx",
            "pallets-sphinx-themes",
            "sphinxcontrib-log-cabinet",
            "sphinx-issues",
            "readme_renderer"
        ],
    }
)
