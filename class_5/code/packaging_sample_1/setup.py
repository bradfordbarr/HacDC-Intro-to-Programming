from cx_Freeze import setup, Executable

setup(
    name = "1_to_99",
    version = "0.1",
    description = "A script that prints 0 thru 99",
    executables = [Executable('1_to_99.py')]
)
