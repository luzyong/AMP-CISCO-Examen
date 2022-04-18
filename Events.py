#!python
from File import File

amp_client_id = '2be0d43ade16fa93ed67'
amp_api_key = 'e624dd38-a305-405e-98d8-c615b2831b13'

def main():
  Registro_Eventos = File(amp_client_id,amp_api_key)
  csv=Registro_Eventos.Eventos()
  Registro_Eventos.CSV(csv)


if __name__=='__main__':
  main()