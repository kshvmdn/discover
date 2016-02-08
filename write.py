import csv
import json
import os
from tabulate import tabulate


def write_data(d, u, f=None):
    if f is not None:

        directory = './data/'

        if not os.path.exists(directory):
            os.makedirs(directory)

        file = open(directory + u + '.' + f, 'w')

        if f == 'json':
            file.write(json.dumps(d, indent=4))
        elif f == 'csv':
            keys = d[0].keys()
            dw = csv.DictWriter(file, fieldnames=keys)
            dw.writeheader()
            dw.writerows(d)
        elif f == 'md':
            file.write('## %s - GitHub repositories\n' % u)
            for row in d:
                file.write(
                    '#### {}\n\n{}  \n_{}_, {} star(s)\n\n'.format(row['name'],
                                                                   row['desc'],
                                                                   row['lang'],
                                                                   row['stars']))
        elif f == 'txt':
            file.write('%s - GitHub repositories\n\n' % u)
            for row in d:
                file.write('{}\n{}\n{}, {} star(s)\n\n'.format(row['name'],
                                                               row['desc'],
                                                               row['lang'],
                                                               row['stars']))
        file.close()
    else:
        print(tabulate(d, headers="keys"))
