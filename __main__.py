#!/usr/bin/env python

import argparse

from githublist.parser import main as get_data
from githublist.serve import serve_content

parser = argparse.ArgumentParser(description='View repositories for any GitHub account.')
parser.add_argument('user', type=str, nargs='+', help='GitHub user handle')
parser.add_argument('-f', '--format', nargs='+',
                    choices=['json', 'csv', 'md', 'raw.txt', 'tbl.txt', 'all'],
                    help='File output format.')


def main():
    args = parser.parse_args()
    user = args.user
    format_ = ['json', 'csv', 'md', 'raw.txt', 'tbl.txt'] if 'all' in args.format else args.format

    for u in user:
        print('Preparing data for {}...'.format(u))
        d = get_data(u)
        for f in format_:
            if f is not None:
                print(' Writing {}...'.format(f), end='')
                serve_content(d, u, f)
                print(' Done!')
            else:
                serve_content(d, u, f)
    print('Complete!')
    return None

if __name__ == '__main__':
    main()
