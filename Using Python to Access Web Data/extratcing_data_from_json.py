import urllib
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json 
    
address = input('Enter location: ')
uh = urllib.request.urlopen(address)
data = uh.read()

all_data = json.loads(data)
user_data = all_data['comments']
total = 0 

for item in user_data:
    total += item["count"] 
    #print(item["count"])
print(total)
