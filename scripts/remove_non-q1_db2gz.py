#!/usr/bin/env python

#removes things with more than 1 charge

import string
import sys
import os
import shutil
import zip
import tempfile
import math

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
    #print outFileName
    outFile = gzip.open(outFileName, 'wb', 9)
    recordLines = []
    chargeOkay = False
    for lineCount, line in enumerate(db2file):
      if 0 == len(recordLines):
        recordLines.append(line)
      elif 1 == len(recordLines):  # line 2
                                   # M +CHA.RGEX +POLAR.SOL +APOLA.SOetc
        charge = math.floor(float(string.split(line)[1]))
        if charge == -1 or charge == 0 or charge == 1:
          chargeOkay = True
        recordLines.append(line)
      elif line[0] == 'E': #end of one record
        recordLines.append(line)
        if chargeOkay:
          for thisLine in recordLines:
            outFile.write(thisLine)
        recordLines = []
        chargeOkay = False
      else:
        recordLines.append(line)
  except (StopIteration, IOError):
    pass
  db2file.close()
  outFile.close()
  shutil.copy(outFileName, input)
  os.unlink(outFileName)
