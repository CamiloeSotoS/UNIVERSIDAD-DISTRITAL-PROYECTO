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

from google.auth.transport.requests import Request as Resquest2
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

from fastapi import FastAPI, Request, HTTPException
from starlette.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel
import pickle 

from pydantic import BaseModel
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from sklearn.ensemble import AdaBoostClassifier 
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression 


from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from lightgbm import LGBMClassifier
from mlens.ensemble import SuperLearner

from sklearn.preprocessing import LabelEncoder, PowerTransformer
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle
from sklearn.tree import DecisionTreeClassifier

# import torch
# import torch.nn as nn
# import torch.optim as optim
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# CARGUE DE DATOS
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# creds = None

# if os.path.exists('token.json'):
#     creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# if not creds or not creds.valid:
#     if creds and creds.expired and creds.refresh_token:
#         creds.refresh(Resquest2())
#     else:
#         flow = InstalledAppFlow.from_client_secrets_file('../credentials.json', SCOPES) # Reemplazar con la ruta correcta
#         creds = flow.run_local_server(port=0)
#     with open('../token.json', 'w') as token:
#         token.write(creds.to_json())
        
# # Crear una instancia de la API de Drive
# drive_service = build('drive', 'v3', credentials=creds)

# # ID de la carpeta de Google Drive
# folder_id = '1hQeetmO4XIObUefS_nzePqKqq3VksUEC'

# # Ruta de destino para guardar los archivos descargados
# cwd = os.getcwd()
# save_path = os.path.join(cwd, 'DATOS')  # Reemplazar con la ruta deseada

# # Función para descargar archivos de la carpeta de Drive
# def download_folder(folder_id, save_path):
#     results = drive_service.files().list(
#         q=f"'{folder_id}' in parents and trashed=false",
#         fields='files(id, name)').execute()
#     items = results.get('files', [])
#     for item in items:
#         file_id = item['id']
#         file_name = item['name']
#         request = drive_service.files().get_media(fileId=file_id)
#         fh = io.FileIO(os.path.join(save_path, file_name), 'wb')
#         downloader = MediaIoBaseDownload(fh, request)
#         done = False
#         while done is False:
#             status, done = downloader.next_chunk()
#             print(f"Descargando {file_name}: {int(status.progress() * 100)}%")
#     print("Descarga completa")

# # Descargar archivos de la carpeta
# download_folder(folder_id, save_path)

# Listar archivos descargados
# files = os.listdir(save_path)
# print("Archivos descargados:")
# for file in files:
#     print(file)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

carrera = ""
semestre = ""
mejor_modelo = None

variables_por_carrera = { 
    'industrial': {
        '1': ['PG_ICFES', 'CON_MAT_ICFES', 'FISICA_ICFES','QUIMICA_ICFES','IDIOMA_ICFES','LOCALIDAD','RENDIMIENTO_UNO'],
        '2': ['LOCALIDAD_COLEGIO', 'PG_ICFES', 'CON_MAT_ICFES', 'FISICA_ICFES', 'BIOLOGIA_ICFES', 'IDIOMA_ICFES', 'LOCALIDAD', 'PROMEDIO_UNO', 'CAR_UNO', 'NCC_UNO', 'NAA_UNO', 'NOTA_DIFERENCIAL', 'NOTA_DIBUJO', 'NOTA_QUIMICA', 'NOTA_CFJC', 'NOTA_TEXTOS', 'NOTA_SEMINARIO', 'NOTA_EE_UNO','RENDIMIENTO_DOS'],
        '3': ['PROMEDIO_UNO', 'NAA_UNO', 'NOTA_DIFERENCIAL', 'NOTA_DIBUJO', 'NOTA_TEXTOS', 'NOTA_EE_UNO', 'PROMEDIO_DOS', 'NCC_DOS', 'NCA_DOS', 'NAA_DOS', 'NOTA_ALGEBRA', 'NOTA_INTEGRAL', 'NOTA_MATERIALES', 'NOTA_PBASICA', 'NOTA_EE_DOS', 'RENDIMIENTO_TRES'],
        '4': ['PROMEDIO_UNO', 'NOTA_EE_UNO', 'PROMEDIO_DOS', 'NOTA_ALGEBRA', 'NOTA_INTEGRAL', 'NOTA_MATERIALES', 'NOTA_EE_DOS', 'NAA_TRES', 'NOTA_MULTIVARIADO', 'NOTA_ESTADISTICA_UNO', 'NOTA_TERMODINAMICA', 'NOTA_TGS', 'NOTA_EE_TRES','RENDIMIENTO_CUATRO'],
        '5': ['PROMEDIO_UNO', 'PROMEDIO_DOS', 'NOTA_ALGEBRA', 'NOTA_INTEGRAL', 'NOTA_MATERIALES', 'NOTA_EE_DOS','PROMEDIO_TRES', 'NAA_TRES', 'NOTA_MULTIVARIADO', 'NOTA_TERMODINAMICA', 'NOTA_ECUACIONES', 'NOTA_ESTADISTICA_DOS', 'NOTA_FISICA_DOS', 'NOTA_MECANICA', 'NOTA_PROCESOSQ', 'RENDIMIENTO_CINCO'],
        '6': ['PROMEDIO_UNO', 'PROMEDIO_DOS', 'NOTA_MATERIALES', 'NOTA_EE_DOS', 'PROMEDIO_TRES', 'NOTA_MULTIVARIADO', 'NOTA_FISICA_DOS', 'NOTA_EE_CUATRO', 'PROMEDIO_CINCO', 'NOTA_PROCESOSM', 'NOTA_ADMINISTRACION', 'NOTA_LENGUA_UNO', 'NOTA_EI_UNO', 'NOTA_EI_DOS', 'RENDIMIENTO_SEIS'],
        '7': ['PROMEDIO_UNO', 'PROMEDIO_DOS', 'NOTA_EE_DOS', 'PROMEDIO_TRES', 'NOTA_MULTIVARIADO', 'NOTA_FISICA_DOS', 'PROMEDIO_CINCO', 'NOTA_PROCESOSM', 'NOTA_LENGUA_UNO', 'NOTA_EI_DOS', 'PROMEDIO_SEIS', 'NCA_SEIS', 'NOTA_PLINEAL', 'NOTA_DISENO', 'NOTA_EI_TRES','RENDIMIENTO_SIETE'],
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

class InputData(BaseModel):
    carrera: str
    semestre: str
    from sklearn.metrics import accuracy_score
    
@app.post("/procesar_datos/")
async def procesar_datos(data: InputData):
    global carrera, semestre
    carrera = data.carrera
    semestre = data.semestre
    print("Carrera actualizada:", carrera)
    print("Semestre actualizado:", semestre)
    cargar_entrenar_modelo()

@app.post("/predict")
def predict(data: dict):
    global mejor_modelo
    if mejor_modelo:
        try:
            prediction = int(mejor_modelo.predict([list(data.values())])[0])
            return {"prediction": prediction}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    else:
        raise HTTPException(status_code=404, detail="No hay modelo entrenado")
    
def cargar_datos(carrera, semestre):
    ruta_archivo = f'C:/Users/Intevo/Desktop/UNIVERSIDAD DISTRITAL PROYECTO FOLDER/UNIVERSIDAD-DISTRITAL-PROYECTO/MODULO_ANALITICA_PRACTICO/DATOS/{carrera}{semestre}.csv'
    datos = pd.read_csv(ruta_archivo, sep=";")
    return datos

def transformacion_johnson(X):
    transformador_johnson = PowerTransformer(method='yeo-johnson', standardize=True).fit(X)
    datos_transformados = transformador_johnson.transform(X)
    datos_transformados_df = pd.DataFrame(data=datos_transformados, columns=X.columns)
    return datos_transformados_df

def numero_a_letras(numero):
    numeros_letras = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez']
    return numeros_letras[int(numero)]

def cargar_entrenar_modelo():
    global mejor_modelo
    try:
        datos = cargar_datos(carrera, semestre)
        columnas_filtradas = variables_por_carrera[carrera][semestre]
        df = datos[columnas_filtradas].astype(int)
        semestre_en_letras = numero_a_letras(semestre)
        X = df.loc[:, ~df.columns.str.contains(f'RENDIMIENTO_{semestre_en_letras.upper()}')]
        Y = df.loc[:, df.columns.str.contains(f'RENDIMIENTO_{semestre_en_letras.upper()}')]
        Y = LabelEncoder().fit_transform(Y.astype('str'))
        X_transformado = transformacion_johnson(X)
        X_trn, X_tst, Y_trn, Y_tst = train_test_split(X_transformado, Y, test_size=0.3, random_state=2)
        
        modelo_knn, accuracy_knn, mejores_hiperparametros_knn = entrenar_modelo_knn_con_transformacion(X_trn, Y_trn, X_tst, Y_tst)
        modelo_svc, accuracy_svc = entrenar_modelo_svc_con_transformacion(X_trn, Y_trn, X_tst, Y_tst)
        modelo_tree, accuracy_tree,mejores_hiperparametros_tree= entrenar_modelo_tree_con_transformacion(X_trn, Y_trn, X_tst, Y_tst)
        modelo_gaussian, accuracy_gaussian=entrenar_modelo_gaussian_con_transformacion(X_trn, Y_trn, X_tst, Y_tst) 
        modelo_LDA, accuracy_LDA = entrenar_modelo_LDA_con_transformacion(X_trn, Y_trn, X_tst, Y_tst) 
        modelo_BG, accuracy_BG, mejores_hiperparametros_BG = entrenar_modelo_BG_con_transformacion(X_trn, Y_trn, X_tst, Y_tst,mejores_hiperparametros_tree)
        modelo_random, accuracy_random, mejores_hiperparametros_random= entrenar_modelo_random_con_transformacion(X_trn, Y_trn, X_tst, Y_tst) 
        modelo_extra, accuracy_extra, mejores_hiperparametros_extra= entrenar_modelo_extra_con_transformacion(X_trn, Y_trn, X_tst, Y_tst)
        modelo_ADA, accuracy_ADA, mejores_hiperparametros_ADA= entrenar_modelo_ADA_con_transformacion(X_trn, Y_trn, X_tst, Y_tst)
        modelo_GD, accuracy_GD, mejores_hiperparametros_GD= entrenar_modelo_GD_con_transformacion(X_trn, Y_trn, X_tst, Y_tst)
        modelo_XB, accuracy_XB, mejores_hiperparametros_XB= entrenar_modelo_XB_con_transformacion(X_trn, Y_trn, X_tst, Y_tst)
        modelo_CB, accuracy_CB,= entrenar_modelo_CB_con_transformacion(X_trn, Y_trn, X_tst, Y_tst)
        modelo_LIGHT, accuracy_LIGHT=entrenar_modelo_LIGHT_con_transformacion(X_trn, Y_trn, X_tst, Y_tst)
        modelo_voting_hard, accuracy_voting_hard=entrenar_modelo_voting_hard_con_transformacion(X_trn, Y_trn,X_tst, Y_tst,
                                                mejores_hiperparametros_GD,
                                                mejores_hiperparametros_tree,
                                                mejores_hiperparametros_ADA,
                                                mejores_hiperparametros_extra,
                                                mejores_hiperparametros_random,
                                                mejores_hiperparametros_BG,
                                                mejores_hiperparametros_XB)
        modelo_voting_soft, accuracy_voting_soft=entrenar_modelo_voting_soft_con_transformacion(X_trn, Y_trn,X_tst, Y_tst,
                                                mejores_hiperparametros_GD,
                                                mejores_hiperparametros_tree,
                                                mejores_hiperparametros_ADA,
                                                mejores_hiperparametros_extra,
                                                mejores_hiperparametros_random,
                                                mejores_hiperparametros_BG)
        modelo_stacking_lineal, accuracy_stacking_lineal=entrenar_modelo_stacking_lineal_con_transformacion(X_trn, Y_trn,X_tst, Y_tst,
                                                mejores_hiperparametros_tree,
                                                mejores_hiperparametros_ADA,
                                                mejores_hiperparametros_extra,
                                                mejores_hiperparametros_random,
                                                mejores_hiperparametros_BG)
        
        modelo_stacking_nolineal, accuracy_stacking_nolineal=entrenar_modelo_stacking_nolineal_con_transformacion(X_trn, Y_trn,X_tst, Y_tst,
                                                mejores_hiperparametros_tree,
                                                mejores_hiperparametros_extra,
                                                mejores_hiperparametros_random,
                                                mejores_hiperparametros_BG)

        modelo_super_aprendiz, accuracy_super_aprendiz=entrenar_modelo_super_aprendiz(X_trn, Y_trn,X_tst, Y_tst,
                            mejores_hiperparametros_tree,mejores_hiperparametros_extra,mejores_hiperparametros_random)

        modelo_super_aprendiz_dos_capas, accuracy_super_aprendiz_dos_capas=entrenar_modelo_super_aprendiz_dos_capas(X_trn, Y_trn,X_tst, Y_tst, 
                                                mejores_hiperparametros_tree,mejores_hiperparametros_extra,mejores_hiperparametros_random)
        
        modelos = {
            'KNeighborsClassifier': (modelo_knn, accuracy_knn),
            'SVC': (modelo_svc, accuracy_svc),
            'DecisionTree': (modelo_tree,accuracy_tree),
            'NaiveBayes': (modelo_gaussian,accuracy_gaussian),
            'LDA':(modelo_LDA,accuracy_LDA),
            'Bagging':(modelo_BG,accuracy_BG),
            'RandomForest': (modelo_random,accuracy_random),
            'Extratrees': (modelo_extra, accuracy_extra),
            'AdaBoost': (modelo_ADA, accuracy_ADA),
            'GradientBoosting':(modelo_GD, accuracy_GD),
            'XGB':(modelo_XB, accuracy_XB),
            'CatBoost':(modelo_CB,accuracy_CB),
            'LIGHT':(modelo_LIGHT, accuracy_LIGHT),
            'VotingHard':(modelo_voting_hard, accuracy_voting_hard),
            'VotingSoft':(modelo_voting_soft,accuracy_voting_soft),
            'StackingLineal':(modelo_stacking_lineal,accuracy_stacking_lineal),
            'StackingNoLineal':(modelo_stacking_nolineal,accuracy_stacking_nolineal),
            'Super_Aprendiz':(modelo_super_aprendiz, accuracy_super_aprendiz),
            'Super_Aprendiz_dos_Capas':(modelo_super_aprendiz_dos_capas,accuracy_super_aprendiz_dos_capas)
        }
        mejor_modelo_nombre = max(modelos, key=lambda x: modelos[x][1])
        mejor_modelo, mejor_precision = modelos[mejor_modelo_nombre]
        print("Mejor modelo:", mejor_modelo_nombre)
        print("Exactitud del modelo:", mejor_precision)
        
    except Exception as e:
        print("Error al cargar y entrenar el modelo:", e)
        

def entrenar_modelo_knn_con_transformacion(X_trn, Y_trn, X_tst, Y_tst):
    parameters = {
        'n_neighbors': [i for i in range(1, 18, 1)],
        'metric': ['euclidean', 'manhattan', 'minkowski'],
        'algorithm': ['auto', 'kd_tree','ball_tree','brute'],
        'weights': ['uniform']
    }
    modelo = KNeighborsClassifier()
    semilla = 5
    num_folds = 10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica = 'accuracy'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejores_hiperparametros_knn = grid_resultado.best_params_
    print("Resultados de GridSearchCV para el modelo")
    print("Mejor valor EXACTITUD usando k-fold:", grid_resultado.best_score_*100)
    print("Mejor valor PARAMETRO usando k-fold:", grid_resultado.best_params_)
    mejor_modelo = KNeighborsClassifier(**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predictions = mejor_modelo.predict(X_tst)
    accuracy = (predictions == Y_tst).mean() 
    return mejor_modelo, accuracy, mejores_hiperparametros_knn

def entrenar_modelo_svc_con_transformacion(X_trn, Y_trn, X_tst, Y_tst):
    parameters = { 'kernel':   ['rbf', 'poly', 'sigmoid','linear'], 
                'C': [i/10000 for i in range(8,12,1)],
                'max_iter':[i for i in range(1,3,1)],
                'gamma' : [i/100 for i in range(80,110,5)],
                'random_state':[i for i in range(1,5,1)],
                }
    modelo = SVC()
    semilla=5
    num_folds=10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica = 'accuracy'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejores_hiperparametros_svc=grid_resultado.best_params_
    print("Resultados de GridSearchCV para el modelo")
    print("Mejor valor EXACTITUD usando k-fold:", grid_resultado.best_score_*100)
    print("Mejor valor PARAMETRO usando k-fold:", grid_resultado.best_params_)
    mejor_modelo = SVC(**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predictions = mejor_modelo.predict(X_tst)
    accuracy = (predictions == Y_tst).mean() 
    return mejor_modelo, accuracy

    
def entrenar_modelo_tree_con_transformacion(X_trn, Y_trn, X_tst, Y_tst):
    parameters = {          
            'max_depth':[i for i in range(1,7,1)],
            'min_samples_split' :  [i for i in range(1,7,1)],  
            'min_samples_leaf' : [i for i in range(1,7,1)], 
            'max_features' : [i for i in range(1,7,1)], 
            'splitter': ["best", "random"],
            'random_state': [i for i in range(1,5,1)],
            }
    modelo = DecisionTreeClassifier()
    semilla=5
    num_folds=10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica = 'accuracy'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejores_hiperparametros_tree=grid_resultado.best_params_
    print("Resultados de GridSearchCV para el modelo")
    print("Mejor valor EXACTITUD usando k-fold:", grid_resultado.best_score_*100)
    print("Mejor valor PARAMETRO usando k-fold:", grid_resultado.best_params_)
    mejor_modelo = DecisionTreeClassifier(**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predictions = mejor_modelo.predict(X_tst)
    accuracy = (predictions == Y_tst).mean()  
    return mejor_modelo, accuracy,mejores_hiperparametros_tree

def entrenar_modelo_gaussian_con_transformacion(X_trn, Y_trn, X_tst, Y_tst):
    X_trn_transformado = X_trn
    parameters = {}
    modelo = GaussianNB()
    semilla=5
    num_folds=10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica = 'accuracy'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    print("Resultados de GridSearchCV para el modelo")
    print("Mejor valor EXACTITUD usando k-fold:", grid_resultado.best_score_*100)
    print("Mejor valor PARAMETRO usando k-fold:", grid_resultado.best_params_)
    mejor_modelo = GaussianNB(**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predictions = mejor_modelo.predict(X_tst)
    accuracy = (predictions == Y_tst).mean()  
    return mejor_modelo, accuracy

def entrenar_modelo_LDA_con_transformacion(X_trn, Y_trn, X_tst, Y_tst):
    parameters = { 'solver':  ['svd','lsqr','eigen'],
            'n_components':[1,2,3,4,5,6,7,8,9,10],
            'shrinkage': ['auto', 0.001, 0.01, 0.1, 0.5,1,10,100,1000],
            'tol':[i/1000 for i in range(1,100,1)]}
    modelo = LinearDiscriminantAnalysis()
    semilla=5
    num_folds=10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica = 'accuracy'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejores_hiperparametros_LDA=grid_resultado.best_params_
    print("Resultados de GridSearchCV para el modelo")
    print("Mejor valor EXACTITUD usando k-fold:", grid_resultado.best_score_*100)
    print("Mejor valor PARAMETRO usando k-fold:", grid_resultado.best_params_)
    mejor_modelo = LinearDiscriminantAnalysis(**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predictions = mejor_modelo.predict(X_tst)
    accuracy = (predictions == Y_tst).mean()  
    return mejor_modelo, accuracy

def entrenar_modelo_BG_con_transformacion(X_trn, Y_trn, X_tst, Y_tst,mejores_hiperparametros_tree):
    parameters = {'n_estimators': [i for i in range(750,760,5)],
            'max_samples' : [i/100.0 for i in range(70,90,5)],
            'max_features': [i/100.0 for i in range(75,85,5)],
            'bootstrap': [True], 
            'bootstrap_features': [True]}
    base_estimator= DecisionTreeClassifier(**mejores_hiperparametros_tree)
    semilla=5
    modelo = BaggingClassifier(estimator=base_estimator,n_estimators=750, random_state=semilla,
                            bootstrap= True, bootstrap_features = True, max_features = 0.7,
                            max_samples= 0.5)
    num_folds=10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica = 'accuracy'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejores_hiperparametros_BG=grid_resultado.best_params_
    print("Resultados de GridSearchCV para el modelo")
    print("Mejor valor EXACTITUD usando k-fold:", grid_resultado.best_score_*100)
    print("Mejor valor PARAMETRO usando k-fold:", grid_resultado.best_params_)
    mejor_modelo = BaggingClassifier(**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predictions = mejor_modelo.predict(X_tst)
    accuracy = (predictions == Y_tst).mean()  
    return mejor_modelo, accuracy, mejores_hiperparametros_BG

def entrenar_modelo_random_con_transformacion(X_trn, Y_trn, X_tst, Y_tst):
    parameters = { 
                'min_samples_split' : [1, 2 , 3,  4 , 6 , 8 , 10 , 15, 20 ],  
                'min_samples_leaf' : [ 1 , 3 , 5 , 7 , 9, 12, 15 ],
                'criterion':('gini','entropy','log_loss')
            }
    modelo = RandomForestClassifier()
    semilla=5
    num_folds=10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica = 'accuracy'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejores_hiperparametros_random=grid_resultado.best_params_
    print("Resultados de GridSearchCV para el modelo")
    print("Mejor valor EXACTITUD usando k-fold:", grid_resultado.best_score_*100)
    print("Mejor valor PARAMETRO usando k-fold:", grid_resultado.best_params_)
    mejor_modelo = RandomForestClassifier(**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predictions = mejor_modelo.predict(X_tst)
    accuracy = (predictions == Y_tst).mean()
    return mejor_modelo, accuracy,mejores_hiperparametros_random


def entrenar_modelo_extra_con_transformacion(X_trn, Y_trn, X_tst, Y_tst):
    parameters = {'min_samples_split' : [i for i in range(1,10,1)], 
                'min_samples_leaf' : [i for i in range(0,10,1)],
                'min_samples_split':[i for i in range(0,10,1)],
                'criterion':('gini','entropy','log_loss')}
    semilla=5            
    modelo = ExtraTreesClassifier(random_state=semilla, 
                                n_estimators=40,
                                bootstrap=True) 
    num_folds=10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica = 'accuracy'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejores_hiperparametros_extra=grid_resultado.best_params_
    print("Resultados de GridSearchCV para el modelo")
    print("Mejor valor EXACTITUD usando k-fold:", grid_resultado.best_score_*100)
    print("Mejor valor PARAMETRO usando k-fold:", grid_resultado.best_params_)
    mejor_modelo = ExtraTreesClassifier(**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predictions = mejor_modelo.predict(X_tst)
    accuracy = (predictions == Y_tst).mean() 
    return mejor_modelo, accuracy, mejores_hiperparametros_extra

def entrenar_modelo_ADA_con_transformacion(X_trn, Y_trn,X_tst, Y_tst):
    parameters = {'learning_rate' : [i/10000.0 for i in range(5,20,5)],
                'n_estimators':[i for i in range(1,50,1)]}
    semilla=5            
    modelo = AdaBoostClassifier(estimator = None,  algorithm = 'SAMME.R', 
                                random_state= None) 
    num_folds=10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica = 'accuracy'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejores_hiperparametros_ADA=grid_resultado.best_params_
    print("Resultados de GridSearchCV para el modelo")
    print("Mejor valor EXACTITUD usando k-fold:", grid_resultado.best_score_*100)
    print("Mejor valor PARAMETRO usando k-fold:", grid_resultado.best_params_)
    mejor_modelo = AdaBoostClassifier(**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predictions = mejor_modelo.predict(X_tst)
    accuracy = (predictions == Y_tst).mean() 
    return mejor_modelo, accuracy, mejores_hiperparametros_ADA

def entrenar_modelo_GD_con_transformacion(X_trn, Y_trn,X_tst, Y_tst):
    parameters = { 
                'learning_rate' : [0.01, 0.05, 0.1,0.15],
                'n_estimators': [i for i in range(100,1200,100)],
                'loss':('log_loss','exponential'),
                'criterion':['friedman_mse']     
            }
    semilla=5
    modelo = GradientBoostingClassifier(random_state=semilla,
                                    n_estimators= 100,learning_rate= 0.1,max_depth= 2,
                                    min_samples_split= 2, min_samples_leaf= 3,max_features= 2)
    semilla=5
    num_folds=10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica = 'accuracy'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejores_hiperparametros_GD=grid_resultado.best_params_
    print("Resultados de GridSearchCV para el modelo")
    print("Mejor valor EXACTITUD usando k-fold:", grid_resultado.best_score_*100)
    print("Mejor valor PARAMETRO usando k-fold:", grid_resultado.best_params_)
    mejor_modelo = GradientBoostingClassifier(**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predictions = mejor_modelo.predict(X_tst)
    accuracy = (predictions == Y_tst).mean() 
    return mejor_modelo, accuracy, mejores_hiperparametros_GD

def entrenar_modelo_XB_con_transformacion(X_trn, Y_trn,X_tst, Y_tst):
    parameters = {'reg_alpha': [0,0.1,0.2,0.3,0.4,0.5],
                'reg_lambda':  [i/1000.0 for i in range(100,150,5)],
                'n_estimators':  [i for i in range(1,10,2)],
                'colsample_bytree': [0.1,0.3, 0.5,0.6,0.7,0.8, 0.9, 1,1.1],
                'objective' : ('binary:logistic', 'Multi: softprob'),
                'loss': ['log_loss'],
                'max_features':('sqrt','log2')
                }
    semilla=5
    modelo = XGBClassifier(random_state=semilla,subsample =1,max_depth =2)
    semilla=5
    num_folds=10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica = 'accuracy'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejores_hiperparametros_XB=grid_resultado.best_params_
    print("Resultados de GridSearchCV para el modelo")
    print("Mejor valor EXACTITUD usando k-fold:", grid_resultado.best_score_*100)
    print("Mejor valor PARAMETRO usando k-fold:", grid_resultado.best_params_)
    mejor_modelo = XGBClassifier(**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predictions = mejor_modelo.predict(X_tst)
    accuracy = (predictions == Y_tst).mean() 
    return mejor_modelo, accuracy, mejores_hiperparametros_XB

def entrenar_modelo_CB_con_transformacion(X_trn, Y_trn,X_tst, Y_tst):
    parameters = {'border_count':[53],'l2_leaf_reg': [42],'learning_rate': [0.01],
                'depth': [4, 6, 8],'thread_count': [4, 8, 12]
                } 
    semilla=5
    modelo = CatBoostClassifier(random_state=semilla, verbose =0)
    semilla=5
    num_folds=10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica = 'accuracy'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejores_hiperparametros_CB=grid_resultado.best_params_
    print("Resultados de GridSearchCV para el modelo")
    print("Mejor valor EXACTITUD usando k-fold:", grid_resultado.best_score_*100)
    print("Mejor valor PARAMETRO usando k-fold:", grid_resultado.best_params_)
    mejor_modelo = CatBoostClassifier(**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predictions = mejor_modelo.predict(X_tst)
    accuracy = (predictions == Y_tst).mean() 
    return mejor_modelo, accuracy

def entrenar_modelo_LIGHT_con_transformacion(X_trn, Y_trn,X_tst, Y_tst):
    parameters = {
    'min_child_samples' : [i for i in range(200, 10000, 100)],'colsample_bytree': [0.6],
    'boosting_type': ['gbdt'],'objective': ['binary', 'multiclass'],'random_state': [42]}
    semilla=7
    modelo = LGBMClassifier(random_state=semilla,                           
                            num_leaves =  10,max_depth = 1, n_estimators = 100,    
                            learning_rate = 0.1 ,class_weight=  None, subsample = 1,
                            colsample_bytree= 1, reg_alpha=  0, reg_lambda = 0,
                            min_split_gain = 0, boosting_type = 'gbdt')
    semilla=5
    num_folds=10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica = 'accuracy'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejores_hiperparametros_LIGHT=grid_resultado.best_params_
    print("Resultados de GridSearchCV para el modelo")
    print("Mejor valor EXACTITUD usando k-fold:", grid_resultado.best_score_*100)
    print("Mejor valor PARAMETRO usando k-fold:", grid_resultado.best_params_)
    mejor_modelo = LGBMClassifier(**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predictions = mejor_modelo.predict(X_tst)
    accuracy = (predictions == Y_tst).mean() 
    return mejor_modelo, accuracy

def entrenar_modelo_voting_hard_con_transformacion(X_trn, Y_trn,X_tst, Y_tst,
                                                mejores_hiperparametros_GD,
                                                mejores_hiperparametros_tree,
                                                mejores_hiperparametros_ADA,
                                                mejores_hiperparametros_extra,
                                                mejores_hiperparametros_random,
                                                mejores_hiperparametros_BG,
                                                mejores_hiperparametros_XB):
    semilla= 5 
    kfold = StratifiedKFold(n_splits=10, random_state=semilla, shuffle=True)
    modelo1 = GradientBoostingClassifier(**mejores_hiperparametros_GD)
    base_estimator=DecisionTreeClassifier(**mejores_hiperparametros_tree)
    modelo2 = AdaBoostClassifier(**mejores_hiperparametros_ADA)
    modelo3 = ExtraTreesClassifier(**mejores_hiperparametros_extra)
    modelo4 = RandomForestClassifier (**mejores_hiperparametros_random)
    model = DecisionTreeClassifier(**mejores_hiperparametros_tree)
    modelo5 = BaggingClassifier(**mejores_hiperparametros_BG)
    modelo6 = DecisionTreeClassifier(**mejores_hiperparametros_tree)
    modelo7 = XGBClassifier(**mejores_hiperparametros_XB)
    metrica = 'accuracy'
    mejor_modelo = VotingClassifier(
    estimators=[('Gradient', modelo1), ('Adaboost', modelo2), 
                                    ('Extratrees', modelo3),('Random Forest',modelo4),
                                    ('Bagging',modelo5),('Decision tree',modelo6),
                                    ('XGB',modelo7)],voting='hard') 
    mejor_modelo.fit(X_trn, Y_trn)
    predictions = mejor_modelo.predict(X_tst)
    accuracy = (predictions == Y_tst).mean()
    return mejor_modelo, accuracy

def entrenar_modelo_voting_soft_con_transformacion(X_trn, Y_trn,X_tst, Y_tst,
                                                mejores_hiperparametros_GD,
                                                mejores_hiperparametros_tree,
                                                mejores_hiperparametros_ADA,
                                                mejores_hiperparametros_extra,
                                                mejores_hiperparametros_random,
                                                mejores_hiperparametros_BG):
    semilla= 5 
    kfold = StratifiedKFold(n_splits=10, random_state=semilla, shuffle=True)
    modelo1 = GradientBoostingClassifier(**mejores_hiperparametros_GD)
    base_estimator=DecisionTreeClassifier(**mejores_hiperparametros_tree)
    modelo2 = AdaBoostClassifier(**mejores_hiperparametros_ADA)
    modelo3 = ExtraTreesClassifier(**mejores_hiperparametros_extra)
    modelo4 = RandomForestClassifier (**mejores_hiperparametros_random)
    model = DecisionTreeClassifier(**mejores_hiperparametros_tree)
    modelo5 = BaggingClassifier(**mejores_hiperparametros_BG)
    modelo6 = DecisionTreeClassifier(**mejores_hiperparametros_tree)
    metrica = 'accuracy'
    mejor_modelo = VotingClassifier(
    estimators=[('Gradient', modelo1), ('Adaboost', modelo2), ('Extratrees', modelo3),
                                    ('Random Forest',modelo4),
                                    ('Bagging',modelo5),('Decision tree',modelo6)],
    voting='soft',weights=[0.9,0.7,0.9,0.9,0.9,0.9]) 
    mejor_modelo.fit(X_trn, Y_trn)
    predictions = mejor_modelo.predict(X_tst)
    accuracy = (predictions == Y_tst).mean()
    return mejor_modelo, accuracy

def entrenar_modelo_stacking_lineal_con_transformacion(X_trn, Y_trn,X_tst, Y_tst,
                                                mejores_hiperparametros_tree,
                                                mejores_hiperparametros_ADA,
                                                mejores_hiperparametros_extra,
                                                mejores_hiperparametros_random,
                                                mejores_hiperparametros_BG):
    semilla= 5
    kfold = StratifiedKFold(n_splits=10, random_state=semilla, shuffle=True)
    base_estimator=DecisionTreeClassifier(**mejores_hiperparametros_tree)
    modelo2 = AdaBoostClassifier(**mejores_hiperparametros_ADA)
    modelo3 = ExtraTreesClassifier(**mejores_hiperparametros_extra)
    modelo4 = RandomForestClassifier (**mejores_hiperparametros_random)
    model = DecisionTreeClassifier(**mejores_hiperparametros_tree)
    modelo5 = BaggingClassifier(**mejores_hiperparametros_BG)
    modelo6 = DecisionTreeClassifier(**mejores_hiperparametros_tree)
    estimador_final = LogisticRegression()
    metrica = 'accuracy'
    mejor_modelo = StackingClassifier(
    estimators=[ ('Adaboost', modelo2), ('Extratrees', modelo3),('Random Forest',modelo4),
                                    ('Bagging',modelo5),('Decision tree',modelo6)], 
                                    final_estimator=estimador_final) 
    mejor_modelo.fit(X_trn, Y_trn)
    predictions = mejor_modelo.predict(X_tst)
    accuracy = (predictions == Y_tst).mean() 
    return mejor_modelo, accuracy

def entrenar_modelo_stacking_nolineal_con_transformacion(X_trn, Y_trn,X_tst, Y_tst,
                                                mejores_hiperparametros_tree,
                                                mejores_hiperparametros_extra,
                                                mejores_hiperparametros_random,
                                                mejores_hiperparametros_BG):
    semilla= 7 
    kfold = StratifiedKFold(n_splits=10, random_state=semilla, shuffle=True)
    modelo1 = ExtraTreesClassifier(**mejores_hiperparametros_extra)
    modelo2 = RandomForestClassifier (**mejores_hiperparametros_random)
    model = DecisionTreeClassifier(**mejores_hiperparametros_tree)
    modelo3 = BaggingClassifier(**mejores_hiperparametros_BG)
    modelo4 = DecisionTreeClassifier(**mejores_hiperparametros_tree)
    estimador_final = ExtraTreesClassifier(**mejores_hiperparametros_extra)
    metrica = 'accuracy'
    mejor_modelo = StackingClassifier(
    estimators=[  ('Extratrees', modelo1),('Random Forest',modelo2),('Bagging',modelo3),
                                    ('Decision tree',modelo4)], 
                                    final_estimator=estimador_final) 
    mejor_modelo.fit(X_trn, Y_trn)
    predictions = mejor_modelo.predict(X_tst)
    accuracy = (predictions == Y_tst).mean() 
    return mejor_modelo, accuracy

def entrenar_modelo_super_aprendiz(X_trn, Y_trn,X_tst, Y_tst,
                            mejores_hiperparametros_tree,mejores_hiperparametros_extra,
                            mejores_hiperparametros_random):
    
    semilla = 5 
    kfold = StratifiedKFold(n_splits=10, random_state=semilla, shuffle=True)
    modelo1 = ExtraTreesClassifier(**mejores_hiperparametros_extra)
    modelo2 = RandomForestClassifier(**mejores_hiperparametros_random)
    model = DecisionTreeClassifier(**mejores_hiperparametros_tree)
    modelo4 = DecisionTreeClassifier(**mejores_hiperparametros_tree)
    estimadores = [('Extratrees', modelo1), ('Random Forest', modelo2),('DecisionTree',modelo4)]
    mejor_modelo = SuperLearner(folds=10, random_state=semilla, verbose=2)
    mejor_modelo.add(estimadores)
    estimador_final = ExtraTreesClassifier(n_estimators=100, max_features=None,
                                        bootstrap=False, max_depth=11, min_samples_split=4, 
                                        min_samples_leaf=1)
    mejor_modelo.add_meta(estimador_final)
    mejor_modelo.fit(X_trn, Y_trn)
    predictions = mejor_modelo.predict(X_tst)
    accuracy = (predictions == Y_tst).mean() 
    return mejor_modelo, accuracy

def entrenar_modelo_super_aprendiz_dos_capas(X_trn, Y_trn,X_tst, Y_tst, mejores_hiperparametros_tree,
                                            mejores_hiperparametros_extra,mejores_hiperparametros_random
                                            ):
    semilla = 5 
    kfold = StratifiedKFold(n_splits=10, random_state=semilla, shuffle=True)
    modelo1 = ExtraTreesClassifier(**mejores_hiperparametros_extra)
    modelo2 = RandomForestClassifier(**mejores_hiperparametros_random)
    model = DecisionTreeClassifier(**mejores_hiperparametros_tree)
    estimadores = [('Extratrees', modelo1), ('Random Forest', modelo2)]
    mejor_modelo = SuperLearner(folds=10, random_state=semilla, verbose=2)
    mejor_modelo.add(estimadores)
    mejor_modelo.add(estimadores)
    estimador_final = ExtraTreesClassifier(n_estimators=100, max_features=None,
                                        bootstrap=False, max_depth=11, min_samples_split=4, 
                                        min_samples_leaf=1)
    mejor_modelo.add_meta(estimador_final)
    mejor_modelo.fit(X_trn, Y_trn)
    predictions = mejor_modelo.predict(X_tst)
    accuracy = (predictions == Y_tst).mean() 
    return mejor_modelo, accuracy

@app.get("/")
def read_root():
    return {"message": "API para predecir calificación de estudiantes"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)

