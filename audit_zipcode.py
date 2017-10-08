"""
The audit_zipcode function is aimed at grouping and counting appearing frequecies of 
certain postal code in the map data
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re

osm_file = open("new-york_new-york.osm", "r")

post_codes = []

def is_ny_zip(elem):
    return (elem.tag == "tag") and (elem.attrib['k'] =="addr:postcode")

def audit_zipcode(osm_file):
    postcode = {}

    for event, elem in ET.iterparse(osm_file):
        
        if is_ny_zip(elem):
            if elem.attrib['v'] in postcode:
                postcode[elem.attrib['v']] = postcode[elem.attrib['v']] + 1
            else:
                postcode[elem.attrib['v']] = 1

    return postcode