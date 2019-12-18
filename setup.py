from setuptools import setup

setup(
    name='aoc2019',
    version='0.1',
    py_modules=['aoc2019'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        aoc2019=aoc2019:cli
    ''',
)