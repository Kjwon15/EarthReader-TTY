from __future__ import print_function

import argparse
try:
    import configparser
except ImportError:
    import ConfigParser as configparser
import os
import sys
try:
    from urllib import parse as urlparse
except ImportError:
    import urlparse


from . import tty
from libearth.session import Session

all = 'main'


config = configparser.ConfigParser()
config.add_section('tty')
config.set('tty', 'session-id', Session().identifier)
config.set('tty', 'repository', None)
config.read(os.path.expanduser('~/.earthreaderrc'))

parser = argparse.ArgumentParser(prog='earthreader')

parser.add_argument('-i', '--session-id',
                    default=config.get('tty', 'session-id'),
                    help='session identifier.  [default: %(default)s]')
parser.add_argument('-d', '--repository-dir',
                    default=config.get('tty', 'repository'),
                    help='repository dir for EarthReader')


def main():
    args = parser.parse_args()

    if not args.repository_dir:
        parser.print_help()
        print('Repository dir is not configured', file=sys.stderr)
        exit(1)

    url = urlparse.urlparse(args.repository_dir)
    if url.scheme == '':
        args.repository_dir = urlparse.urljoin('file://', args.repository_dir)

    tty.main(args)


if __name__ == '__main__':
    main()
