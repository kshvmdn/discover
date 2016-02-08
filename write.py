import colour
import csv
import json
import os
import pprint


# write to file as json, csv, markdown, plaintext or print table


def write_data(data, user, format=None):
    if format is not None:

        directory = './data/'

        if not os.path.exists(directory):
            os.makedirs(directory)

        f = open(directory + user + '.' + format, 'w')

        if format == 'json':
            f.write(json.dumps(data, indent=4))
        elif format == 'csv':
            keys = data[0].keys()
            dw = csv.DictWriter(f, fieldnames=keys)
            dw.writeheader()
            dw.writerows(data)
        elif format == 'md':
            f.write('## %s - GitHub repositories\n' % user)
            for row in data:
                f.write(
                    '#### {}\n\n{}  \n_{}_, {} star(s)\n\n'.format(row['name'],
                                                                   row['desc'],
                                                                   row['lang'],
                                                                   row['stars']))
        elif format == 'txt':
            f.write('%s - GitHub repositories\n\n' % user)
            for row in data:
                f.write('{}\n{}\n{}, {} star(s)\n\n'.format(row['name'],
                                                            row['desc'],
                                                            row['lang'],
                                                            row['stars']))

        f.close()
