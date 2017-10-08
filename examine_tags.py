"""
Using the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
Fill out the count_tags function. It should return a dictionary with the 
tag name as the key and number of times this tag can be encountered in 
the map as value.

"""
import xml.etree.cElementTree as ET
import pprint

def count_tags(filename):
    count_tags = {}
    for event, elem in ET.iterparse(filename):
        if elem.tag not in count_tags:
            count_tags[elem.tag] = 1
        else:
            count_tags[elem.tag] += 1
    return count_tags

tags = count_tags('new-york_new-york.osm')
pprint.pprint(tags)