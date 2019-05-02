#liberries
import datetime
from datetime import timedelta
import sched, time
# import httplib
import urllib.request







#getting the current datetime time and date 
starttime=time.time()
ts = datetime.datetime.fromtimestamp(starttime).strftime('%m-%d-%Y %H:%M:%S')



#function that tests the internet and outputs whether the internet is working or not
def testInternet() :
    #making internetWasDown global
    global internetWasDown
    #internet
    try:
        
        #getting the current datetime time and date 
        starttime=time.time()
        ts = datetime.datetime.fromtimestamp(starttime).strftime('%m-%d-%Y %H:%M:%S')

        
        #trying to connect to google.com
        with urllib.request.urlopen('http://www.google.com') as response:
           html = response.read()
           test = response

        #if it gets this far, the internet is up 
        #only need to print if it's up if it has been down previously
        #print(global internetWasDown) 
        if internetWasDown == True:
            #writing it to a file 
            # file-output.py
            f = open('/home/james/internet/internetouttages.txt','a')
            f.write("Internet is BACK UP at " + str(ts) + "\n\n")
            f.close()
            #time.sleep(1.0 - ((time.time() - starttime) % 1.0))

        #reset internetWasDown
        internetWasDown = False

        #print("Internet working at " + str(ts))



    #if something fails 
    except:
    
        
    
        #if internetWasDown == False then this is the first time the internet was down so output internetWasDown
        if internetWasDown == False:
            #writing it to a file 
            # file-output.py
            f = open('/home/james/internet/internetouttages.txt','a')
            f.write("Internet is DOWN at " + str(ts) + '\n')
            #close the file 
            f.close()
    
        

    
        #making internetWasDown True 
        internetWasDown = True
    
    
        #getting the time in human format
        #ts = datetime.datetime.fromtimestamp(starttime).strftime('%m-%d-%Y %H:%M:%S')
        #outputting 
        #should be the time from 
        #print("Internet failed at " + str(ts))



#global variables 
internetWasDown = False

#writing PROGRAM STARTED to the file  
# file-output.py
f = open('/home/james/internet/internetouttages.txt','a')
f.write("\nscript started at " + str(ts) + '\n')
#close the file 
f.close()

#starting the loop
while True:
  #getting the time 
  now = datetime.datetime.now()


  #call the internet testing function
  testInternet()

  # file-output.py
  # f = open('internetouttages.txt','a')
  # f.write(str(now) + '\n')
  # f.close()
  time.sleep(1.0 - ((time.time() - starttime) % 1.0))






