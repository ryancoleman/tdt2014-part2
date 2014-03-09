#!/usr/bin/env python

import sys
import string

idColumn = 2
energyColumn = 18

if len(sys.argv) < 3:
  print "Usage: make_tcams_output.py tcams.smi extract_all.sort.uniq.txt"
  print "data will be written to standard output"
else:
  smiIdsFile = open(sys.argv[1], 'r')
  extractFile = open(sys.argv[2], 'r')
  idToSmi = {}
  for line in smiIdsFile:
    tokens = string.split(line)
    #the 1: removes the T prefix on the ID code
    idToSmi[string.strip(tokens[1])[1:]] = string.strip(tokens[0])
  smiIdsFile.close()
  idsDone = set(idToSmi.keys())
  lastEnergy = None
  for line in extractFile:
    tokens = string.split(line)
    id = string.strip(tokens[idColumn])[1:]  # again, remove the T prefix
    energy = string.strip(tokens[energyColumn])
    idsDone.remove(id)
    print id, idToSmi[id], energy
    lastEnergy = energy
  extractFile.close()
  #okay, now do all the ones that somehow didn't get docked
  for id in idsDone:
    print id, idToSmi[id], str(float(lastEnergy) + 1.0)
