#!/usr/bin/python
import csv
import sys
def main():
    csvreader = csv.reader(sys.stdin, delimiter=',', quotechar='"')
    for row in csvreader:
        # field: # 8 is contribution amount, 9 is date, 19 is contributor zipcode, 
        #         27 is recipient party
        if row[19]!="" and len(row[19]) >= 0:
            myzip = 0
            try: myzip = int(row[19])
            except: pass
            if myzip >= 48005 and myzip <= 48462: print row[8],row[9],row[19],row[27]

if __name__ == "__main__":
    main()
        


