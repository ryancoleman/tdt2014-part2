#!/usr/bin/env python 

#Ryan G. Coleman
#takes a chembl file, processes it into a smiles/chemblid file

import string
import sys
import os
import subprocess
import shutil

def doStuff(inFile):
  '''takes only lines with good affinities, outputs smiles + chembid'''
  cid = 'CMPD_CHEMBLID'
  smi = 'CANONICAL_SMILES'
  exp = 'STANDARD_TYPE'
  rel = 'RELATION'
  val = 'STANDARD_VALUE'
  unt = 'STANDARD_UNITS'
  firstLine = None
  indices = {}
  try:
    readIn = open(inFile, 'r')
    for line in readIn:
      if firstLine is None:
        firstLine = line
        tokens = string.split(firstLine, '\t')
        for item in [cid, smi, exp, rel, val, unt]:
          indices[item] = tokens.index(item)
      else: #actual work
        tokens = string.split(line, '\t')
        good = True
        if 1 >= len(tokens):
          good = False
        if good: #do complete test for acceptable experiment
          good = False #must be set to true later
          if tokens[indices[exp]] in ["Activity", "Binding", "Concentration",
                 "Dose", "EC50", "ED50", "Effect", "Emesis", "I50", "IC50",
                 "Inhbition", "Kd", "Ki", "Km", "PDE"]:
            good = True
        if good and "" == tokens[indices[unt]]: #blank units is BAD
          good = False
        if good and "" == tokens[indices[exp]]: #blank experiment is BAD
          good = False
        if good and "" == tokens[indices[val]]: #blank value is BAD
          good = False
        if good and "nM" != tokens[indices[unt]]: #anything but this is rejected
          good = False
        if good and "%" == tokens[indices[unt]]: #% units is too hard to decode
          good = False
        if good and ">" == tokens[indices[rel]]: #greater than is useless
          good = False
        if good and "~" == tokens[indices[rel]]: #seriously?
          good = False
        if good and ">=" == tokens[indices[rel]]: #greater than is useless
          good = False
        if good and 10000. < float(tokens[indices[val]]): #10000 nM cutoff for now
          good = False
        if good:
          print tokens[indices[smi]], 'E00'+tokens[indices[cid]][-6:]
  except StopIteration:
    readIn.close()
  finally:
    pass
 
if -1 != string.find(sys.argv[0], "chembl2smi.py"):
  if len(sys.argv) > 1:
    doStuff(sys.argv[1])
  else:
    print "chembl2smi.py chembl.xls "




