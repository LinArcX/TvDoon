from setuptools import setup

setup(
    name="tvdoon",
    version="1.3.0",
    author="LinArcX",
    author_email="linarcx@gmail.com",
    description="Show Information About Tv Show's, Ratings And So Many Cool Features!",
    license=" GPLv3",
    keywords="tvShow, upcoming tvShow",
    url="https://github.com/LinArcX/tvdoon",
    download_url='https://github.com/LinArcX/tvdoon/archive/1.3.0.tar.gz',
    packages=['tvdoon','utility', 'threads'],
    install_requires= ['requests', 'pytvmaze','prettytable', 'pyfiglet', 'pip'],
    setup_requires = ['requests', 'pytvmaze', 'prettytable', 'pyfiglet', 'pip'],
    scripts=['tvdoon/tvdoon'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
