#!/usr/bin/env python 
#ryan g. coleman ryangc@mail.med.upenn.edu 
#usage: grab_pdb_chain.py file

#grab system, string,  regular expression, and operating system modules
import sys, string, re, os, math
import grab_pdb #for getCode function
import pdb #for chain sorting ease

def getCodeChain(pdbCode, chain):
  fileName = grab_pdb.getCode(pdbCode)
  pdbD = pdb.pdbData(fileName)
  newPdbD = pdbD.getOneChain(chain)
  newPdbD.write(pdbCode + "." + chain + ".pdb")

def copyCode(pdbCode):
  fileName = grab_pdb.getCode(pdbCode)
  pdbD = pdb.pdbData(fileName)
  pdbD.write(pdbCode + ".-.pdb")

if -1 != string.find(sys.argv[0], "grab_pdb_chain.py"): 
  list = open(sys.argv[1], 'r')
  linesList = list.readlines()
  list.close()
  for line in linesList:
    tokens = string.split(line)
    if len(tokens) == 1: 
      code = string.strip(tokens[0])
      if len(code) == 4: #just pdb, no chain necessary
        copyCode(code)
      else:
        codePdb = code[:4]
        codeChain = code[4]
        getCodeChain(codePdb, codeChain)
    elif len(tokens) > 1:
      code = string.strip(tokens[0])
      chain = string.strip(tokens[1])
      getCodeChain(code, chain)


