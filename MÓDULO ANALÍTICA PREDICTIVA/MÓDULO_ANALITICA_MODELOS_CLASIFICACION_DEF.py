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
from pandas import read_csv
import io
import base64
import json
from openpyxl import Workbook
from openpyxl.drawing.image import Image as XLImage

import os
import os.path
from unidecode import unidecode

from urllib.error import HTTPError

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

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression 
from catboost import CatBoostClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC
from lightgbm import LGBMClassifier
from mlens.ensemble import SuperLearner


from sklearn.ensemble import AdaBoostClassifier 
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import StackingClassifier

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.metrics import normalized_mutual_info_score
from sklearn.metrics import cohen_kappa_score
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
save_path = 'C:/Users/Intevo/Desktop/UNIVERSIDAD DISTRITAL PROYECTO FOLDER/UNIVERSIDAD-DISTRITAL-PROYECTO/MÓDULO ANALÍTICA PREDICTIVA/DATOS'  # Reemplazar con la ruta deseada

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

carrera = ""
semestre = ""
modelo=""

class InputData(BaseModel):
    
    carrera: str
    semestre: str
    modelo: str

@app.post("/procesar_datos/")
async def procesar_datos(data: InputData):
    global modelo, carrera, semestre
    modelo= data.modelo
    carrera = data.carrera
    semestre = data.semestre
    
    
    print("Diccionario seleccion actualizado:", modelo)
    print("Carrera actualizada:", carrera)
    print("Semestre actualizado:", semestre)
    
    variables_por_carrera = {
    'industrial': {
        '1': ['PG_ICFES', 'CON_MAT_ICFES', 'FISICA_ICFES','QUIMICA_ICFES','IDIOMA_ICFES','LOCALIDAD','RENDIMIENTO_UNO'],
        '2': ['LOCALIDAD_COLEGIO', 'PG_ICFES', 'CON_MAT_ICFES', 'FISICA_ICFES', 'BIOLOGIA_ICFES', 'IDIOMA_ICFES', 'LOCALIDAD', 'PROMEDIO_UNO', 'CAR_UNO', 'NCC_UNO', 'NAA_UNO', 'NOTA_DIFERENCIAL', 'NOTA_DIBUJO', 'NOTA_QUIMICA', 'NOTA_CFJC', 'NOTA_TEXTOS', 'NOTA_SEMINARIO', 'NOTA_EE_UNO','RENDIMIENTO_DOS'],
        '3': ['PROMEDIO_UNO', 'NAA_UNO', 'NOTA_DIFERENCIAL', 'NOTA_DIBUJO', 'NOTA_TEXTOS', 'NOTA_EE_UNO', 'PROMEDIO_DOS', 'NCC_DOS', 'NCA_DOS', 'NAA_DOS', 'NOTA_ALGEBRA', 'NOTA_INTEGRAL', 'NOTA_MATERIALES', 'NOTA_PBASICA', 'NOTA_EE_DOS', 'RENDIMIENTO_TRES'],
        '4': ['PROMEDIO_UNO', 'NOTA_EE_UNO', 'PROMEDIO_DOS', 'NOTA_ALGEBRA', 'NOTA_INTEGRAL', 'NOTA_MATERIALES', 'NOTA_EE_DOS', 'NAA_TRES', 'NOTA_MULTIVARIADO', 'NOTA_ESTADISTICA_UNO', 'NOTA_TERMODINAMICA', 'NOTA_TGS', 'NOTA_EE_TRES','RENDIMIENTO_CUATRO'],
        '5': ['PROMEDIO_UNO', 'PROMEDIO_DOS', 'NOTA_ALGEBRA', 'NOTA_INTEGRAL', 'NOTA_MATERIALES', 'NOTA_EE_DOS','PROMEDIO_TRES', 'NAA_TRES', 'NOTA_MULTIVARIADO', 'NOTA_TERMODINAMICA', 'NOTA_ECUACIONES', 'NOTA_ESTADISTICA_DOS', 'NOTA_FISICA_DOS', 'NOTA_MECANICA', 'NOTA_PROCESOSQ', 'RENDIMIENTO_CINCO'],
        '6': ['PROMEDIO_UNO', 'PROMEDIO_DOS', 'NOTA_MATERIALES', 'NOTA_EE_DOS', 'PROMEDIO_TRES', 'NOTA_MULTIVARIADO', 'NOTA_FISICA_DOS', 'NOTA_EE_CUATRO', 'PROMEDIO_CINCO', 'NOTA_PROCESOSM', 'NOTA_ADMINISTRACION', 'NOTA_LENGUA_UNO', 'NOTA_EI_UNO', 'NOTA_EI_DOS', 'RENDIMIENTO_SEIS'],
        '7': ['PROMEDIO_UNO', 'PROMEDIO_DOS', 'NOTA_EE_DOS', 'PROMEDIO_TRES', 'NOTA_MULTIVARIADO', 'NOTA_FISICA_DOS', 'PROMEDIO_CINCO', 'NOTA_PROCESOSM', 'NOTA_LENGUA_UNO', 'NOTA_EI_DOS', 'PROMEDIO_SEIS', 'NCA_SEIS', 'NOTA_PLINEAL', 'NOTA_DISE O', 'NOTA_EI_TRES','RENDIMIENTO_SIETE'],
        '8': ['PROMEDIO_DOS', 'NOTA_EE_CUATRO', 'PROMEDIO_CINCO', 'NOTA_LENGUA_UNO','PROMEDIO_SEIS', 'NOTA_IECONOMICA', 'PROMEDIO_SIETE', 'NAA_SIETE', 'NOTA_GRAFOS', 'NOTA_CALIDAD_UNO', 'NOTA_ERGONOMIA', 'NOTA_EI_CINCO', 'RENDIMIENTO_OCHO'],
        '9': ['PROMEDIO_DOS', 'NOTA_EE_CUATRO', 'PROMEDIO_CINCO', 'PROMEDIO_SEIS', 'NOTA_IECONOMICA', 'PROMEDIO_SIETE', 'NAA_SIETE', 'NOTA_GRAFOS', 'NOTA_CALIDAD_UNO', 'NOTA_ERGONOMIA', 'NOTA_EI_CINCO', 'PROMEDIO_OCHO', 'NCC_OCHO', 'NOTA_LOG_UNO', 'NOTA_GOPERACIONES','NOTA_CALIDAD_DOS', 'NOTA_LENGUA_DOS', 'NOTA_CONTEXTO', 'RENDIMIENTO_NUEVE'],
        '10': ['PROMEDIO_SEIS', 'PROMEDIO_SIETE', 'PROMEDIO_OCHO', 'NOTA_CALIDAD_DOS', 'PROMEDIO_NUEVE', 'NAA_NUEVE', 'NOTA_GRADO_UNO', 'NOTA_LOG_DOS', 'NOTA_FINANZAS', 'NOTA_HISTORIA', 'RENDIMIENTO_DIEZ']
    },
    'sistemas': {
        '1': ['LOCALIDAD_COLEGIO', 'PG_ICFES', 'CON_MAT_ICFES', 'FISICA_ICFES', 'QUIMICA_ICFES', 'IDIOMA_ICFES', 'LOCALIDAD', 'RENDIMIENTO_UNO'],
        '2': ['LOCALIDAD_COLEGIO', 'PG_ICFES', 'CON_MAT_ICFES', 'IDIOMA_ICFES', 'PROMEDIO_UNO', 'NOTA_DIFERENCIAL', 'NOTA_PROG_BASICA', 'NOTA_CATEDRA_FJC', 'NOTA_TEXTOS', 'NOTA_SEMINARIO', 'NOTA_CATEDRA_DEM', 'NOTA_CATEDRA_CON', 'NOTA_LOGICA', 'RENDIMIENTO_DOS'],
        '3': ['LOCALIDAD_COLEGIO', 'PG_ICFES', 'CON_MAT_ICFES', 'IDIOMA_ICFES', 'PROMEDIO_UNO', 'PROMEDIO_DOS', 'NOTA_PROG_BASICA', 'NOTA_TEXTOS', 'NOTA_CATEDRA_DEM', 'NOTA_INTEGRAL', 'NOTA_PROG_ORIENTADA', 'NOTA_ETICA', 'RENDIMIENTO_TRES'],
        '4': ['LOCALIDAD_COLEGIO', 'PG_ICFES', 'CON_MAT_ICFES', 'IDIOMA_ICFES', 'PROMEDIO_UNO', 'PROMEDIO_DOS', 'PROMEDIO_TRES', 'NOTA_PROG_BASICA', 'NOTA_TEXTOS', 'NOTA_CATEDRA_DEM', 'NOTA_INTEGRAL', 'NOTA_PROG_ORIENTADA', 'NOTA_ETICA', 'NOTA_FISICA_DOS', 'NOTA_TGS', 'NOTA_PROG_AVANZADA', 'RENDIMIENTO_CUATRO'],
        '5': ['PROMEDIO_UNO', 'PROMEDIO_DOS', 'NOTA_ALGEBRA', 'NOTA_INTEGRAL', 'NOTA_MATERIALES', 'NOTA_EE_DOS', 'PROMEDIO_TRES', 'NAA_TRES', 'NOTA_MULTIVARIADO', 'NOTA_TERMODINAMICA', 'NOTA_ECUACIONES', 'NOTA_ESTADISTICA_DOS', 'NOTA_FISICA_DOS', 'NOTA_MECANICA', 'NOTA_PROCESOSQ', 'RENDIMIENTO_CINCO'],
        '6': ['PROMEDIO_UNO', 'NOTA_EE_UNO', 'PROMEDIO_DOS', 'NOTA_MATERIALES', 'NOTA_EE_DOS', 'PROMEDIO_TRES', 'NOTA_MULTIVARIADO', 'NOTA_ECONOMIA_UNO', 'NOTA_FISICA_DOS', 'NOTA_EE_CUATRO', 'PROMEDIO_CINCO', 'NOTA_PROCESOSM', 'NOTA_ADMINISTRACION', 'NOTA_LENGUA_UNO', 'NOTA_EI_UNO', 'NOTA_EI_DOS', 'RENDIMIENTO_SEIS'],
        '7': ['PROMEDIO_UNO', 'PROMEDIO_DOS', 'NOTA_EE_DOS', 'PROMEDIO_TRES', 'NOTA_MULTIVARIADO', 'NOTA_FISICA_DOS', 'PROMEDIO_CINCO', 'NOTA_PROCESOSM', 'NOTA_LENGUA_UNO', 'NOTA_EI_DOS', 'PROMEDIO_SEIS', 'NCA_SEIS', 'NOTA_PLINEAL', 'NOTA_DISE O', 'NOTA_EI_TRES', 'RENDIMIENTO_SIETE'],
        '8': ['PROMEDIO_UNO', 'PROMEDIO_DOS', 'NOTA_EE_DOS', 'PROMEDIO_TRES', 'NOTA_MULTIVARIADO', 'NOTA_FISICA_DOS', 'NOTA_EE_CUATRO', 'PROMEDIO_CINCO', 'NOTA_LENGUA_UNO', 'PROMEDIO_SEIS', 'NOTA_IECONOMICA', 'PROMEDIO_SIETE', 'NAA_SIETE', 'NOTA_GRAFOS', 'NOTA_CALIDAD_UNO', 'NOTA_ERGONOMIA', 'NOTA_EI_CINCO', 'RENDIMIENTO_OCHO'],
        '9': ['PROMEDIO_DOS', 'NOTA_EE_CUATRO', 'PROMEDIO_CINCO', 'PROMEDIO_SEIS', 'NOTA_IECONOMICA', 'PROMEDIO_SIETE', 'NAA_SIETE', 'NOTA_GRAFOS', 'NOTA_CALIDAD_UNO', 'NOTA_ERGONOMIA', 'NOTA_EI_CINCO', 'PROMEDIO_OCHO', 'NCC_OCHO', 'NOTA_LOG_UNO', 'NOTA_GOPERACIONES', 'NOTA_CALIDAD_DOS', 'NOTA_LENGUA_DOS', 'NOTA_CONTEXTO', 'RENDIMIENTO_NUEVE'],
        '10': ['PROMEDIO_SEIS', 'PROMEDIO_SIETE', 'PROMEDIO_OCHO', 'NOTA_CALIDAD_DOS', 'PROMEDIO_NUEVE', 'NAA_NUEVE', 'NOTA_GRADO_UNO', 'NOTA_LOG_DOS', 'NOTA_FINANZAS', 'NOTA_HISTORIA', 'RENDIMIENTO_DIEZ']
    },
    'catastral': {
        '1': ['variable1_catastral', 'variable2_catastral', 'variable3_catastral'],
        '2': ['variable4_catastral', 'variable5_catastral', 'variable6_catastral']
    }
    }
    
    def cargar_datos(carrera, semestre):
        ruta_archivo = f'C:/Users/Intevo/Desktop/UNIVERSIDAD DISTRITAL PROYECTO FOLDER/UNIVERSIDAD-DISTRITAL-PROYECTO/MÓDULO ANALÍTICA PREDICTIVA/DATOS/{carrera}{semestre}.csv'
        datos = pd.read_csv(ruta_archivo,sep=";")
        return datos
    
    datos = cargar_datos(carrera, semestre)
    columnas_filtradas = variables_por_carrera[carrera][semestre]
    df = datos[columnas_filtradas]
    print("DataFrame con columnas filtradas:")
    df=df.astype(int)
    df
    
    def numero_a_letras(numero):
        numeros_letras = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez']
        return numeros_letras[int(numero)]

    semestre_en_letras = numero_a_letras(semestre)
    print(semestre_en_letras)
    
    X = df.loc[:, ~df.columns.str.contains(f'RENDIMIENTO_{semestre_en_letras.upper()}')]
    Y = df.loc[:, df.columns.str.contains(f'RENDIMIENTO_{semestre_en_letras.upper()}')]                                                     
    print("Separación de datos usando Pandas") 
    print(X.shape, Y.shape)
    Y = LabelEncoder().fit_transform(Y.astype('str'))                
    print(X.shape, Y.shape)
    
    X_T_JOHNSON1 = X.copy(deep=True)
    def transformacion_johnson(X):
        transformador_johnson = PowerTransformer(method='yeo-johnson', standardize=True).fit(X)
        datos_transformados = transformador_johnson.transform(X)
        set_printoptions(precision=3)
        print(datos_transformados[:5, :])
        datos_transformados_df = pd.DataFrame(data=datos_transformados, columns=X.columns)
        return datos_transformados_df
    Xpandas_T_JOHNSON1 = transformacion_johnson(X_T_JOHNSON1)
    Xpandas_T_JOHNSON1.head(2)
    
    X_trn, X_tst, Y_trn, Y_tst = train_test_split(Xpandas_T_JOHNSON1, Y, test_size=0.3, random_state=2)
    
    # ---------------------------------------------------------------------------------------
    # MODELO KNEIGHBORS CLASSIFIER
    def entrenar_modelo_knn_con_transformacion(X_trn, Y_trn):
        X_trn_transformado = X_trn
        parameters = {
            'n_neighbors': [i for i in range(14, 18, 1)],
            'metric': ['euclidean', 'manhattan', 'minkowski'],
            'algorithm': ['auto'],
            'p': [i for i in range(1, 6)],
            'weights': ['uniform']
        }
        modelo = KNeighborsClassifier()
        semilla = 5
        num_folds = 10
        kfold = KFold(n_splits=num_folds, random_state=semilla, shuffle=True)
        metrica = 'accuracy'
        grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
        grid_resultado = grid.fit(X_trn_transformado, Y_trn)
        print("Resultados de GridSearchCV para el modelo")
        print("Mejor valor EXACTITUD usando k-fold:", grid_resultado.best_score_*100)
        print("Mejor valor PARAMETRO usando k-fold:", grid_resultado.best_params_)

        # Entrenar el modelo con los mejores hiperparámetros
        mejor_modelo = KNeighborsClassifier(**grid_resultado.best_params_)
        mejor_modelo.fit(X_trn_transformado, Y_trn)
        return mejor_modelo

    X_trn = X_trn
    Y_trn = Y_trn 

    modelo_knn = entrenar_modelo_knn_con_transformacion(X_trn, Y_trn)
    
    # Predecir las etiquetas para los datos de prueba
    resultados_df_knn = pd.DataFrame(columns=['MÉTRICA', 'VALOR'])

    Y_pred_entrenamiento= modelo_knn.predict(X_trn)

    precision = precision_score(Y_trn, Y_pred_entrenamiento, average='weighted')
    recall = recall_score(Y_trn, Y_pred_entrenamiento, average='weighted')
    f1 = f1_score(Y_trn, Y_pred_entrenamiento, average='weighted')
    accuracy = accuracy_score(Y_trn, Y_pred_entrenamiento)
    nmi = normalized_mutual_info_score(Y_trn, Y_pred_entrenamiento)
    kappa = cohen_kappa_score(Y_trn, Y_pred_entrenamiento)
    print("Precisión: ", round(precision*100,2))
    print("Exhaustividad: ", round(recall*100,2))
    print("Puntuación F1: ", round(f1*100,2))
    print("Exactitud: ", round(accuracy*100,2))
    print("Información Mutua Normalizada (NMI):", round(nmi*100,2))
    print("Índice Kappa de Cohen:", round(kappa*100,2))

    # Crear un DataFrame para cada métrica
    df_precision = pd.DataFrame({'MÉTRICA': ['Precisión'], 'VALOR': [round(precision*100, 2)]})
    df_recall = pd.DataFrame({'MÉTRICA': ['Exhaustividad'], 'VALOR': [round(recall*100, 2)]})
    df_f1 = pd.DataFrame({'MÉTRICA': ['Puntuación F1'], 'VALOR': [round(f1*100, 2)]})
    df_accuracy = pd.DataFrame({'MÉTRICA': ['Exactitud'], 'VALOR': [round(accuracy*100, 2)]})
    df_nmi=pd.DataFrame({'MÉTRICA': ['Información Mutua Normalizada (NMI)'], 'VALOR': [round(nmi*100, 2)]})
    df_kappa=pd.DataFrame({'MÉTRICA': ['Índice Kappa de Cohen'], 'VALOR': [round(kappa*100, 2)]})

    # Concatenar los DataFrames
    resultados_df_knn_entrenamiento = pd.concat([resultados_df_knn, df_precision, df_recall, df_f1, df_accuracy,df_nmi,df_kappa], ignore_index=True)
    resultados_df_knn_entrenamiento["MODELO"]='KNeighbors'
    resultados_df_knn_entrenamiento["TIPO_DE_DATOS"]='Entrenamiento'
    # Imprimir el DataFrame con los resultados
    resultados_df_knn_entrenamiento

    # Predecir las etiquetas para los datos de prueba
    resultados_df_knn = pd.DataFrame(columns=['MÉTRICA', 'VALOR'])

    Y_pred_prueba = modelo_knn.predict(X_tst)

    precision = precision_score(Y_tst, Y_pred_prueba, average='weighted')
    recall = recall_score(Y_tst, Y_pred_prueba, average='weighted')
    f1 = f1_score(Y_tst, Y_pred_prueba, average='weighted')
    accuracy = accuracy_score(Y_tst, Y_pred_prueba)
    nmi = normalized_mutual_info_score(Y_tst, Y_pred_prueba)
    kappa = cohen_kappa_score(Y_tst, Y_pred_prueba)
    print("Precisión: ", round(precision*100,2))
    print("Exhaustividad: ", round(recall*100,2))
    print("Puntuación F1: ", round(f1*100,2))
    print("Exactitud: ", round(accuracy*100,2))
    print("Información Mutua Normalizada (NMI):", round(nmi*100,2))
    print("Índice Kappa de Cohen:", round(kappa*100,2))

    # Crear un DataFrame para cada métrica
    df_precision = pd.DataFrame({'MÉTRICA': ['Precisión'], 'VALOR': [round(precision*100, 2)]})
    df_recall = pd.DataFrame({'MÉTRICA': ['Exhaustividad'], 'VALOR': [round(recall*100, 2)]})
    df_f1 = pd.DataFrame({'MÉTRICA': ['Puntuación F1'], 'VALOR': [round(f1*100, 2)]})
    df_accuracy = pd.DataFrame({'MÉTRICA': ['Exactitud'], 'VALOR': [round(accuracy*100, 2)]})
    df_nmi=pd.DataFrame({'MÉTRICA': ['Información Mutua Normalizada (NMI)'], 'VALOR': [round(nmi*100, 2)]})
    df_kappa=pd.DataFrame({'MÉTRICA': ['Índice Kappa de Cohen'], 'VALOR': [round(kappa*100, 2)]})

    # Concatenar los DataFrames
    resultados_df_knn_prueba = pd.concat([resultados_df_knn, df_precision, df_recall, df_f1, df_accuracy,df_nmi,df_kappa], ignore_index=True)
    resultados_df_knn_prueba["MODELO"]='KNeighbors'
    resultados_df_knn_prueba["TIPO_DE_DATOS"]='Prueba'
    # Imprimir el DataFrame con los resultados
    resultados_df_knn_prueba
    resultados_df_knn = pd.concat([resultados_df_knn_prueba,resultados_df_knn_entrenamiento], ignore_index=True)
    resultados_df_knn

    data_with_columns = resultados_df_knn.to_dict(orient='records')

    diccionario_dataframes = [
            {
                'dataTransformacion': data_with_columns,
                'columnas': resultados_df_knn.columns.tolist()
            }
        ]
    with open("resultados_df_knn.json", "w") as json_file:
        json.dump({"data": diccionario_dataframes}, json_file, indent=4)

        print("Los DataFrames han sido guardados en 'resultados_df_knn.json'.")





@app.get("/")
async def read_root():
    return {"message": "¡Bienvenido a la API!", "modelo": modelo, "carrera": carrera, "semestre": semestre}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)