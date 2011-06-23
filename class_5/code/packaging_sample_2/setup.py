# import the components from cx_Freeze
from cx_Freeze import setup, Executable

# we call the setup function here passing,
setup(
    name = "urllib2_example",   # the name of the program
    version = "0.1",            # the version
    description = "A script that downloads a page",     # a description
    executables = [Executable('urllib2_example.py')]    # calls the build function
)
