import argparse
from copy import deepcopy
import csv


def convert_to_csv(infile, outfile):
    columns = ['Date', 'Time', 'Name', 'System Name', 'Operator', 'Action',
               'Comment', 'Type', 'Revision', 'Location', 'Seq Number']

    with open(infile.name, newline='') as input:
        reader = csv.reader(input, delimiter=',', quotechar='"')
        data = []
        d = {}
        for row in reader:
            if '*****' in row[0]:
                data.append(deepcopy(d))
                d = {}
            for idx, item in enumerate(row):
                if item.strip(':') in columns:
                    d[item.strip(':')] = row[idx + 1]

    with open(outfile.name, 'w') as output:
        writer = csv.DictWriter(output, fieldnames=columns)
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'))
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'))
    args = parser.parse_args()

    try:
        convert_to_csv(args.infile, args.outfile)
    except:
        print('Usage:   python3 script.py inputfile outputfile')