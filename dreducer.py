#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_year = None
current_production = 0
word = None

for line in sys.stdin:
    
    line = line.strip()

    
    word, count = line.split('\t', 1)

   
    try:
        count = int(count)
    except ValueError:
        continue

   
    if current_year == word:
        current_production += count
    else:
        if current_year:
            print '%s\t%s' % (current_year, current_production)
        current_production = count
        current_year = word
	

if current_year == word:
    print '%s\t%s' % (current_year, current_production)


