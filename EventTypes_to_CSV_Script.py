import requests
import pandas
import json
amp_client_id = '2be0d43ade16fa93ed67'

amp_api_key = 'e624dd38-a305-405e-98d8-c615b2831b13'
stream_id = 1090519054

url = 'https://api.amp.cisco.com/v1/events?start_date=2015-10-01T00%3A00%3A00%2B00%3A00'

request = requests.get(url, auth=(amp_client_id, amp_api_key))
datos=request.json()
csv = {"data":[]}
#print(datos)

j=0
for i in datos['data']:
  if 'severity' in i:
    if i['severity']=='Low' or i['severity']=='Critical':
      csv['data'].append({"File Name":i['file']['file_name'],
                      "Disposition":i['file']['disposition'],
                      "Type Event":i['event_type'],
                      "Severity":i['severity'],
                      "SHA256":i['file']['identity']['sha256'],
                      "Hostname":i['computer']['hostname']})
                      #"Filepath":i['file']})
  j+=1
df = pandas.DataFrame.from_dict(csv['data'])
df.to_csv("./out.csv")