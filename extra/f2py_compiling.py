import os
import sys
import tempfile
import numpy.f2py
from numpy.distutils.exec_command import exec_command

def compile_fortran(file_path,modulename,extra_args=''):


    main_folder = os.path.dirname(os.path.realpath(__file__))
    relative_folder = os.path.dirname(file_path)
    f90_file = os.path.basename(file_path)
    folder = os.path.join(main_folder,relative_folder)

    args = ' -c -m {} {} {}'.format(modulename, f90_file, extra_args)
    command = 'cd {} && {} -c "import numpy.f2py as f2py2e;f2py2e.main()" {}'.format(folder,sys.executable, args)
    status, output = exec_command(command)

    return status, output, command

def compile_math():

    file_path='../gamusino/lib/libmath.f90'
    modulename='libmath'
    return compile_fortran(file_path,modulename)



## Que tengo que probar
# https://stackoverflow.com/questions/7932028/setup-py-for-packages-that-depend-on-both-cython-and-f2py
# https://gist.github.com/johntut/1d8edea1fd0f5f1c057c
# http://www.vallis.org/blogfiles/progtricks/scipy2007/wrap.pdf
# http://f2py-users.cens.ioc.narkive.com/2zTBwOMq/f2py-extensions-using-setuptools
# https://stackoverflow.com/questions/12696520/cython-and-fortran-how-to-compile-together-without-f2py
# https://stackoverflow.com/questions/14453208/mixing-f2py-with-distutils
# https://stackoverflow.com/questions/17094300/how-to-include-only-some-modules-in-f2py-via-setup-py

