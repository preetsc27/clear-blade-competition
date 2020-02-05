import os
import sys
import psutil
from clearblade.ClearBladeCore import System

# I am only taking cpu percentage of utilisation and virtual_memory details in %
# getting the data
cpu_info = psutil.cpu_percent()
vmemory_info = psutil.virtual_memory()[2]  # physical memory usage

# creating a dict to store the data
data = {
    "cpu_info": cpu_info,
    "vmemory_info": vmemory_info
}

# System credentials
SystemKey = "9ae6d1e30bda958cfc9cf69bfde201"
SystemSecret = "9AE6D1E30BC8E5BA9CB3BB8DF02E"

mySystem = System(SystemKey, SystemSecret)

# geeting the password from environment
password = "MyBlabePass"# os.environ["clearblabe_password"]
print(password)

# Log in as Preet
preet = mySystem.User("preetsc27@gmail.com", password)

# Accessing the messaging client
mqtt = mySystem.Messaging(preet)

# Connecting...
mqtt.connect()

# coverting the data to string format
str_data = str(data)

# sending the data
mqtt.publish("preetlaptop", str_data )

