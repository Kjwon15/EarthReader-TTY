import os.path
import sys

try:
    from setuptools import find_packages, setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import find_packages, setup


def readme():
    try:
        with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
            return f.read()
    except (IOError, OSError):
        return ''


install_requires = [
    'libearth >= 0.1.1',
]
if sys.version_info < (2, 7):
    install_requires.append('argparse >= 1.2.1')


setup(
    name='EarthReader-TTY',
    description='Earth Reader for TTY',
    long_description=readme(),
    url='http://earthreader.org/',
    author='Kjwon15',
    author_email='kjwonmail' '@' 'gmail.com',
    license='AGPLv3 or later',
    entry_points={
        'console_scripts': [
            'ert = earthreader.command:main'
        ]
    },
    packages=find_packages(),
    install_requires=install_requires,
    dependency_links=[
        'https://github.com/earthreader/libearth/archive/master.zip'
        '#egg=libearth-dev'
    ],
    download_url='https://github.com/Kjwon15/EarthReader-TTY/releases',
)
