#!/usr/bin/env python

import argparse

from githublist.parser import main as get_data
from githublist.serve import serve_content

parser = argparse.ArgumentParser(description='View repositories for any GitHub account.')
parser.add_argument('user', type=str, help='GitHub user handle')
parser.add_argument('-f', '--format', choices=['json', 'csv', 'md', 'raw.txt', 'tbl.txt'],
                    help='File output format.')


def main():
    args = parser.parse_args()
    user, format_ = args.user, args.format

    return serve_content(get_data(user), user, format_)

if __name__ == '__main__':
    main()
