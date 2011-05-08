#! /usr/bin/env python
import sys
import os
import time

print "Please input the job name:"
job_name = sys.stdin.readline()
job_name = job_name[:-1]

print "Please input the Image XML filename:"
xml_filename = sys.stdin.readline()
xml_filename = xml_filename[:-1]

print "Please input the width of the Image:"
image_width = sys.stdin.readline()
image_width = image_width[:-1]

print "Please input the height of the Image:"
image_height = sys.stdin.readline()
image_height = image_height[:-1]

print "Please input the number to devide the image for each row"
x_devide_num = sys.stdin.readline()
x_devide_num = x_devide_num[:-1]

print "Please input the number to devide the image for each colum"
y_devide_num = sys.stdin.readline()
y_devide_num = y_devide_num[:-1]

os.system("python $HADOOP_HOME/app/preprocess.py " + image_width + ' ' + image_height + ' ' + x_devide_num + ' ' + y_devide_num)

os.system("$HADOOP_HOME/bin/hadoop fs -mkdir /" + job_name) #need to check if exists
os.system("$HADOOP_HOME/bin/hadoop fs -put input /" + job_name)
os.system("cp input $HADOOP_HOME/app/")

hadoop_command = "$HADOOP_HOME/bin/hadoop jar " \
		+ "$HADOOP_HOME/mapred/contrib/streaming/hadoop-0.21.0-streaming.jar "\
		+ "-input /" + job_name + "/input "\
		+ "-output /" + job_name + "/output "\
		+ '-mapper "python mapper.py ' + xml_filename + '" '\
		+ '-reducer "python reducer.py ' + image_width + ' ' + image_height + '" '\
		+ "-file $HADOOP_HOME/app/mapper.py $HADOOP_HOME/app/reducer.py "\
		+ "$HADOOP_HOME/app/" + xml_filename + " "\
		+ "-jobconf mapred.reduce.tasks=1"
s1 = time.time()
os.system(hadoop_command)
e1 = time.time()
os.system("$HADOOP_HOME/bin/hadoop fs -get /" + job_name + "/output/part* $HADOOP_HOME/app/")
os.system("cat $HADOOP_HOME/app/part* | python $HADOOP_HOME/app/tgaFromstring.py "\
		+ image_width + ' ' + image_height + ' withhadoop.tga')
os.system("rm $HADOOP_HOME/app/part*")

test_command = 'cat input | python $HADOOP_HOME/app/mapper.py $HADOOP_HOME/app/' + xml_filename + ' | python $HADOOP_HOME/app/'\
		+'reducer.py ' + image_width + ' ' + image_height + ' > $HADOOP_HOME/app/part-000'
s2 = time.time()
os.system(test_command)
e2 = time.time()
os.system("cat $HADOOP_HOME/app/part* | python $HADOOP_HOME/app/tgaFromstring.py "\
		+ image_width + ' ' + image_height + ' withouthadoop.tga')
os.system("rm $HADOOP_HOME/app/part*")
os.system("rm input")
os.system("rm $HADOOP_HOME/app/input")

print "hadoop execution time:" + str(e1 - s1)
print "no hadoop execution time:" + str(e2 - s2)
