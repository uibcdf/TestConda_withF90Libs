# Setting up and uploading a python package with f90 library to Anaconda.

The purpose of this repo is to show how a python package with a f90 fortran library is setup and distributed via anaconda.

A simple setup file `setup.py` includes the necessary declarations to compile the fortran code through numpy (f2py).

Any comment is appreciated.

## Instructions

### Manually testing the package

The fortran code can be compiled manually with f2py and the package locally invoked to run a first test:

```bash
cd extra
python f2py_compiling.py
cd ..
python
```

Once the python interpreter is opened you can already check that the fortran
library is usable with the piece of python code in the 'Finnal test' subsection.


### Building and uploading the package to your anaconda channel

Find the conda recipe and steps description in [devtools/conda-recipe](https://github.com/uibcdf/TestConda_withF90Libs/tree/master/devtools/conda-recipe).

### Finnal test:

conda install -c YOUR_ANACONDA_CHANNEL vector_normalization

```python
import numpy as np
from vector_normalization import normalize_vector()

vect=np.array([1.0,1.0,1.0])
normalize_vector(vect)
print(vect)
```
