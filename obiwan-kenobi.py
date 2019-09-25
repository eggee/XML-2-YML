#!/usr/bin/env python3.7

import xml.etree.ElementTree as ET
import sys

# argCount = len(sys.argv)
# if argCount == 3:
#     XML_Input = sys.argv[1]
#     YML_Output = sys.argv[2]
# else:
#     sys.exit("Insufficient number of arguments, please try again")
# try:
#     XML = open(XML_Input)
# except IOError:
#     sys.exit("Can't find the given input file, exiting gracefully")
#
# tree = ET.parse(XML_Input)
tree = ET.parse("XML-input.xml")
root = tree.getroot()


if tree._root._children[0].attrib['name'] == 'olt1':
    print("found it")
    print("Help me ObiWan Kenobi...")
    print("You're my only hope...")