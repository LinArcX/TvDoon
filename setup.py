import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
#def read(fname):
 #   return open(os.path.join(os.path.dirname(__file__), fname)).read()

# requirements = [         
#                     'tvdb_api',
#                     'PTable',
#                 ]

setup(
    name = "tvdoon",
    version = "0.1",
    author = "LinArcX",
    author_email = "linarcx@gmail.com",
    description = ("Show Information About Tv Show's, Ratings And So Many Cool Fatures!"),
    license = "GPL3",
    keywords = "tvShow, upcoming tvshow",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['tvdoon'],
    #install_requires=requirements,
    #install_requires= ['tvdb_api','PTable','prettytable'],
    install_requires= ['prettytable'],
    setup_requires= ['prettytable'],
    scripts=['tvdoon/tvdoon'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: GPL3 License",
    ],
)
