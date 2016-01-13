import os
import sys
from distutils.sysconfig import get_python_lib
from setuptools import find_packages, setup, Command


# Dynamically calculate the version based on django.VERSION.
version = __import__('oneway').get_version()


class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)


setup(
    name='oneway',
    version=version,
    url='https://github.com/green-latte/oneway',
    author='Green Latte',
    author_email='k.takeuchi@warrantee.co.jp',
    description=('[Todo: description]'),
    license='MIT',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 0 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    cmdclass = {'test': PyTest},
)
