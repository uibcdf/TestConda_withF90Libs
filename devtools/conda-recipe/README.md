# Instructions

## Conda packages required

```bash
conda install anaconda-client conda-build
```

## Building and pushing the package to https://anaconda.org/YourUser

```bash
conda config --set anaconda_upload no
conda build .
## If you need to check the package path:
# conda build . --output
anaconda login
anaconda upload --user uibcdf /path/to/conda-package.tar.bz2
### Or if the package is uploaded to an organization account https://anaconda.org/YourOrg
# anaconda upload --user YourOrg /path/to/conda-package.tar.bz2
conda build purge
anaconda logout
```

## Additional Info
https://docs.anaconda.com/anaconda-cloud/user-guide/tasks/work-with-packages
