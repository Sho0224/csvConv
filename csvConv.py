#!/usr/bin/env python
import argparse
import pandas
import pylab as plt
import datetime
import matplotlib
import os
def main():
  psr = argparse.ArgumentParser()
  psr.add_argument('path')
  psr.add_argument('-o','--output',action='store_true')
  psr.add_argument('-a','--all', action='store_true')
  args = psr.parse_args()
  if args.all:
    files = os.listdir(args.path)

    for file in files:
      if file.find('csv') > -1:
        generatePlot(args.path, args.output)
  else:
    generatePlot(args.path, args.output)

def generatePlot(path,isOutput):
  nonExtFilepath, ext = os.path.splitext(path)
  filename, ext = os.path.splitext( os.path.basename(path) )

  df = pandas.read_csv(path)
  df.columns = ['time', 'timestamp/relative', 'motorspeed', 'speedctl', 'motorkt_raw', 'type', 'motorperiod', 'fault', 'motorcurrent_raw']
  datetimeList = []
  for key,column in df.iteritems():
    if(key == 'time'):
      for val in column:
        tmpDatetime = datetime.datetime.fromtimestamp(val) + datetime.timedelta(hours=10)
        datetimeList.append(tmpDatetime)
  # print(datetimeList)
  df['datetime'] = datetimeList
  # print(df)
  ax = df.plot(x='datetime', y='motorspeed',linewidth=1,linestyle='-',rot=90)

  xfmt = matplotlib.dates.DateFormatter("%H:%M:%S")
  xloc = matplotlib.dates.MinuteLocator()
  ax.xaxis.set_major_locator(xloc)
  ax.xaxis.set_major_formatter(xfmt)
  # startDate = datetime(2017,9,8,6,20)
  # plt.plot(['06:16:00', 0], ['06:16:00', 200], 'k-', lw=2)
  plt.title(filename)
  plt.ylim([100, 120])

  if (isOutput):
    outputFilepath = nonExtFilepath + '.png'
    print(outputFilepath)
    plt.savefig(outputFilepath)
  else:
    plt.show()
if __name__ == '__main__': main()
