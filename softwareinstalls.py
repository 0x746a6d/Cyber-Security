import os 
from setuptools import setup
from reporter import __version__

def __read__(file_name):
    return open (os.path.join(os.path.dirname(__file__),
    file_name)).read()

setup(
    name
)