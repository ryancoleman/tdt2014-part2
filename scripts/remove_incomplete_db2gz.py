#!/usr/bin/env python

#due to stupid cluster issues, old code produces these
#X      1003  30    351   +6.8084   -3.1632   -7.8126                            
# X      1004  31    351   +5.7896   -2.640M     ZINC52473197        98  
#find them and remove them

import string, sys, os, shutil, gzip #i need these, i need them all
import tempfile

if len(sys.argv) > 1:
  inputFiles = sys.argv[1:]
else:
  print 'no .db2.gz files given!'
  sys.exit(1)
for input in inputFiles:
  print "running", input, " now"
  try:
    db2file = gzip.open(input, 'rb')
    outFileName = tempfile.NamedTemporaryFile(dir='.', delete=False).name
    outFile = gzip.open(outFileName, 'wb', 9)
    recordLines = []
    for lineCount, line in enumerate(db2file):
      if 0 == len(recordLines):
        recordLines.append(line)
      elif line.find('M    ') != -1: #this is bad, just dump it.
        position = line.find('M    ')
        recordLines = [line[position:]] #dump everything before this, start over
        print "broken file", input, " repaired at line", lineCount
      elif line[0] == 'E': #end of one record
        recordLines.append(line)
        for thisLine in recordLines:
          outFile.write(thisLine)
        recordLines = []
      else:
        recordLines.append(line)
  except StopIteration:
    pass
  db2file.close()
  outFile.close()
  shutil.copy(outFileName, input)
  os.unlink(outFileName)
    
