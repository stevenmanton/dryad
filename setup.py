from setuptools import setup, find_packages

setup(
    name="dryad",
    version="0.1.0",
    author="Steven Anton",
    author_email="steven.m.anton@gmail.com",
    description="An implementation of an object-oriented variable ontology",
    keywords="ontology pandas",
    long_description="",
    packages=find_packages(),
    package_dir={'dryad': 'dryad'},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
