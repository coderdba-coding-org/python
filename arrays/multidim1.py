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

  #args = parse_args()
  #print args

  offices = []
  offices.append('city1')
  offices.append('city2')
  offices.append('city3')
  print offices

  mdarray = values_yaml['prometheus']['server']['extraConfigmapMounts']
  for env in envs:
    extraconfigmapmounts.append({
      'name': '{}-sd-config'.format(env),
      'mountPath': '/file_sd_configs/{}'.format(env),
      'configMap': '{}-sd-config'.format(env),
      'readOnly': True
    })
