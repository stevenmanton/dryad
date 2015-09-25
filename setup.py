try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        import sys

        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)


setup(
    name="dryad",
    version="0.1.0",
    author="Steven Anton",
    author_email="steven.m.anton@gmail.com",
    description="An implementation of an object-oriented variable ontology",
    keywords="ontology pandas",
    long_description="",
    packages=[
        'dryad',
    ],
    package_dir={'dryad': 'dryad'},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    cmdclass={'test': PyTest},
)
