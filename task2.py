import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = (time.strftime('%H')) 
print(timestamp)
timestamp = time.strftime('%M') 
print(timestamp)
timestamp = time.strftime('%S') 
print(timestamp)
# next code
import time
t = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
hour = int(input("Enter hour:"))
print(hour)
if(hour>=0 and hour<12):
    print("good morning")
elif(hour>=12 and hour<18):
    print("good evening")
if(hour>=17 and hour<0):
    print("good night")
