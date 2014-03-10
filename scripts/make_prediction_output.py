#!/usr/bin/env python

import sys
import string

idColumn = 2

if len(sys.argv) < 4:
  print "Usage: make_predictions_output.py emolecules.smi extract_all.sort.uniq.txt number"
  print "data will be written to standard output"
else:
  smiIdsFile = open(sys.argv[1], 'r')
  extractFile = open(sys.argv[2], 'r')
  number = int(sys.argv[3])
  idToSmi = {}
  for line in smiIdsFile:
    tokens = string.split(line)
    #the 1: removes the T prefix on the ID code
    idToSmi[string.strip(tokens[1])[1:]] = string.strip(tokens[0])
  smiIdsFile.close()
  for line in extractFile.readlines()[:number]:  # only get this many
    tokens = string.split(line)
    id = string.strip(tokens[idColumn])[1:]  # again, remove the T prefix
    print id, idToSmi[id]
  extractFile.close()
