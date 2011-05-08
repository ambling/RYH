#! /usr/bin/env python
import sys
import Image, ImageDraw

print "Please input the image file name:"
filename = sys.stdin.readline()
filename = filename[:-1]

print "Please input the input file name:"
inputfile = sys.stdin.readline()
inputfile = inputfile[:-1]

im = Image.open(filename)
draw = ImageDraw.Draw(im)

pieces = inputfile.readlines()
for piece in pieces:
	coor = piece.split(',')
	draw.rectangle([int(coor[2]), int(coor[3]), \
			int(coor[2])+int(coor[1]), int(coor[3])+int(coor[0])], outline=255)

del draw
im.save(filename+"_show")

