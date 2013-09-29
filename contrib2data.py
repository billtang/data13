#!/usr/bin/python
#
# extract federal campion finance data fields
#
import csv
import sys
def main():
    mydata = {}

#    mpcomponent="code_alg_Utham_newsrank";
#    mp = MathpakEngine.MathpakEngine(mpcomponent);
    csvinput = open('contrib.csv','r')
    csvreader = csv.reader(csvinput, delimiter=',', quotechar='"')
    #csvreader = csv.reader(sys.stdin, delimiter=',', quotechar='"')
    for row in csvreader:
        # field: # 8 is contribution amount, 9 is date, 19 is contributor zipcode, 
        #         27 is recipient party
        if row[19]!="" and len(row[19]) >= 0:
            myzip = 0
            try: 
                myzip = int(row[19])
            except: pass
            # zipcode range is from tx data: 
            #   cat Det*.csv|awk -F, '{print $1}'|sort -u
            if myzip >= 48005 and myzip <= 48462: 

                myparty = 'U'
                if row[27]!='' and len(row[27])>0: myparty = row[27]
                
                myvalue = float(row[8])
                myyear = row[9][:4]
                myzipcode = row[19]
                mykey = myyear, myzipcode , myparty

                if mykey in mydata:
                    mydata[ mykey ] = mydata [mykey] + myvalue
                else:
                    mydata[ mykey ] = myvalue

    csvinput.close()

    csvoutput = open('sum.csv','w')
    csvwriter = csv.writer(csvoutput,delimiter=',', quotechar='"')
    #csvwriter = csv.writer(sys.stdout,delimiter=',', quotechar='"')
    for key in mydata:
        csvwriter.writerow([ mydata[key], key[0], key[1], key[2] ])
    csvoutput.close()

if __name__ == "__main__":
    main()
        


