#! /usr/bin/env python
import sys
import Image
import base64
#python $HADOOP_HOME/app/tgaFromstring.py image_width image_height
image_width = int(sys.argv[1]) 
image_height = int(sys.argv[2])
filename = sys.argv[3]
size = image_width,image_height

for line in sys.stdin.readlines():
	s = base64.b64decode(line)
	im = Image.fromstring("RGB", size, s)
	im.show()
	im.save("/home/hadoop/hadoop/app/output/" + filename)
	#print line
	#print "good"
