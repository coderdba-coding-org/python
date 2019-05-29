#!/usr/bin/env python

import json
import yaml

def create_configmap_yaml(in_env):

  # Notes:
  # The {} next to data is only a placeholder - not really to be replaced using 'format' function
  # The attributes of 'data:' is set by array operations 
  #
  configmap = {
    'apiVersion': 'v1',
    'data': {},
    'kind': 'ConfigMap',
    'metadata': {
      'name': '{}-sd-config'.format(in_env.lower())
    }
  }

  
  print "configmap data field value before - " 
  print configmap ['data']
  print

  print "configmap before - "
  print yaml.dump (configmap)

  print
  print "PROCESSING data FIELD"
  print

  data1 = {"abc": "def"}
  
  # For 'data1' a semicolon gets applied automatically
  # The json.dumps is not so much for treating this configmap as json, 
  #  --> rather, it is a json input for something else in the configmap
  #
  configmap ['data']['data1'] = json.dumps(data1)
  print
  print "configmap after - "
  print yaml.dump (configmap)
  

# MAIN PROGRAM
create_configmap_yaml ('DEV')
