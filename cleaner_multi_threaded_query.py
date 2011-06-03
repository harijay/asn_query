#!/usr/bin/python
import csv
import pprint
import pymongo
from PDB_HBOND_processor import PDB_HBOND_processor
NUM_THREADS = 6
con = pymongo.Connection()
db = con.ligandlist

#db.pdbligands.find().count()          
#232862
# Setup Queue
from Queue import Queue
in_queue = Queue()
out_queue = Queue()

for an_entry in db.pdbligands.find():
    in_queue.put(an_entry["PDB ID"])

for i in range(NUM_THREADS):
    in_queue.put(None)     

# Setup threads

from threading import Thread,Lock


worker_thread_list = []
for i in range(NUM_THREADS):
    worker_thread = PDB_HBOND_processor(in_queue , out_queue)
    worker_thread.start()
    worker_thread_list.append(worker_thread)

     




