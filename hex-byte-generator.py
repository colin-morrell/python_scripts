#!/usr/bin/python

# I couldn't find a script to generate a list of all 256 hex bytes, so I wrote one.
# This format is good for testing for buffer overflows, etc.

string = ""
temp = ""

for o in range(256):
	temp = hex(o)
	if len( temp ) == 3:
		temp=temp[:2]+'0'+temp[2:]
	temp=temp[1:]
	string = string + '\\' + temp

print string
