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
"""
SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

creds = None
if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "C:/Users/Intevo/Desktop/conversion de documentos/credentials.json", SCOPES
        )  # Reemplazar con la ruta correcta
        creds = flow.run_local_server(port=0)
    with open(
        "C:/Users/Intevo/Desktop/conversion de documentos/token.json", "w"
    ) as token:
        token.write(creds.to_json())

# Crear una instancia de la API de Drive
drive_service = build("drive", "v3", credentials=creds)

# ID de la carpeta de Google Drive
folder_id = "1hQeetmO4XIObUefS_nzePqKqq3VksUEC"

# Ruta de destino para guardar los archivos descargados
save_path = "C:/Users/Intevo/Desktop/conversion de documentos/Datos"  # Reemplazar con la ruta deseada


# Función para descargar archivos de la carpeta de Drive
def download_folder(folder_id, save_path):
    results = (
        drive_service.files()
        .list(q=f"'{folder_id}' in parents and trashed=false", fields="files(id, name)")
        .execute()
    )
    items = results.get("files", [])
    for item in items:
        file_id = item["id"]
        file_name = item["name"]
        request = drive_service.files().get_media(fileId=file_id)
        fh = io.FileIO(os.path.join(save_path, file_name), "wb")
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(f"Descargando {file_name}: {int(status.progress() * 100)}%")
    print("Descarga completa")


# Descargar archivos de la carpeta
download_folder(folder_id, save_path)

# Listar archivos descargados
files = os.listdir(save_path)
print("Archivos descargados:")
for file in files:
    print(file)
"""
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
z = ""

class InputData(BaseModel):
    carrera: str
    semestre: int
    x: str
    y: str
    z: str

@app.post("/generar_graficas/")
async def procesar_datos(data: InputData):
    global x, y, z, carrera, semestre

    carrera = data.carrera
    semestre = data.semestre
    x = data.x
    y = data.y
    z = data.z

    print("Carrera: ", carrera)
    print("Semestre: ", semestre)
    print("Valor: ", x)
    print("Valor: ", y)
    print("Valor: ", z)

    # Definir la función de carga de datos
    def cargar_datos(carrera, semestre):
        ruta_archivo = f"C:/Users/Intevo/Desktop/UNIVERSIDAD DISTRITAL PROYECTO FOLDER/UNIVERSIDAD-DISTRITAL-PROYECTO/MODULO_ANALITICA_DIAGNOSTICA/DATOS/{carrera}{semestre}.csv"
        datos = pd.read_csv(ruta_archivo, sep=";")

        datos['GENERO'] = datos['GENERO'].replace({0:'MASCULINO', 1:'FEMENINO'})
        datos['CALENDARIO'] = datos['CALENDARIO'].replace({0:'NO REGISTRA',0:'O', 1:'A', 2:'B', 3:'F'})
        datos['TIPO_COLEGIO'] = datos['TIPO_COLEGIO'].replace({0:'NO REGISTRA', 1:'OFICIAL', 2:'NO OFICIAL'})
        datos['LOCALIDAD_COLEGIO'] = datos['LOCALIDAD_COLEGIO'].replace({0:'NO REGISTRA', 1:'USAQUEN', 2:'CHAPINERO', 3:'SANTA FE', 3:'SANTAFE', 4:'SAN CRISTOBAL', 5:'USME', 6:'TUNJUELITO', 7:'BOSA', 8:'KENNEDY', 9:'FONTIBON', 10:'ENGATIVA',11: 'SUBA',12: 'BARRIOS UNIDOS', 13:'TEUSAQUILLO',14: 'LOS MARTIRES',15: 'ANTONIO NARINO', 16:'PUENTE ARANDA', 17: 'LA CANDELARIA', 18:'RAFAEL URIBE URIBE', 18:'RAFAEL URIBE', 19:'CIUDAD BOLIVAR', 20:'FUERA DE BOGOTA', 20:'SIN LOCALIDAD', 21:'SOACHA',22:'FUERA DE BOGOTA'})
        datos['DEPARTAMENTO'] = datos['DEPARTAMENTO'].replace({ 0: 'NO REGISTRA', 1: 'AMAZONAS', 2: 'ANTIOQUIA', 3: 'ARAUCA', 4: 'ATLANTICO', 5: 'BOGOTA', 6: 'BOLIVAR', 7: 'BOYACA', 8: 'CALDAS', 9: 'CAQUETA', 10: 'CASANARE', 11: 'CAUCA', 12: 'CESAR', 13: 'CHOCO', 14: 'CORDOBA', 15: 'CUNDINAMARCA', 16: 'GUAINIA', 17: 'GUAVIARE', 18: 'HUILA', 19: 'LA GUAJIRA', 20: 'MAGDALENA', 21: 'META', 22: 'NARINO', 23: 'NORTE SANTANDER', 24: 'PUTUMAYO', 25: 'QUINDIO', 26: 'RISARALDA', 27: 'SAN ANDRES Y PROVIDENCIA', 28: 'SANTANDER', 29: 'SUCRE', 30: 'TOLIMA', 31: 'VALLE', 32: 'VAUPES', 33: 'VICHADA'})
        datos['DEPARTAMENTO'] = np.where((datos['DEPARTAMENTO']==34)|(datos['DEPARTAMENTO']==36)|(datos['DEPARTAMENTO']==37),'NO REGISTRA',datos['DEPARTAMENTO'])  
        datos['LOCALIDAD'] = datos['LOCALIDAD'].replace({0: "NO REGISTRA", 1: "USAQUEN", 2: "CHAPINERO", 3: "SANTA FE", 4: "SAN CRISTOBAL", 5: "USME", 6: "TUNJUELITO", 7: "BOSA", 8: "KENNEDY", 9: "FONTIBON", 10: "ENGATIVA", 11: "SUBA", 12: "BARRIOS UNIDOS", 13: "TEUSAQUILLO", 14: "LOS MARTIRES", 15: "ANTONIO NARINO", 16: "PUENTE ARANDA", 17: "LA CANDELARIA", 18: "RAFAEL URIBE URIBE", 19: "CIUDAD BOLIVAR"})
        datos['LOCALIDAD'] = np.where((datos['LOCALIDAD']==20)|(datos['LOCALIDAD']==21)|(datos['LOCALIDAD']==22),'FUERA DE BOGOTA',datos['LOCALIDAD'])               
        datos['INSCRIPCION'] = datos['INSCRIPCION'].replace({0:'NO REGISTRA', 1:'BENEFICIARIOS LEY 1081 DE 2006', 2:'BENEFICIARIOS LEY 1084 DE 2006', 3:'CONVENIO ANDRES BELLO', 4:'DESPLAZADOS', 5:'INDIGENAS', 6:'MEJORES BACHILLERES COL. DISTRITAL OFICIAL', 7:'MINORIAS ETNICAS Y CULTURALES', 8:'MOVILIDAD ACADEMICA INTERNACIONAL', 9:'NORMAL', 10:'TRANSFERENCIA EXTERNA', 11:'TRANSFERENCIA INTERNA'})
        datos['MUNICIPIO'] = datos['MUNICIPIO'].replace({0:'NO REGISTRA', 1:'ACACIAS', 2:'AGUACHICA', 3:'AGUAZUL', 4:'ALBAN', 5:'ALBAN (SAN JOSE)', 6:'ALVARADO', 7:'ANAPOIMA', 8:'ANOLAIMA', 9:'APARTADO', 10:'ARAUCA', 11:'ARBELAEZ', 12:'ARMENIA', 13:'ATACO', 14:'BARRANCABERMEJA', 16:'BARRANQUILLA', 17:'BELEN DE LOS ANDAQUIES', 18:'BOAVITA', 19:'BOGOTA', 20:'BOJACA', 21:'BOLIVAR', 22:'BUCARAMANGA', 23:'BUENAVENTURA', 24:'CABUYARO', 25:'CACHIPAY', 26:'CAICEDONIA', 27:'CAJAMARCA', 28:'CAJICA', 29:'CALAMAR', 30:'CALARCA', 31:'CALI', 32:'CAMPOALEGRE', 33:'CAPARRAPI', 34:'CAQUEZA', 35:'CARTAGENA', 36:'CASTILLA LA NUEVA', 37:'CERETE', 38:'CHAPARRAL', 39:'CHARALA', 40:'CHIA', 41:'CHIPAQUE', 42:'CHIQUINQUIRA', 43:'CHOACHI', 44:'CHOCONTA', 45:'CIENAGA', 46:'CIRCASIA', 47:'COGUA', 48:'CONTRATACION', 49:'COTA', 50:'CUCUTA', 51:'CUMARAL', 52:'CUMBAL', 53:'CURITI', 54:'CURUMANI', 55:'DUITAMA', 56:'EL BANCO', 57:'EL CARMEN DE BOLIVAR', 58:'EL COLEGIO', 59:'EL CHARCO', 60:'EL DORADO', 61:'EL PASO', 62:'EL ROSAL', 63:'ESPINAL', 64:'FACATATIVA', 65:'FLORENCIA', 66:'FLORIDABLANCA', 67:'FOMEQUE', 68:'FONSECA', 69:'FORTUL', 70:'FOSCA', 71:'FUNZA', 72:'FUSAGASUGA', 73:'GACHETA', 74:'GALERAS (NUEVA GRANADA)', 75:'GAMA', 76:'GARAGOA', 77:'GARZON', 78:'GIGANTE', 79:'GIRARDOT', 80:'GRANADA', 81:'GUACHUCAL', 82:'GUADUAS', 83:'GUAITARILLA', 84:'GUAMO', 85:'GUASCA', 86:'GUATEQUE', 87:'GUAYATA', 88:'GUTIERREZ', 89:'IBAGUE', 90:'INIRIDA', 91:'INZA', 92:'IPIALES', 93:'ITSMINA', 94:'JENESANO', 95:'LA CALERA', 96:'LA DORADA', 98:'LA MESA', 99:'LA PLATA', 100:'LA UVITA', 101:'LA VEGA', 102:'LIBANO', 103:'LOS PATIOS', 104:'MACANAL', 105:'MACHETA', 106:'MADRID', 107:'MAICAO', 108:'MALAGA', 109:'MANAURE BALCON DEL 12', 110:'MANIZALES', 111:'MARIQUITA', 112:'MEDELLIN', 113:'MEDINA', 114:'MELGAR', 115:'MITU', 116:'MOCOA', 117:'MONTERIA', 118:'MONTERREY', 119:'MOSQUERA', 120:'NATAGAIMA', 121:'NEIVA', 122:'NEMOCON', 123:'OCANA', 124:'ORITO', 125:'ORTEGA', 126:'PACHO', 127:'PAEZ (BELALCAZAR)', 128:'PAICOL', 129:'PAILITAS', 130:'PAIPA', 131:'PALERMO', 132:'PALMIRA', 133:'PAMPLONA', 134:'PANDI', 135:'PASCA', 136:'PASTO', 137:'PAZ DE ARIPORO', 138:'PAZ DE RIO', 139:'PITALITO', 140:'POPAYAN', 141:'PUENTE NACIONAL', 142:'PUERTO ASIS', 143:'PUERTO BOYACA', 144:'PUERTO LOPEZ', 145:'PUERTO SALGAR', 146:'PURIFICACION', 147:'QUETAME', 148:'QUIBDO', 149:'RAMIRIQUI', 150:'RICAURTE', 151:'RIOHACHA', 152:'RIVERA', 153:'SABOYA', 154:'SAHAGUN', 155:'SALDAÑA', 156:'SAMACA', 157:'SAMANA', 158:'SAN AGUSTIN', 159:'SAN ANDRES', 160:'SAN BERNARDO', 161:'SAN EDUARDO', 162:'SAN FRANCISCO', 163:'SAN GIL', 164:'SAN JOSE DEL FRAGUA', 165:'SAN JOSE DEL GUAVIARE', 166:'SAN LUIS DE PALENQUE', 167:'SAN MARCOS', 168:'SAN MARTIN', 169:'SANDONA', 170:'SAN VICENTE DEL CAGUAN', 171:'SANTA MARTA', 172:'SANTA SOFIA', 173:'SESQUILE', 174:'SIBATE', 175:'SIBUNDOY', 176:'SILVANIA', 177:'SIMIJACA', 178:'SINCE', 179:'SINCELEJO', 180:'SOACHA', 181:'SOATA', 182:'SOCORRO', 183:'SOGAMOSO', 184:'SOLEDAD', 185:'SOPO', 186:'SORACA', 187:'SOTAQUIRA', 188:'SUAITA', 189:'SUBACHOQUE', 190:'SUESCA', 191:'SUPATA', 192:'SUTAMARCHAN', 193:'SUTATAUSA', 194:'TABIO', 195:'TAMESIS', 196:'TARQUI', 197:'TAUSA', 198:'TENA', 199:'TENJO', 200:'TESALIA', 201:'TIBANA', 202:'TIMANA', 203:'TOCANCIPA', 204:'TUBARA', 205:'TULUA', 206:'TUMACO', 207:'TUNJA', 208:'TURBACO', 209:'TURMEQUE', 210:'UBATE', 211:'UMBITA', 212:'UNE', 213:'VALLEDUPAR', 214:'VELEZ', 215:'VENADILLO', 216:'VENECIA (OSPINA PEREZ)', 217:'VILLA DE LEYVA', 218:'VILLAHERMOSA', 219:'VILLANUEVA', 220:'VILLAPINZON', 221:'VILLAVICENCIO', 222:'VILLETA', 223:'YACOPI', 224:'YOPAL', 225:'ZIPACON', 226:'ZIPAQUIRA'})

        return datos

    df = cargar_datos(carrera, semestre)

    def generar_archivo(x,y,z,carrera,semestre):
        df_grafico=df[[x,y,z]]
        ruta='C:/Users/URIELDARIO/Desktop/'
        df_grafico.to_csv(f"C:/Users/Intevo/Desktop/UNIVERSIDAD DISTRITAL PROYECTO FOLDER/UNIVERSIDAD-DISTRITAL-PROYECTO/MODULO_ANALITICA_DIAGNOSTICA/DATOS_{carrera}{semestre}.csv",index=False)
        data_with_columns = df_grafico.to_dict(orient='records')
        diccionario_dataframes = [
            {
                'dataTransformacion': data_with_columns,
            }
        ]
        ruta = f"C:/Users/Intevo/Desktop/UNIVERSIDAD DISTRITAL PROYECTO FOLDER/UNIVERSIDAD-DISTRITAL-PROYECTO/MODULO_ANALITICA_DIAGNOSTICA/DATOS_{carrera}{semestre}.json"
        with open(ruta, "w") as json_file:
            json.dump({"data": diccionario_dataframes}, json_file, indent=4)
        print(f"El archivo JSON ha sido guardado en '{ruta}'.")

        return df_grafico
    
    generar_archivo(x,y,z,carrera,semestre)

    def generar_grafico(x, y, z, df):
        # Imprimir los valores de x e y
        print(x, y, z, df)

    # Configurar el tema de Seaborn
    sns.set_theme(style="whitegrid")
    
    custom_palette = ["#8c1919", "#fdb400","#000"]
    # Crear el gráfico utilizando Seaborn
    g = sns.catplot(
        data=df,
        kind="bar",
        x=x,
        y=y,
        hue=z,
        errorbar="sd",
        palette=custom_palette,
        alpha=0.6,
        height=6,
        aspect=2
    )

    #ax = g.ax
    #for p in ax.patches:
    #    ax.annotate(f'{p.get_height():.2f}', 
    #                (p.get_x() + p.get_width() / 2., p.get_height()), 
    #                ha='center', va='center', 
    #                xytext=(0, 10), 
    #                textcoords='offset points',
    #                rotation=90)

    # plt.figure(figsize=(10, 5))
    plt.xticks(rotation=90)
    plt.show()
    # Guardar el gráfico en un archivo temporal
    temp_file = io.BytesIO()
    g.savefig(temp_file, format="png")
    temp_file.seek(0)

    base64_image = base64.b64encode(temp_file.read()).decode("utf-8")
    imagen_base64 = {"data": base64_image}
    ruta_especifica = "C:/Users/Intevo/Desktop/UNIVERSIDAD DISTRITAL PROYECTO FOLDER/UNIVERSIDAD-DISTRITAL-PROYECTO/MODULO_ANALITICA_DIAGNOSTICA/Imagenes_Transformacion.json"
    with open(ruta_especifica, "w") as json_file:
        json.dump(imagen_base64, json_file)
    print(f"Los códigos Base64 de las imágenes han sido guardados en '{ruta_especifica}'.")
    # Retornar la imagen base64
    return imagen_base64

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)