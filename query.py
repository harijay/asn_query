#!/usr/bin/python
import csv
import pprint
import pymongo
from pymongo import Connection
con = Connection()
db = con.ligandlist

unique_dict = []

reader = csv.reader(open("tabularResults.csv","r"));
outfile = open("liglist.txt","w")


for i in reader:
    try:
        if i[0] in unique_dict:
            pass
        else :
            unique_dict.append(i[0])
            outfile.write(i[0] + "\n")
            anentry = {"pdbid" : i[0], "resn":i[2]}
            # Collection
            entries = db.entries
            entries.insert(anentry)
            
            #print "Found",len(unique_dict)
    except IndexError:
        print "Number uniques:", len(unique_dict)
    

outfile.close()
pprint.pprint(unique_dict)

