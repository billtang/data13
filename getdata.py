#!/usr/bin/python
import csv
import sys
def main():
    csvwriter = csv.writer(sys.stdout,delimiter=',', quotechar='"')
    csvreader = csv.reader(sys.stdin, delimiter=',', quotechar='"')
    for row in csvreader:
        # field: # 8 is contribution amount, 9 is date, 19 is contributor zipcode, 
        #         27 is recipient party
        if row[19]!="" and len(row[19]) >= 0:
            myzip = 0
            try: myzip = int(row[19])
            except: pass
            if myzip >= 48005 and myzip <= 48462: 
                myparty = 'U'
                if row[27]!='' and len(row[27])>0: myparty = row[27]
                csvwriter.writerow([row[8],row[9][:4],row[19],myparty])

if __name__ == "__main__":
    main()
        


