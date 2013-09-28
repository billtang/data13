#!/usr/bin/python
#
# sum data extracted
#
import csv
import sys
def main():
    mydata = {}
    csvwriter = csv.writer(sys.stdout,delimiter=',', quotechar='"')
    csvreader = csv.reader(sys.stdin, delimiter=',', quotechar='"')
    for row in csvreader:
        # field: # 1 is contribution amount, 2 is year, 3 is contributor zipcode, 
        #          4 is recipient party
        myvalue = float(row[0])
        mykey = row[1], row[2], row[3]
        if mykey in mydata:
            mydata[ mykey ] = mydata [mykey] + myvalue
        else:
            mydata[ mykey ] = myvalue

    for key in mydata:
        csvwriter.writerow([ mydata[key], key[0], key[1], key[2] ])

if __name__ == "__main__":
    main()
        


