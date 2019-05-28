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

def url_list(offices):
  url_stub = '{}vm001.company.com'
  urls = [url_stub.format(office) for office in offices]
  return urls

# MAIN PROGRAM
print "reading arguments"

if __name__ == '__main__':

  args = parse_args()
  print args

  offices = []
  offices.append('city1')
  offices.append('city2')
  offices.append('city3')
  print offices

  urls = url_list(offices)
  print urls

