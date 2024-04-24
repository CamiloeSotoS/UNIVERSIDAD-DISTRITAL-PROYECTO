#---------------------------------------------------------------
#---------------------------------------------------------------
# LIBRERIAS
#---------------------------------------------------------------
import warnings
warnings.filterwarnings('ignore')
from numpy import set_printoptions
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
pd.options.display.max_columns=None
import seaborn as sns 
import io
import base64
import json
import os
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
#---------------------------------------------------------------
#---------------------------------------------------------------
# CARGUE DE DATOS
#---------------------------------------------------------------
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('C:/Users/Intevo/Desktop/UNIVERSIDAD DISTRITAL PROYECTO FOLDER/credentials.json', SCOPES) # Reemplazar con la ruta correcta
        creds = flow.run_local_server(port=0)
    with open('C:/Users/Intevo/Desktop/UNIVERSIDAD DISTRITAL PROYECTO FOLDER/token.json', 'w') as token:
        token.write(creds.to_json())
        
# Crear una instancia de la API de Drive
drive_service = build('drive', 'v3', credentials=creds)

# ID de la carpeta de Google Drive
folder_id = '1hQeetmO4XIObUefS_nzePqKqq3VksUEC'

# Ruta de destino para guardar los archivos descargados
save_path = 'C:/Users/Intevo/Desktop/UNIVERSIDAD DISTRITAL PROYECTO FOLDER/UNIVERSIDAD-DISTRITAL-PROYECTO/MODULO_ANALITICA_PREDICTIVA/DATOS'  # Reemplazar con la ruta deseada

# Función para descargar archivos de la carpeta de Drive
def download_folder(folder_id, save_path):
    results = drive_service.files().list(
        q=f"'{folder_id}' in parents and trashed=false",
        fields='files(id, name)').execute()
    items = results.get('files', [])
    for item in items:
        file_id = item['id']
        file_name = item['name']
        request = drive_service.files().get_media(fileId=file_id)
        fh = io.FileIO(os.path.join(save_path, file_name), 'wb')
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
    

app = FastAPI()

diccionario_seleccion = {
    "columnas": [],
}
carrera = ""
semestre = ""

class InputData(BaseModel):
    columnas: List[str]
    carrera: str
    semestre: int

@app.post("/procesar_datos/")
async def procesar_datos(data: InputData):
    global diccionario_seleccion, carrera, semestre
    
    diccionario_seleccion["columnas"] = data.columnas
    carrera = data.carrera
    semestre = data.semestre
    
    print("Diccionario seleccion actualizado:", diccionario_seleccion)
    print("Carrera actualizada:", carrera)
    print("Semestre actualizado:", semestre)
    
    # Definir la función de carga de datos
    def cargar_datos(carrera, semestre):
        ruta_archivo = f'C:/Users/Intevo/Desktop/UNIVERSIDAD DISTRITAL PROYECTO FOLDER/UNIVERSIDAD-DISTRITAL-PROYECTO/MODULO_ANALITICA_PREDICTIVA/DATOS/{carrera}{semestre}.csv'
        datos = pd.read_csv(ruta_archivo,sep=";")
        return datos
    df = cargar_datos(carrera, semestre)
    #df = df.drop(['NUMERO'], axis=1)
    X=df             
    print(X.shape)
    X1=X.copy(deep=True)
    X_R1 = X.copy(deep=True)  
    X_E1 = X.copy(deep=True)  
    X_N1 = X.copy(deep=True)   
    X_ROB1 = X.copy(deep=True)   
    X_T_BOX1 = X.copy(deep=True)  
    X_T_JOHNSON1 = X.copy(deep=True) 
    
    #---------------------------------------------------------------
    #---------------------------------------------------------------
    # TRANSFORMACIONES
    #---------------------------------------------------------------
    # SIN TRANSFORMACION
    print("sin transformaición)")
    columnas_seleccionadas = diccionario_seleccion.get('columnas', [])
    if columnas_seleccionadas:
        X = X1[columnas_seleccionadas]
    else:
        X = X1 
    fig1, ax = plt.subplots(figsize=(4, 6))
    for columna in X.columns:
        sns.kdeplot(X[columna], ax=ax, label=columna)
    ax.set_title('SIN TRANSFORMAR')
    ax.set_xlabel('Valor')
    ax.set_ylabel('Densidad')
    ax.legend()
    plt.show()
    print("sin transformaición)")
    #---------------------------------------------------------------
    # REESCALADO
    print("reescalado)")
    def reescalar_datos(X):
        transformador = MinMaxScaler(feature_range=(0, 1)).fit(X)
        datos_reescalados = transformador.transform(X)
        set_printoptions(precision=3)
        print(datos_reescalados[:5, :])
        datos_reescalados_df = pd.DataFrame(data=datos_reescalados, columns=X.columns)
        return datos_reescalados_df
    Xpandas_R1 = reescalar_datos(X_R1)
    Xpandas_R1.head(2)

    columnas_seleccionadas = diccionario_seleccion.get('columnas', [])
    if columnas_seleccionadas:
        Xpandas_R = Xpandas_R1[columnas_seleccionadas]
    else:
        Xpandas_R = Xpandas_R1
    fig2, ax = plt.subplots(figsize=(4, 6))
    for columna in Xpandas_R.columns:
        sns.kdeplot(Xpandas_R[columna], ax=ax, label=columna)
    ax.set_title('REESCALAR')
    ax.set_xlabel('Valor')
    ax.set_ylabel('Densidad')
    ax.legend()
    plt.show()
    print("reescalado)")
    #---------------------------------------------------------------
    # ESTANDARIZADO
    print("estandarizado)")
    def estandarizar_datos(X):
        transformador = StandardScaler().fit(X)
        datos_estandarizados = transformador.transform(X)
        set_printoptions(precision=3)
        print(datos_estandarizados[:5, :])
        datos_estandarizados_df = pd.DataFrame(data=datos_estandarizados, columns=X.columns)
        return datos_estandarizados_df
    Xpandas_E1 = estandarizar_datos(X_E1)
    Xpandas_E1.head(2)
    columnas_seleccionadas = diccionario_seleccion.get('columnas', [])

    if columnas_seleccionadas:
        Xpandas_E = Xpandas_E1[columnas_seleccionadas]
    else:
        Xpandas_E = Xpandas_E1 
    fig3, ax = plt.subplots(figsize=(4, 6))
    for columna in Xpandas_E.columns:
        sns.kdeplot(Xpandas_E[columna], ax=ax, label=columna)
    ax.set_title('ESTANDARIZACIÓN')
    ax.set_xlabel('Valor')
    ax.set_ylabel('Densidad')
    ax.legend()
    plt.show()
    print("estandarizado)")
    #---------------------------------------------------------------
    # NORMALIZADO
    print("normalizado")
    def normalizar_datos(X):
        transformador = Normalizer().fit(X)
        datos_normalizados = transformador.transform(X)
        set_printoptions(precision=3)
        print(datos_normalizados[:5, :])
        datos_normalizados_df = pd.DataFrame(data=datos_normalizados, columns=X.columns)
        return datos_normalizados_df
    Xpandas_N1 = normalizar_datos(X_N1)
    Xpandas_N1.head(2)

    columnas_seleccionadas = diccionario_seleccion.get('columnas', [])
    if columnas_seleccionadas:
        Xpandas_N = Xpandas_N1[columnas_seleccionadas]
    else:
        Xpandas_N = Xpandas_N1 

    fig4, ax = plt.subplots(figsize=(4, 6))
    for columna in Xpandas_N.columns:
        sns.kdeplot(Xpandas_N[columna], ax=ax, label=columna)
    ax.set_title('NORMALIZACIÓN')
    ax.set_xlabel('Valor')
    ax.set_ylabel('Densidad')
    ax.legend()
    plt.show()
    print("normalizado")
    
    #---------------------------------------------------------------
    # ESTANDARIZACION ROBUSTA
    print("robusta")
    def estandarizacion_robusta(X):
        transformador = RobustScaler(quantile_range=(25, 75)).fit(X)
        datos_estandarizados = transformador.transform(X)
        set_printoptions(precision=3)
        print(datos_estandarizados[:5, :])
        datos_estandarizados_df = pd.DataFrame(data=datos_estandarizados, columns=X.columns)
        return datos_estandarizados_df
    Xpandas_ROB1 = estandarizacion_robusta(X_ROB1)
    Xpandas_ROB1.head(2)

    columnas_seleccionadas = diccionario_seleccion.get('columnas', [])
    if columnas_seleccionadas:
        Xpandas_ROB = Xpandas_ROB1[columnas_seleccionadas]
    else:
        Xpandas_ROB = Xpandas_ROB1 

    fig5, ax = plt.subplots(figsize=(4, 6))
    for columna in Xpandas_ROB.columns:
        sns.kdeplot(Xpandas_ROB[columna], ax=ax, label=columna)
    ax.set_title('ESTANDARIZACIÓN ROBUSTA')
    ax.set_xlabel('Valor')
    ax.set_ylabel('Densidad')
    ax.legend()
    plt.show()
    print("robusta")
    #---------------------------------------------------------------
    # YEO JHONSON
    print("yeo")
    def transformacion_johnson(X):
        transformador_johnson = PowerTransformer(method='yeo-johnson', standardize=True).fit(X)
        datos_transformados = transformador_johnson.transform(X)
        set_printoptions(precision=3)
        print(datos_transformados[:5, :])
        datos_transformados_df = pd.DataFrame(data=datos_transformados, columns=X.columns)
        return datos_transformados_df
    Xpandas_T_JOHNSON1 = transformacion_johnson(X_T_JOHNSON1)
    Xpandas_T_JOHNSON1.head(2)

    columnas_seleccionadas = diccionario_seleccion.get('columnas', [])
    if columnas_seleccionadas:
        Xpandas_T_JOHNSON = Xpandas_T_JOHNSON1[columnas_seleccionadas]
    else:
        Xpandas_T_JOHNSON = Xpandas_T_JOHNSON1

    fig6, ax = plt.subplots(figsize=(4, 6))
    for columna in Xpandas_T_JOHNSON.columns:
        sns.kdeplot(Xpandas_T_JOHNSON[columna], ax=ax, label=columna)
    ax.set_title('TRANSFORMACIÓN YEO-JHONSON')
    ax.set_xlabel('Valor')
    ax.set_ylabel('Densidad')
    ax.legend()
    plt.show()
    print("yeo")
    #---------------------------------------------------------------
    # BOX COX
    print("box")
    def transformacion_minmax_boxcox(X):
        std_dev = X.std()
        constantes = std_dev[std_dev == 0].index
        X_sin_constantes = X.drop(constantes, axis=1)
        minmax_scaler = MinMaxScaler(feature_range=(1, 2))
        Reescalar_X_R = minmax_scaler.fit_transform(X_sin_constantes)
        print("Reescalamiento Min-Max:")
        print(Reescalar_X_R[:5])
        boxcox_transformer = PowerTransformer(method='box-cox', standardize=True)
        Reescalar_X_T_BOX = boxcox_transformer.fit_transform(pd.DataFrame(Reescalar_X_R, columns=X_sin_constantes.columns))
        print("\nTransformación Box-Cox:")
        print(Reescalar_X_T_BOX[:5])
        Xpandas_T_BOX = pd.DataFrame(data=Reescalar_X_T_BOX, columns=X_sin_constantes.columns)
        return Xpandas_T_BOX
    Xpandas_T_BOX1 = transformacion_minmax_boxcox(X_T_BOX1)
    Xpandas_T_BOX1.head(2)

    std_dev = X1.std()
    constantes = std_dev[std_dev == 0].index
    print("Columnas constantes:", constantes)
    columnas_constantes = std_dev[std_dev == 0].index
    columnas_recuperar = [col for col in columnas_constantes if col in Xpandas_T_BOX1.columns]
    columnas_recuperadas = X1[columnas_recuperar]
    Xpandas_T_BOX1 = pd.concat([Xpandas_T_BOX1, columnas_recuperadas], axis=1)


    columnas_seleccionadas = diccionario_seleccion.get('columnas', [])
    if columnas_seleccionadas:
        Xpandas_T_BOX = Xpandas_T_BOX1[columnas_seleccionadas]
    else:
        Xpandas_T_BOX = Xpandas_T_BOX1 

    fig7, ax = plt.subplots(figsize=(4, 6))
    for columna in Xpandas_T_BOX.columns:
        sns.kdeplot(Xpandas_T_BOX[columna], ax=ax, label=columna)
    ax.set_title('TRANSFORMACIÓN BOX-COX')
    ax.set_xlabel('Valor')
    ax.set_ylabel('Densidad')
    ax.legend()
    plt.show()
    print("box")
    #---------------------------------------------------------------
    #---------------------------------------------------------------
    # FIGURAS B64
    #---------------------------------------------------------------
    figuras = {
        "fig1": fig1,
        "fig2": fig2,
        "fig3": fig3,
        "fig4": fig4,
        "fig5": fig5,
        "fig6": fig6,
        "fig7": fig7
    }  

    imagenes_base64 = []

    for nombre_figura, figura in figuras.items():
        buf = io.BytesIO()
        figura.savefig(buf, format='png')
        buf.seek(0)

        imagen_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        imagenes_base64.append(imagen_base64)

        print(f"El código Base64 de la imagen {nombre_figura} ha sido guardado.")

    with open("Imagenes_Transformacion.json", "w") as json_file:
        json.dump({"data": imagenes_base64}, json_file)
    print("Los códigos Base64 de las imágenes han sido guardados en 'Imagenes_Transformacion.json'.")

    X1["TRANSFORMACION"]="SIN TRANSFORMACION"
    Xpandas_R1["TRANSFORMACION"]="REESCALADO"
    Xpandas_E1["TRANSFORMACION"]="ESTANDARIZACION"
    Xpandas_N1["TRANSFORMACION"]="NORMALIZADO"
    Xpandas_ROB1["TRANSFORMACION"]="ESTANDARIZACION ROBUSTA"
    Xpandas_T_BOX1["TRANSFORMACION"]="BOX COX"
    Xpandas_T_JOHNSON1["TRANSFORMACION"]="YEO JHONSON"


    X_values1=pd.concat([X1,Xpandas_R1,Xpandas_E1,Xpandas_N1,
                        Xpandas_ROB1,Xpandas_T_BOX1,Xpandas_T_JOHNSON1],axis=0)
    X_values1.fillna(0,inplace=True)

    data_with_columns = X_values1.to_dict(orient='records')

    diccionario_dataframes = [
        {

            'dataTransformacion': data_with_columns,
            'columnas': X_values1.columns.tolist()
        }
    ]

    # Guardar en archivo JSON
    with open("Dataframe_Transformacion.json", "w") as json_file:
        json.dump({"data": diccionario_dataframes}, json_file, indent=4)

    print("Los DataFrames han sido guardados en 'Dataframe_Transformacion.json'.")


@app.get("/")
async def read_root():
    return {"message": "¡Bienvenido a la API!", "diccionario_seleccion": diccionario_seleccion, "carrera": carrera, "semestre": semestre}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)









