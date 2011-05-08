#! /usr/bin/env python
import sys
import Image
import base64

width = int(sys.argv[1])
height = int(sys.argv[2])
size = width,height
large_im = Image.new('RGB', size)

for line in sys.stdin:
	if line == '\n' or line[0] == '\t' or line == '': continue
	numbers = line.split(',')
	box = (int(numbers[2]), int(numbers[3]), \
		int(numbers[2])+int(numbers[0]), int(numbers[3])+int(numbers[1]))
	small_size = int(numbers[0]), int(numbers[1])
	im = Image.fromstring("RGB", small_size, base64.b64decode(numbers[4]))
	large_im.paste(im, box)

s = large_im.tostring()
out = base64.b64encode(s)
print out
