#!/bin/python

import urllib
import json

filename = '/tmp/merge_conflict.csv' #Filename, where the output(Roll no.s) will get stored.

#Initial decorations to the CSV file.

pre_w = open(filename, 'a')
pre_w.write("Roll Number" + '\n')
pre_w.write("-----------" + '\n')
pre_w.close()



#URL to the github SDES2015 repo's  Pull request page

a = urllib.urlopen('https://api.github.com/repos/FOSSEE/SDES2015/pulls?page=1&per_page=72&state=open')

#Convert the response to a JSON object.

b = json.load(a)


for i in b:
  num = i["number"]          #'number' is a attribute of a pull request, specifically, the PR id.
  c = "https://personal-access-token:59991ce5b2c3cfc9551de8b46b31a47fc1161c31@api.github.com/repos/FOSSEE/SDES2015/pulls/%s/files" % (num)
  x = urllib.urlopen(c)
  y = json.load(x)
  for j in y:
    p=j["patch"]    #'patch' is a attribute of a specific PR.
    q=p.strip('+')
    r=q.split('\n')
    s=r[4].replace('+Roll number: ','')
  w = open(filename, 'a')
  print s, num
  w.write(s + '\n')

w.close()
  
  
    
    
  


  
  
    
    



  



