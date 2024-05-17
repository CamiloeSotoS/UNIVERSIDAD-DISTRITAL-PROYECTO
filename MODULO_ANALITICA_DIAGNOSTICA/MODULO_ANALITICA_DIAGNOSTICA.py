# ----------------------------------------------------------------
# LIBRERIAS
# ----------------------------------------------------------------

import warnings

warnings.filterwarnings("ignore")
from numpy import set_printoptions
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

pd.options.display.max_columns = None
import seaborn as sns
import io
import base64
import json
import os
import uvicorn
from openpyxl import Workbook
from openpyxl.drawing.image import Image as XLImage

from fastapi import FastAPI, Request
from typing import List
from pydantic import BaseModel

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import PowerTransformer


# ---------------------------------------------------------------
# CARGUE DE DATOS
# ---------------------------------------------------------------
# SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

# creds = None
# if os.path.exists("token.json"):
#     creds = Credentials.from_authorized_user_file("token.json", SCOPES)
# if not creds or not creds.valid:
#     if creds and creds.expired and creds.refresh_token:
#         creds.refresh(Request())
#     else:
#         flow = InstalledAppFlow.from_client_secrets_file(
#             "C:/Users/Intevo/Desktop/conversion de documentos/credentials.json", SCOPES
#         )  # Reemplazar con la ruta correcta
#         creds = flow.run_local_server(port=0)
#     with open(
#         "C:/Users/Intevo/Desktop/conversion de documentos/token.json", "w"
#     ) as token:
#         token.write(creds.to_json())

# # Crear una instancia de la API de Drive
# drive_service = build("drive", "v3", credentials=creds)

# # ID de la carpeta de Google Drive
# folder_id = "1hQeetmO4XIObUefS_nzePqKqq3VksUEC"

# # Ruta de destino para guardar los archivos descargados
# save_path = "C:/Users/Intevo/Desktop/conversion de documentos/Datos"  # Reemplazar con la ruta deseada


# # Función para descargar archivos de la carpeta de Drive
# def download_folder(folder_id, save_path):
#     results = (
#         drive_service.files()
#         .list(q=f"'{folder_id}' in parents and trashed=false", fields="files(id, name)")
#         .execute()
#     )
#     items = results.get("files", [])
#     for item in items:
#         file_id = item["id"]
#         file_name = item["name"]
#         request = drive_service.files().get_media(fileId=file_id)
#         fh = io.FileIO(os.path.join(save_path, file_name), "wb")
#         downloader = MediaIoBaseDownload(fh, request)
#         done = False
#         while done is False:
#             status, done = downloader.next_chunk()
#             print(f"Descargando {file_name}: {int(status.progress() * 100)}%")
#     print("Descarga completa")


# # Descargar archivos de la carpeta
# download_folder(folder_id, save_path)

# # Listar archivos descargados
# files = os.listdir(save_path)
# print("Archivos descargados:")
# for file in files:
#     print(file)

#----------------------------------------------------------------
# GENERACION DE GRAFICAS
#----------------------------------------------------------------

app = FastAPI()
@app.get("/")
def index():
    return "Hello, world!"

carrera = ""
semestre = ""
x = ""
y = ""

class InputData(BaseModel):
    carrera: str
    semestre: int
    x: str
    y: str

@app.post("/generar_graficas/")
async def procesar_datos(data: InputData):
    global x, x, carrera, semestre

    carrera = data.carrera
    semestre = data.semestre
    x = data.x
    y = data.y

    print("Carrera: ", carrera)
    print("Semestre: ", semestre)
    print("Valor: ", x)
    print("Valor", y)

    # Definir la función de carga de datos
    def cargar_datos(carrera, semestre):
        ruta_archivo = f"C:/Users/Intevo/Desktop/UNIVERSIDAD DISTRITAL PROYECTO FOLDER/UNIVERSIDAD-DISTRITAL-PROYECTO/MODULO_ANALITICA_PREDICTIVA/DATOS/{carrera}{semestre}.csv"
        datos = pd.read_csv(ruta_archivo, sep=";")
        return datos

    df = cargar_datos(carrera, semestre)

    def generar_grafico(x, y, df):
        # Imprimir los valores de x e y
        print(x, y, df)

    # Configurar el tema de Seaborn
    sns.set_theme(style="whitegrid")
    

    # Crear el gráfico utilizando Seaborn
    g = sns.catplot(
        data=df,
        kind="bar",
        x=x,
        y=y,
        errorbar="sd",
        palette="dark",
        alpha=0.6,
        height=6,
        aspect=2
    )
    # plt.figure(figsize=(10, 5))
    plt.xticks(rotation=90)
    plt.show()
    # Guardar el gráfico en un archivo temporal
    temp_file = io.BytesIO()
    g.savefig(temp_file, format="png")
    temp_file.seek(0)

    # Leer el archivo temporal y convertirlo en una cadena base64
    base64_image = base64.b64encode(temp_file.read()).decode("utf-8")

    # Guardar la cadena base64 en un diccionario JSON
    imagen_base64 = {"data": base64_image}

    # Guardar el diccionario JSON en un archivo JSON
    with open("Imagenes_Transformacion.json", "w") as json_file:
        json.dump(imagen_base64, json_file)

    # Imprimir un mensaje indicando que los códigos base64 de las imágenes han sido guardados en 'Imagenes_Transformacion.json'
    print("Los códigos Base64 de las imágenes han sido guardados en 'Imagenes_Transformacion.json'.")

    # Retornar la imagen base64
    return imagen_base64

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)