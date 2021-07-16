import xml.etree.cElementTree as ET
from xml.etree.cElementTree import ElementTree, Element

tree = ET.parse('C:\\Users\\Sperry3\\acquisition\\create_xml\\master_xml_hcam_SCN_run.xml')
root = tree.getroot()
pause = Element('DAPause')

#for child in root.findall(".//*[@name='Regbead_1_00']"):
 #       child.insert(1, pause)
#for child in root.findall(".//*[@name='IRbead_2_00']"):
#        child.insert(1, pause)
#for child in root.findall(".//*[@name='IRconv_00']"):
#        child.insert(1, pause)
#for child in root.findall(".//*[@name='IRFFC_0']"):
#        child.insert(1, pause)
for child in root.findall(".//*[@name='750storm_000']"):
        child.insert(1, pause)
for child in root.findall(".//*[@name='750storm_00']"):
        child.insert(1, pause)
#for child in root.findall(".//*[@name='750storm_0']"):
#        child.insert(1, pause)
#for child in root.findall(".//*[@name='488storm_00']"):
#        child.insert(1, pause)
for child in root.findall(".//*[@name='561storm_000']"):
        child.insert(1, pause)
for child in root.findall(".//*[@name='561storm_00']"):
        child.insert(1, pause)
#for child in root.findall(".//*[@name='488storm_00']"):
#         child.insert(1, pause)        
tree.write('master_xml_hcam_SCN_run_pause.xml')
