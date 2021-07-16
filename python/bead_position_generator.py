
import os
import sys
from xml.dom import minidom, Node

folder = 'C:\\Users\\Sperry3\\acquisition\\'
basefolder = folder + 'create_xml\\'
position_file = basefolder + "positions.txt"
bead_position_file = basefolder + "bead_positions.txt"
#powerfolder = basefolder + 'powertest\\'
#conv_descriptor_file = basefolder + "conv.xml"
#reg_descriptor_file = basefolder + "bead_registration.xml"
#ffc_descriptor_file = basefolder + "ffc.xml"
#storm_descriptor_file = basefolder + "storm.xml"

#output_file = basefolder + "acquisition_master.xml"
#xdim = 1
#ydim = 1
#neuron_threshold = 2000


nl = "\n"
pause = 1
pos_fp = open(position_file, "r")
bead_pos_fp = open(bead_position_file, "r")
#out_fp = open(output_file, "w")

# Load position data
x_pos = []
y_pos = []
while 1:
    line = pos_fp.readline()
    if not line: break
    [x, y] = line.split(",")
    x_pos.append(float(x))
    y_pos.append(float(y))
   

# Load bead position data and generate registration and ffc bead positions
b_x_pos = []
b_y_pos = []
while 1:
    line = bead_pos_fp.readline()
    if not line: break
    [x, y] = line.split(",")
    b_x_pos.append(float(x))
    b_y_pos.append(float(y))
r1_x_pos = []
r1_y_pos = []
r2_x_pos = []

r2_y_pos = []
f_x_pos = []
f_y_pos = []

for x in range (0, 28, 7):
  for y in range (0, 28, 7):
    region1_list = str((b_x_pos[0] + float(x))) + ", "  + str(b_y_pos[0] + float(y))
    #print region1_list
    region1 = open(basefolder + "bead_field_1.txt", "a")
    region1.write(region1_list + "\n")


for x in range (0, 60, 20):
  for y in range (0, 60, 20):
    region1_list = str((b_x_pos[2] + float(x))) + ", "  + str(b_y_pos[2] + float(y))
    #print region1_list
    region1 = open(basefolder + "ffc_bead_field.txt", "a")
    region1.write(region1_list + "\n")
    

for x in range (0, 28, 7):
  for y in range (0, 28, 7):
    region1_list = str((b_x_pos[1] + float(x))) + ", "  + str(b_y_pos[1] + float(y))
    #print region1_list
    region1 = open(basefolder + "bead_field_2.txt", "a")
    region1.write(region1_list + "\n")

# this last section writes an additional file, which is necessary to complete
# the full string list of positions from the last list
# goofy, but works
for x in range (0, 28, 7):
  for y in range (0, 28, 7):
    region1_list = str((b_x_pos[2] + float(x))) + ", "  + str(b_y_pos[2] + float(y))
    #print region1_list
    region1 = open(basefolder + "dummy.txt", "a")
    region1.write(region1_list + "\n")
    region1.close()
    os.remove(basefolder + "dummy.txt")

