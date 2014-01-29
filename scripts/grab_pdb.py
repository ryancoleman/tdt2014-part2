#!/usr/bin/env python 
#ryan g. coleman ryangc@mail.med.upenn.edu 
#usage: grab_pdb.py pdbListFile

#grab system, string,  regular expression, and operating system modules
import sys, string, re, os, math

#http://www.rcsb.org/pdb/cgi/export.cgi/1GKL.pdb?format=PDB&pdbId=1GKL&compression=None
#http://www.rcsb.org/pdb/download/downloadFile.do?fileFormat=pdb&compression=NO&structureId=9ICD
#wget -b -O code URL

def getBiolUnit(code):
  filename = code + ".unit.pdb"
  if not os.path.exists(filename): #then download it  
    command = "wget -O " + filename + " \"http://www.pdb.org/pdb/files/" + code + ".pdb1\" "
    os.popen(command)
  return filename #filename of saved file

def getCode(code):
  filename = code + ".pdb"
  if not os.path.exists(filename): #then download it  
    command = "wget -O " + filename + " \"http://www.rcsb.org/pdb/cgi/export.cgi/" + code + ".pdb?format=PDB&pdbId=" + code + "&compression=None\" "
    os.popen(command)
  return filename #filename of saved file

if -1 != string.find(sys.argv[0], "grab_pdb.py"): 
  list = open(sys.argv[1], 'r')
  linesList = list.readlines()
  list.close()
  for line in linesList:
    for code in string.split(line):
      code = string.strip(code)
      getCode(code)
