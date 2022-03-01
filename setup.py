from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.3'
DESCRIPTION = 'A package which generates a csv file containing topsis scores and ranks.'
LONG_DESCRIPTION = 'Just give a csv file as an input which contains a dataset on which topsis can be applied. We have also to provide weights and impacts according to which topsis will be applied on the given input file. Use command "from Topsis_Vaibhav_102083059 import topsis as v" and then "v.Topsis_dataset(file=<name of the file in the form of a string>,Weights=<comma separated weights in the form of string>,Impacts=<Comma separated + or - in the form of string>)" and this function will generate a dataframe which will contain topsis score and ranks of the initially given data. '

# Setting up
setup(
    name="Topsis-Vaibhav-102083059",
    version=VERSION,
    author="Vaibhav Mukhi",
    author_email="mukhivaibhav4@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'Topsis', 'Topsis Package', 'Topsis Libraray', 'Vaibhav'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)