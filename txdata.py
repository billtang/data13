#!/usr/bin/python
#
# extract tx data
#
import csv
import sys
def main():
    mydata = {}
    csvreader = csv.reader(sys.stdin, delimiter=',', quotechar='"')
    csvwriter = csv.writer(sys.stdout,delimiter=',', quotechar='"')
    rownum = 0
    for row in csvreader:
        if rownum > 0:
            try:  
                mycount = int(row[1])  # field: 0 is zipcode, 1: n1
                myrow = [ row[0], row[1] ]                
                for i in range(2,157): # skip 157: county_name, 158: state
                    myrow.append( str( float(row[i]) / mycount ) )
                for i in range(157,159):
                    myrow.append( row[i] )
                for i in range(159,161):
                    myrow.append( str( float(row[i]) / mycount ) )
       

                csvwriter.writerow(myrow)
            except: pass
        else: rownum = 1 # skip header row

if __name__ == "__main__":
    main()
        


