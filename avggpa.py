import urllib
from BeautifulSoup import BeautifulSoup
import time

usnlst = []
for i in range(66,127):
    if i == 110 or i == 106: continue                                               #Makes a list of usn's from 066 to 126
    if i < 100:
        usnlst.append('1XX15CS0'+str(i))
    else:
        usnlst.append('1XX15CS'+str(i))
        

missedlist = []
sumgpa = 0.0
highest = 0.0
highlst = []
for usn in usnlst:
    url = 'University website'
    url = url + usn + '&sem=2'                                                    #Gives the result url for that usn
    urlh = urllib.urlopen(url)  
    data = urlh.read()                                                  #Reads the html file of the results page
    soup = BeautifulSoup(data)
    try:                                          #Creates a BeautifulSoup object of the html file
        gpa = float(soup.find(id = "lblSGPA").b.string)
    except:
        missedlist.append(url)
        continue
    sumgpa += gpa
    if gpa >= highest:
        highest = gpa
        highlst.append((usn,gpa))
    print usn + '  ' + str(gpa)
 
n = len(missedlist)
while(len(missedlist)>0):
   url = missedlist[0]
   urlh = urllib.urlopen(url)  
   data = urlh.read()                                                  #Reads the html file of the results page
   soup = BeautifulSoup(data)
   try:                                          #Creates a BeautifulSoup object of the html file
       gpa = float(soup.find(id = "lblSGPA").b.string)
   except:
        continue
   sumgpa += gpa
   missedlist.pop(0)
   if gpa >= highest:
        highest = gpa
        highlst.append((url[50:-5],gpa))
   print url[50:-5] + '  ' + str(gpa)
 
avggpa = sumgpa/len(usnlst)
print "Average gpa is: %.2f" %(avggpa)                                #Prints average gpa of class
     
print "Highest gpa is : " , highlst
