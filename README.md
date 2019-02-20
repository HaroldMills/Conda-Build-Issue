# Conda-Build-Issue
Demonstrates a problem building a simple Conda package that depends on
`pysoundfile`.

To reproduce the problem:

1. Clone this repository with:

        git clone https://github.com/HaroldMills/Conda-Build-Issue.git
        
2. `cd` to the repository directory `Conda-Build-Issue`.

3. Issue the command:

        conda build conda_recipe
        
On my computer, running macOS and using `conda` 4.6.4 and `conda_build` 3.17.8,
the build fails with error messages from `setup.py`. One of the messages is:

        RuntimeError: Setuptools downloading is disabled in conda build. Be sure to add all dependencies in the meta.yaml  url=https://pypi.org/simple/pysoundfile/

which seems to suggest that `pysoundfile` needs to be included in the
package's `meta.yaml` file. However, it is included already. The complete
output of the command is in the file `Build Output.txt` of this repository.

Why does this simple package not build, and what do I need to do to fix the
problem?
