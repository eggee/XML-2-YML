import xml.etree.ElementTree as ET
import sys

#project://PQ_Production_Project/Python_Libraries/cp_Python_Procedures.fftc#Py_ParseAbacusResultXML
# -XML C:\\Abacus_Results\\BBDLC_System_InterMix_MGCP_SIP_GR303.xml
# -Script GR303-to-MGCP-N18S4Rpots-to-N18S5A2c
# to execute: >python tje-Abacus-Result-parsing.py $XML $Script

argCount = len(sys.argv)
if argCount == 3:
    Result_XML = sys.argv[1]
    script = sys.argv[2]
else:
    sys.exit("Insufficient number of arguments, abort execution")
try:
    XML = open(Result_XML)
except IOError:
    sys.exit("The file does not exist, exiting gracefully")

tree = ET.parse(Result_XML)
root = tree.getroot()

#Gets the Set# for the given Script Name
for neighbor in root.iter('set'):
    if neighbor[3][2].text == script:
        set_num = neighbor.attrib.values()[0]

neighbor.attrib.values()[1] = 0
for neighbor in root.iter('stat-channels'):
    if neighbor.attrib.values()[1] == set_num:
        total = neighbor[0][0].attrib
        CC = total.get('percent-call-completions')
        SC = total.get("percent-script-completions")
        print '<?xml version="1.0" encoding="ISO-8859-1"?>'
        print "<ParsingResults>"
        print '<' + "Script_Completion_Percentage" + '>' + SC + '</' + "Script_Completion_Percentage" + '>'
        print '<' + "Call_Completion_Percentage" + '>' + CC + '</' + "Call_Completion_Percentage" + '>'
        print "</ParsingResults>"
        sys.exit()
if neighbor.attrib.values()[1] != set_num:
	sys.exit("No channels are assigned for the set number")

