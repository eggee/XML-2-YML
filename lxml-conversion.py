from lxml import etree


def parseXML(xmlfile):
    """
    Pars the xml
    :param xmlFile:
    :return:
    """
    with open(xmlfile) as fobj:
        xml = fobj.read().encode('utf-8')

    root = etree.fromstring(xml)

    for appt in root.getchildren():
        for elem in appt.getchildren():
            if not elem.text:
                text = "None"
            else:
                text = elem.text
            print(elem.tag + " => " + text)


if __name__ == "__main__":
    parseXML("resources/XML-Input.xml")
