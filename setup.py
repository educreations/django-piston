#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages
    
import os

setup(
    name = "django-piston",
    version = "0.2.3rc2",
    author = 'Jesper Noehr',
    author_email = 'jesper@noehr.org',
    url = 'https://github.com/streeter/django-piston',
    description = "Piston is a Django mini-framework creating APIs.",
    license = 'BSD',
    packages = find_packages(),
    zip_safe = False,
    install_requires=[
    ],
    include_package_data = True,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
