import urllib2, urllib,re
mydata=[('ID',101),('two',2)]    #The first is the var name the second is the value
mydata=urllib.urlencode(mydata)
path='http://www.newpythonscripts.16mb.com/new5.php'    #the url you want to POST to
req=urllib2.Request(path, mydata)
req.add_header("Content-type", "application/x-www-form-urlencoded")
page=urllib2.urlopen(req).read()

pattern = r"\<q\>(.+?)\<\/q\>"

pattern2 = r"(\d+?)\|\|(.+?)\|\|(.+?)\|\|(.+?)\|\|(.+?)"

out = re.findall(pattern,page)

print re.findall(pattern2,out[0])
#for match in out:
#    print re.fndall(patterm)
#    print 'rinnin'
