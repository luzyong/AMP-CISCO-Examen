import requests
import pandas
class File:
    id=''
    key=''
    url = 'https://api.amp.cisco.com/v1/events?event_type[]=1107296274&event_type[]=1090519054'
    csv = {"data":[]}

    def __init__(self,ampId,ampKey):
        self.id=ampId
        self.key=ampKey

    def Eventos(self):
        request = requests.get(self.url, auth=(self.id, self.key))
        datos=request.json()
        return datos

    def CSV(self,datos):
        for i in datos['data']:
            if i['severity']=='High' or i['severity']=='Critical':
                if 'file' in i:
                    if 'detection' in i:
                        self.csv['data'].append({"File Name":i['file']['file_name'],
                            "Detection":i['detection'],
                            "Disposition":i['file']['disposition'],
                            "Type Event":i['event_type'],
                            "Severity":i['severity'],
                            "SHA256":i['file']['identity']['sha256'],
                            "Hostname":i['computer']['hostname'],
                            "File path":i['file']['file_path']
                            })
                    else:
                        self.csv['data'].append({"File Name":i['file']['file_name'],
                            "Detection":"",
                            "Disposition":i['file']['disposition'],
                            "Type Event":i['event_type'],
                            "Severity":i['severity'],
                            "SHA256":i['file']['identity']['sha256'],
                            "Hostname":i['computer']['hostname'],
                            "File path":i['file']['file_path']
                            })
                else:
                    self.csv['data'].append({"File Name":i['cloud_ioc']['description'],
                        "Detection":"",
                        "Disposition":i['network_info']['parent']['disposition'],
                        "Type Event":i['event_type'],
                        "Severity":i['severity'],
                        "SHA256":i['network_info']['parent']['identity']['sha256'],
                        "Hostname":i['computer']['hostname'],
                        "File path":i['network_info']['dirty_url']
                        })
        df = pandas.DataFrame.from_dict(self.csv['data'])
        df.to_csv("./out.csv")