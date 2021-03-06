import os
import sys
from setuptools import setup, find_packages
from django.core import management

with open(os.path.join(os.path.dirname(__file__), 'README.markdown')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# translation files compilation
currentdir = os.getcwd()
os.chdir(os.path.join(currentdir, 'paiji2_survey'))
management.call_command('compilemessages', stdout=sys.stdout)
os.chdir(currentdir)

setup(
    name='django-paiji2-survey',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    description='A simple survey app',
    long_description=README,
    install_requires=[
        'django-graphos',
        'django-bootstrap3>=6',
    ],
    url='https://github.com/rezometz/django-paiji2-survey',
    author='Supelec Rezo Metz',
    author_email='paiji-dev@rezometz.org',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
