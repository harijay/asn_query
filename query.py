#!/usr/bin/python
# Simple script to read the tabular results of the ligand entries in the PDB and deposit them into mongodb
import csv
import pprint
import pymongo
from pymongo import Connection
from ligand_interactions import list_interactions
con = Connection()
db = con.ligandlist


unique_list = []
reader = csv.DictReader(open("tabularResults.csv","r"));
outfile = open("liglist.txt","w")


for i in reader:
    try:
        if i["PDB ID"] in unique_list:
            pass
        else:
            unique_list.append(i["PDB ID"])
            outfile.write(i["PDB ID"] + "\n")
        # Collection Named pdbligands
 #       pdbligands = db.pdbligands
 #       pdbligands.insert(i)
    except IndexError:
        print "Number Uniques:", len(unique_list)
        print "Caught IndexError"
 
    

outfile.close()


