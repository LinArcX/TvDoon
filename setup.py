from setuptools import setup

setup(
    name="tvdoon",
    version="0.3",
    author="LinArcX",
    author_email="linarcx@gmail.com",
    description="Show Information About Tv Show's, Ratings And So Many Cool Features!",
    license=" GPLv3",
    keywords="tvShow, upcoming tvShow",
    url="https://github.com/LinArcX/tvdoon",
    packages=['tvdoon'],
    install_requires= ['tvdb_api','prettytable', 'pyfiglet'],
    setup_requires = ['tvdb_api', 'prettytable', 'pyfiglet'],
    scripts=['tvdoon/tvdoon'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
