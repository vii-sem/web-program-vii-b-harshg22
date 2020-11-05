#Create Virtual Environment in Python2,use the following commands in the terminal
virtualenv -p `which python2` env

source env/bin/activate

#copy the below program in any file say --->thread.py

import thread
import time
# Define a function for the thread
def print_time(threadName, delay):
    count=0
    while count <5:
        time.sleep(delay)
        count+=1
        print("%s: %s" %(threadName,time.ctime(time.time() ) ))
# Create two threads as follows
try: 
    thread.start_new_thread(print_time,("Thread-1",2,)) 
    thread.start_new_thread(print_time,("Thread-2",4,)) 
except:
    print("Error: unable to start thread")
    
while 1: 
    pass

#Run the program
python thread.py
