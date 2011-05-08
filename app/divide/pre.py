#! /usr/bin/env python
import sys

print "In pre.py:"

print "Opening files:"
infile = open("afterDevide", 'r')
outfile = open("input", 'w')

width = sys.argv[1]
height = sys.argv[2]
small_size = int(sys.argv[3])

def diff(x):
	result = float(x) / small_size - int(x) / small_size
	return result

print "Generating input file:"
for line in infile.readlines():
	if(line == ''): continue
	
	numbers = line.split(',')
	x_start = int(numbers[0]) * int(width) / small_size
	y_start = int(numbers[1]) * int(height) / small_size
	s_width = int(numbers[2]) * int(width) / small_size
	s_height = int(numbers[2]) * int(height) / small_size
	
	if(diff(int(numbers[0]) * int(width) ) > diff((int(numbers[0]) + int(numbers[2])) * int(width))):
		s_width += 1
	if(diff(int(numbers[1]) * int(height) ) > diff((int(numbers[1]) + int(numbers[2])) * int(height))):
		s_height += 1
		
	outline = str(s_width) + "," + str(s_height) + "," + \
			str(x_start) + "," + str(y_start) + ",\n";
	outfile.write(outline)
	
print "Input file generation successful."
