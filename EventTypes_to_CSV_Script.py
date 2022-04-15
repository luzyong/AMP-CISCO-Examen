import requests
import pandas
import json
amp_client_id = '2be0d43ade16fa93ed67'

amp_api_key = 'e624dd38-a305-405e-98d8-c615b2831b13'
stream_id = 1090519054

url = 'https://api.amp.cisco.com/v1/events'

request = requests.get(url, auth=(amp_client_id, amp_api_key))
datos=request.json()
#print(datos['data'])
j=0
'''for i in datos['data']:
  if datos['data'][j]['event_type_id'] == stream_id:
    print(datos['data'][j]['event_type'])
  j+=1
'''
df = pandas.DataFrame(datos['data'])
df.to_csv("./out.csv")