#!/usr/bin/python

import zipfile2
wordlist = ['111', '123', 'password123', '98124']
for i in wordlist:
  	try:
	  zip = zipfile2.ZipFile('protected.zip', 'r')
	  zipfile2.ZipFile.extractall(zip, pwd=i)
	  print 'The Password is: ', i
	except:
	  continue
