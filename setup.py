from distutils.core import setup
from setuptools import find_packages


setup(
    name="AppBundler",
    version="1.0",
    description="App bundling utility for macOS",
    author="Ennis Massey",
    author_email="ennisbaradine@gmail.com",
    packages=find_packages,
    classifiers=[
        "Developement Status :: 4 - Beta",
        "Environment :: MacOS X",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python 3 :: Only",
        "Topic :: Utilities"
    ]
)