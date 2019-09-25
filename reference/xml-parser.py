#next draft to use 'dictionaries' instead of passing long line of variable to/from function
# 1) get the 'script-comment' results
# 2) get the 'test_run_info.'
#Use these command line parameters in the initial test call
#C:/Abacus_Results/BBDLC_CPOTS_BulkCall_LoadTest_via_CrossConnects.xml N26S3-48p

import xml.etree.ElementTree as ET
import sys

# Give the Abacus Results file path/name that is in the xml format
Result_XML = "XML-Input.xml"
# Give the 'script name' (from the environment partition&timing table) for which to parse for results
script = "N26S3-48p"

def open_the_xml_report(Result_XML):
    tree = ET.parse(Result_XML)
    root = tree.getroot()

    return root

def get_test_run_info(root):
    #initialize a local dictionary
    dict = {}
    #Search the 'root' for a tag called 'test-status'
    for neighbor in root.iter('test-status'):
        test_status = neighbor.attrib
        start_time_with_space = test_status.get('start')
        start_time = start_time_with_space.replace(" ", "_")
        dict['start_time'] = start_time
        stop_time_with_space = test_status.get('end')
        dict['stop_time'] = stop_time_with_space.replace(" ", "_")
        dict['run_time'] = test_status.get ('elapsed')

    return dict

def get_script_results_info(set_num, root):
    # for the given 'set_num" - get the results
    #Search for 'stat-channels', then compare it's 'set_num'
    dict2 = {}
    for neighbor in root.iter('stat-channels'):
        if neighbor.attrib.values()[1] == set_num:
            total_channel_stats = neighbor[0][0].attrib
            single_channel_stats = neighbor[1].attrib
            dict2['percent_callcompletions'] = total_channel_stats.get('percent-call-completions')
            dict2['percent_scriptcompletions'] = total_channel_stats.get("percent-script-completions")
            dict2['call_attempts_per_sec'] = total_channel_stats.get ('call-attempts-per-sec')
            dict2['Total_call_attempts'] = total_channel_stats.get('call-attempts')
            dict2['Total_Script_attempts'] = total_channel_stats.get ('script-attempts')
            dict2['call_cycles'] = single_channel_stats.get ('call-attempts')

        if neighbor.attrib.values()[1] == 0:
            sys.exit("Set Number is not there in Result XMl File")

    return dict2

#MAIN
def main():

    root = open_the_xml_report(Result_XML)
    set_num = get_the_setnum(root, script)

    run_info = get_test_run_info(root)
    print "\n *** Abacus Test Run Info. for %s ***\n" % script
    print "Start Time:", run_info['start_time']
    print "Stop Time:", run_info['stop_time']
    print "Run  Time:", run_info['run_time']

    results_info = get_script_results_info(set_num, root)
    print "\n *** Results Info. for %s ***\n" % script
    print "Percent Call Completions:\t", results_info['percent_callcompletions']
    print "Percent Script Completions:\t", results_info['percent_scriptcompletions']
    print "Call Attempts per Second:\t", results_info['call_attempts_per_sec']
    print "Total Call Attempts:\t\t", results_info['Total_call_attempts']
    print "Total Script Attempts:\t\t", results_info['Total_Script_attempts']
    print "Total Call Attempts:\t\t", results_info['call_cycles']

#Run Main
main()
