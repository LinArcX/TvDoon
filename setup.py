import os
from setuptools import setup

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
    # install_requires= ['tvdb_api','prettytable', 'pyfiglet'],
    # setup_requires= ['tvdb_api', 'prettytable', 'pyfiglet'],
    scripts=['tvdoon/tvdoon'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: GPL3 License",
    ],
)