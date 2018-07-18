from setuptools import find_packages
from setuptools import setup

setup(
    name='package',
    version='0.0.0',
    description='project description',
    packages=find_packages(),
    install_requires=[
        'requests',
        'typing',
        'conjure-client>=0.0.0,<1',
    ],
)
