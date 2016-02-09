#!/usr/bin/env python

import argparse
from termcolor import colored, cprint

from githublist.parser import main as get_data
from githublist.serve import serve_content

parser = argparse.ArgumentParser(description='View repositories for any GitHub account.')
parser.add_argument('user', type=str, nargs='+', help='GitHub user handle')
parser.add_argument('--format', nargs='+',
                    choices=['json', 'csv', 'md', 'raw.txt', 'tbl.txt', 'all'],
                    help='File output format. default=tbl.txt', default=['tbl.txt'])


def main():
    args = parser.parse_args()
    user = args.user
    format_ = args.format
    if 'all' in args.format:
        format_ = ['json', 'csv', 'md', 'raw.txt', 'tbl.txt']

    for u in user:
        print('Preparing data for {}...'.format(colored(u, 'white')))
        d = get_data(u)
        for f in format_:
            print(' Writing {}...'.format(colored(f, 'white')), end='')
            serve_content(d, u, f)
            print(' Done!')
    cprint('Complete!', 'red')
    return None

if __name__ == '__main__':
    main()
