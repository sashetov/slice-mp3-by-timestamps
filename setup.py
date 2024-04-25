from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("mp3_slicer.pyx", 
                            compiler_directives={'language_level' : "3"}),
    scripts=['mp3_slicer.pyx']
)
