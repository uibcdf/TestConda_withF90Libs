import os
import sys
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

    file_path='../vector_normalization/lib/libmath.f90'
    modulename='libmath'
    return compile_fortran(file_path,modulename)

if __name__ == "__main__":

    # execute only if run as a script

    status, output, command = compile_math()
