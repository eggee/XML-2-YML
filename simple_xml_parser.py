#!/usr/bin/env python3.7

import xml.etree.ElementTree as ET
import sys

olt = str

argCount = len(sys.argv)
if argCount == 3:
    XML_Input = sys.argv[1]
    YML_Output = sys.argv[2]
else:
    sys.exit("Insufficient number of arguments, please try again")
try:
    XML = open(XML_Input)
except IOError:
    sys.exit("Can't find the given input file, exiting gracefully")

tree = ET.parse(XML_Input)

tree = ET.parse(XML_Input)
root = tree.getroot()

for child in root:
    print(child.tag)
    print(child.attrib)
    print(child.attrib['outer_vlan_id'])
    print(child.attrib['part_number'])
    print(child.attrib['product'])
    print(child.attrib['name'])

#
# if tree._root._children[0].attrib['name'] == 'olt1':
#     print("found it")
#     print("Help me ObiWan Kenobi...")
#     print("You're my only hope...")
#
#     print("onus:")
#     print("    OBJECT-TYPE: \"device\"")
#     print("    model-name: \"ta_401\"")
#     print("    INSTANCES:")
#     print("        - name: \"ont_5\"")
#     print("          interface-names: ['TECH Service']")
#     print("          object-parameters:")
#     print("              serial-number: \"ADTN18423D62\"")
#     print("              onu-id: \"5\"")
#
#




# for neighbor in root.iter('stat-channels'):
#     if neighbor.attrib.values()[1] == set_num:
#         total = neighbor[0][0].attrib
#         CC = total.get('percent-call-completions')