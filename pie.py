#!/usr/bin/env python

from operator import itemgetter
import sys

import numpy as np
import matplotlib.pyplot as plt

list1 = []
list2 = []
for line in sys.stdin:
    
	line = line.strip()

    	#print line
	words = line.split()
	list1.append(words[0])
	list2.append(words[1])
#print list1
#print list2

slices =list2
activities = list1
lcrime = list1
cols = ['y' ,'r' , 'g','b']
#explode = (0.06,0.06,0.06,0.06)
explode = (0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02)

plt.pie(slices, explode=explode ,labels=lcrime, colors=cols, autopct='%1.1f%%',shadow=True ,startangle=140)

plt.axis('equal')
plt.title('Crop production in Maharatsra')
#plt.xlabel('X axis')
plt.legend()
plt.show()

