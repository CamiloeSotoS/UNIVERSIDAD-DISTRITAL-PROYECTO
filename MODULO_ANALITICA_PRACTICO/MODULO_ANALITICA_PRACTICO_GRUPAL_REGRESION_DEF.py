from fastapi import FastAPI, Request
from typing import List
from pydantic import BaseModel
import pickle 

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
from sklearn.model_selection import StratifiedKFold

from sklearn.ensemble import BaggingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from lightgbm import LGBMRegressor
from sklearn.ensemble import VotingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import StackingRegressor
from mlens.ensemble import SuperLearner

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.metrics import mean_squared_log_error, median_absolute_error
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C, WhiteKernel

from sklearn.neighbors import KNeighborsRegressor
from fastapi import FastAPI, HTTPException
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import KFold, GridSearchCV


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
save_path = 'C:/Users/Intevo/Desktop/UNIVERSIDAD DISTRITAL PROYECTO FOLDER/UNIVERSIDAD-DISTRITAL-PROYECTO/MODULO_ANALITICA_PRACTICO/DATOS'  # Reemplazar con la ruta deseada

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
mejor_modelo = None

variables_por_carrera = { 
    'industrial': {
        '1': ['PG_ICFES', 'CON_MAT_ICFES', 'FISICA_ICFES','QUIMICA_ICFES','IDIOMA_ICFES','LOCALIDAD','PROMEDIO_UNO'],
        '2': ['LOCALIDAD_COLEGIO', 'PG_ICFES', 'CON_MAT_ICFES', 'FISICA_ICFES', 'BIOLOGIA_ICFES', 'IDIOMA_ICFES', 'LOCALIDAD', 'PROMEDIO_UNO', 'CAR_UNO', 'NCC_UNO', 'NAA_UNO', 'NOTA_DIFERENCIAL', 'NOTA_DIBUJO', 'NOTA_QUIMICA', 'NOTA_CFJC', 'NOTA_TEXTOS', 'NOTA_SEMINARIO', 'NOTA_EE_UNO','PROMEDIO_DOS'],
        '3': ['PROMEDIO_UNO', 'NAA_UNO', 'NOTA_DIFERENCIAL', 'NOTA_DIBUJO', 'NOTA_TEXTOS', 'NOTA_EE_UNO', 'PROMEDIO_DOS', 'NCC_DOS', 'NCA_DOS', 'NAA_DOS', 'NOTA_ALGEBRA', 'NOTA_INTEGRAL', 'NOTA_MATERIALES', 'NOTA_PBASICA', 'NOTA_EE_DOS', 'PROMEDIO_TRES'],
        '4': ['PROMEDIO_UNO', 'NOTA_EE_UNO', 'PROMEDIO_DOS', 'NOTA_ALGEBRA', 'NOTA_INTEGRAL', 'NOTA_MATERIALES', 'NOTA_EE_DOS', 'NAA_TRES', 'NOTA_MULTIVARIADO', 'NOTA_ESTADISTICA_UNO', 'NOTA_TERMODINAMICA', 'NOTA_TGS', 'NOTA_EE_TRES','PROMEDIO_CUATRO'],
        '5': ['PROMEDIO_UNO', 'PROMEDIO_DOS', 'NOTA_ALGEBRA', 'NOTA_INTEGRAL', 'NOTA_MATERIALES', 'NOTA_EE_DOS','PROMEDIO_TRES', 'NAA_TRES', 'NOTA_MULTIVARIADO', 'NOTA_TERMODINAMICA', 'NOTA_ECUACIONES', 'NOTA_ESTADISTICA_DOS', 'NOTA_FISICA_DOS', 'NOTA_MECANICA', 'NOTA_PROCESOSQ', 'PROMEDIO_CINCO'],
        '6': ['PROMEDIO_UNO', 'PROMEDIO_DOS', 'NOTA_MATERIALES', 'NOTA_EE_DOS', 'PROMEDIO_TRES', 'NOTA_MULTIVARIADO', 'NOTA_FISICA_DOS', 'NOTA_EE_CUATRO', 'PROMEDIO_CINCO', 'NOTA_PROCESOSM', 'NOTA_ADMINISTRACION', 'NOTA_LENGUA_UNO', 'NOTA_EI_UNO', 'NOTA_EI_DOS', 'PROMEDIO_SEIS'],
        '7': ['PROMEDIO_UNO', 'PROMEDIO_DOS', 'NOTA_EE_DOS', 'PROMEDIO_TRES', 'NOTA_MULTIVARIADO', 'NOTA_FISICA_DOS', 'PROMEDIO_CINCO', 'NOTA_PROCESOSM', 'NOTA_LENGUA_UNO', 'NOTA_EI_DOS', 'PROMEDIO_SEIS', 'NCA_SEIS', 'NOTA_PLINEAL', 'NOTA_DISENO', 'NOTA_EI_TRES','PROMEDIO_SIETE'],
        '8': ['PROMEDIO_DOS', 'NOTA_EE_CUATRO', 'PROMEDIO_CINCO', 'NOTA_LENGUA_UNO','PROMEDIO_SEIS', 'NOTA_IECONOMICA', 'PROMEDIO_SIETE', 'NAA_SIETE', 'NOTA_GRAFOS', 'NOTA_CALIDAD_UNO', 'NOTA_ERGONOMIA', 'NOTA_EI_CINCO', 'PROMEDIO_OCHO'],
        '9': ['PROMEDIO_DOS', 'NOTA_EE_CUATRO', 'PROMEDIO_CINCO', 'PROMEDIO_SEIS', 'NOTA_IECONOMICA', 'PROMEDIO_SIETE', 'NAA_SIETE', 'NOTA_GRAFOS', 'NOTA_CALIDAD_UNO', 'NOTA_ERGONOMIA', 'NOTA_EI_CINCO', 'PROMEDIO_OCHO', 'NCC_OCHO', 'NOTA_LOG_UNO', 'NOTA_GOPERACIONES','NOTA_CALIDAD_DOS', 'NOTA_LENGUA_DOS', 'NOTA_CONTEXTO', 'PROMEDIO_NUEVE'],
        '10': ['PROMEDIO_SEIS', 'PROMEDIO_SIETE', 'PROMEDIO_OCHO', 'NOTA_CALIDAD_DOS', 'PROMEDIO_NUEVE', 'NAA_NUEVE', 'NOTA_GRADO_UNO', 'NOTA_LOG_DOS', 'NOTA_FINANZAS', 'NOTA_HISTORIA', 'PROMEDIO_DIEZ']
    },
    'sistemas': {
        '1': ['CON_MAT_ICFES','IDIOMA_ICFES','LOCALIDAD_COLEGIO','BIOLOGIA_ICFES','QUIMICA_ICFES','PG_ICFES','LITERATURA_ICFES','PROMEDIO_UNO'],
        '2': ['PROMEDIO_UNO','NOTA_DIFERENCIAL','NOTA_CATEDRA_DEM','NOTA_PROG_BASICA','NAA_UNO','CAR_UNO','NOTA_TEXTOS','NOTA_LOGICA','NOTA_SEMINARIO','VECES_LOGICA','NAC_UNO','NCC_UNO','NCA_UNO','IDIOMA_ICFES','VECES_CATEDRA_DEM','NOTA_EE_UNO','PG_ICFES','NAP_UNO','VECES_DIFERENCIAL','CON_MAT_ICFES','NOTA_CATEDRA_CON','VECES_EE_UNO','PROMEDIO_DOS'],
        '3': ['PROMEDIO_UNO','PROMEDIO_DOS','NOTA_TGS','NOTA_PROG_AVANZADA','NOTA_FISICA_DOS','NOTA_MULTIVARIADO','NOTA_SEGUNDA_LENGUA_DOS','VECES_FISICA_DOS','NOTA_EE_DOS','VECES_PROG_AVANZADA','NAA_DOS','VECES_TGS','NCA_DOS','VECES_MULTIVARIADO','NOTA_ECUACIONES','NOTA_DIFERENCIAL','NAC_DOS','PROMEDIO_TRES'],
        '4': ['PROMEDIO_UNO','PROMEDIO_DOS','NOTA_METODOS_NUM','NOTA_A_SISTEMAS','NOTA_MOD_PROG_UNO','NOTA_MAT_DIS','NOTA_HOMBRE','NOTA_GT_DOS','VECES_A_SISTEMAS','VECES_HOMBRE','NCC_TRES','NAA_DOS','NAA_TRES','NOTA_FUND_BASES','NAC_TRES','PROMEDIO_CUATRO'],
        '5': ['PROMEDIO_UNO','PROMEDIO_DOS','PROMEDIO_TRES','NOTA_PROB','NOTA_CIENCIAS_COMP_UNO','NOTA_MOD_PROG_DOS','NOTA_ARQ_COMP','NOTA_INV_OP_UNO','NOTA_FISICA_TRES','VECES_INV_OP_UNO','VECES_PROB','NOTA_METODOS_NUM','NOTA_MOD_PROG_UNO','VECES_MOD_PROG_DOS','VECES_FISICA_TRES','PROMEDIO_CINCO'],
        '6': ['PROMEDIO_UNO','PROMEDIO_DOS','PROMEDIO_TRES','NOTA_HISTORIA_COL','NOTA_ESTADISTICA','NOTA_CIBERNETICA_UNO','NOTA_INV_OP_DOS','NOTA_REDES_COM_UNO','NOTA_GI_UNO','VECES_HISTORIA_COL','VECES_CIBERNETICA_UNO','NOTA_CIENCIAS_COMP_DOS','VECES_REDES_COM_UNO','VECES_GI_UNO','VECES_ESTADISTICA','NOTA_MOD_PROG_DOS','VECES_CIENCIAS_COMP_DOS','VECES_INV_OP_DOS','CAR_CINCO','NOTA_METODOS_NUM','VECES_FISICA_TRES','PROMEDIO_SEIS'],
        '7': ['PROMEDIO_UNO','PROMEDIO_DOS','PROMEDIO_TRES','PROMEDIO_CINCO','NOTA_F_ING_SOF','NOTA_GT_TRES','NOTA_ECONOMIA','NOTA_EI_DOS','NOTA_REDES_COM_DOS','VECES_ECONOMIA','NOTA_CIBERNETICA_UDOS','NOTA_INV_OP_TRES','NOTA_INV_OP_DOS','NOTA_HISTORIA_COL','VECES_F_ING_SOF','VECES_REDES_COM_DOS','NOTA_METODOS_NUM','VECES_EI_DOS','VECES_CIBERNETICA_DOS','NOTA_ESTADISTICA','NCP_SEIS','NOTA_MOD_PROG_DOS','NOTA_GI_DOS','PROMEDIO_SIETE'],
        '8': ['PROMEDIO_UNO','PROMEDIO_DOS','PROMEDIO_TRES','PROMEDIO_CINCO','PROMEDIO_SEIS','NOTA_DIS_ARQ_SOFT','NOTA_EI_OP_AI','NOTA_ING_ECONOMICA','NOTA_REDES_COM_TRES','NOTA_CIBERNETICA_TRES','VECES_EI_OP_AI','VECES_DIS_ARQ_SOFT','VECES_ING_ECONOMICA','VECES_EI_OP_BI','VECES_CIBERNETICA_TRES','NOTA_INV_OP_DOS','PROMEDIO_OCHO'],
        '9': ['PROMEDIO_TRES','PROMEDIO_CINCO','PROMEDIO_SEIS','PROMEDIO_SIETE','NOTA_EI_OP_AII','NOTA_GES_CAL_VAL_SOFT','NOTA_EI_OP_CI','NOTA_SIS_OP','VECES_EI_OP_AII','VECES_SIS_OP','NOTA_ING_ECONOMICA','VECES_EI_OP_CI','NAC_OCHO','VECES_GES_CAL_VAL_SOFT','PROMEDIO_NUEVE'],
        '10': ['PROMEDIO_TRES','PROMEDIO_CINCO','PROMEDIO_SEIS','PROMEDIO_SIETE','NOTA_FOGEP','NOTA_EI_OP_DI','NOTA_EI_OP_CII','NOTA_EI_OP_CI','NOTA_EI_OP_AIII','NOTA_ING_ECONOMICA','VECES_FOGEP','NOTA_GRADO_UNO','NOTA_GRADO_DOS','VECES_EI_OP_DI','NOTA_EI_OP_BIII','NCP_NUEVE','NOTA_GES_CAL_VAL_SOFT','PROMEDIO_DIEZ']
    },
    'catastral': {
        '1': ['CON_MAT_ICFES','IDIOMA_ICFES','BIOLOGIA_ICFES','GENERO','FILOSOFIA_ICFES','LOCALIDAD','LITERATURA_ICFES','QUIMICA_ICFES','PG_ICFES','PROMEDIO_UNO'],
        '2': ['PROMEDIO_UNO','NOTA_ALGEBRA','NOTA_DITO','NOTA_TEXTOS','NOTA_CD&C','NCA_UNO','NAA_UNO','BIOLOGIA_ICFES','NOTA_HIST','QUIMICA_ICFES','NOTA_SEM','FILOSOFIA_ICFES','IDIOMA_ICFES','LITERATURA_ICFES','NOTA_DIF','CON_MAT_ICFES','NAP_UNO','VECES_HIST','VECES_ALGEBRA','NCP_UNO','GENERO','PROMEDIO_DOS'],
        '3': ['PROMEDIO_UNO','PROMEDIO_DOS','EPA_DOS','NOTA_TOP','NOTA_PROGB','NOTA_FIS_UNO','NOTA_HIST','LITERATURA_ICFES','NOTA_INT','VECES_TOP','NCA_UNO','IDIOMA_ICFES','NAP_UNO','VECES_HIST','NOTA_EYB','NOTA_DIF','PROMEDIO_TRES'],
        '4': ['PROMEDIO_UNO','PROMEDIO_DOS','PROMEDIO_TRES','NOTA_DIF','NOTA_SUELOS','NOTA_POO','NOTA_FIS_DOS','NOTA_TOP','NOTA_EYB','IDIOMA_ICFES','NOTA_HIST','NOTA_ECUA','NOTA_PROGB','LITERATURA_ICFES','NCA_TRES','NOTA_FOTO','NOTA_CFJC','VECES_SUELOS','PROMEDIO_CUATRO'],
        '5': ['PROMEDIO_UNO','PROMEDIO_DOS','PROMEDIO_TRES','PROMEDIO_CUATRO','NOTA_GEOGEO','NOTA_TOP','NCA_CUATRO','NOTA_SUELOS','NOTA_POO','NOTA_PRII','NOTA_FOTO','EPA_CUATRO','LITERATURA_ICFES','NOTA_PROGB','NOTA_PROB','NOTA_ECUA','NOTA_CFJC','PROMEDIO_CINCO'],
        '6': ['PROMEDIO_UNO','PROMEDIO_DOS','PROMEDIO_TRES','PROMEDIO_CUATRO','PROMEDIO_CINCO','NOTA_SUELOS','NOTAS_SISC','NOTA_TOP','NOTA_GEOGEO','NOTA_POO','VECES_BD','NOTA_ME','NOTA_ECUA','CAR_CINCO','NOTA_PROGB','NOTA_FOTO','NOTA_CARTO','LITERATURA_ICFES','VECES_CARTO','NOTA_CFJC','PROMEDIO_SEIS'],
        '7': ['PROMEDIO_UNO','PROMEDIO_DOS','PROMEDIO_CUATRO','PROMEDIO_CINCO','PROMEDIO_SEIS','NOTA_GEO_FIS','NOTA_L_DOS','NOTA_ECUA','CAR_CINCO','NOTA_CARTO','NOTA_LEGIC','NOTA_GEOGEO','NOTA_POO','NOTA_CFJC','NOTA_INGECO','VECES_L_DOS','NOTA_SUELOS','NOTA_FOTO','PROMEDIO_SIETE'],
        '8': ['PROMEDIO_DOS','PROMEDIO_CINCO','PROMEDIO_SEIS','PROMEDIO_SIETE','NOTA_L_DOS','NOTA_ECONOMET','NOTA_AVAP','CAR_CINCO','NOTA_POO','NOTA_ECUA','NOTA_FOTO','NOTA_GEOGEO','NOTA_EI_UNO','PROMEDIO_OCHO'],
        '9': ['PROMEDIO_CINCO','PROMEDIO_SEIS','PROMEDIO_SIETE','PROMEDIO_OCHO','NOTA_FOTO','NOTA_POO','NOTA_L_DOS','NOTA_FOTOD','NOTA_AVAM','NOTA_AVAP','NOTA_EI_CUATRO','NOTA_L_TRES','NOTA_EI_UNO','NOTA_ECONOMET','NOTA_FGEP','NOTA_ECUA','NOTA_GEOGEO','PROMEDIO_NUEVE'],
        '10': ['PROMEDIO_CINCO','PROMEDIO_SEIS','PROMEDIO_SIETE','PROMEDIO_NUEVE','NOTA_TG_UNO','NOTA_L_DOS','NOTA_AVAP','NOTA_EI_CINCO','NOTA_ECONOMET','NOTA_AVAM','NOTA_FOTO','NOTA_FGEP','NOTA_EI_SEIS','NOTA_EE_DOS','NOTA_ECUA','PROMEDIO_DIEZ']
    },
    'electrica':{
        '1': ['IDIOMA_ICFES','PG_ICFES','FISICA_ICFES','ANO_INGRESO','APT_VERB_ICFES','QUIMICA_ICFES','FILOSOFIA_ICFES','GENERO','BIOLOGIA_ICFES','PROMEDIO_UNO'],
        '2': ['PROMEDIO_UNO','NOTA_POO','NOTA_INT','NOTA_FIS_DOS','NOTA_EYB','NOTA_DEM','NOTA_CIR_UNO','NOTA_HCI','VECES_INT','VECES_FIS_DOS','PG_ICFES','PROMEDIO_DOS'],
        '3': ['PROMEDIO_DOS','NOTA_ECUA','NOTA_TERMO','NOTA_CIR_DOS','NOTA_FIS_DOS','NOTA_EL_UNO','VECES_ECUA','NOTA_FIS_TRES','NOTA_MULTI','NCP_DOS','NCA_DOS','VECES_TERMO','PROMEDIO_TRES'],
        '4': ['PROMEDIO_DOS','NOTA_EL_DOS','NOTA_MPI','NOTA_ME','NOTA_PYE','NOTA_ELD','VECES_ME','VECES_EL_DOS','NOTA_GEE','NOTA_CIR_TRES','VECES_PYE','PROMEDIO_CUATRO'],
        '5': ['PROMEDIO_CUATRO','NOTA_ASD','NOTA_CEM','NOTA_IO_UNO','NOTA_INSE','NOTA_IYM','NOTA_EE_UNO','NOTA_GENH','VECES_CEM','NOTA_EL_DOS','VECES_IYM','VECES_INSE','PROMEDIO_CINCO'],
        '6': ['PROMEDIO_CUATRO','NOTA_INGECO','NOTA_DDP','NOTA_CTRL','NOTA_CONEM','NOTA_TDE','VECES_INGECO','VECES_IO_DOS','VECES_DDP','NAC_CINCO','NOTAS_RDC','PROMEDIO_SEIS'],
        '7': ['VECES_ECO','NOTA_L_UNO','NOTA_ASP','NOTA_ELECPOT','NOTA_ECO','NOTA_MAQEL','VECES_ASP','NAC_CINCO','NOTA_AUTO','PROMEDIO_SIETE'],
        '8': ['PROMEDIO_SIETE','NOTA_FGEP','NOTA_HIST','NOTA_CCON','NOTA_L_DOS','NOTA_AIELEC','NOTA_SUBEL','VECES_SUBEL','VECES_FGEP','VECES_L_DOS','VECES_HIST','NOTA_L_UNO','PROMEDIO_OCHO'],
        '9': ['PROMEDIO_SIETE','NOTA_L_TRES','NOTA_HSE','NOTA_ADMIN','NOTA_TGUNO','VECES_HSE','NOTA_EI_TRES','NOTA_EE_DOS','NOTA_PROTELEC','NCC_OCHO','VECES_L_TRES','VECES_PROTELEC','CAR_OCHO','VECES_ADMIN','PROMEDIO_NUEVE'],
        '10': ['PROMEDIO_NUEVE','NOTA_EI_CINCO','NOTA_TGDOS','NOTA_EI_SEIS','NOTA_EI_TRES','NOTA_EE_TRES','NOTA_EE_DOS','NCC_NUEVE','VECES_EI_CINCO','NOTA_HSE','PROMEDIO_DIEZ']
    },
    'electronica':{
        '1': ['CON_MAT_ICFES','QUIMICA_ICFES','PG_ICFES','FISICA_ICFES','IDIOMA_ICFES','BIOLOGIA_ICFES','GENERO','LOCALIDAD','LITERATURA_ICFES','PROMEDIO_UNO'],
        '2': ['PROMEDIO_UNO','NOTA_DIF','CON_MAT_ICFES','EPA_UNO','FISICA_ICFES','PG_ICFES','NOTA_PROGB','NOTA_FIS_UNO','BIOLOGIA_ICFES','IDIOMA_ICFES','LITERATURA_ICFES','NCP_UNO','NOTA_TEXTOS','NOTA_CFJC','NAP_UNO','PROMEDIO_DOS'],
        '3': ['PROMEDIO_UNO','PROMEDIO_DOS','PG_ICFES','BIOLOGIA_ICFES','NAA_DOS','FISICA_ICFES','NOTA_INT','VECES_INT','NCA_DOS','NOTA_FIS_DOS','CON_MAT_ICFES','CAR_DOS','PROMEDIO_TRES'],
        '4': ['PROMEDIO_UNO','PROMEDIO_DOS','PROMEDIO_TRES','NOTA_INT','NCA_DOS','NCA_TRES','NOTA_FIS_DOS','PG_ICFES','NOTA_FIS_TRES','NOTA_EL_UNO','VECES_FIS_TRES','NOTA_DEM','PROMEDIO_CUATRO'],
        '5': ['PROMEDIO_TRES','PROMEDIO_CUATRO','NOTA_FIS_DOS','NOTA_EL_DOS','NOTA_CAMPOS','NOTA_FCD','VECES_FCD','NOTA_PROGAPL','NOTA_VARCOM','NCA_TRES','NOTA_INT','NCP_CUATRO','PROMEDIO_CINCO'],
        '6': ['PROMEDIO_TRES','PROMEDIO_CINCO','NOTA_EE_DOS','NCC_CINCO','NOTA_ADMICRO','NOTA_FCD','NAP_CINCO','NOTA_VARCOM','NOTA_TFM','VECES_ADMICRO','NOTA_EL_DOS','NAC_CINCO','PROMEDIO_SEIS'],
        '7': ['PROMEDIO_TRES','PROMEDIO_CINCO','PROMEDIO_SEIS','NOTA_TFM','NOTA_VARCOM','NOTA_COMANA','NOTA_MOYGE','NOTA_CCON','VECES_ADMICRO','VECES_COMANA','VECES_DDM','NOTAS_SYS','PROMEDIO_SIETE'],
        '8': ['PROMEDIO_TRES','PROMEDIO_SEIS','PROMEDIO_SIETE','NOTA_SISDIN','NOTA_ELECPOT','NOTA_COMDIG','NOTA_FDS','NOTA_VARCOM','NOTA_COMANA','NOTA_TFM','NCC_SIETE','PROMEDIO_OCHO'],
        '9': ['PROMEDIO_SEIS','PROMEDIO_OCHO','NOTA_STG','NOTA_C_UNO','NOTA_FDS','NOTA_ELECPOT','NOTA_INSIND','NOTA_SISDIN','NAP_OCHO','NOTA_INGECO','NOTA_TFM','PROMEDIO_NUEVE'],
        '10': ['PROMEDIO_SEIS','PROMEDIO_NUEVE','NOTA_INSIND','NOTA_TV','NOTA_C_UNO','NOTA_EI_IA','NOTA_ELECPOT','VECES_EI_IIA','NOTA_EI_IIIA','VECES_TV','PROMEDIO_DIEZ']
    }
}

variables_por_carrera2 = { 
    'industrial': {
        '1': ['PG_ICFES', 'CON_MAT_ICFES', 'FISICA_ICFES','QUIMICA_ICFES','IDIOMA_ICFES','LOCALIDAD'],
        '2': ['LOCALIDAD_COLEGIO', 'PG_ICFES', 'CON_MAT_ICFES', 'FISICA_ICFES', 'BIOLOGIA_ICFES', 'IDIOMA_ICFES', 'LOCALIDAD', 'PROMEDIO_UNO', 'CAR_UNO', 'NCC_UNO', 'NAA_UNO', 'NOTA_DIFERENCIAL', 'NOTA_DIBUJO', 'NOTA_QUIMICA', 'NOTA_CFJC', 'NOTA_TEXTOS', 'NOTA_SEMINARIO', 'NOTA_EE_UNO'],
        '3': ['PROMEDIO_UNO', 'NAA_UNO', 'NOTA_DIFERENCIAL', 'NOTA_DIBUJO', 'NOTA_TEXTOS', 'NOTA_EE_UNO', 'PROMEDIO_DOS', 'NCC_DOS', 'NCA_DOS', 'NAA_DOS', 'NOTA_ALGEBRA', 'NOTA_INTEGRAL', 'NOTA_MATERIALES', 'NOTA_PBASICA', 'NOTA_EE_DOS'],
        '4': ['PROMEDIO_UNO', 'NOTA_EE_UNO', 'PROMEDIO_DOS', 'NOTA_ALGEBRA', 'NOTA_INTEGRAL', 'NOTA_MATERIALES', 'NOTA_EE_DOS', 'NAA_TRES', 'NOTA_MULTIVARIADO', 'NOTA_ESTADISTICA_UNO', 'NOTA_TERMODINAMICA', 'NOTA_TGS', 'NOTA_EE_TRES'],
        '5': ['PROMEDIO_UNO', 'PROMEDIO_DOS', 'NOTA_ALGEBRA', 'NOTA_INTEGRAL', 'NOTA_MATERIALES', 'NOTA_EE_DOS','PROMEDIO_TRES', 'NAA_TRES', 'NOTA_MULTIVARIADO', 'NOTA_TERMODINAMICA', 'NOTA_ECUACIONES', 'NOTA_ESTADISTICA_DOS', 'NOTA_FISICA_DOS', 'NOTA_MECANICA', 'NOTA_PROCESOSQ'],
        '6': ['PROMEDIO_UNO', 'PROMEDIO_DOS', 'NOTA_MATERIALES', 'NOTA_EE_DOS', 'PROMEDIO_TRES', 'NOTA_MULTIVARIADO', 'NOTA_FISICA_DOS', 'NOTA_EE_CUATRO', 'PROMEDIO_CINCO', 'NOTA_PROCESOSM', 'NOTA_ADMINISTRACION', 'NOTA_LENGUA_UNO', 'NOTA_EI_UNO', 'NOTA_EI_DOS'],
        '7': ['PROMEDIO_UNO', 'PROMEDIO_DOS', 'NOTA_EE_DOS', 'PROMEDIO_TRES', 'NOTA_MULTIVARIADO', 'NOTA_FISICA_DOS', 'PROMEDIO_CINCO', 'NOTA_PROCESOSM', 'NOTA_LENGUA_UNO', 'NOTA_EI_DOS', 'PROMEDIO_SEIS', 'NCA_SEIS', 'NOTA_PLINEAL', 'NOTA_DISENO', 'NOTA_EI_TRES'],
        '8': ['PROMEDIO_DOS', 'NOTA_EE_CUATRO', 'PROMEDIO_CINCO', 'NOTA_LENGUA_UNO','PROMEDIO_SEIS', 'NOTA_IECONOMICA', 'PROMEDIO_SIETE', 'NAA_SIETE', 'NOTA_GRAFOS', 'NOTA_CALIDAD_UNO', 'NOTA_ERGONOMIA', 'NOTA_EI_CINCO'],
        '9': ['PROMEDIO_DOS', 'NOTA_EE_CUATRO', 'PROMEDIO_CINCO', 'PROMEDIO_SEIS', 'NOTA_IECONOMICA', 'PROMEDIO_SIETE', 'NAA_SIETE', 'NOTA_GRAFOS', 'NOTA_CALIDAD_UNO', 'NOTA_ERGONOMIA', 'NOTA_EI_CINCO', 'PROMEDIO_OCHO', 'NCC_OCHO', 'NOTA_LOG_UNO', 'NOTA_GOPERACIONES','NOTA_CALIDAD_DOS', 'NOTA_LENGUA_DOS', 'NOTA_CONTEXTO'],
        '10': ['PROMEDIO_SEIS', 'PROMEDIO_SIETE', 'PROMEDIO_OCHO', 'NOTA_CALIDAD_DOS', 'PROMEDIO_NUEVE', 'NAA_NUEVE', 'NOTA_GRADO_UNO', 'NOTA_LOG_DOS', 'NOTA_FINANZAS', 'NOTA_HISTORIA']
    },
    'sistemas': {
        '1': ['CON_MAT_ICFES','IDIOMA_ICFES','LOCALIDAD_COLEGIO','BIOLOGIA_ICFES','QUIMICA_ICFES','PG_ICFES','LITERATURA_ICFES'],
        '2': ['PROMEDIO_UNO','NOTA_DIFERENCIAL','NOTA_CATEDRA_DEM','NOTA_PROG_BASICA','NAA_UNO','CAR_UNO','NOTA_TEXTOS','NOTA_LOGICA','NOTA_SEMINARIO','VECES_LOGICA','NAC_UNO','NCC_UNO','NCA_UNO','IDIOMA_ICFES','VECES_CATEDRA_DEM','NOTA_EE_UNO','PG_ICFES','NAP_UNO','VECES_DIFERENCIAL','CON_MAT_ICFES','NOTA_CATEDRA_CON','VECES_EE_UNO'],
        '3': ['PROMEDIO_UNO','PROMEDIO_DOS','NOTA_TGS','NOTA_PROG_AVANZADA','NOTA_FISICA_DOS','NOTA_MULTIVARIADO','NOTA_SEGUNDA_LENGUA_DOS','VECES_FISICA_DOS','NOTA_EE_DOS','VECES_PROG_AVANZADA','NAA_DOS','VECES_TGS','NCA_DOS','VECES_MULTIVARIADO','NOTA_ECUACIONES','NOTA_DIFERENCIAL','NAC_DOS'],
        '4': ['PROMEDIO_UNO','PROMEDIO_DOS','NOTA_METODOS_NUM','NOTA_A_SISTEMAS','NOTA_MOD_PROG_UNO','NOTA_MAT_DIS','NOTA_HOMBRE','NOTA_GT_DOS','VECES_A_SISTEMAS','VECES_HOMBRE','NCC_TRES','NAA_DOS','NAA_TRES','NOTA_FUND_BASES','NAC_TRES'],
        '5': ['PROMEDIO_UNO','PROMEDIO_DOS','PROMEDIO_TRES','NOTA_PROB','NOTA_CIENCIAS_COMP_UNO','NOTA_MOD_PROG_DOS','NOTA_ARQ_COMP','NOTA_INV_OP_UNO','NOTA_FISICA_TRES','VECES_INV_OP_UNO','VECES_PROB','NOTA_METODOS_NUM','NOTA_MOD_PROG_UNO','VECES_MOD_PROG_DOS','VECES_FISICA_TRES'],
        '6': ['PROMEDIO_UNO','PROMEDIO_DOS','PROMEDIO_TRES','NOTA_HISTORIA_COL','NOTA_ESTADISTICA','NOTA_CIBERNETICA_UNO','NOTA_INV_OP_DOS','NOTA_REDES_COM_UNO','NOTA_GI_UNO','VECES_HISTORIA_COL','VECES_CIBERNETICA_UNO','NOTA_CIENCIAS_COMP_DOS','VECES_REDES_COM_UNO','VECES_GI_UNO','VECES_ESTADISTICA','NOTA_MOD_PROG_DOS','VECES_CIENCIAS_COMP_DOS','VECES_INV_OP_DOS','CAR_CINCO','NOTA_METODOS_NUM','VECES_FISICA_TRES'],
        '7': ['PROMEDIO_UNO','PROMEDIO_DOS','PROMEDIO_TRES','PROMEDIO_CINCO','NOTA_F_ING_SOF','NOTA_GT_TRES','NOTA_ECONOMIA','NOTA_EI_DOS','NOTA_REDES_COM_DOS','VECES_ECONOMIA','NOTA_CIBERNETICA_UDOS','NOTA_INV_OP_TRES','NOTA_INV_OP_DOS','NOTA_HISTORIA_COL','VECES_F_ING_SOF','VECES_REDES_COM_DOS','NOTA_METODOS_NUM','VECES_EI_DOS','VECES_CIBERNETICA_DOS','NOTA_ESTADISTICA','NCP_SEIS','NOTA_MOD_PROG_DOS','NOTA_GI_DOS'],
        '8': ['PROMEDIO_UNO','PROMEDIO_DOS','PROMEDIO_TRES','PROMEDIO_CINCO','PROMEDIO_SEIS','NOTA_DIS_ARQ_SOFT','NOTA_EI_OP_AI','NOTA_ING_ECONOMICA','NOTA_REDES_COM_TRES','NOTA_CIBERNETICA_TRES','VECES_EI_OP_AI','VECES_DIS_ARQ_SOFT','VECES_ING_ECONOMICA','VECES_EI_OP_BI','VECES_CIBERNETICA_TRES','NOTA_INV_OP_DOS'],
        '9': ['PROMEDIO_TRES','PROMEDIO_CINCO','PROMEDIO_SEIS','PROMEDIO_SIETE','NOTA_EI_OP_AII','NOTA_GES_CAL_VAL_SOFT','NOTA_EI_OP_CI','NOTA_SIS_OP','VECES_EI_OP_AII','VECES_SIS_OP','NOTA_ING_ECONOMICA','VECES_EI_OP_CI','NAC_OCHO','VECES_GES_CAL_VAL_SOFT'],
        '10': ['PROMEDIO_TRES','PROMEDIO_CINCO','PROMEDIO_SEIS','PROMEDIO_SIETE','NOTA_FOGEP','NOTA_EI_OP_DI','NOTA_EI_OP_CII','NOTA_EI_OP_CI','NOTA_EI_OP_AIII','NOTA_ING_ECONOMICA','VECES_FOGEP','NOTA_GRADO_UNO','NOTA_GRADO_DOS','VECES_EI_OP_DI','NOTA_EI_OP_BIII','NCP_NUEVE','NOTA_GES_CAL_VAL_SOFT']
    },
    'catastral': {
        '1': ['CON_MAT_ICFES','IDIOMA_ICFES','BIOLOGIA_ICFES','GENERO','FILOSOFIA_ICFES','LOCALIDAD','LITERATURA_ICFES','QUIMICA_ICFES','PG_ICFES'],
        '2': ['PROMEDIO_UNO','NOTA_ALGEBRA','NOTA_DITO','NOTA_TEXTOS','NOTA_CD&C','NCA_UNO','NAA_UNO','BIOLOGIA_ICFES','NOTA_HIST','QUIMICA_ICFES','NOTA_SEM','FILOSOFIA_ICFES','IDIOMA_ICFES','LITERATURA_ICFES','NOTA_DIF','CON_MAT_ICFES','NAP_UNO','VECES_HIST','VECES_ALGEBRA','NCP_UNO','GENERO'],
        '3': ['PROMEDIO_UNO','PROMEDIO_DOS','EPA_DOS','NOTA_TOP','NOTA_PROGB','NOTA_FIS_UNO','NOTA_HIST','LITERATURA_ICFES','NOTA_INT','VECES_TOP','NCA_UNO','IDIOMA_ICFES','NAP_UNO','VECES_HIST','NOTA_EYB','NOTA_DIF'],
        '4': ['PROMEDIO_UNO','PROMEDIO_DOS','PROMEDIO_TRES','NOTA_DIF','NOTA_SUELOS','NOTA_POO','NOTA_FIS_DOS','NOTA_TOP','NOTA_EYB','IDIOMA_ICFES','NOTA_HIST','NOTA_ECUA','NOTA_PROGB','LITERATURA_ICFES','NCA_TRES','NOTA_FOTO','NOTA_CFJC','VECES_SUELOS'],
        '5': ['PROMEDIO_UNO','PROMEDIO_DOS','PROMEDIO_TRES','PROMEDIO_CUATRO','NOTA_GEOGEO','NOTA_TOP','NCA_CUATRO','NOTA_SUELOS','NOTA_POO','NOTA_PRII','NOTA_FOTO','EPA_CUATRO','LITERATURA_ICFES','NOTA_PROGB','NOTA_PROB','NOTA_ECUA','NOTA_CFJC'],
        '6': ['PROMEDIO_UNO','PROMEDIO_DOS','PROMEDIO_TRES','PROMEDIO_CUATRO','PROMEDIO_CINCO','NOTA_SUELOS','NOTAS_SISC','NOTA_TOP','NOTA_GEOGEO','NOTA_POO','VECES_BD','NOTA_ME','NOTA_ECUA','CAR_CINCO','NOTA_PROGB','NOTA_FOTO','NOTA_CARTO','LITERATURA_ICFES','VECES_CARTO','NOTA_CFJC'],
        '7': ['PROMEDIO_UNO','PROMEDIO_DOS','PROMEDIO_CUATRO','PROMEDIO_CINCO','PROMEDIO_SEIS','NOTA_GEO_FIS','NOTA_L_DOS','NOTA_ECUA','CAR_CINCO','NOTA_CARTO','NOTA_LEGIC','NOTA_GEOGEO','NOTA_POO','NOTA_CFJC','NOTA_INGECO','VECES_L_DOS','NOTA_SUELOS','NOTA_FOTO'],
        '8': ['PROMEDIO_DOS','PROMEDIO_CINCO','PROMEDIO_SEIS','PROMEDIO_SIETE','NOTA_L_DOS','NOTA_ECONOMET','NOTA_AVAP','CAR_CINCO','NOTA_POO','NOTA_ECUA','NOTA_FOTO','NOTA_GEOGEO','NOTA_EI_UNO'],
        '9': ['PROMEDIO_CINCO','PROMEDIO_SEIS','PROMEDIO_SIETE','PROMEDIO_OCHO','NOTA_FOTO','NOTA_POO','NOTA_L_DOS','NOTA_FOTOD','NOTA_AVAM','NOTA_AVAP','NOTA_EI_CUATRO','NOTA_L_TRES','NOTA_EI_UNO','NOTA_ECONOMET','NOTA_FGEP','NOTA_ECUA','NOTA_GEOGEO'],
        '10': ['PROMEDIO_CINCO','PROMEDIO_SEIS','PROMEDIO_SIETE','PROMEDIO_NUEVE','NOTA_TG_UNO','NOTA_L_DOS','NOTA_AVAP','NOTA_EI_CINCO','NOTA_ECONOMET','NOTA_AVAM','NOTA_FOTO','NOTA_FGEP','NOTA_EI_SEIS','NOTA_EE_DOS','NOTA_ECUA']
    },
    'electrica':{
        '1': ['IDIOMA_ICFES','PG_ICFES','FISICA_ICFES','ANO_INGRESO','APT_VERB_ICFES','QUIMICA_ICFES','FILOSOFIA_ICFES','GENERO','BIOLOGIA_ICFES'],
        '2': ['PROMEDIO_UNO','NOTA_POO','NOTA_INT','NOTA_FIS_DOS','NOTA_EYB','NOTA_DEM','NOTA_CIR_UNO','NOTA_HCI','VECES_INT','VECES_FIS_DOS','PG_ICFES'],
        '3': ['PROMEDIO_DOS','NOTA_ECUA','NOTA_TERMO','NOTA_CIR_DOS','NOTA_FIS_DOS','NOTA_EL_UNO','VECES_ECUA','NOTA_FIS_TRES','NOTA_MULTI','NCP_DOS','NCA_DOS','VECES_TERMO'],
        '4': ['PROMEDIO_DOS','NOTA_EL_DOS','NOTA_MPI','NOTA_ME','NOTA_PYE','NOTA_ELD','VECES_ME','VECES_EL_DOS','NOTA_GEE','NOTA_CIR_TRES','VECES_PYE'],
        '5': ['PROMEDIO_CUATRO','NOTA_ASD','NOTA_CEM','NOTA_IO_UNO','NOTA_INSE','NOTA_IYM','NOTA_EE_UNO','NOTA_GENH','VECES_CEM','NOTA_EL_DOS','VECES_IYM','VECES_INSE'],
        '6': ['PROMEDIO_CUATRO','NOTA_INGECO','NOTA_DDP','NOTA_CTRL','NOTA_CONEM','NOTA_TDE','VECES_INGECO','VECES_IO_DOS','VECES_DDP','NAC_CINCO','NOTAS_RDC'],
        '7': ['VECES_ECO','NOTA_L_UNO','NOTA_ASP','NOTA_ELECPOT','NOTA_ECO','NOTA_MAQEL','VECES_ASP','NAC_CINCO','NOTA_AUTO'],
        '8': ['PROMEDIO_SIETE','NOTA_FGEP','NOTA_HIST','NOTA_CCON','NOTA_L_DOS','NOTA_AIELEC','NOTA_SUBEL','VECES_SUBEL','VECES_FGEP','VECES_L_DOS','VECES_HIST','NOTA_L_UNO'],
        '9': ['PROMEDIO_SIETE','NOTA_L_TRES','NOTA_HSE','NOTA_ADMIN','NOTA_TGUNO','VECES_HSE','NOTA_EI_TRES','NOTA_EE_DOS','NOTA_PROTELEC','NCC_OCHO','VECES_L_TRES','VECES_PROTELEC','CAR_OCHO','VECES_ADMIN'],
        '10': ['PROMEDIO_NUEVE','NOTA_EI_CINCO','NOTA_TGDOS','NOTA_EI_SEIS','NOTA_EI_TRES','NOTA_EE_TRES','NOTA_EE_DOS','NCC_NUEVE','VECES_EI_CINCO','NOTA_HSE']
    },
    'electronica':{
        '1': ['CON_MAT_ICFES','QUIMICA_ICFES','PG_ICFES','FISICA_ICFES','IDIOMA_ICFES','BIOLOGIA_ICFES','GENERO','LOCALIDAD','LITERATURA_ICFES'],
        '2': ['PROMEDIO_UNO','NOTA_DIF','CON_MAT_ICFES','EPA_UNO','FISICA_ICFES','PG_ICFES','NOTA_PROGB','NOTA_FIS_UNO','BIOLOGIA_ICFES','IDIOMA_ICFES','LITERATURA_ICFES','NCP_UNO','NOTA_TEXTOS','NOTA_CFJC','NAP_UNO'],
        '3': ['PROMEDIO_UNO','PROMEDIO_DOS','PG_ICFES','BIOLOGIA_ICFES','NAA_DOS','FISICA_ICFES','NOTA_INT','VECES_INT','NCA_DOS','NOTA_FIS_DOS','CON_MAT_ICFES','CAR_DOS'],
        '4': ['PROMEDIO_UNO','PROMEDIO_DOS','PROMEDIO_TRES','NOTA_INT','NCA_DOS','NCA_TRES','NOTA_FIS_DOS','PG_ICFES','NOTA_FIS_TRES','NOTA_EL_UNO','VECES_FIS_TRES','NOTA_DEM'],
        '5': ['PROMEDIO_TRES','PROMEDIO_CUATRO','NOTA_FIS_DOS','NOTA_EL_DOS','NOTA_CAMPOS','NOTA_FCD','VECES_FCD','NOTA_PROGAPL','NOTA_VARCOM','NCA_TRES','NOTA_INT','NCP_CUATRO'],
        '6': ['PROMEDIO_TRES','PROMEDIO_CINCO','NOTA_EE_DOS','NCC_CINCO','NOTA_ADMICRO','NOTA_FCD','NAP_CINCO','NOTA_VARCOM','NOTA_TFM','VECES_ADMICRO','NOTA_EL_DOS','NAC_CINCO'],
        '7': ['PROMEDIO_TRES','PROMEDIO_CINCO','PROMEDIO_SEIS','NOTA_TFM','NOTA_VARCOM','NOTA_COMANA','NOTA_MOYGE','NOTA_CCON','VECES_ADMICRO','VECES_COMANA','VECES_DDM','NOTAS_SYS'],
        '8': ['PROMEDIO_TRES','PROMEDIO_SEIS','PROMEDIO_SIETE','NOTA_SISDIN','NOTA_ELECPOT','NOTA_COMDIG','NOTA_FDS','NOTA_VARCOM','NOTA_COMANA','NOTA_TFM','NCC_SIETE'],
        '9': ['PROMEDIO_SEIS','PROMEDIO_OCHO','NOTA_STG','NOTA_C_UNO','NOTA_FDS','NOTA_ELECPOT','NOTA_INSIND','NOTA_SISDIN','NAP_OCHO','NOTA_INGECO','NOTA_TFM'],
        '10': ['PROMEDIO_SEIS','PROMEDIO_NUEVE','NOTA_INSIND','NOTA_TV','NOTA_C_UNO','NOTA_EI_IA','NOTA_ELECPOT','VECES_EI_IIA','NOTA_EI_IIIA','VECES_TV']
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

def cargar_datos(carrera, semestre):
    ruta_archivo = f'C:/Users/Intevo/Desktop/UNIVERSIDAD DISTRITAL PROYECTO FOLDER/UNIVERSIDAD-DISTRITAL-PROYECTO/MODULO_ANALITICA_PRACTICO/DATOS/{carrera}{semestre}.csv'
    datos = pd.read_csv(ruta_archivo,sep=";")
    ruta_archivo_prediccion= f'C:/Users/Intevo/Desktop/UNIVERSIDAD DISTRITAL PROYECTO FOLDER/UNIVERSIDAD-DISTRITAL-PROYECTO/MODULO_ANALITICA_PRACTICO/DATOS/{carrera}{semestre}_prediccion_grupal.csv'
    datos_prediccion=pd.read_csv(ruta_archivo_prediccion,sep=';')
    return datos,datos_prediccion
carrera="industrial"
semestre="1"

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
        datos,datos_prediccion = cargar_datos(carrera, semestre)
        columnas_filtradas = variables_por_carrera[carrera][semestre]
        df = datos[columnas_filtradas]
        print("DataFrame con columnas filtradas:")
        df=df.astype(int)
        df
        datos,datos_prediccion = cargar_datos(carrera, semestre)
        columnas_filtradas = variables_por_carrera2[carrera][semestre]
        df_prediccion = datos_prediccion[columnas_filtradas]
        print("DataFrame con columnas filtradas:")
        df_prediccion=df_prediccion.astype(int)
        df_prediccion
        
        semestre_en_letras = numero_a_letras(semestre)
        X = df.loc[:, ~df.columns.str.contains(f'PROMEDIO_{semestre_en_letras.upper()}')]
        Y = df.loc[:, df.columns.str.contains(f'PROMEDIO_{semestre_en_letras.upper()}')]
        Y = LabelEncoder().fit_transform(Y.astype('str'))
        
        X_transformado = transformacion_johnson(X)
        X_trn, X_tst, Y_trn, Y_tst = train_test_split(X_transformado, Y, test_size=0.3, random_state=2)
        
        X_prediccion = df_prediccion.loc[:, ~df_prediccion.columns.str.contains(f'PROMEDIO_{semestre_en_letras.upper()}')]
        Y_prediccion = df_prediccion.loc[:, df_prediccion.columns.str.contains(f'PROMEDIO_{semestre_en_letras.upper()}')]                                                     
        print("Separación de datos usando Pandas") 
        print(X_prediccion.shape, Y_prediccion.shape)
        
        modelo_knn, r2_knn, mejores_hiperparametros_knn = entrenar_modelo_knn_con_transformacion(X_trn, Y_trn, X_tst, Y_tst)
        modelo_svc, r2_svc, mejores_hiperparametros_svc= entrenar_modelo_svc_con_transformacion(X_trn, Y_trn, X_tst, Y_tst)
        modelo_tree, r2_tree, mejores_hiperparametros_tree=entrenar_modelo_tree_con_transformacion(X_trn, Y_trn, X_tst, Y_tst)
        modelo_gaussian, r2_gaussian, mejores_hiperparametros_gaussian=entrenar_modelo_gaussian_con_transformacion(X_trn, Y_trn, X_tst, Y_tst)
        modelo_LDA, r2_LDA, mejores_hiperparametros_LDA=entrenar_modelo_LDA_con_transformacion(X_trn, Y_trn, X_tst, Y_tst)
        modelo_BG, r2_BG, mejores_hiperparametros_BG=entrenar_modelo_BG_con_transformacion(X_trn, Y_trn, X_tst, Y_tst, mejores_hiperparametros_tree)
        modelo_random, r2_random, mejores_hiperparametros_random=entrenar_modelo_random_con_transformacion(X_trn, Y_trn, X_tst, Y_tst)
        modelo_extra, r2_extra, mejores_hiperparametros_extra= entrenar_modelo_extra_con_transformacion(X_trn, Y_trn, X_tst, Y_tst)
        modelo_ADA, r2_ADA, mejores_hiperparametros_ADA= entrenar_modelo_ADA_con_transformacion(X_trn, Y_trn, X_tst, Y_tst)
        modelo_GD, r2_GD, mejores_hiperparametros_GD= entrenar_modelo_GD_con_transformacion(X_trn, Y_trn, X_tst, Y_tst)
        modelo_XB, r2_XB, mejores_hiperparametros_XB= entrenar_modelo_XB_con_transformacion(X_trn, Y_trn, X_tst, Y_tst)
        modelo_CB, r2_CB, mejores_hiperparametros_CB=entrenar_modelo_CB_con_transformacion(X_trn, Y_trn, X_tst, Y_tst)
        modelo_LIGHT, r2_LIGHT, mejores_hiperparametros_LIGHT= entrenar_modelo_LIGHT_con_transformacion(X_trn, Y_trn, X_tst, Y_tst)
        
        modelo_voting, r2_voting= entrenar_modelo_voting_con_transformacion(X_trn, Y_trn, X_tst, Y_tst,
                                                mejores_hiperparametros_GD,
                                                mejores_hiperparametros_tree,
                                                mejores_hiperparametros_ADA,
                                                mejores_hiperparametros_extra,
                                                mejores_hiperparametros_random,
                                                mejores_hiperparametros_BG,
                                                mejores_hiperparametros_XB)
        modelo_stacking_lineal, r2_stacking_lineal, mejores_hiperparametros_stacking_lineal=entrenar_modelo_stacking_lineal_con_transformacion(X_trn, Y_trn, X_tst, Y_tst,
                                                mejores_hiperparametros_tree,
                                                mejores_hiperparametros_ADA,
                                                mejores_hiperparametros_extra,
                                                mejores_hiperparametros_random)
        modelo_stacking_nolineal, r2_stacking_nolineal, mejores_hiperparametros_stacking_nolineal=entrenar_modelo_stacking_nolineal_con_transformacion(X_trn, Y_trn, X_tst, Y_tst,
                                                mejores_hiperparametros_tree,
                                                mejores_hiperparametros_ADA,
                                                mejores_hiperparametros_extra,
                                                mejores_hiperparametros_random)
        modelo_super_aprendiz, r2_super_aprendiz=entrenar_modelo_super_aprendiz_con_transformacion(X_trn, Y_trn, X_tst, Y_tst,
                                mejores_hiperparametros_GD,
                            mejores_hiperparametros_tree,mejores_hiperparametros_extra,
                            mejores_hiperparametros_random)
        modelo_super_aprendiz_dos_capas, r2_super_aprendiz_dos_capas=entrenar_modelo_super_aprendiz_dos_capas(X_trn, Y_trn, X_tst, Y_tst, mejores_hiperparametros_tree,
                                            mejores_hiperparametros_extra,mejores_hiperparametros_random)

        exactitudes = {
            'KNEIGHBORSCLASSIFIER': r2_knn,
            'SVC': r2_svc,
            'DECISION_TREE': r2_tree,
            'NAIVE_BAYES':r2_gaussian,
            'LDA':r2_LDA,
            'BAGGING':r2_BG,
            'RANDOM_FOREST':r2_random,
            'EXTRATREE':r2_extra,
            'ADA':r2_ADA,
            'GRADIENTBOOST': r2_GD,
            'XGBOOST':r2_XB,
            'CATBOOST':r2_CB,
            'LIGHT':r2_LIGHT,
            'VOTING':r2_voting,
            'STACKING_LINEAL':r2_stacking_lineal,
            'STACKING_NO_LINEAL':r2_stacking_nolineal,
            'SUPER_APRENDIZ':r2_super_aprendiz,
            'SUPER_APRENDIZ_DOS_CAPAS':r2_super_aprendiz_dos_capas
            }       
        modelos_entrenados = {
            'KNEIGHBORSCLASSIFIER': modelo_knn,
            'SVC': modelo_svc,
            'DECISION_TREE': modelo_tree,
            'NAIVE_BAYES': modelo_gaussian,
            'LDA': modelo_LDA,
            'BAGGING': modelo_BG,
            'RANDOM_FOREST':modelo_random,
            'EXTRATREE': modelo_extra,
            'ADA': modelo_ADA,
            'GRADIENTBOOST': modelo_GD,
            'XGBOOST':modelo_XB,
            'CATBOOST':modelo_CB,
            'LIGHT':modelo_LIGHT,
            'VOTING':modelo_voting,
            'STACKING_LINEAL':modelo_stacking_lineal,
            'STACKING_NO_LINEAL':modelo_stacking_nolineal,
            'SUPER_APRENDIZ':modelo_super_aprendiz,
            'SUPER_APRENDIZ_DOS_CAPAS':modelo_super_aprendiz_dos_capas
            }
        mejor_modelo = max(exactitudes, key=exactitudes.get)
        modelo_seleccionado = modelos_entrenados.get(mejor_modelo)
        print("Mejor modelo:", mejor_modelo)
        print(exactitudes)
        if modelo_seleccionado is not None:
            predicciones_nuevos_datos = modelo_seleccionado.predict(transformacion_johnson(X_prediccion))
            df_prediccion[f'PROMEDIO_{semestre_en_letras.upper()}']=predicciones_nuevos_datos
            df_prediccion
            df_prediccion.to_csv(f'Prediccion_Regresion_{carrera}_{semestre}.csv',sep=";",index=False)
            data_with_columns = df_prediccion.to_dict(orient='records')
            diccionario_dataframes = [
                    {
                        'dataTransformacion': data_with_columns,
                    }
                ]
            with open("Prediccion_Regresion.json", "w") as json_file:
                json.dump({"data": diccionario_dataframes}, json_file, indent=4)
                print("Los DataFrames han sido guardados en 'Prediccion_Regresion.json'.")
        else:
            print("El modelo seleccionado no está disponible.")
            
    except Exception as e:
        print("Error al cargar y entrenar el modelo:", e)
        
def entrenar_modelo_knn_con_transformacion(X_trn, Y_trn, X_tst, Y_tst):
    parameters = {
        'n_neighbors': [i for i in range(1, 18, 1)],
        'metric': ['euclidean', 'manhattan', 'minkowski'],
        'algorithm': ['auto'],
        'p': [i for i in range(1, 6)],
        'weights': ['uniform']
    }
    modelo = KNeighborsRegressor()
    semilla = 5
    num_folds = 10
    kfold =StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica = 'neg_mean_squared_error'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejores_hiperparametros_knn = grid_resultado.best_params_
    mejor_modelo = KNeighborsRegressor(**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predicciones = mejor_modelo.predict(X_tst)
    r2 = r2_score(Y_tst, predicciones)
    return mejor_modelo, r2, mejores_hiperparametros_knn

def entrenar_modelo_svc_con_transformacion(X_trn, Y_trn, X_tst, Y_tst):
    parameters = { 'kernel':  ['rbf', 'poly', 'sigmoid','linear'], 
            'C': [i/10000 for i in range(8,12,1)],
            'max_iter':[i for i in range(1,3,1)],
            'gamma' : [i/100 for i in range(90,110,5)]}
    modelo = SVR()
    semilla=5
    num_folds=10
    kfold =StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica = 'neg_mean_squared_error'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejores_hiperparametros_svc = grid_resultado.best_params_
    mejor_modelo = SVR(**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predicciones = mejor_modelo.predict(X_tst)
    r2 = r2_score(Y_tst, predicciones)
    return mejor_modelo, r2, mejores_hiperparametros_svc

def entrenar_modelo_tree_con_transformacion(X_trn, Y_trn, X_tst, Y_tst):
    parameters = {          
            'max_depth':[i for i in range(1,7,1)], 
            'min_samples_leaf' : [i for i in range(1,7,1)], 
            'max_features' : [i for i in range(1,7,1)], 
            'splitter': ["best", "random"],
            'random_state': [i for i in range(1,7,1)]}
    modelo = DecisionTreeRegressor()
    semilla=5
    num_folds=10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica = 'neg_mean_squared_error'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejores_hiperparametros_tree = grid_resultado.best_params_
    mejor_modelo = DecisionTreeRegressor(**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predicciones = mejor_modelo.predict(X_tst)
    r2 = r2_score(Y_tst, predicciones)
    return mejor_modelo, r2, mejores_hiperparametros_tree

def entrenar_modelo_gaussian_con_transformacion(X_trn, Y_trn, X_tst, Y_tst):
    parameters = {
        'alpha': [1e-10, 1e-5, 1e-2, 1e-1],
        'n_restarts_optimizer': [0, 1, 2, 3],
        'normalize_y': [True, False],
        'optimizer': ['fmin_l_bfgs_b']
    }
    modelo = GaussianProcessRegressor()
    semilla=5
    num_folds=10
    kfold =StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica = 'neg_mean_squared_error'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejor_modelo = GaussianProcessRegressor(**grid_resultado.best_params_)
    mejores_hiperparametros_gaussian=grid_resultado.best_params_
    mejor_modelo.fit(X_trn, Y_trn)
    predicciones = mejor_modelo.predict(X_tst)
    r2 = r2_score(Y_tst, predicciones)
    return mejor_modelo, r2, mejores_hiperparametros_gaussian

def entrenar_modelo_LDA_con_transformacion(X_trn, Y_trn, X_tst, Y_tst):
    parameters = { 'solver':  ['svd','lsqr','eigen'],
            'n_components':[1,2,3,4,5,6,7,8,9,10],
            'shrinkage': ['auto', 0.001, 0.01, 0.1, 0.5,1,10,100,1000]
            }
    modelo = LinearDiscriminantAnalysis()
    semilla=5
    num_folds=10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica= 'neg_mean_squared_error'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejor_modelo = LinearDiscriminantAnalysis(**grid_resultado.best_params_)
    mejores_hiperparametros_LDA=grid_resultado.best_params_
    mejor_modelo.fit(X_trn, Y_trn)
    predicciones = mejor_modelo.predict(X_tst)
    r2 = r2_score(Y_tst, predicciones)
    return mejor_modelo, r2, mejores_hiperparametros_LDA

def entrenar_modelo_BG_con_transformacion(X_trn, Y_trn, X_tst, Y_tst,mejores_hiperparametros_tree):
    parameters = {'n_estimators': [i for i in range(750,760,5)],
            'max_samples' : [i/100.0 for i in range(70,90,5)],
            'max_features': [i/100.0 for i in range(75,85,5)],
            'bootstrap': [True], 
            'bootstrap_features': [True]}
    base_estimator= DecisionTreeRegressor(**mejores_hiperparametros_tree)
    semilla=5
    modelo = BaggingRegressor(estimator=base_estimator,n_estimators=750, random_state=semilla,
                            bootstrap= True, bootstrap_features = True, max_features = 0.7,
                            max_samples= 0.5)
    num_folds=10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica =  'neg_mean_squared_error'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejores_hiperparametros_BG=grid_resultado.best_params_
    mejor_modelo = BaggingRegressor(**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predicciones = mejor_modelo.predict(X_tst)
    r2 = r2_score(Y_tst, predicciones)
    return mejor_modelo, r2, mejores_hiperparametros_BG
    
def entrenar_modelo_random_con_transformacion(X_trn, Y_trn, X_tst, Y_tst):
    parameters = { 
                'min_samples_split' : [1, 2 , 3,  4 , 6 , 8 , 10 , 15, 20 ],  
                'min_samples_leaf' : [ 1 , 3 , 5 , 7 , 9, 12, 15 ],
            }
    modelo = RandomForestRegressor()
    semilla=5
    num_folds=10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica =  'neg_mean_squared_error'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejores_hiperparametros_random=grid_resultado.best_params_
    mejor_modelo = RandomForestRegressor(**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predicciones = mejor_modelo.predict(X_tst)
    r2 = r2_score(Y_tst, predicciones)
    return mejor_modelo, r2, mejores_hiperparametros_random

def entrenar_modelo_extra_con_transformacion(X_trn, Y_trn, X_tst, Y_tst):
    parameters = {'min_samples_split' : [i for i in range(1,10,1)], 
                'criterion':('absolute_error', 'squared_error', 'friedman_mse', 'poisson')}
    semilla=5            
    modelo = ExtraTreesRegressor(random_state=semilla, 
                                n_estimators=40,
                                bootstrap=True) 
    num_folds=10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica ='neg_mean_squared_error'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejores_hiperparametros_extra=grid_resultado.best_params_
    mejor_modelo = ExtraTreesRegressor(**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predicciones = mejor_modelo.predict(X_tst)
    r2 = r2_score(Y_tst, predicciones)
    return mejor_modelo, r2, mejores_hiperparametros_extra

def entrenar_modelo_ADA_con_transformacion(X_trn, Y_trn, X_tst, Y_tst):
    parameters = {'learning_rate' : [i/10000.0 for i in range(5,20,5)],
                'n_estimators':[i for i in range(1,50,1)]}
    semilla=5            
    modelo = AdaBoostRegressor(estimator = None,random_state= None) 
    num_folds=10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica ='neg_mean_squared_error'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejores_hiperparametros_ADA=grid_resultado.best_params_
    mejor_modelo = AdaBoostRegressor(**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predicciones = mejor_modelo.predict(X_tst)
    r2 = r2_score(Y_tst, predicciones)
    return mejor_modelo, r2, mejores_hiperparametros_ADA

def entrenar_modelo_GD_con_transformacion(X_trn, Y_trn, X_tst, Y_tst):
    parameters = { 
                'learning_rate' : [0.01, 0.05, 0.1,0.15],
                'loss':('absolute_error', 'squared_error', 'quantile', 'huber'),
                'criterion':['friedman_mse']}
    semilla=5
    modelo = GradientBoostingRegressor(random_state=semilla,
                                    n_estimators= 100,learning_rate= 0.1,max_depth= 2,
                                    min_samples_split= 2, min_samples_leaf= 3,max_features= 2)
    semilla=5
    num_folds=10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica ='neg_mean_squared_error'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejores_hiperparametros_GD=grid_resultado.best_params_
    mejor_modelo = GradientBoostingRegressor(**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predicciones = mejor_modelo.predict(X_tst)
    r2 = r2_score(Y_tst, predicciones)
    return mejor_modelo, r2, mejores_hiperparametros_GD

def entrenar_modelo_XB_con_transformacion(X_trn, Y_trn, X_tst, Y_tst):
    parameters = {'reg_alpha': [0,0.1,0.2,0.3,0.4,0.5],
                'reg_lambda':  [i/1000.0 for i in range(100,150,5)],
                'colsample_bytree': [0.1,0.3, 0.5,0.6,0.7,0.8, 0.9, 1,1.1],
                'max_features':('sqrt','log2')
                }
    semilla=5
    modelo = XGBRegressor(random_state=semilla,subsample =1,max_depth =2)
    num_folds=10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica ='neg_mean_squared_error'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejor_modelo= XGBRegressor(**grid_resultado.best_params_)
    mejores_hiperparametros_XB=grid_resultado.best_params_
    mejor_modelo.fit(X_trn, Y_trn)
    predicciones = mejor_modelo.predict(X_tst)
    r2 = r2_score(Y_tst, predicciones)
    return mejor_modelo, r2, mejores_hiperparametros_XB

def entrenar_modelo_CB_con_transformacion(X_trn, Y_trn, X_tst, Y_tst):
    parameters = {} 
    semilla=5
    modelo = CatBoostRegressor(random_state=semilla, verbose =0)
    semilla=5
    num_folds=10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica ='neg_mean_squared_error'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejores_hiperparametros_CB=grid_resultado.best_params_
    mejor_modelo = CatBoostRegressor(verbose=0,**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predicciones = mejor_modelo.predict(X_tst)
    r2 = r2_score(Y_tst, predicciones)
    return mejor_modelo, r2, mejores_hiperparametros_CB

def entrenar_modelo_LIGHT_con_transformacion(X_trn, Y_trn, X_tst, Y_tst):
    parameters = {
    'min_child_samples' : [i for i in range(1, 100, 50)],'colsample_bytree': [0.6, 0.8],
    'boosting_type': ['gbdt'],'objective': ['binary', 'multiclass'],'random_state': [42]}
    semilla=5
    modelo = LGBMRegressor(random_state=semilla,                           
                            num_leaves =  10,max_depth = 1, n_estimators = 100,    
                            learning_rate = 0.1 ,class_weight=  None, subsample = 1,
                            colsample_bytree= 1, reg_alpha=  0, reg_lambda = 0,
                            min_split_gain = 0, boosting_type = 'gbdt')
    semilla=5
    num_folds=10
    kfold = StratifiedKFold(n_splits=num_folds, random_state=semilla, shuffle=True)
    metrica ='neg_mean_squared_error'
    grid = GridSearchCV(estimator=modelo, param_grid=parameters, scoring=metrica, cv=kfold, n_jobs=-1)
    grid_resultado = grid.fit(X_trn, Y_trn)
    mejores_hiperparametros_LIGHT=grid_resultado.best_params_
    mejor_modelo = LGBMRegressor(verbose=-1,**grid_resultado.best_params_)
    mejor_modelo.fit(X_trn, Y_trn)
    predicciones = mejor_modelo.predict(X_tst)
    r2 = r2_score(Y_tst, predicciones)
    return mejor_modelo, r2, mejores_hiperparametros_LIGHT

def entrenar_modelo_voting_con_transformacion(X_trn, Y_trn, X_tst, Y_tst,
                                                mejores_hiperparametros_GD,
                                                mejores_hiperparametros_tree,
                                                mejores_hiperparametros_ADA,
                                                mejores_hiperparametros_extra,
                                                mejores_hiperparametros_random,
                                                mejores_hiperparametros_BG,
                                                mejores_hiperparametros_XB):
    semilla= 5 
    kfold = StratifiedKFold(n_splits=10, random_state=semilla, shuffle=True)
    modelo1 = GradientBoostingRegressor(**mejores_hiperparametros_GD)
    base_estimator=DecisionTreeRegressor(**mejores_hiperparametros_tree)
    modelo2 = AdaBoostRegressor(**mejores_hiperparametros_ADA)
    modelo3 = ExtraTreesRegressor(**mejores_hiperparametros_extra)
    modelo4 = RandomForestRegressor(**mejores_hiperparametros_random)
    model = DecisionTreeRegressor(**mejores_hiperparametros_tree)
    modelo5 = BaggingRegressor(**mejores_hiperparametros_BG)
    modelo6 = DecisionTreeRegressor(**mejores_hiperparametros_tree)
    modelo7 = XGBRegressor(**mejores_hiperparametros_XB)
    metrica ='neg_mean_squared_error'
    mejor_modelo = VotingRegressor(
    estimators=[('Gradient', modelo1), ('Adaboost', modelo2), 
                                    ('Extratrees', modelo3),('Random Forest',modelo4),
                                    ('Bagging',modelo5),('Decision tree',modelo6),
                                    ('XGB',modelo7)]) 
    mejor_modelo.fit(X_trn, Y_trn)
    predicciones = mejor_modelo.predict(X_tst)
    r2 = r2_score(Y_tst, predicciones)
    return mejor_modelo, r2

def entrenar_modelo_stacking_lineal_con_transformacion(X_trn, Y_trn, X_tst, Y_tst,
                                                mejores_hiperparametros_tree,
                                                mejores_hiperparametros_ADA,
                                                mejores_hiperparametros_extra,
                                                mejores_hiperparametros_random):
    semilla= 5 
    kfold = StratifiedKFold(n_splits=10, random_state=semilla, shuffle=True)
    base_estimator=DecisionTreeRegressor(**mejores_hiperparametros_tree)
    modelo2 = AdaBoostRegressor(**mejores_hiperparametros_ADA)
    modelo3 = ExtraTreesRegressor(**mejores_hiperparametros_extra)
    modelo4 = RandomForestRegressor (**mejores_hiperparametros_random)
    model = DecisionTreeRegressor(**mejores_hiperparametros_tree)
    modelo5 = DecisionTreeRegressor(**mejores_hiperparametros_tree)
    estimador_final = LinearRegression()
    metrica ='neg_mean_squared_error'
    mejor_modelo = StackingRegressor(
    estimators=[ ('Adaboost', modelo2), ('Extratrees', modelo3),
                ('Random Forest',modelo4),
                ('Decision tree',modelo5)
                ], final_estimator=estimador_final) 
    mejor_modelo.fit(X_trn, Y_trn)
    mejores_hiperparametros_stacking_lineal=mejor_modelo.get_params
    predicciones = mejor_modelo.predict(X_tst)
    r2 = r2_score(Y_tst, predicciones)
    return mejor_modelo, r2, mejores_hiperparametros_stacking_lineal

def entrenar_modelo_stacking_nolineal_con_transformacion(X_trn, Y_trn, X_tst, Y_tst,
                                                mejores_hiperparametros_tree,
                                                mejores_hiperparametros_ADA,
                                                mejores_hiperparametros_extra,
                                                mejores_hiperparametros_random):
    semilla= 5 
    kfold = StratifiedKFold(n_splits=10, random_state=semilla, shuffle=True)
    base_estimator=DecisionTreeRegressor(**mejores_hiperparametros_tree)
    modelo2 = AdaBoostRegressor(**mejores_hiperparametros_ADA)
    modelo3 = ExtraTreesRegressor(**mejores_hiperparametros_extra)
    modelo4 = RandomForestRegressor (**mejores_hiperparametros_random)
    model = DecisionTreeRegressor(**mejores_hiperparametros_tree)
    modelo5 = DecisionTreeRegressor(**mejores_hiperparametros_tree)
    estimador_final = ExtraTreesRegressor()
    metrica ='neg_mean_squared_error'
    mejor_modelo = StackingRegressor(
    estimators=[ ('Adaboost', modelo2), ('Extratrees', modelo3),
                ('Random Forest',modelo4),
                ('Decision tree',modelo5)
                ], final_estimator=estimador_final) 
    mejor_modelo.fit(X_trn, Y_trn)
    mejores_hiperparametros_stacking_nolineal=mejor_modelo.get_params
    predicciones = mejor_modelo.predict(X_tst)
    r2 = r2_score(Y_tst, predicciones)
    return mejor_modelo, r2, mejores_hiperparametros_stacking_nolineal

def entrenar_modelo_super_aprendiz_con_transformacion(X_trn, Y_trn, X_tst, Y_tst,
                            mejores_hiperparametros_GD,
                            mejores_hiperparametros_tree,mejores_hiperparametros_extra,
                            mejores_hiperparametros_random):
    semilla = 5 
    kfold = StratifiedKFold(n_splits=10, random_state=semilla, shuffle=True)
    modelo1 = ExtraTreesRegressor(**mejores_hiperparametros_extra)
    modelo2 = RandomForestRegressor(**mejores_hiperparametros_random)
    model = DecisionTreeRegressor(**mejores_hiperparametros_tree)
    modelo4 = DecisionTreeRegressor(**mejores_hiperparametros_tree)
    modelo5 = GradientBoostingRegressor(**mejores_hiperparametros_GD) 
    estimadores = [('Extratrees', modelo1), 
                ('Random Forest', modelo2), 
                ('Decision tree', modelo4),
                ('Gradient',modelo5)]
    mejor_modelo = SuperLearner(folds=10, random_state=semilla, verbose=2)
    mejor_modelo.add(estimadores)
    estimador_final = ExtraTreesRegressor(n_estimators=100, max_features=None,
                                        bootstrap=False, max_depth=11, min_samples_split=4, 
                                        min_samples_leaf=1)
    mejor_modelo.add_meta(estimador_final)
    mejor_modelo.fit(X_trn, Y_trn)
    mejores_hiperparametros_super_learner=mejor_modelo.get_params
    predicciones = mejor_modelo.predict(X_tst)
    r2 = r2_score(Y_tst, predicciones)
    return mejor_modelo, r2

def entrenar_modelo_super_aprendiz_dos_capas(X_trn, Y_trn, X_tst, Y_tst, 
                                            mejores_hiperparametros_tree,mejores_hiperparametros_extra,
                                            mejores_hiperparametros_random):
    semilla = 5 
    kfold = StratifiedKFold(n_splits=10, random_state=semilla, shuffle=True)
    modelo1 = ExtraTreesRegressor(**mejores_hiperparametros_extra)
    modelo2 = RandomForestRegressor(**mejores_hiperparametros_random)
    model = DecisionTreeRegressor(**mejores_hiperparametros_tree)
    modelo3 = DecisionTreeRegressor(**mejores_hiperparametros_tree)
    estimadores = [('Extratrees', modelo1), 
                ('Random Forest', modelo2), 
                ('Decision tree', modelo3)]
    mejor_modelo = SuperLearner(folds=10, random_state=semilla, verbose=2)
    mejor_modelo.add(estimadores)
    mejor_modelo.add(estimadores)
    estimador_final = ExtraTreesRegressor(n_estimators=100, max_features=None,
                                        bootstrap=False, max_depth=11, min_samples_split=4, 
                                        min_samples_leaf=1)
    mejor_modelo.add_meta(estimador_final)
    mejor_modelo.fit(X_trn, Y_trn)
    mejores_hiperparametros_superaprendiz_dos_capas=mejor_modelo.get_params
    predicciones = mejor_modelo.predict(X_tst)
    r2 = r2_score(Y_tst, predicciones)
    return mejor_modelo, r2

@app.get("/")
def read_root():
    return {"message": "API para predecir calificación de estudiantes"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)