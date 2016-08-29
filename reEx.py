#Author : Kunchala Anil
#Date : 29 Aug 2016
#Simple Data Parsing

import re
regex = r"\<q\>(.+?)\<\/q\>"
line = "<q>12||Question1||opta||optb||optc||optd</q> <q>34||question2||opta||optb||optc||optd</q>"

pattern = r"\<q\>(.+?)\<\/q\>"

pattern2 = r"(\d+?)\|\|(.+?)\|\|(.+?)\|\|(.+?)\|\|(.+?)\|\|(.+?)$"

out = re.findall(pattern,line)

print re.findall(pattern2,out[0])
