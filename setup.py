import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-flatpage-images",
    version = "0.1",
    description = "Allow to extend contrib flatpages app in order to link multiples images to one flatpage",
    long_description = read('README.rst'),
    url = 'https://github.com/rmaceissoft/django-flatpage-images',
    author = 'Reiner Marquez',
    author_email = 'rmaceissoft@gmail.com',
    packages = find_packages(exclude=['tests', 'example', 'docs']),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)