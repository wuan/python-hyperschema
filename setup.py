# coding=utf-8
import glob

from setuptools import setup, find_packages

setup(
    name='hyperschema',
    version='0.2.1',
    packages=find_packages(exclude='tests'),
    scripts=glob.glob('scripts/*'),
    description='Python client library for JSON hyperschema REST services',
    author='Andreas Würl',
    author_email='andreas@wuerl.net',
    url='https://github.com/wuan/python-hyperschema',
    license='Apache-2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    install_requires=['requests'],
    tests_require=['pytest-cov', 'mock', 'assertpy'],
)
