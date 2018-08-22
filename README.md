# Conda-Build-Issue
Demonstrates a problem building a simple Conda package that depends on Keras.

To reproduce the problem:

1. Clone this repository with:

        git clone https://github.com/HaroldMills/Conda-Build-Issue.git
        
2. `cd` to the repository directory `Conda-Build-Issue`.

3. Issue the command:

        conda build conda_recipe
        
On my computer, running macOS and using `conda` 4.5.10 and `conda_build` 3.13.0,
the build fails with error messages suggesting that `setup.py` encounters a
problem concerning the package `keras-preprocessing`. The complete output of the
command is in the file `Build Output.txt` of this repository.

I'm not sure what the problem is, since there certainly is a package called
`keras-preprocessing` available from the default Anaconda channel. I have also
tried building with:

        conda build -c conda-forge conda_recipe
        
(i.e. using the `conda-forge` channel instead of the default Anaconda channel)
with similar results.

One of the error messages in the build output suggests ensuring that all
dependencies are included in the `meta.yaml` file. However, adding
the `keras-preprocessing` package to that file does not help: the build
output is the same.
