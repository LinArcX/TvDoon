from setuptools import setup

setup(
    name="tvdoon",
    version="1.1.0",
    author="LinArcX",
    author_email="linarcx@gmail.com",
    description="Show Information About Tv Show's, Ratings And So Many Cool Features!",
    license=" GPLv3",
    keywords="tvShow, upcoming tvShow",
    url="https://github.com/LinArcX/tvdoon",
    download_url='https://github.com/LinArcX/tvdoon/archive/1.1.0.zip',
    packages=['tvdoon','utility'],
    install_requires= ['pytvmaze','prettytable', 'pyfiglet'],
    setup_requires = ['pytvmaze', 'prettytable', 'pyfiglet'],
    scripts=['tvdoon/tvdoon'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
