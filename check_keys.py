"""
Check the "k" value for each "<tag>" and see if there are any potential problems.

The function 'key_type' provides a count of each of four tag categories in a dictionary:
  "lower", for tags that contain only lowercase letters and are valid,
  "lower_colon", for otherwise valid tags with a colon in their names,
  "problemchars", for tags with problematic characters, and
  "other", for other tags that do not fall into the other three categories.
"""


import xml.etree.cElementTree as ET
import pprint
import re


"""
3 regular expressions provided by Udacity Data Analyst Nanodegree 
checking for certain patterns in the tags. 
"""
lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


def key_type(element, keys):
    if element.tag == "tag":
        key = element.attrib['k']
        if lower.search(key):
            keys['lower'] = keys['lower'] + 1
        elif lower_colon.search(key):
            keys['lower_colon'] = keys['lower_colon'] + 1
        elif problemchars.search(key):
            keys['problemchars'] = keys['problemchars'] + 1
        else:
            keys['other'] = keys['other'] + 1
            
    return keys


def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys


keys = process_map('new-york_new-york.osm')
pprint.pprint(keys)