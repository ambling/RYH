#! /usr/bin/env python
import sys
import Image, ImageDraw

#print "Please input the image file name:"
#filename = sys.stdin.readline()
#filename = filename[:-1]
#filename = sys.argv[1]

#print "Please input the input file name:"
#inputfile = sys.stdin.readline()
#inputfile = inputfile[:-1]
#inputfile = sys.argv[2]

jobname = sys.argv[1]

infile = open("/home/hadoop/hadoop/app/output/" + jobname + "_input", 'r')

im = Image.open("/home/hadoop/hadoop/app/output/" + jobname + "_byhadoop.tga")
draw = ImageDraw.Draw(im)

pieces = infile.readlines()
for piece in pieces:
	coor = piece.split(',')
	draw.rectangle([int(coor[2]), int(coor[3]), \
			int(coor[2])+int(coor[0]), int(coor[3])+int(coor[1])], outline=255)

del draw
#im.save("show_"+filename)
im.save("/home/hadoop/hadoop/app/output/" + jobname + "_byhadoop_show.tga")
