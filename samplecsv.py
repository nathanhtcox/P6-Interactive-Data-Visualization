import csv
from random import random

with open('prosperLoanData.csv', 'rb') as srcfile:
    srcreader = csv.reader(srcfile)
    
    with open('sampledProsperLoanData.csv', 'wb') as outfile:
        outwriter = csv.writer(outfile)
    
        headers = next(srcreader)
        outwriter.writerow(headers)
        
        for row in srcreader:
            if random() < 0.1:
                outwriter.writerow(row)    
   

