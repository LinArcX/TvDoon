from setuptools import setup

setup(
    name="tvdoon",
    version="0.1.0",
    author="LinArcX",
    author_email="linarcx@gmail.com",
    description="Show Information About Tv Show's, Ratings And So Many Cool Features!",
    license=" GPLv3",
    keywords="tvShow, upcoming tvShow",
    url="https://github.com/LinArcX/tvdoon",
    download_url='https://github.com/LinArcX/tvdoon/archive/0.1.0.tar.gz',
    packages=['tvdoon'],
    install_requires= ['tvdb_api','prettytable', 'pyfiglet', 'requests-cache'],
    setup_requires = ['tvdb_api', 'prettytable', 'pyfiglet', 'requests-cache'],
    scripts=['tvdoon/tvdoon'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
