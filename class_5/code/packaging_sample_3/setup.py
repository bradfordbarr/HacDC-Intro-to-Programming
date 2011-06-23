from cx_Freeze import setup, Executable

setup(
    name = "pickle_example",
    version = "0.1",
    description = "Player Pickling Example",
    executables = [Executable('pickle_example.py')]
)
