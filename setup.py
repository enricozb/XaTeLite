from codecs import open
from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))
long_description = open(path.join(here, 'README.md'), encoding='utf-8').read()
requirements = ['flask']

setup(
    name='xatelite',
    packages=['xatelite'],
    version='0.1.1',
    description='A Python3 LaTeX over SSH/HTTP service',
    long_description=long_description,
    author='Enrico Borba',
    author_email='enricozb@gmail.com',
    url='https://github.com/enricozb/XaTeLite',
    install_requires=requirements,
    python_requires='>=3',
    keywords=['latex', 'ssh'],
    license='MIT',
    entry_points={
        'console_scripts': [
            'xatelite=xatelite:main',
        ],
    },
)

