#!/usr/bin/env python

import sys

for line in sys.stdin:
	line = line.strip()
	row = line.split('\t')
	if len(row)<19:
		continue
	id=row[0]
	body= row[4]
	body=body.strip()
	#print body
	for ch in [',','.',"!","?",":",";","\"","(",")",'<',">","[","]","#","$","=","-","/"]:
		body=body.replace(ch,' ')
	body=body.split()
	#print body
	for word in body:
		print( "%s\t%s" % (word, id) )
