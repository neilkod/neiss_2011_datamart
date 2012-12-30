#!/bin/python
f = open('data/NEISS_SAS_formats.txt')
dims={}
dim_data={}
current_dim = None

for line in f.readlines():
  dt = line.strip()
  if dt.startswith('VALUE'):
    if current_dim != None:
      dims[current_dim]=dim_data
      dim_data={}
    # we found a new dim
    current_dim = dt.split(' ')[1]
    print current_dim
  elif dt.startswith('PROC FORMAT') or dt.startswith(';')\
      or dt=='' or dt.startswith('/*') or dt == 'RUN;':
    None
  else:
    # print "data:",current_dim,dt
    k,v = dt.split('=')
    dim_data[k]=v.replace('\'','')
dims[current_dim]=dim_data

