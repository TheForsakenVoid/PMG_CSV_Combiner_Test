import csv
import sys
import os

def combine_csv(files):
    rows= []
    for file in files:
        header_written = False
        with open(file, 'r') as f:
            reader = csv.reader(f)
            if not header_written:
                header = next(reader)
                header.append('filename')
                header_written = True
            for row in reader:
                row.append(os.path.basename(file))
                rows.append(row)

       
    writer = csv.writer(sys.stdout)
    writer.writerow(header)
    writer.writerows(rows)


        

if __name__ == '__main__':
    combine_csv(sys.argv[1:])