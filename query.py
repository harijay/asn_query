#!/usr/bin/python
# Simple script to read the tabular results of the ligand entries in the PDB and deposit them into mongodb
import csv
import pprint
import pymongo
from pymongo import Connection
from ligand_interactions import list_interactions
con = Connection()
db = con.ligandlist



reader = csv.DictReader(open("tabularResults.csv","r"));
outfile = open("liglist.txt","w")


for i in reader:
    try:
        # Collection Named pdbligands
        pdbligands = db.pdbligands
        pdbligands.insert(i)
    except IndexError:
        print "Caught IndexError"
 
    

outfile.close()


