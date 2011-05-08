#! /usr/bin/env python
import sys
import os
import time

def findWidth(filename):
	infile = open(filename, 'r')
	word = infile.readline()
	while word != '':
		w_index = word.find("<width ")
		if w_index != -1: #eg. <width ival="800"/>
			return word[w_index+13 : -4]
		word = infile.readline()
	infile.close()

def findHeight(filename):
	infile = open(filename, 'r')
	word = infile.readline()
	while word != '':
		h_index = word.find("<height ")
		if h_index != -1: #eg. <height ival="600"/>
			return word[h_index+14 : -4]
		word = infile.readline()
	infile.close()


print "Please input the job name:"
job_name = sys.stdin.readline()
job_name = job_name[:-1]

print "Please input the XML file name:"
xml_file = sys.stdin.readline()
xml_file = xml_file[:-1]

os.system("cp $HADOOP_HOME/app/xmls/" + xml_file + " " + xml_file)
#print "Please input the width:"
#width = sys.stdin.readline()
#width = width[:-1]
image_width = findWidth(xml_file)

#print "Please input the height:"
#height = sys.stdin.readline()
#height = height[:-1]
image_height = findHeight(xml_file)

#print width
#print height

os.system("python $HADOOP_HOME/app/divide/simplize.py " + xml_file + " 64")
os.system("python $HADOOP_HOME/app/divide/divide.py 0.05 5")
os.system("python $HADOOP_HOME/app/divide/pre.py " + image_width + " " + image_height + " 64")

os.system("rm afterSimplize.xml")
os.system("rm afterSimplize.tga")
os.system("rm afterDevide")
#input file has been generated

print "$HADOOP_HOME/bin/hadoop fs -mkdir /" + job_name + ":"
os.system("$HADOOP_HOME/bin/hadoop fs -mkdir /" + job_name)  #need to check if exists
print "$HADOOP_HOME/bin/hadoop fs -put input /" + job_name + ":"
os.system("$HADOOP_HOME/bin/hadoop fs -put input /" + job_name)
os.system("mv input $HADOOP_HOME/app/output/"+job_name+'_input')

hadoop_command = "$HADOOP_HOME/bin/hadoop jar " \
		+ "$HADOOP_HOME/contrib/streaming/hadoop-0.20.2-streaming.jar "\
		+ "-D mapred.reduce.tasks=1 "\
		+ "-D mapred.map.tasks=4 "\
		+ "-input /" + job_name + "/input "\
		+ "-output /" + job_name + "/output "\
		+ '-mapper "python mapper.py ' + xml_file + '" '\
		+ '-reducer "python reducer.py ' + image_width + ' ' + image_height + '" '\
		+ "-file $HADOOP_HOME/app/render/mapper.py "\
		+ "-file $HADOOP_HOME/app/render/reducer.py "\
		+ "-file $HADOOP_HOME/app/xmls/" + xml_file + " "

print "Begin rendering:"
s1 = time.time()
os.system(hadoop_command)
e1 = time.time()

print "Hadoop process over."

print "Getting output file from hadoop:"
os.system("$HADOOP_HOME/bin/hadoop fs -get /"+job_name+"/output/part* $HADOOP_HOME/app/output/"+job_name)
os.system("cat $HADOOP_HOME/app/output/"+job_name + " | python $HADOOP_HOME/app/render/tgaFromstring.py "\
		+ image_width + ' ' + image_height + ' ' + job_name + '_byhadoop.tga')
os.system("python $HADOOP_HOME/app/output/showdivide.py " + job_name)

os.system("rm " + xml_file)
print "Rendering successful."
print "Redering by hadoop with elapsed time(s): " + str(e1 - s1)
