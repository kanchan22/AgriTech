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

y_pos = np.arange(len(list1))
plt.bar(y_pos ,list2 ,align='center' ,alpha=0.5)
plt.xticks(y_pos , list1)
	#plt.yticks(list , list3)
plt.ylabel('Production In 2000')
plt.xlabel('Crops')
plt.title('Total Production of crops in Respective Years ')
plt.show()
