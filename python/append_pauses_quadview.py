import xml.etree.cElementTree as ET
from xml.etree.cElementTree import ElementTree, Element

tree = ET.parse('C:\\Users\\Sperry3\\aquisition\\create_xml\\master_xml_quadview_run.xml')
root = tree.getroot()
pause = Element('DAPause')

for child in root.findall(".//*[@name='IRbead_1_00']"):
        child.insert(1, pause)
for child in root.findall(".//*[@name='IRconv_00']"):
        child.insert(1, pause)
for child in root.findall(".//*[@name='IRFFC_0']"):
        child.insert(1, pause)
for child in root.findall(".//*[@name='750storm_00']"):
        child.insert(1, pause)
for child in root.findall(".//*[@name='488storm_00']"):
        child.insert(1, pause)        
tree.write('master_xml_quadview_run.xml')
