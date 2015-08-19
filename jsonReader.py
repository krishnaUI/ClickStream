#!/usr/bin/python
import json
import time
import sys
#def jsonRead(line):

for line in sys.stdin:
	try:	
		clickStream=json.loads(line)
		date    = clickStream["t"]
		month   = time.gmtime(date)[1]
		country = clickStream["c"]
		url     = clickStream["u"]
		j	= 0
		s	= ""
		for i in url:
			
			if(i=="/"):
				j+=1
			if(j!=3):
				s+=i
			else:
				break	
		print str(s),country,month
		#print str(url)str(country)+"\t"+str(month)
		
	except KeyError:
		s="sa"
	except ValueError:
		s="sa"
