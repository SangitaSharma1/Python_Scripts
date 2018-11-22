#!/usr/bin/python3.6
import os
import subprocess
import re

process=subprocess.Popen("top -n 1 | grep ^%  | awk '{print $6}'", shell=True, stdout=subprocess.PIPE)
for line in process.stdout:
    #line = str(line,'utf-8')
    #line=line.split()
    p = int(float(line[0]))
    if (p > 90):
        print ("alert")
    else:
        print("stable")
print("the current cpu utilization is ", p)
