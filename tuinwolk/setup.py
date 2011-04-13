import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "TuinWolk",
    version = "0.0.1",
    author = "Mattijs Ugen & Peter Wagenaar",
	#author_email = "andrewjcarter@gmail.com", TODO: which mailaddresses should we use?
    description = ("A distributed backup solution using git"),
	license = "https://github.com/TuinfeesT/TuinWolk/blob/master/license.md",
    keywords = "backup git distributed cloud",
	url = "https://github.com/TuinfeesT/TuinWolk",
	#packages=['an_example_pypi_project', 'tests'], TODO: fill me
    long_description=read('../readme.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
		"Topic :: System :: Archiving :: Backup",
		"Topic :: System :: Archiving :: Mirroring",
    ],
)
