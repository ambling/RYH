#! /usr/bin/env python
import sys
import os

print "Please input the job name:"
job_name = sys.stdin.readline()
job_name = job_name[:-1]

print "Please input the XML file name:"
xml_file = sys.stdin.readline()
xml_file = xml_file[:-1]

print "Please input the width:"
width = sys.stdin.readline()
width = width[:-1]

print "Please input the height:"
height = sys.stdin.readline()
height = height[:-1]

os.system("python simplize.py " + xml_file + " 64")
os.system("python divide.py 0.2 8")
os.system("python pre.py " + width + " " + height + " 64")
demand = "cat input | python mapper.py " + xml_file + " | python reducer.py " \
		+ width + " " + height + " | python tgaFromstring.py " + width + " " \
		+ height + " " + job_name
os.system(demand)

os.system("rm afterSimplize.xml")
os.system("rm afterSimplize.tga")
os.system("rm afterDevide")
os.system("rm input")
