#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    
    line = line.strip()

    #print line
   
    words = line.split()
	
    #print words

    #print words[2]
    #print words[6]
 
    #for row in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
    print '%s\t%s' % (words[1], words[6])
#print (words[1], words[6])

