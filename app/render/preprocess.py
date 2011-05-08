#! /usr/bin/env python
import sys

in_file = open("input", 'w')

#python $HADOOP_HOME/app/preprocess.py image_width image_height devide_num
width = int(sys.argv[1]) 
height = int(sys.argv[2])
x_count = int(sys.argv[3])
y_count = int(sys.argv[4])

x = 0
y = 0
count = 0
while y < height:
	h = height / y_count
	if y + h >= height:
		h = height - y

	while x < width:
		w = width / x_count
		if x + w >= width:
			w = width - x
			
		line =  str(count) + ',' + str(w) + "," + str(h) + \
			"," + str(x) + "," + str(y) + ",\n"
		in_file.write(line)
		count += 1
		x += w
	y += h
	x = 0

