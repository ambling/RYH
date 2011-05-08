#! /usr/bin/env python
import sys
import os

print "In simplize.py:"

print "Opening files:"
filename = sys.argv[1]
small_size = sys.argv[2]

#os.system("cp $HADOOP_HOME/app/xmls/" + filename + " " + filename)
os.system("cp $HADOOP_HOME/app/divide/simplest_material.xml simplest_material.xml")
os.system("cp $HADOOP_HOME/app/divide/simplest_background.xml simplest_background.xml")

infile = open(filename, 'r')
material_file = open("simplest_material.xml", 'r')
background_file = open("simplest_background.xml", 'r')
outfile = open("afterSimplize.xml", 'w')

print "Generating afterSimplize.xml:"
#0 for not changed, 1 for inside the area but not changed, -1 for changed but outside area, -2 for changed and inside area
material = 0 
background = 0
mesh = 0
camera = 0
render = 0

for line in infile.readlines():	
	if (material == 1 or material == -2) and line != "</material>\n" :
		continue
	elif material == -2 and line == "</material>\n" :
		material = -1;
		continue
	elif material == 1 and line == "</material>\n" :
		material = -1;
		for m_word in material_file.readlines():
			outfile.write(m_word)
		continue
			
	if (background == 1 or background == -2) and line != "</background>\n" :
		continue
	elif background == -2 and line == "</background>\n" :
		background = -1;
		continue
	elif background == 1 and line == "</background>\n" :
		background = -1;
		for b_word in background_file.readlines():
			outfile.write(b_word)
		continue
	
	if mesh == 1 and line == "</mesh>\n":
		mesh = 0
		outfile.write(line)
		continue
	elif mesh == 1:
		index = line.find("<set_material")
		if index != -1:
			line = '			<set_material sval="Material"/>\n'
		outfile.write(line)
		continue
		
	if camera == 1 and line == "</camera>\n":
		camera = 0
		outfile.write(line)
		continue
	elif camera == 1:
		cx_index = line.find("<resx")
		cy_index = line.find("<resy")
		if cx_index != -1:
			line = '	<resx ival="' + small_size + '"/>\n'
		if cy_index != -1:
			line = '	<resy ival="' + small_size + '"/>\n'
		outfile.write(line)
		continue

	if render == 1 and line == "</render>\n":
		render = 0
		outfile.write(line)
		continue
	elif render == 1:
		rx_index = line.find("<width")
		ry_index = line.find("<height")
		if rx_index != -1:
			line = '	<width ival="' + small_size + '"/>\n'
		if ry_index != -1:
			line = '	<height ival="' + small_size + '"/>\n'
		outfile.write(line)
		continue
		
	if line[0:9] == "<material":
		if material == 0:
			material = 1
		else:
			material = -2
		continue	
	if line[0:11] == "<background":
		if background == 0:
			background = 1
		else:
			background = -2
		continue	
	if line[0:5] == "<mesh":
		mesh = 1
		outfile.write(line)
		continue
	if line[0:7] == "<camera":
		camera = 1
		outfile.write(line)
		continue
	if line == "<render>\n":
		render = 1
		outfile.write(line)
		continue
	outfile.write(line)

outfile.close()
#os.system("rm " + filename)
os.system("rm simplest_material.xml")
os.system("rm simplest_background.xml")

print "Pre-rendering:"
#os.system("yafaray-xml afterSimplize.xml >> not_used")	
os.system("yafaray-xml afterSimplize.xml")	
os.system("mv yafaray.tga afterSimplize.tga")

print "Simplization successful."
