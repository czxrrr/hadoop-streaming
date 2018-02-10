#!/usr/bin/env python

import sys
 
last_key = None
current_index = []
 
for input_line in sys.stdin:
	input_line = input_line.strip()
	this_key, value = input_line.split("\t", 1)
 
	if last_key == this_key:
		if value not in current_index:
       			current_index.append(value)
   	else:
       		if last_key:
           		print( "%s\t%s" % (last_key, str(current_index)) )
       		current_index = [value]
       		last_key = this_key
 
if last_key == this_key:
	print( "%s\t%s" % (last_key, str(current_index)) )
