#!/usr/bin/env python

import sys
import argparse

import requests
import yaml
import json
import os


# FUNCTIONS
def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '--name'
  )
  parser.add_argument(
    '--surname',
    nargs='+'
  )
  return parser.parse_args()

def function_stub (in_list, function_name):

  # 'getattr' makes the argument string function_name as a module-name (that is, actual function to be called)
  # -- somewhat similar to class-for-name in java
  # so, essentially, this calls function_name(in_list) as a function

  the_list = getattr(sys.modules[__name__], function_name)(in_list)

  return [{ "targets": the_list }]

def function_a(in_list):
  print 
  print "in function_a"
  print  __name__
  print

  # Here there are two {} - they are replaced by the format function in the order of the arguments to format()
  target_stub = '{}vm000{}.company.com'
  targets = [target_stub.format(item, i) for item in in_list for i in range(1, 4)]
  return targets

# MAIN PROGRAM

if __name__ == '__main__':
  
  #print "reading arguments"
  #args = parse_args()
    #print args

  in_list = ['abc', 'def']

  out_list = function_stub (in_list, 'function_a')
  print out_list
