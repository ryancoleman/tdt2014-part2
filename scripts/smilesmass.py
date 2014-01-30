#!/usr/bin/env python

import sys
import string
from openeye.oechem import *

#assume smiles is in first column. add new column of molecular mass.

#OECalculateMolecularWeight(thisMolecule)

inFile = open(sys.argv[1], 'r')
for line in inFile.readlines():
  thisMolecule = OEGraphMol()
  tokens = string.split(line)
  OEParseSmiles(thisMolecule, tokens[0])
  molmass = OECalculateMolecularWeight(thisMolecule)
  tokens.append(str(molmass))
  print string.join(tokens, ' ')
