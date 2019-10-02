#!/usr/bin/env python3.7

import xml.etree.ElementTree as ET
import sys

class Onu():
    """
    This will format the new ONU Yaml entity which will look like below

    onus:
    OBJECT-TYPE: "device"
    model-name: "ta_401"
    INSTANCES:
        - name: "ont_5"
          interface-names: ['TECH Service']
          object-parameters:
              serial-number: "ADTN18423D62"
              onu-id: "5"
    """
    def __init__(self, model_name, name, interface_names, serial_number, onu_id):
        self.model_name = model_name
        self.name = name
        self.interface_names = interface_names
        self.serial_number = serial_number
        self.onu_id = onu_id

class Olt():
    """
    This will format the new ONU Yaml entity which will look like below

    olts:
    model-name: "16-port TECH BOX"
    management-domain-static-ipv4:
        mask: "255.255.255.0"
        gateway: "10.214.254.254"
    INSTANCES:
        - name: "olt3"
          management-domain-static-ipv4:
              ip-address: "10.214.254.47"
    """

    def __init__(self, model_name, mask, gateway, name, ip_address):
        self.model_name = model_name
        self.mask = mask
        self.gateway = gateway
        self.name = name
        self.ip_address = ip_address


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

for child in root:
    if child == 'outer_vlan_id':
        print(child.attrib['outer_vlan_id'])
        print(child.attrib['outer_vlan_id'])
        print(child.attrib['outer_vlan_id'])

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