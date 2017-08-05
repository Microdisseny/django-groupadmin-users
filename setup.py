from distutils.core import setup
from setuptools import find_packages


VERSION = '0.2'

CLASSIFIERS = [
    'Framework :: Django',
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

setup(
    name='django-groupadmin-users',
    description='Edit users in group from the Group add and edit pages',
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
