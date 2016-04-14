import urllib
from BeautifulSoup import BeautifulSoup
import time

usnlst = []
for i in range(66,127):
    if i == 110: continue                               #Makes a list of usn's from 066 to 126
    if i < 100:
        usnlst.append('1XX15YY0'+str(i))                #Made some changes due to privacy issues
    else:
        usnlst.append('1XX15YY'+str(i))
        


sumgpa = 0.0

for usn in usnlst:
    url = 'http://result.vtu.ac.in/cbcs_results2016.aspx?usn='
    url = url + usn                                     #Gives the result url for that usn
    urlh = urllib.urlopen(url)  
    data = urlh.read()                                  #Reads the html file of the results page
    soup = BeautifulSoup(data)                          #Creates a BeautifulSoup object of the html file
    gpa = float(soup.find(id = "lblSGPA").b.string)     #Grabs the gpa from the html file
    sumgpa += gpa
    print usn + '  ' + str(gpa)
    time.sleep(1)
    
avggpa = sumgpa/float(len(usnlst))
print "Average gpa is: %.2f" %(avggpa)                  #Prints average gpa of class
     
