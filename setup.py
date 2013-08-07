
from distutils.core import setup

setup(
    name='PyHuddle',
    version='1.0.0',
    author='Adam.Flax',
    author_email='adammflax@btopenworld.com',
    packages=['pyhuddle', 'pyhuddle.tests', 'pyhuddle.api', 'pyhuddle.httpadapter', 'pyhuddle.oauth2'],
    url='https://github.com/adammflax/PyHuddle',
    license='LICENSE.txt',
    description='pyhuddle is a python library for Huddles Api. The library was built to abstract away from the wire protocol',
)