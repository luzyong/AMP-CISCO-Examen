import requests
import pandas


amp_client_id = '2be0d43ade16fa93ed67'
amp_api_key = 'e624dd38-a305-405e-98d8-c615b2831b13'

url = 'https://api.amp.cisco.com/v1/events?event_type[]=1107296274&event_type[]=1090519054'

request = requests.get(url, auth=(amp_client_id, amp_api_key))
datos=request.json()
csv = {"data":[]}


for i in datos['data']:
    if i['severity']=='High' or i['severity']=='Critical' or i['severity']=='Medium':
      if 'file' in i:
        if 'detection' in i:
          csv['data'].append({"File Name":i['file']['file_name'],
                      "Detection":i['detection'],
                      "Disposition":i['file']['disposition'],
                      "Type Event":i['event_type'],
                      "Severity":i['severity'],
                      "SHA256":i['file']['identity']['sha256'],
                      "Hostname":i['computer']['hostname'],
                      "File path":i['file']['file_path']
                      })
        else:
          csv['data'].append({"File Name":i['file']['file_name'],
                      "Detection":"",
                      "Disposition":i['file']['disposition'],
                      "Type Event":i['event_type'],
                      "Severity":i['severity'],
                      "SHA256":i['file']['identity']['sha256'],
                      "Hostname":i['computer']['hostname'],
                      "File path":i['file']['file_path']
                      })
      else:
        csv['data'].append({"File Name":i['cloud_ioc']['description'],
                      "Detection":"",
                      "Disposition":i['network_info']['parent']['disposition'],
                      "Type Event":i['event_type'],
                      "Severity":i['severity'],
                      "SHA256":i['network_info']['parent']['identity']['sha256'],
                      "Hostname":i['computer']['hostname'],
                      "File path":i['network_info']['dirty_url']
                      })
df = pandas.DataFrame.from_dict(csv['data'])
df.to_csv("./out.csv")