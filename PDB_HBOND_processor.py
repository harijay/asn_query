#!/usr/bin/python
# PDB class that takes in an input queue and output queue and populates the db
from threading import Thread
import pymongo
import subprocess
from ligand_interactions import list_interactions
con_insert = pymongo.Connection()
db_interactions = con_insert.ligandlist.multithreadedlisttry1

class PDB_HBOND_processor(Thread):

    def __init__(self,in_queue,out_queue):
        Thread.__init__(self)
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        while True:
            pdb_id = self.in_queue.get()
            if pdb_id is not None:
                print "Got pdb_id {pdb_id}\n".format(pdb_id = pdb_id)
                # Code for processing hbonds and populating database
                # Will use the subprocess module and have pymol process file and return a data structure with hbonds to stdout
                # We will then parse the stdout and input to mongo
                subprocess.call(["python","ligand_interactions.py","%s" %pdb_id ])
                db_interactions.insert({"PDB_ID" :pdb_id})
            if pdb_id is None:
                print "ATTEMPTING TO DIE\n"
                break
                
                
