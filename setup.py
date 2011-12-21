import os, sys

from setuptools import setup

def main():
    setup(
        name='detox',
        description='distributing tests via tox',
        #long_description = open('README.txt').read(),
        version='0.4.dev2',
        url='http://bitbucket.org/hpk42/detox',
        license='AGPL3',
        platforms=['unix', 'linux', 'osx', 'cygwin', 'win32'],
        author='holger krekel',
        author_email='holger at merlinux.eu',
        classifiers=['Development Status :: 6 - Mature',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: POSIX',
                     'Operating System :: Microsoft :: Windows',
                     'Operating System :: MacOS :: MacOS X',
                     'Topic :: Software Development :: Testing',
                     'Topic :: Software Development :: Libraries',
                     'Topic :: Utilities',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 3'],
        packages=['detox',
        ],
        install_requires=['tox>=1.3', 'eventlet>=0.9.16',],
        entry_points={'console_scripts': 'detox=detox.main:main'},
    )

if __name__ == '__main__':
    main()
