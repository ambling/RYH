#! /usr/bin/env python
import sys
import os
import base64
import Image

#python mapper.py xml_filename image_width image_height
xml_filename = sys.argv[1]
#image_width = int(sys.argv[2]) 
#image_height = int(sys.argv[3])
#size = image_width,image_height

for line in sys.stdin:
	if line == '': continue
	numbers = line.split(',')
	origin_file = open(xml_filename, 'r')
	render_file = open("render.xml", 'w')
	word = origin_file.readline()
	while word != '':
		w_index = word.find("<width ")
		h_index = word.find("<height ")
		x_index = word.find("<xstart ")
		y_index = word.find("<ystart ")
		if w_index != -1:
			word = '	<width ival="' + numbers[0] + '"/>' + '\n'
		elif h_index != -1:
			word = '	<height ival="' + numbers[1] + '"/>' + '\n'
		elif x_index != -1:
			word = '	<xstart ival="' + numbers[2] + '"/>' + '\n'
		elif y_index != -1:
			word = '	<ystart ival="' + numbers[3] + '"/>' + '\n'
		render_file.write(word)
		word = origin_file.readline()
	origin_file.close()
	render_file.close()
	os.system('yafaray-xml render.xml >> not_used')
	
	im = Image.open("yafaray.tga")
#large_im = Image.new(im.mode, size, "#ffffff")
	
#box = (int(numbers[2]), int(numbers[3]), int(numbers[2])+int(numbers[0]), int(numbers[3])+int(numbers[1]))
#large_im.paste(im, box)

#s = large_im.tostring()
#out = base64.b64encode(s)
	s = im.tostring()
	line = line[:-1]
	out = line + base64.b64encode(s)
	print out
	os.system("rm yafaray.tga")
	os.system("rm not_used")

