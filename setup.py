# Heiko Menzler
# heikogeorg.menzler@stud.uni-goettingen.de
#
# Date: 30.06.2022

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chess_blind",
    author="Heiko Menzler, ...",  # feel free to add your names here
    author_email="heikogeorg.menzler@stud.uni-goettingen.de, ...",  # and here
    description="Statisical Physics on disordered systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "code"},
    packages=setuptools.find_packages(where="code"),
    python_requires=">=3.10.4",
)
