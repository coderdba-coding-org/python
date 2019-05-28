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


# MAIN PROGRAM
print "reading arguments"

if __name__ == '__main__':
  args = parse_args()

  print args

