#!/usr/bin/python
"""
Sample usage for SimpleEvcorrWrapper.

Requires accompanying files:
* sample.conf
* sample.input

If sec is not installed, you will hear about it from SimpleEvcorrWrapper __init__().
"""

import json

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import SimpleEvcorrWrapper

foo = SimpleEvcorrWrapper.SimpleEvcorrWrapper(conf_path="sample.conf")
events = foo.start("sample.input")
for event in events:
    thing = json.loads(event)
    print "{} duration: {}".format(thing['name'], thing['stop'] - thing['start'])
    if thing['name'] == "john":
        foo.stop()
print "Done"

