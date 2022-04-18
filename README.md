# AMP-CISCO-Examen
Examen resuelto de consumo de la api de CISCO Secure Endpoint.

Obtener eventos de seguridad de tipo Threat Detected y Cloud IOC con severidad High y
Critical, cada evento debe contener la siguiente información:
• File Name
• Detection
• Disposition
• Type Event
• Severity
• SHA256
• Hostname
• File Path

El examen se soluciona con el archivo Events, que es el script principal. Events crea un nuevo objeto de la clase File.
La clase File tiene dos métodos:
Eventos, que es el que permite hacer el consumo de la API y obtener los eventos especificados, regresando un json llamado datos, que contiene toda la información relacionada
con los eventos especificados en la url.
CSV, que es el que recibe los eventos, los filtra para obtener únicamente la información requerida en el examen y crear el archivo final en formato csv.
