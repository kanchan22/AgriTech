#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys
#import numpy as np
#import matplotlib.pyplot as plt

current_crop = None
current_production = 0
crp = []
prdn = []
word = None

for line in sys.stdin:
    
    line = line.strip()
    word, count = line.split('\t', 1)
  


    try:
        count = int(count)
    except ValueError:
        continue
    
    if current_crop == word:
	#print '---------match'
        current_production += count
	
	
    else:
        if current_crop:
            print '%s\t%s' % (current_crop, current_production)
	    crp.append(current_crop)
	    prdn.append(current_production)
        current_production = count
        current_crop = word
	
	


if current_crop == word:
    print '%s\t%s' % (current_crop, current_production)
    
  
'''print crp
print prdn


y_pos = np.arange(len(crp))
plt.bar(y_pos ,prdn ,align='center' ,alpha=0.5)
plt.xticks(y_pos ,crp)
#plt.yticks(list , list3)
plt.ylabel('Production In 2000')
plt.xlabel('Crops')
plt.title('Total Production of crops in Respective Years ')
plt.show()'''

