#! /usr/bin/env python
import sys
import os
import time

amount = int(sys.argv[1])
jobname = sys.argv[2]
xmlfile = sys.argv[3]

for i in range(amount):
	os.system("python main.py " + jobname \
			+ "_amount_" + str(i) + " " + xmlfile + " > "\
			+ jobname + "_output_" + str(i) + " &")
	time.sleep(3)
