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
        datos['GENERO']= np.where(datos['GENERO']==2,'FEMENINO',datos['GENERO'])
        datos['CALENDARIO'] = datos['CALENDARIO'].replace({0:'NO REGISTRA',0:'O', 1:'A', 2:'B', 3:'F'})
        datos['TIPO_COLEGIO'] = datos['TIPO_COLEGIO'].replace({0:'NO REGISTRA', 1:'OFICIAL', 2:'NO OFICIAL'})
        datos['LOCALIDAD_COLEGIO'] = datos['LOCALIDAD_COLEGIO'].replace({0:'NO REGISTRA', 1:'USAQUEN', 2:'CHAPINERO', 3:'SANTA FE', 3:'SANTAFE', 4:'SAN CRISTOBAL', 5:'USME', 6:'TUNJUELITO', 7:'BOSA', 8:'KENNEDY', 9:'FONTIBON', 10:'ENGATIVA',11: 'SUBA',12: 'BARRIOS UNIDOS', 13:'TEUSAQUILLO',14: 'LOS MARTIRES',15: 'ANTONIO NARINO', 16:'PUENTE ARANDA', 17: 'LA CANDELARIA', 18:'RAFAEL URIBE URIBE', 18:'RAFAEL URIBE', 19:'CIUDAD BOLIVAR', 20:'FUERA DE BOGOTA', 20:'SIN LOCALIDAD', 21:'SOACHA',22:'FUERA DE BOGOTA'})
        datos["DEPARTAMENTO"] = np.where((datos["DEPARTAMENTO"] >= 34), "NO REGISTRA", datos["DEPARTAMENTO"])
        datos["DEPARTAMENTO"] = datos["DEPARTAMENTO"].replace({"0": "NO REGISTRA", "1": "AMAZONAS", "2": "ANTIOQUIA", "3": "ARAUCA", "4": "ATLANTICO", "5": "BOGOTA", "6": "BOLIVAR", "7": "BOYACA", "8": "CALDAS", "9": "CAQUETA", "10": "CASANARE", "11": "CAUCA", "12": "CESAR", "13": "CHOCO", "14": "CORDOBA", "15": "CUNDINAMARCA", "16": "GUAINIA", "17": "GUAVIARE", "18": "HUILA", "19": "LA GUAJIRA", "20": "MAGDALENA", "21": "META", "22": "NARINO", "23": "NORTE SANTANDER", "24": "PUTUMAYO", "25": "QUINDIO", "26": "RISARALDA", "27": "SAN ANDRES Y PROVIDENCIA", "28": "SANTANDER", "29": "SUCRE", "30": "TOLIMA", "31": "VALLE", "32": "VAUPES", "33": "VICHADA",})
        datos["LOCALIDAD"] = np.where((datos["LOCALIDAD"] >= 20), "FUERA DE BOGOTA", datos["LOCALIDAD"])
        datos["LOCALIDAD"] = datos["LOCALIDAD"].replace({"0": "NO REGISTRA", "1": "USAQUEN", "2": "CHAPINERO", "3": "SANTA FE", "4": "SAN CRISTOBAL", "5": "USME", "6": "TUNJUELITO", "7": "BOSA", "8": "KENNEDY", "9": "FONTIBON", "10": "ENGATIVA", "11": "SUBA", "12": "BARRIOS UNIDOS", "13": "TEUSAQUILLO", "14": "LOS MARTIRES", "15": "ANTONIO NARINO", "16": "PUENTE ARANDA", "17": "LA CANDELARIA", "18": "RAFAEL URIBE URIBE", "19": "CIUDAD BOLIVAR",})
        datos["INSCRIPCION"] = np.where(datos["INSCRIPCION"] > 11, "NO REGISTRA", datos["INSCRIPCION"])
        datos["INSCRIPCION"] = datos["INSCRIPCION"].replace({"0": "NO REGISTRA", "1": "BENEFICIARIOS LEY 1081 DE 2006", "2": "BENEFICIARIOS LEY 1084 DE 2006", "3": "CONVENIO ANDRES BELLO", "4": "DESPLAZADOS", "5": "INDIGENAS", "6": "MEJORES BACHILLERES COL. DISTRITAL OFICIAL", "7": "MINORIAS ETNICAS Y CULTURALES", "8": "MOVILIDAD ACADEMICA INTERNACIONAL", "9": "NORMAL", "10": "TRANSFERENCIA EXTERNA", "11": "TRANSFERENCIA INTERNA",})
        datos["MUNICIPIO"] = np.where((datos["MUNICIPIO"] >= 225), "NO REGISTRA", datos["MUNICIPIO"])
        datos["MUNICIPIO"] = datos["MUNICIPIO"].replace({"0": "NO REGISTRA", "1": "ACACIAS", "2": "AGUACHICA", "3": "AGUAZUL", "4": "ALBAN", "5": "ALBAN (SAN JOSE)", "6": "ALVARADO", "7": "ANAPOIMA", "8": "ANOLAIMA", "9": "APARTADO", "10": "ARAUCA", "11": "ARBELAEZ", "12": "ARMENIA", "13": "ATACO", "14": "BARRANCABERMEJA", "15": "BARRANQUILLA", "16": "BELEN DE LOS ANDAQUIES", "17": "BOAVITA", "18": "BOGOTA", "19": "BOJACA", "20": "BOLIVAR", "21": "BUCARAMANGA", "22": "BUENAVENTURA", "23": "CABUYARO", "24": "CACHIPAY", "25": "CAICEDONIA", "26": "CAJAMARCA", "27": "CAJICA", "28": "CALAMAR", "29": "CALARCA", "30": "CALI", "31": "CAMPOALEGRE", "32": "CAPARRAPI", "33": "CAQUEZA", "34": "CARTAGENA", "35": "CASTILLA LA NUEVA", "36": "CERETE", "37": "CHAPARRAL", "38": "CHARALA", "39": "CHIA", "40": "CHIPAQUE", "41": "CHIQUINQUIRA", "42": "CHOACHI", "43": "CHOCONTA", "44": "CIENAGA", "45": "CIRCASIA", "46": "COGUA", "47": "CONTRATACION", "48": "COTA", "49": "CUCUTA", "50": "CUMARAL", "51": "CUMBAL", "52": "CURITI", "53": "CURUMANI", "54": "DUITAMA", "55": "EL BANCO", "56": "EL CARMEN DE BOLIVAR", "57": "EL COLEGIO", "58": "EL CHARCO", "59": "EL DORADO", "60": "EL PASO", "61": "EL ROSAL", "62": "ESPINAL", "63": "FACATATIVA", "64": "FLORENCIA", "65": "FLORIDABLANCA", "66": "FOMEQUE", "67": "FONSECA", "68": "FORTUL", "69": "FOSCA", "70": "FUNZA", "71": "FUSAGASUGA", "72": "GACHETA", "73": "GALERAS (NUEVA GRANADA)", "74": "GAMA", "75": "GARAGOA", "76": "GARZON", "77": "GIGANTE", "78": "GIRARDOT", "79": "GRANADA", "80": "GUACHUCAL", "81": "GUADUAS", "82": "GUAITARILLA", "83": "GUAMO", "84": "GUASCA", "85": "GUATEQUE", "86": "GUAYATA", "87": "GUTIERREZ", "88": "IBAGUE", "89": "INIRIDA", "90": "INZA", "91": "IPIALES", "92": "ITSMINA", "93": "JENESANO", "94": "LA CALERA", "95": "LA DORADA", "96": "LA MESA", "97": "LA PLATA", "98": "LA UVITA", "99": "LA VEGA", "100": "LIBANO", "101": "LOS PATIOS", "102": "MACANAL", "103": "MACHETA", "104": "MADRID", "105": "MAICAO", "106": "MALAGA", "107": "MANAURE BALCON DEL 12", "108": "MANIZALES", "109": "MARIQUITA", "110": "MEDELLIN", "111": "MEDINA", "112": "MELGAR", "113": "MITU", "114": "MOCOA", "115": "MONTERIA", "116": "MONTERREY", "117": "MOSQUERA", "118": "NATAGAIMA", "119": "NEIVA", "120": "NEMOCON", "121": "OCANA", "122": "ORITO", "123": "ORTEGA", "124": "PACHO", "125": "PAEZ (BELALCAZAR)", "126": "PAICOL", "127": "PAILITAS", "128": "PAIPA", "129": "PALERMO", "130": "PALMIRA", "131": "PAMPLONA", "132": "PANDI", "133": "PASCA", "134": "PASTO", "135": "PAZ DE ARIPORO", "136": "PAZ DE RIO", "137": "PITALITO", "138": "POPAYAN", "139": "PUENTE NACIONAL", "140": "PUERTO ASIS", "141": "PUERTO BOYACA", "142": "PUERTO LOPEZ", "143": "PUERTO SALGAR", "144": "PURIFICACION", "145": "QUETAME", "146": "QUIBDO", "147": "RAMIRIQUI", "148": "RICAURTE", "149": "RIOHACHA", "150": "RIVERA", "151": "SABOYA", "152": "SAHAGUN", "153": "SALDAÑA", "154": "SAMACA", "155": "SAMANA", "156": "SAN AGUSTIN", "157": "SAN ANDRES", "158": "SAN BERNARDO", "159": "SAN EDUARDO", "160": "SAN FRANCISCO", "161": "SAN GIL", "162": "SAN JOSE DEL FRAGUA", "163": "SAN JOSE DEL GUAVIARE", "164": "SAN LUIS DE PALENQUE", "165": "SAN MARCOS", "166": "SAN MARTIN", "167": "SANDONA", "168": "SAN VICENTE DEL CAGUAN", "169": "SANTA MARTA", "170": "SANTA SOFIA", "171": "SESQUILE", "172": "SIBATE", "173": "SIBUNDOY", "174": "SILVANIA", "175": "SIMIJACA", "176": "SINCE", "177": "SINCELEJO", "178": "SOACHA", "179": "SOATA", "180": "SOCORRO", "181": "SOGAMOSO", "182": "SOLEDAD", "183": "SOPO", "184": "SORACA", "185": "SOTAQUIRA", "186": "SUAITA", "187": "SUBACHOQUE", "188": "SUESCA", "189": "SUPATA", "190": "SUTAMARCHAN", "191": "SUTATAUSA", "192": "TABIO", "193": "TAMESIS", "194": "TARQUI", "195": "TAUSA", "196": "TENA", "197": "TENJO", "198": "TESALIA", "199": "TIBANA", "200": "TIMANA", "201": "TOCANCIPA", "202": "TUBARA", "203": "TULUA", "204": "TUMACO", "205": "TUNJA", "206": "TURBACO", "207": "TURMEQUE", "208": "UBATE", "209": "UMBITA", "210": "UNE", "211": "VALLEDUPAR", "212": "VELEZ", "213": "VENADILLO", "214": "VENECIA (OSPINA PEREZ)", "215": "VILLA DE LEYVA", "216": "VILLAHERMOSA", "217": "VILLANUEVA", "218": "VILLAPINZON", "219": "VILLAVICENCIO", "220": "VILLETA", "221": "YACOPI", "222": "YOPAL", "223": "ZIPACON", "224": "ZIPAQUIRA"})
        
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