import csv


def read_csv(filename):

    with open(filename, 'r') as csvfile:

        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
            print(row)
            # get total number of rows
        print("Total no. of rows: %d" % csvreader.line_num)

        # printing the field names
    print('Headers:' + ', '.join(field for field in fields))


def write_csv(header1,value1):
    import csv
    import os
    headers = header1

    with open('file.csv', 'w') as f:
        file_is_empty = os.stat('file.csv').st_size == 0
        writer = csv.writer(f, lineterminator='\n')
        if file_is_empty:
            writer.writerow(headers)
        writer.writerow(value1)


if __name__ == '__main__':
    Header = ['header1', 'header2', 'header3']
    rows = ['value1', 'value2', 'value3']
    write_csv(Header, rows)
    # read the same csv file
    read_csv("file.csv")
