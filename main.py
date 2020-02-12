import os
import sys
import psutil
from clearblade.ClearBladeCore import System

# I am only taking cpu percentage of utilisation and virtual_memory details in %
# getting the dataif 
cpu_info = psutil.cpu_percent()
## Change: Looking for None check
if cpu_info == None:
    print("Not able to find CPU usage")
    ## We will exit with status 1(error)
    sys.exit(1)

vmemory_info = psutil.virtual_memory()  # physical memory usage
## Change: Looking for None check
if vmemory_info == None:
    print("Not able to find Virtual Memory")
    ## We will exit with status 1(error)
    sys.exit(1)
else:
    ## Change: Looking if the @var vmemory_info length is more than 2
    ## because we need the 2nd index value from it
    if len(vmemory_info) < 2:
        print("Not able to find CPU usage")
        ## We will exit with status 1(error)
        sys.exit(1)

## Change: Getting the memory usage
memory_usage = vmemory_info[2]

# creating a dict to store the data
data = {
    "cpu_info": cpu_info,
    "vmemory_info": memory_usage
}

# System credentials
## Change: to increase the security we will get the keys from the env variables
systemKey = os.environ.get("SystemKey", None)
# None check for system key
if systemKey == None:
    print("Please add System Key")
    sys.exit(1)

systemSecret = os.environ.get("SystemSecret", None)
if systemSecret == None:
    print("Please add System Secret")
    sys.exit(1)

mySystem = System(systemKey, systemSecret)


## Change: geeting the password from environment
password =  os.environ.get("clearblabe_password", None)
if password == None:
    print("Please add PASSWORD")
    sys.exit(1)
print(password)

# Log in as Preet
preet = mySystem.User("preetsc27@gmail.com", password)

# Accessing the messaging client
mqtt = mySystem.Messaging(preet)

# Connecting...
mqtt.connect()

# coverting the data to string format
## change: no need to convert data to string 
str_data = str(data)

# sending the data
mqtt.publish("preetlaptop", str_data)

## Change: logging out the user
preet.logout()

## Change: disconnecting the messaging service
mqtt.disconnect()
