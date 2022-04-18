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

    #El método Eventos se encarga de hacer el get a la api de CISCO y regresa el json con los eventos que se solicitaron
    def Eventos(self):
        request = requests.get(self.url, auth=(self.id, self.key))
        datos=request.json()
        return datos

    #El método CSV se encarga de guardar los datos obtenidos con el get en un archivo csv
    def CSV(self,datos):
        for i in datos['data']:
            #Se comprueban los criterios de selección
            if i['severity']=='High' or i['severity']=='Critical':
                #Si existe el atributo file en el documento
                if 'file' in i:
                    #Si además existe el atributo detection en el documento, guarda los siguientes atributos en csv
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
                    #Si no existe detection, el diccionario se queda con el siguiente formato
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
                #Si no existe file dentro de los atributos, el diccionario se queda con el siguiente formato
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
        #Convierte el diccionario en un DataFrame para posteriormente poder convertirlo en un archivo csv
        df = pandas.DataFrame.from_dict(self.csv['data'])
        df.to_csv("./out.csv")