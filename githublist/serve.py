import csv
import json
import os
import time
from tabulate import tabulate


def serve_content(data, user, format_=None):
    if format_ is not None and len(data) > 0:
        directory = './out/' + user + '/'
        if not os.path.exists(directory):
            os.makedirs(directory)

        # filename will be user.mmddyy.format e.g. kshvmdn.020816.json
        f = open(directory + time.strftime("%m%d%y") + '.' + format_, 'w')

        if format_ == 'json':
            f.write(json.dumps(data, indent=4))
        elif format_ == 'csv':
            keys = data[0].keys()
            dw = csv.DictWriter(f, fieldnames=keys)
            dw.writeheader()
            dw.writerows(data)
        elif format_ == 'md':
            f.write('## %s - GitHub repositories\n' % user)
            for row in data:
                f.write(
                    '#### {}\n\n{}  \n_{}_, {} star(s)\n\n'.format(row['name'],
                                                                   row['desc'],
                                                                   row['lang'],
                                                                   row[
                                                                       'stars']))
        elif format_ == 'txt':
            f.write('%s - GitHub repositories\n\n' % user)
            for row in data:
                f.write('{}\n{}\n{}, {} star(s)\n\n'.format(row['name'],
                                                            row['desc'],
                                                            row['lang'],
                                                            row['stars']))
        f.close()
    else:
        print(tabulate(data, headers="keys"))


if __name__ == '__main__':
    serve_content([], 'kshvmdn')
