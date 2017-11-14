#!/usr/bin/env python
import argparse
import pandas
import pylab as plt
from datetime import datetime
import matplotlib
import os
import subprocess

def main():
  psr = argparse.ArgumentParser()
  psr.add_argument('path')
  psr.add_argument('-m','--mode',default = 'v')
  args = psr.parse_args()
  nonExtFilepath, ext = os.path.splitext(args.path)
  filename, ext = os.path.splitext( os.path.basename(args.path) )

  files = os.listdir(args.path)

  for file in files:
    if file.find('csv') > -1:
      cmd = "python csvConv.py " + file + " -m f" 
      print cmd
      subprocess.call( cmd, shell=True ) 
if __name__ == '__main__': main()
