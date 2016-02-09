import csv
import json
import os
import time
from tabulate import tabulate


def write_data(data, user, format_=None):
    if format_ is not None:

        directory = './out/'

        if not os.path.exists(directory):
            os.makedirs(directory)

        # filename will be in form user.mmddyy.format e.g. kshvmdn.020816.json
        file = open(directory + user + '.' + time.strftime("%m%d%y") + '.' + format_, 'w')

        if format_ == 'json':
            file.write(json.dumps(data, indent=4))
        elif format_ == 'csv':
            keys = data[0].keys()
            dw = csv.DictWriter(file, fieldnames=keys)
            dw.writeheader()
            dw.writerows(data)
        elif format_ == 'md':
            file.write('## %s - GitHub repositories\n' % user)
            for row in data:
                file.write(
                    '#### {}\n\n{}  \n_{}_, {} star(s)\n\n'.format(row['name'],
                                                                   row['desc'],
                                                                   row['lang'],
                                                                   row['stars']))
        elif format_ == 'txt':
            file.write('%s - GitHub repositories\n\n' % user)
            for row in data:
                file.write('{}\n{}\n{}, {} star(s)\n\n'.format(row['name'],
                                                               row['desc'],
                                                               row['lang'],
                                                               row['stars']))
        file.close()
    else:
        print(tabulate(data, headers="keys"))
