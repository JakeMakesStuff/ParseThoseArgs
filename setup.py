from setuptools import setup, Extension, find_packages

setup(
    name="ParseThoseArgs",
    version="1.0",
    ext_modules=[
        Extension("_parsethoseargs_c_parser", ['./parsethoseargs/python_wrapper.c']),
    ],
    packages=find_packages(exclude=('tests',)),
    author="Jake Gealer",
    author_email="jake@auttaja.io",
    url="https://github.com/JakeMakesStuff/ParseThoseArgs"
)
