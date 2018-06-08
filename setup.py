import setuptools

# To compile f90 with f2py 'setup' has to come from numpy.
# This is not the case with cython.
# In addition, the option cmdclass = {'build_ext': build_ext} is not needed
# Check for example:
# https://github.com/perrette/python-fortran-cpp-template/blob/master/setup.py
# https://stackoverflow.com/questions/14453208/mixing-f2py-with-distutils
# https://gist.github.com/johntut/1d8edea1fd0f5f1c057c

from numpy.distutils.core import setup
from numpy.distutils.extension import Extension

ext_math = Extension(
    name = 'lib.libmath',
    extra_compile_args = [],
    libraries = [],
    language = 'f90',
    sources = ['lib/libmath.f90'],
)

setup(
    name='vector_normalization',
    version='1.0',
    author='UIBCDF Lab',
    author_email='uibcdf@gmail.com',
    package_dir={'vector_normalization': 'vector_normalization'},
    packages=find_packages(),
    package_data={'vector_normalization': [], '': ['*.f90']},
    ext_modules=[ext_math],
    url='http://uibcdf.org',
    download_url ='https://github.com/uibcdf/TestsConda',
    license='MIT',
    description="doc to be written",
    long_description="long doc to be written",
)
