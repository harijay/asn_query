#!/usr/bin/python
import __main__
__main__.pymol_argv = [ 'pymol', '-qc'] 

import pprint
import pymongo
import sys,time,os



db = pymongo.Connection()
collection = db.ligandlist.entries
mongointeractions = db.ligandlist.hopethisworksinteractions

def list_interactions(pdbid):
    allligs = collection.find({"PDB ID": pdbid.upper()})
    pdbid = pdbid.lower() 
    directory = pdbid.lower()[1:3]
    pymol.cmd.load("/media/Elements/pdb/data/structures/divided/pdb/{directory}/pdb{pdbid}.ent.gz".format(directory = directory , pdbid = pdbid),"%s" % pdbid)
    print "Loaded", "/media/Elements/pdb/data/structures/divided/pdb/{directory}/pdb{pdbid}.ent.gz".format(directory = directory , pdbid = pdbid)
    myint = {}
    for alig in allligs:
        stored.dummy = []
        stored.dummyids = []
        print "INFOINFOINFO Examining %s for closeby residues " % alig["Ligand ID"]
        pymol.cmd.select("%s" % alig["Ligand ID"] , "/{pdbid}//{Chain_ID}/{Ligand_ID}/*/".format(Chain_ID=alig["Chain ID"],Ligand_ID=alig["Ligand ID"],pdbid=pdbid))
        numatoms = pymol.cmd.count_atoms("%s" % alig["Ligand ID"])
        if numatoms == 0:
            pymol.cmd.select("%s" % alig["Ligand ID"],"resn %s" % alig["Ligand ID"])
#        print "%s" % alig["Ligand ID"] , "/{pdbid}//{Chain_ID}/{Ligand_ID}/*/".format(Chain_ID=alig["Chain ID"],Ligand_ID=alig["Ligand ID"],pdbid=pdbid)
        pymol.cmd.select("interactions_%s" % alig["Ligand ID"],"all within 3.5 of %s" % alig["Ligand ID"] )
#        pymol.cmd.iterate("interactions_%s"%  alig["Ligand ID"] ,"print \"IFOINFOINFO\" , resi, resn,name,type")
        my_interactions = {}
        pymol.cmd.iterate("interactions_%s" %  alig["Ligand ID"] , "stored.dummy.append((resn,resi))")
        pymol.cmd.iterate("interactions_%s" %  alig["Ligand ID"],"stored.dummyids.append(resn)")
        if stored.dummy != []:
            myint = {"PDB_ID" : pdbid ,"LIGAND_ID" : alig["Ligand ID"],"NEARBY" : stored.dummy ,"NEARBY_RESN": stored.dummyids}
            pprint.pprint(myint)
            mongointeractions.insert(myint)
        

                                                    
if __name__ == '__main__':
    import __main__
    __main__.pymol_argv = [ 'pymol' ,'-cq']
    import pymol
    from pymol import stored
    pymol.finish_launching()
    list_interactions(sys.argv[1])
else:
    import  pymol
    from pymol import stored
    
