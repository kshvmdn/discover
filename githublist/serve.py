import csv
import json
import os
import time
from tabulate import tabulate


def serve_content(data, user, format_=None):
    if format_ is not None and len(data) > 0:
        directory = './out/'
        if not os.path.exists(directory):
            os.makedirs(directory)

        # filename will be user.mmddyy.format e.g. kshvmdn.020816.json
        file_ = '{}{}.{}.{}'.format(
            directory, user, time.strftime('%m%d%y'), format_)
        f = open(file_, 'w')

        if format_ == 'json':
            f.write(json.dumps(data, indent=4))
        elif format_ == 'csv':
            keys = data[0].keys()
            dw = csv.DictWriter(f, fieldnames=keys)
            dw.writeheader()
            dw.writerows(data)
        elif format_ == 'md':
            f.write('## %s - GitHub repositories\n\n' % user)
            for r in data:
                star_str = 'star' if r['stars'] == 1 else 'stars'
                f.write('### {}\n\n{}  \n_{}_, {} {}\n\n'.format(r['name'],
                                                                 r['desc'],
                                                                 r['lang'],
                                                                 r['stars'],
                                                                 star_str))
        elif format_ == 'raw.txt':
            f.write('%s - GitHub repositories\n\n' % user)
            for r in data:
                star_str = 'star' if r['stars'] == 1 else 'stars'
                f.write('{}\n{}\n{}, {} {}\n\n'.format(r['name'],
                                                       r['desc'],
                                                       r['lang'],
                                                       r['stars'],
                                                       star_str))
        elif format_ == 'tbl.txt':
            f.write('%s - GitHub repositories\n\n' % user)
            f.write(tabulate(data, headers="keys"))
        f.close()
    else:
        print(tabulate(data, headers="keys"))
    return None


if __name__ == '__main__':
    serve_content([], 'kshvmdn')
