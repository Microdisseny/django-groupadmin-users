from distutils.core import setup

from setuptools import find_packages

VERSION = '0.3.5'

CLASSIFIERS = [
    'Framework :: Django',
    'Framework :: Django :: 1.8',
    'Framework :: Django :: 1.9',
    'Framework :: Django :: 1.10',
    'Framework :: Django :: 1.11',
    'Framework :: Django :: 2.0',
    'Framework :: Django :: 2.1',
    'Framework :: Django :: 2.2',
    'Framework :: Django :: 3.0',
    'Framework :: Django :: 3.1',
    'Framework :: Django :: 3.2',
    'Framework :: Django :: 4.0',
    'Framework :: Django :: 5.2',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Topic :: Software Development',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Environment :: Web Environment',
    'Development Status :: 5 - Production/Stable',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

with open('README.rst', 'r') as f:
    long_desc = f.read()

setup(
    name='django-groupadmin-users',
    description='Edit users in group from the Group add and edit pages',
    long_description=long_desc,
    version=VERSION,
    author='Manel Clos',
    author_email='manelclos@gmail.com',
    license='BSD License',
    platforms=['OS Independent'],
    url='http://github.com/microdisseny/django-groupadmin-users',
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    classifiers=CLASSIFIERS,
)
