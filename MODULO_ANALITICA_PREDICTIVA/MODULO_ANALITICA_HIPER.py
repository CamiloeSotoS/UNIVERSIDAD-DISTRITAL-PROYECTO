#---------------------------------------------------------------
#---------------------------------------------------------------
# LIBRERIAS
#---------------------------------------------------------------
import warnings
warnings.filterwarnings('ignore')
import pandas as pd 
pd.options.display.max_columns=None
import json
import os

from fastapi import APIRouter
from pydantic import BaseModel

# System route
cwd = os.getcwd()

# Router FastApi
router = APIRouter(prefix='/predictiva/hiperparametros')

# Model input data
class InputDataHiperParametros(BaseModel):
    tipoModelo: str
    # modelos: List[str]
    modelo: str
    carrera: str
    semestre: int|str

# Resquest post
@router.post("/getDataHiperparametros/")
async def getDataHiperparametros(data: InputDataHiperParametros):

    jsonAbierto = None
    jsonExport = []
    
    path = os.path.join(cwd, f'HiperparametrosPredictiva/{data.tipoModelo}_{data.carrera}_{data.semestre}.json')
    
    with open(path) as json_file:
        jsonAbierto = json.load(json_file)
        json_file.close()
    
    for item in jsonAbierto["dataTransformacion"]:
        if item["MODELO"] == data.modelo:
            jsonExport.append(item)
    
    # Y luego devolver una respuesta
    return {"data": jsonExport}










