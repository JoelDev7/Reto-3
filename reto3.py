import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO

from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person

KEY = "062db349713f4b87a3f8a0680c642b5a"
ENDPOINT = "https://reto3ai-tienda.cognitiveservices.azure.com/"

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

"""
La url estática se sustituiría por una lista de url's que se consultarían ya fuera en los servidores
locales de la empresa o en algún sistema de archivos en azure que contenga las fotos de las personas
para analizar
"""
face_image_url = 'https://media.comicbook.com/2021/02/icarly-netflix-now-streaming-season-1-2-1255950-1280x0.jpeg'
detected_faces = face_client.face.detect_with_url(url=face_image_url, return_face_id=False, return_face_attributes={'age', 'gender', 'smile', 'glasses', 'emotion'})

#Se crea la lista que tendrá los resultados ya con formato de dicccionario
people = []

for face in detected_faces: people.append(face.as_dict())

#Lo ideal sería que en lugar de solo imprimir en consola la lista de personas se guardara en una base de datos. 
for person in people: print(f"{person}\n")


