# This .py file is used to manually correct discrepancy of coordinates between Steve 60* and 40*.

# This file can only work under current the directory (C:\Users\Sperry\Desktop\acquisition\create_xml\)
# Both positions.txt and bead_positions.txt will be corrected.

# Important: the offset value (as shown in Steve, offset for 60*) should be entered manually. (4* offset value should be 0)

# Last modified on 7.23.2018

import os

xoffset = input('Input: x offset: ')
yoffset = input('Iput: y offset: ')
xoffset = 0 - int(xoffset)
yoffset = 0 - int(yoffset)

with open('positions.txt','r+') as f:
    with open('positions_fixed.txt','w+') as new:
        for line in f:
            a=line
            a=a.rstrip()
            a=a.split(',')
            x=float(a[0])
            y=float(a[1])
            x=x+xoffset
            y=y+yoffset
            
            new.write('%d,%d\n' % (x,y))
os.remove('positions.txt')
os.rename('positions_fixed.txt','positions.txt')

with open('bead_positions.txt','r+') as f:
    with open('bead_positions_fixed.txt','w+') as new:
        for line in f:
            a=line
            a=a.rstrip()
            a=a.split(',')
            x=float(a[0])
            y=float(a[1])
            x=x+xoffset
            y=y+yoffset
            
            new.write('%d,%d\n' % (x,y))
os.remove('bead_positions.txt')
os.rename('bead_positions_fixed.txt','bead_positions.txt')

print('Done!')
