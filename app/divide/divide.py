#! /usr/bin/env python
import sys
import Image

print "In divide.py:"

ratio = float(sys.argv[1])
maxlayer = int(sys.argv[2])

def devide(im):
	length = im[2] / 2
	four = [(im[0], im[1], length, im[3]+1), \
			(im[0]+length, im[1], length, im[3]+1), \
			(im[0], im[1]+length, length, im[3]+1), \
			(im[0]+length, im[1]+length, length, im[3]+1)]
	return four

def check(im):
	if im[3] == maxlayer: 
		return 1
	count = 0
	for i in range(im[2]):
		for j in range(im[2]):
			pix = originIm.getpixel((im[0]+i, im[1]+j))
			#print (im[0]+i, im[1]+j)
			if pix != (255, 255, 255):
				count += 1
	#print count
	if count >= ratio * total:
		#need to devide
		return 0
	else:
		#do not need to devide any more
		#print count
		return 1

def process(im):
	four = devide(im)
	for i in range(4):
		#print four[i]
		if check(four[i]):
			out = open("afterDevide", 'a')
			out.write(str(four[i][0]) + "," + str(four[i][1]) + \
						"," + str(four[i][2]) + ',\n')
			out.close()
		else:
			process(four[i])

print "Preparing: "
output = open("afterDevide", 'w')
originIm = Image.open("afterSimplize.tga")
origin = (0, 0, originIm.size[0], 0) #x, y, size, layer

total = 0
for i in range(origin[2]):
	for j in range(origin[2]):
		pix = originIm.getpixel((i, j))
		if pix != (255, 255, 255):
			total += 1
#print total

print "Begin dividing:"
process(origin)

print "Dividing successful."
		
