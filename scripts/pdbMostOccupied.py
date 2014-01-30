#!/usr/bin/env python 

#ryan g coleman ryangc@mail.med.upenn.edu
#kim sharp, brian shoichet, upenn, ucsf own this, whatevers
#reads a pdb file, for each atom, pick the most occupied one. 
#useful when the alternate positions and occupancies are meaningful.
#if tie, just pick a consistent set for each residue.

import sys,os,string,math        #necessary for file and string stuff
import pdb

def pdbMostOccupied(pdbFileName, outName=None, exceptions=[]):
  pdbEntry = pdb.pdbData(pdbFileName)
  newPdb = pdbEntry.copy()
  #print newPdb.altChars.count('A'), newPdb.altChars.count('B')
  newPdb.selectMostOccupied(exceptions=exceptions)
  #print newPdb.altChars.count('A'), newPdb.altChars.count('B')
  newPdb.write(outName)

#this is the main loop here
if -1 != string.find(sys.argv[0], "pdbMostOccupied.py"):
  outName = None
  exceptions = []
  if len(sys.argv) > 3:
    ids = string.split(sys.argv[3], '+')
    for id in ids:
      exceptions.append(int(id))
  if len(sys.argv) > 2:
    outName = sys.argv[2]
    pdbFileName = sys.argv[1]
    pdbMostOccupied(pdbFileName, outName, exceptions)
  else:
    print "Usage: pdbMostOccupied.py pdbFile outFile [exceptions]"
    print "  exceptions is a list of residue ids like 55+66 that the minor form"
    print "  of each will be chosen instead of the most occupied form"
