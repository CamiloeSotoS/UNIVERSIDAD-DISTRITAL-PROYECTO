from fastapi import FastAPI, File, UploadFile, File
from fastapi.responses import FileResponse
import pandas as pd
import numpy as np
import glob
import csv
import os

app = FastAPI()

def procesar_archivos(archivo_base_path):
    # Tu lógica de procesamiento aquí
    # Aquí he dejado parte de tu código de procesamiento, pero deberías adaptarlo según tus necesidades
    
    industrial = pd.read_csv(archivo_base_path, sep=',')
    #municipios = pd.read_csv(archivo_municipios_path, sep=',')
    
    #merged_df = pd.merge(industrial, municipios, on='MUNICIPIO')
    #merged_df = merged_df.drop(columns=['MUNICIPIO'])
    #merged_df = merged_df.rename(columns={'NUM_MUNI': 'MUNICIPIO'})
    #industrial = merged_df

#ruta_archivo = 'C:/Users/User/Desktop/udistrital/Base-ingeniería-industrial-original.csv'
#industrial = pd.read_csv(ruta_archivo, sep=',')

#ruta_archivo_2 = 'C:/Users/User/Desktop/udistrital/municipios_ud.csv'
#municipios = pd.read_csv(ruta_archivo_2, sep=',')


    industrial['DISTANCIA'] = np.where(((industrial['LOCALIDAD'] == 'TEUSAQUILLO') | (industrial['LOCALIDAD'] == 'CHAPINERO') | (industrial['LOCALIDAD'] == 'SANTA FE')) , '1' , np.nan)
    industrial['DISTANCIA'] = np.where(((industrial['LOCALIDAD'] == 'LOS MARTIRES')|(industrial['LOCALIDAD'] == 'LA CANDELARIA')|(industrial['LOCALIDAD'] == 'PUENTE ARANDA')), '2' , industrial['DISTANCIA'])
    industrial['DISTANCIA'] = np.where(((industrial['LOCALIDAD'] == 'BARRIOS UNIDOS')|(industrial['LOCALIDAD'] == 'RAFAEL URIBE URIBE')|(industrial['LOCALIDAD'] == 'ANTONIO NARINO')|(industrial['LOCALIDAD'] == 'ENGATIVA')|(industrial['LOCALIDAD'] == 'KENNEDY')), '3' , industrial['DISTANCIA'])
    industrial['DISTANCIA'] = np.where(((industrial['LOCALIDAD'] == 'FONTIBON')|(industrial['LOCALIDAD'] == 'SAN CRISTOBAL')), '4' , industrial['DISTANCIA'])
    industrial['DISTANCIA'] = np.where(((industrial['LOCALIDAD'] == 'USAQUEN')|(industrial['LOCALIDAD'] == 'BOSA')|(industrial['LOCALIDAD'] == 'SUBA')|(industrial['LOCALIDAD'] == 'TUNJUELITO')|(industrial['LOCALIDAD'] == 'CIUDAD BOLIVAR')), '5' , industrial['DISTANCIA'])
    industrial['DISTANCIA'] = np.where(((industrial['LOCALIDAD'] == 'USME')|(industrial['LOCALIDAD'] == 'FUERA DE BOGOTA')|(industrial['LOCALIDAD'] == 'SOACHA')|(industrial['LOCALIDAD'] == 'SUMAPAZ')), '6' , industrial['DISTANCIA'])
    industrial['DISTANCIA'] = np.where(((industrial['LOCALIDAD'] == 'NO REGISTRA')|(industrial['LOCALIDAD'] == 'SIN LOCALIDAD')), '7' , industrial['DISTANCIA'])

    industrial['GENERO'] = industrial['GENERO'].replace({'MASCULINO': 0, 'FEMENINO': 1})
    industrial['TIPO_COLEGIO'] = industrial['TIPO_COLEGIO'].replace({'NO REGISTRA': 0, 'OFICIAL': 1, 'NO OFICIAL':2})
    industrial['LOCALIDAD_COLEGIO'] = industrial['LOCALIDAD_COLEGIO'].replace({'NO REGISTRA': 0, 'USAQUEN': 1, 'CHAPINERO': 2, 'SANTAFE': 3, 'SANTA FE': 3, 'SAN CRISTOBAL': 4, 'USME': 5, 'TUNJUELITO': 6, 'BOSA': 7, 'KENNEDY': 8, 'FONTIBON': 9, 'ENGATIVA': 10, 'SUBA': 11, 'BARRIOS UNIDOS': 12, 'TEUSAQUILLO': 13, 'LOS MARTIRES': 14, 'ANTONIO NARINO': 15, 'PUENTE ARANDA': 16, 'LA CANDELARIA': 17, 'RAFAEL URIBE URIBE': 18, 'RAFAEL URIBE': 18, 'CIUDAD BOLIVAR': 19, 'FUERA DE BOGOTA': 20, 'SIN LOCALIDAD': 21, 'SOACHA':20})
    industrial['CALENDARIO'] = industrial['CALENDARIO'].replace({'NO REGISTRA': 0,'O': 0, 'A': 1, 'B': 2, 'F': 3})
    industrial['DEPARTAMENTO'] = industrial['DEPARTAMENTO'].replace({'NO REGISTRA': 0, 'AMAZONAS': 1, 'ANTIOQUIA': 2,'ARAUCA': 3, 'ATLANTICO': 4, 'BOGOTA': 5, 'BOLIVAR': 6, 'BOYACA': 7, 'CALDAS': 8, 'CAQUETA': 9, 'CASANARE': 10, 'CAUCA': 11, 'CESAR': 12, 'CHOCO': 13, 'CORDOBA': 14, 'CUNDINAMARCA': 15, 'GUAINIA': 16, 'GUAVIARE': 17, 'HUILA': 18, 'LA GUAJIRA': 19, 'MAGDALENA':20, 'META': 21, 'NARINO': 22, 'NORTE SANTANDER': 23, 'PUTUMAYO': 24, 'QUINDIO': 25, 'RISARALDA': 26, 'SAN ANDRES Y PROVIDENCIA': 27, 'SANTANDER': 28, 'SUCRE': 29, 'TOLIMA': 30, 'VALLE': 31, 'VAUPES': 32, 'VICHADA': 33})
    industrial['LOCALIDAD'] = industrial['LOCALIDAD'].replace({'NO REGISTRA': 0, 'USAQUEN': 1, 'CHAPINERO': 2, 'SANTA FE': 3, 'SAN CRISTOBAL': 4, 'USME': 5, 'TUNJUELITO': 6, 'BOSA': 7, 'KENNEDY': 8, 'FONTIBON': 9, 'ENGATIVA': 10, 'SUBA': 11, 'BARRIOS UNIDOS': 12, 'TEUSAQUILLO': 13, 'LOS MARTIRES': 14, 'ANTONIO NARINO': 15, 'PUENTE ARANDA': 16, 'LA CANDELARIA': 17, 'RAFAEL URIBE URIBE': 18, 'CIUDAD BOLIVAR': 19, 'FUERA DE BOGOTA': 20, 'SIN LOCALIDAD': 20, 'SOACHA': 20, 'SUMAPAZ': 20})
    industrial['INSCRIPCION'] = industrial['INSCRIPCION'].replace({'NO REGISTRA': 0, 'BENEFICIARIOS LEY 1081 DE 2006': 1, 'BENEFICIARIOS LEY 1084 DE 2006': 2, 'CONVENIO ANDRES BELLO': 3, 'DESPLAZADOS': 4, 'INDIGENAS': 5, 'MEJORES BACHILLERES COL. DISTRITAL OFICIAL': 6, 'MINORIAS ETNICAS Y CULTURALES': 7, 'MOVILIDAD ACADEMICA INTERNACIONAL': 8, 'NORMAL': 9, 'TRANSFERENCIA EXTERNA': 10, 'TRANSFERENCIA INTERNA': 11,})
    industrial['ESTADO_FINAL'] = industrial['ESTADO_FINAL'].replace({'ABANDONO': 1, 'ACTIVO': 2, 'APLAZO': 3, 'CANCELADO': 4, 'EGRESADO': 5, 'INACTIVO': 6, 'MOVILIDAD': 7, 'N.A.': 8, 'NO ESTUDIANTE AC004': 9, 'NO SUP. PRUEBA ACAD.': 10, 'PRUEBA AC Y ACTIVO': 11, 'PRUEBA ACAD': 12, 'RETIRADO': 13, 'TERMINO MATERIAS': 14, 'TERMINO Y MATRICULO': 15, 'VACACIONES': 16})
    industrial['MUNICIPIO'] = industrial['MUNICIPIO'].replace({"NO REGISTRA": 0, "ACACIAS": 1, "AGUACHICA": 2, "AGUAZUL": 3, "ALBAN": 4, "ALBAN (SAN JOSE)": 5, "ALVARADO": 6, "ANAPOIMA": 7, "ANOLAIMA": 8, "APARTADO": 9, "ARAUCA": 10, "ARBELAEZ": 11, "ARMENIA": 12, "ATACO": 13, "BARRANCABERMEJA": 14, "BARRANQUILLA": 15, "BELEN DE LOS ANDAQUIES": 16, "BOAVITA": 17, "BOGOTA": 18, "BOJACA": 19, "BOLIVAR": 20, "BUCARAMANGA": 21, "BUENAVENTURA": 22, "CABUYARO": 23, "CACHIPAY": 24, "CAICEDONIA": 25, "CAJAMARCA": 26, "CAJICA": 27, "CALAMAR": 28, "CALARCA": 29, "CALI": 30, "CAMPOALEGRE": 31, "CAPARRAPI": 32, "CAQUEZA": 33, "CARTAGENA": 34, "CASTILLA LA NUEVA": 35, "CERETE": 36, "CHAPARRAL": 37, "CHARALA": 38, "CHIA": 39, "CHIPAQUE": 40, "CHIQUINQUIRA": 41, "CHOACHI": 42, "CHOCONTA": 43, "CIENAGA": 44, "CIRCASIA": 45, "COGUA": 46, "CONTRATACION": 47, "COTA": 48, "CUCUTA": 49, "CUMARAL": 50, "CUMBAL": 51, "CURITI": 52, "CURUMANI": 53, "DUITAMA": 54, "EL BANCO": 55, "EL CARMEN DE BOLIVAR": 56, "EL COLEGIO": 57, "EL CHARCO": 58, "EL DORADO": 59, "EL PASO": 60, "EL ROSAL": 61, "ESPINAL": 62, "FACATATIVA": 63, "FLORENCIA": 64, "FLORIDABLANCA": 65, "FOMEQUE": 66, "FONSECA": 67, "FORTUL": 68, "FOSCA": 69, "FUNZA": 70, "FUSAGASUGA": 71, "GACHETA": 72, "GALERAS (NUEVA GRANADA)": 73, "GAMA": 74, "GARAGOA": 75, "GARZON": 76, "GIGANTE": 77, "GIRARDOT": 78, "GRANADA": 79, "GUACHUCAL": 80, "GUADUAS": 81, "GUAITARILLA": 82, "GUAMO": 83, "GUASCA": 84, "GUATEQUE": 85, "GUAYATA": 86, "GUTIERREZ": 87, "IBAGUE": 88, "INIRIDA": 89, "INZA": 90, "IPIALES": 91, "ITSMINA": 92, "JENESANO": 93, "LA CALERA": 94, "LA DORADA": 95, "LA MESA": 96, "LA PLATA": 97, "LA UVITA": 98, "LA VEGA": 99, "LIBANO": 100, "LOS PATIOS": 101, "MACANAL": 102, "MACHETA": 103, "MADRID": 104, "MAICAO": 105, "MALAGA": 106, "MANAURE BALCON DEL 12": 107, "MANIZALES": 108, "MARIQUITA": 109, "MEDELLIN": 110, "MEDINA": 111, "MELGAR": 112, "MITU": 113, "MOCOA": 114, "MONTERIA": 115, "MONTERREY": 116, "MOSQUERA": 117, "NATAGAIMA": 118, "NEIVA": 119, "NEMOCON": 120, "OCANA": 121, "ORITO": 122, "ORTEGA": 123, "PACHO": 124, "PAEZ (BELALCAZAR)": 125, "PAICOL": 126, "PAILITAS": 127, "PAIPA": 128, "PALERMO": 129, "PALMIRA": 130, "PAMPLONA": 131, "PANDI": 132, "PASCA": 133, "PASTO": 134, "PAZ DE ARIPORO": 135, "PAZ DE RIO": 136, "PITALITO": 137, "POPAYAN": 138, "PUENTE NACIONAL": 139, "PUERTO ASIS": 140, "PUERTO BOYACA": 141, "PUERTO LOPEZ": 142, "PUERTO SALGAR": 143, "PURIFICACION": 144, "QUETAME": 145, "QUIBDO": 146, "RAMIRIQUI": 147, "RICAURTE": 148, "RIOHACHA": 149, "RIVERA": 150, "SABOYA": 151, "SAHAGUN": 152, "SALDAÑA": 153, "SAMACA": 154, "SAMANA": 155, "SAN AGUSTIN": 156, "SAN ANDRES": 157, "SAN BERNARDO": 158, "SAN EDUARDO": 159, "SAN FRANCISCO": 160, "SAN GIL": 161, "SAN JOSE DEL FRAGUA": 162, "SAN JOSE DEL GUAVIARE": 163, "SAN LUIS DE PALENQUE": 164, "SAN MARCOS": 165, "SAN MARTIN": 166, "SANDONA": 167, "SAN VICENTE DEL CAGUAN": 168, "SANTA MARTA": 169, "SANTA SOFIA": 170, "SESQUILE": 171, "SIBATE": 172, "SIBUNDOY": 173, "SILVANIA": 174, "SIMIJACA": 175, "SINCE": 176, "SINCELEJO": 177, "SOACHA": 178, "SOATA": 179, "SOCORRO": 180, "SOGAMOSO": 181, "SOLEDAD": 182, "SOPO": 183, "SORACA": 184, "SOTAQUIRA": 185, "SUAITA": 186, "SUBACHOQUE": 187, "SUESCA": 188, "SUPATA": 189, "SUTAMARCHAN": 190, "SUTATAUSA": 191, "TABIO": 192, "TAMESIS": 193, "TARQUI": 194, "TAUSA": 195, "TENA": 196, "TENJO": 197, "TESALIA": 198, "TIBANA": 199, "TIMANA": 200, "TOCANCIPA": 201, "TUBARA": 202, "TULUA": 203, "TUMACO": 204, "TUNJA": 205, "TURBACO": 206, "TURMEQUE": 207, "UBATE": 208, "UMBITA": 209, "UNE": 210, "VALLEDUPAR": 211, "VELEZ": 212, "VENADILLO": 213, "VENECIA (OSPINA PEREZ)": 214, "VILLA DE LEYVA": 215, "VILLAHERMOSA": 216, "VILLANUEVA": 217, "VILLAPINZON": 218, "VILLAVICENCIO": 219, "VILLETA": 220, "YACOPI": 221, "YOPAL": 222, "ZIPACON": 223, "ZIPAQUIRA": 224})
    
    industrial = industrial.apply(pd.to_numeric)

    # Recorrer todas las columnas que comienzan con "CREDITOS_"
    for columna in industrial.columns:
        if columna.startswith('CREDITOS_'):
            # Obtener el valor distinto de cero en la columna
            otro_valor = industrial.loc[industrial[columna] != 0, columna].iloc[0]
            # Reemplazar ceros por el otro valor
            industrial[columna] = industrial[columna].replace(0, otro_valor)

    # Imprimir el DataFrame modificado
    print("\nDataFrame modificado:")

    """#PRIMER SEMESTRE INDUSTRIAL"""

    #Lista industrial primer semestre
    NOTAS_INDUSTRIAL_UNO= ['NOTA_DIFERENCIAL','NOTA_DIBUJO','NOTA_QUIMICA','NOTA_CFJC','NOTA_TEXTOS','NOTA_SEMINARIO','NOTA_EE_UNO']
    VECES_INDUSTRIAL_UNO= ['VECES_DIFERENCIAL','VECES_DIBUJO','VECES_QUIMICA','VECES_CFJC','VECES_TEXTOS','VECES_SEMINARIO','VECES_EE_UNO']
    CREDITOS_INDUSTRIAL_UNO= ['CREDITOS_DIFERENCIAL','CREDITOS_DIBUJO','CREDITOS_QUIMICA','CREDITOS_CFJC','CREDITOS_TEXTOS','CREDITOS_SEMINARIO','CREDITOS_EE_UNO']

    promedios_semestre = []

    # Iterar sobre cada estudiante
    for index, row in industrial.iterrows():
        notas_estudiante = []
        creditos_estudiante = []
        # Iterar sobre las materias del semestre
        for nota_col, veces_col, creditos_col in zip(NOTAS_INDUSTRIAL_UNO, VECES_INDUSTRIAL_UNO, CREDITOS_INDUSTRIAL_UNO):
            # Verificar si el estudiante cursó la materia al menos una vez y si tiene un promedio registrado
            if row[veces_col] > 0 and not pd.isnull(row[nota_col]):
                # Agregar la nota y los créditos a las listas correspondientes
                notas_estudiante.append(row[nota_col])
                creditos_estudiante.append(row[creditos_col])
        # Calcular el promedio ponderado para el semestre actual
        if len(notas_estudiante) > 0:
            promedio_semestre = np.average(notas_estudiante, weights=creditos_estudiante)
        else:
            # Si el estudiante no cursó ninguna materia, asignar promedio cero
            promedio_semestre = 0
        # Agregar el promedio del semestre a la lista de promedios
        promedios_semestre.append(promedio_semestre)

    # Agregar la lista de promedios por semestre al DataFrame
    industrial['PROMEDIO_UNO'] = promedios_semestre

    # Calcular métricas por semestre
    industrial['CAR_UNO'] = industrial[VECES_INDUSTRIAL_UNO].apply(lambda x: (x > 1).sum(), axis=1)
    industrial['NAC_UNO'] = industrial[VECES_INDUSTRIAL_UNO].apply(lambda x: (x > 0).sum(), axis=1)
    industrial['NAA_UNO'] = industrial[NOTAS_INDUSTRIAL_UNO].apply(lambda x: (x >= 30).sum(), axis=1)
    industrial['NAP_UNO'] = industrial['NAC_UNO'] - industrial['NAA_UNO']
    industrial['EPA_UNO'] = industrial.apply(lambda row: 1 if row['PROMEDIO_UNO'] < 30 or row['NAP_UNO'] >= 3 else 2, axis=1)

    # Construir NCC
    def calcular_creditos_cursados(row):
        creditos_cursados = 0
        for veces_col, creditos_col in zip(VECES_INDUSTRIAL_UNO, CREDITOS_INDUSTRIAL_UNO):
            if row[veces_col] > 0:
                creditos_cursados += row[creditos_col]
        return creditos_cursados
    industrial['NCC_UNO'] = industrial.apply(calcular_creditos_cursados, axis=1)

    # Construir NCA
    def calcular_creditos_aprobados(row):
        creditos_aprobados = 0
        for nota_col, creditos_col in zip(NOTAS_INDUSTRIAL_UNO, CREDITOS_INDUSTRIAL_UNO):
            if row[nota_col] >= 30:
                creditos_aprobados += row[creditos_col]
        return creditos_aprobados
    industrial['NCA_UNO'] = industrial.apply(calcular_creditos_aprobados, axis=1)

    # Construir NCP

    industrial['NCP_UNO'] = industrial['NCC_UNO'] - industrial['NCA_UNO']

    # Rendimiento UNO
    conditions = [(industrial['PROMEDIO_UNO'] >= 0) & (industrial['PROMEDIO_UNO'] < 30),
                (industrial['PROMEDIO_UNO'] >= 30) & (industrial['PROMEDIO_UNO'] < 40),
                (industrial['PROMEDIO_UNO'] >= 40) & (industrial['PROMEDIO_UNO'] < 45),
                (industrial['PROMEDIO_UNO'] >= 45) & (industrial['PROMEDIO_UNO'] < 50)]
    values = [1, 2, 3, 4]
    industrial['RENDIMIENTO_UNO'] = pd.Series(pd.cut(industrial['PROMEDIO_UNO'], bins=[0, 30, 40, 45, 50], labels=values))

    """# SEGUNDO SEMRESTRE INDUSTRIAL"""

    # Lista industrial segundo semestre
    NOTAS_INDUSTRIAL_DOS = ['NOTA_ALGEBRA', 'NOTA_INTEGRAL', 'NOTA_FISICA_UNO', 'NOTA_MATERIALES', 'NOTA_DEMOCRACIA', 'NOTA_PBASICA', 'NOTA_EE_DOS']
    VECES_INDUSTRIAL_DOS = ['VECES_ALGEBRA', 'VECES_INTEGRAL', 'VECES_FISICA_UNO', 'VECES_MATERIALES', 'VECES_DEMOCRACIA', 'VECES_PBASICA', 'VECES_EE_DOS']
    CREDITOS_INDUSTRIAL_DOS = ['CREDITOS_ALGEBRA', 'CREDITOS_INTEGRAL', 'CREDITOS_FISICA_UNO', 'CREDITOS_MATERIALES', 'CREDITOS_DEMOCRACIA', 'CREDITOS_PBASICA', 'CREDITOS_EE_DOS']

    industrial.columns

    promedios_semestre = []

    # Iterar sobre cada estudiante
    for index, row in industrial.iterrows():
        notas_estudiante = []
        creditos_estudiante = []
        # Iterar sobre las materias del semestre
        for nota_col, veces_col, creditos_col in zip(NOTAS_INDUSTRIAL_DOS, VECES_INDUSTRIAL_DOS, CREDITOS_INDUSTRIAL_DOS):
            # Verificar si el estudiante cursó la materia al menos una vez y si tiene un promedio registrado
            if row[veces_col] > 0 and not pd.isnull(row[nota_col]):
                # Agregar la nota y los créditos a las listas correspondientes
                notas_estudiante.append(row[nota_col])
                creditos_estudiante.append(row[creditos_col])
        # Calcular el promedio ponderado para el semestre actual
        if len(notas_estudiante) > 0:
            promedio_semestre = np.average(notas_estudiante, weights=creditos_estudiante)
        else:
            # Si el estudiante no cursó ninguna materia, asignar promedio cero
            promedio_semestre = 0
        # Agregar el promedio del semestre a la lista de promedios
        promedios_semestre.append(promedio_semestre)

    # Agregar la lista de promedios por semestre al DataFrame
    industrial['PROMEDIO_DOS'] = promedios_semestre

    # Calcular métricas por semestre
    industrial['CAR_DOS'] = industrial[VECES_INDUSTRIAL_DOS].apply(lambda x: (x > 1).sum(), axis=1)
    industrial['NAC_DOS'] = industrial[VECES_INDUSTRIAL_DOS].apply(lambda x: (x > 0).sum(), axis=1)
    industrial['NAA_DOS'] = industrial[NOTAS_INDUSTRIAL_DOS].apply(lambda x: (x >= 30).sum(), axis=1)
    industrial['NAP_DOS'] = industrial['NAC_DOS'] - industrial['NAA_DOS']
    industrial['EPA_DOS'] = industrial.apply(lambda row: 1 if row['PROMEDIO_DOS'] < 30 or row['NAP_DOS'] >= 3 else 2, axis=1)

    # Construir NCC
    def calcular_creditos_cursados(row):
        creditos_cursados = 0
        for veces_col, creditos_col in zip(VECES_INDUSTRIAL_DOS, CREDITOS_INDUSTRIAL_DOS):
            if row[veces_col] > 0:
                creditos_cursados += row[creditos_col]
        return creditos_cursados
    industrial['NCC_DOS'] = industrial.apply(calcular_creditos_cursados, axis=1)

    # Construir NCA
    def calcular_creditos_aprobados(row):
        creditos_aprobados = 0
        for nota_col, creditos_col in zip(NOTAS_INDUSTRIAL_DOS, CREDITOS_INDUSTRIAL_DOS):
            if row[nota_col] >= 30:
                creditos_aprobados += row[creditos_col]
        return creditos_aprobados
    industrial['NCA_DOS'] = industrial.apply(calcular_creditos_aprobados, axis=1)

    # Construir NCP

    industrial['NCP_DOS'] = industrial['NCC_DOS'] - industrial['NCA_DOS']

    # Rendimiento DOS
    conditions = [(industrial['PROMEDIO_DOS'] >= 0) & (industrial['PROMEDIO_DOS'] < 30),
                (industrial['PROMEDIO_DOS'] >= 30) & (industrial['PROMEDIO_DOS'] < 40),
                (industrial['PROMEDIO_DOS'] >= 40) & (industrial['PROMEDIO_DOS'] < 45),
                (industrial['PROMEDIO_DOS'] >= 45) & (industrial['PROMEDIO_DOS'] < 50)]
    values = [1, 2, 3, 4]
    industrial['RENDIMIENTO_DOS'] = pd.Series(pd.cut(industrial['PROMEDIO_DOS'], bins=[0, 30, 40, 45, 50], labels=values))

    """# TERCER SEMESTRE INDUSTRIAL"""

    # Lista industrial tercer semestre

    NOTAS_INDUSTRIAL_TRES = ['NOTA_MULTIVARIADO', 'NOTA_ESTADISTICA_UNO', 'NOTA_TERMODINAMICA', 'NOTA_TGS', 'NOTA_ETICA', 'NOTA_PORIENTADA', 'NOTA_EE_TRES']
    VECES_INDUSTRIAL_TRES = ['VECES_MULTIVARIADO', 'VECES_ESTADISTICA_UNO', 'VECES_TERMODINAMICA', 'VECES_TGS', 'VECES_ETICA', 'VECES_PORIENTADA', 'VECES_EE_TRES']
    CREDITOS_INDUSTRIAL_TRES = ['CREDITOS_MULTIVARIADO', 'CREDITOS_ESTADISTICA_UNO', 'CREDITOS_TERMODINAMICA', 'CREDITOS_TGS', 'CREDITOS_ETICA', 'CREDITOS_PORIENTADA', 'CREDITOS_EE_TRES']

    promedios_semestre = []

    # Iterar sobre cada estudiante
    for index, row in industrial.iterrows():
        notas_estudiante = []
        creditos_estudiante = []
        # Iterar sobre las materias del semestre
        for nota_col, veces_col, creditos_col in zip(NOTAS_INDUSTRIAL_TRES, VECES_INDUSTRIAL_TRES, CREDITOS_INDUSTRIAL_TRES):
            # Verificar si el estudiante cursó la materia al menos una vez y si tiene un promedio registrado
            if row[veces_col] > 0 and not pd.isnull(row[nota_col]):
                # Agregar la nota y los créditos a las listas correspondientes
                notas_estudiante.append(row[nota_col])
                creditos_estudiante.append(row[creditos_col])
        # Calcular el promedio ponderado para el semestre actual
        if len(notas_estudiante) > 0:
            promedio_semestre = np.average(notas_estudiante, weights=creditos_estudiante)
        else:
            # Si el estudiante no cursó ninguna materia, asignar promedio cero
            promedio_semestre = 0
        # Agregar el promedio del semestre a la lista de promedios
        promedios_semestre.append(promedio_semestre)

    # Agregar la lista de promedios por semestre al DataFrame
    industrial['PROMEDIO_TRES'] = promedios_semestre

    # Calcular métricas por semestre
    industrial['CAR_TRES'] = industrial[VECES_INDUSTRIAL_TRES].apply(lambda x: (x > 1).sum(), axis=1)
    industrial['NAC_TRES'] = industrial[VECES_INDUSTRIAL_TRES].apply(lambda x: (x > 0).sum(), axis=1)
    industrial['NAA_TRES'] = industrial[NOTAS_INDUSTRIAL_TRES].apply(lambda x: (x >= 30).sum(), axis=1)
    industrial['NAP_TRES'] = industrial['NAC_TRES'] - industrial['NAA_TRES']
    industrial['EPA_TRES'] = industrial.apply(lambda row: 1 if row['PROMEDIO_TRES'] < 30 or row['NAP_TRES'] >= 3 else 2, axis=1)

    # Construir NCC
    def calcular_creditos_cursados(row):
        creditos_cursados = 0
        for veces_col, creditos_col in zip(VECES_INDUSTRIAL_TRES, CREDITOS_INDUSTRIAL_TRES):
            if row[veces_col] > 0:
                creditos_cursados += row[creditos_col]
        return creditos_cursados
    industrial['NCC_TRES'] = industrial.apply(calcular_creditos_cursados, axis=1)

    # Construir NCA
    def calcular_creditos_aprobados(row):
        creditos_aprobados = 0
        for nota_col, creditos_col in zip(NOTAS_INDUSTRIAL_TRES, CREDITOS_INDUSTRIAL_TRES):
            if row[nota_col] >= 30:
                creditos_aprobados += row[creditos_col]
        return creditos_aprobados
    industrial['NCA_TRES'] = industrial.apply(calcular_creditos_aprobados, axis=1)

    # Construir NCP

    industrial['NCP_TRES'] = industrial['NCC_TRES'] - industrial['NCA_TRES']

    # Rendimiento TRES
    conditions = [(industrial['PROMEDIO_TRES'] >= 0) & (industrial['PROMEDIO_TRES'] < 30),
                (industrial['PROMEDIO_TRES'] >= 30) & (industrial['PROMEDIO_TRES'] < 40),
                (industrial['PROMEDIO_TRES'] >= 40) & (industrial['PROMEDIO_TRES'] < 45),
                (industrial['PROMEDIO_TRES'] >= 45) & (industrial['PROMEDIO_TRES'] < 50)]
    values = [1, 2, 3, 4]
    industrial['RENDIMIENTO_TRES'] = pd.Series(pd.cut(industrial['PROMEDIO_TRES'], bins=[0, 30, 40, 45, 50], labels=values))

    """# CUARTO SEMESTRE INDUSTRIAL"""

    #Lista industrial cuarto semestre

    NOTAS_INDUSTRIAL_CUATRO = ['NOTA_ECONOMIA_UNO', 'NOTA_ECUACIONES', 'NOTA_ESTADISTICA_DOS', 'NOTA_FISICA_DOS', 'NOTA_MECANICA', 'NOTA_PROCESOSQ', 'NOTA_EE_CUATRO']
    VECES_INDUSTRIAL_CUATRO = ['VECES_ECONOMIA_UNO', 'VECES_ECUACIONES', 'VECES_ESTADISTICA_DOS', 'VECES_FISICA_DOS', 'VECES_MECANICA', 'VECES_PROCESOSQ', 'VECES_EE_CUATRO']
    CREDITOS_INDUSTRIAL_CUATRO = ['CREDITOS_ECONOMIA_UNO', 'CREDITOS_ECUACIONES', 'CREDITOS_ESTADISTICA_DOS', 'CREDITOS_FISICA_DOS', 'CREDITOS_MECANICA', 'CREDITOS_PROCESOSQ', 'CREDITOS_EE_CUATRO']

    promedios_semestre = []

    # Iterar sobre cada estudiante
    for index, row in industrial.iterrows():
        notas_estudiante = []
        creditos_estudiante = []
        # Iterar sobre las materias del semestre
        for nota_col, veces_col, creditos_col in zip(NOTAS_INDUSTRIAL_CUATRO, VECES_INDUSTRIAL_CUATRO, CREDITOS_INDUSTRIAL_CUATRO):
            # Verificar si el estudiante cursó la materia al menos una vez y si tiene un promedio registrado
            if row[veces_col] > 0 and not pd.isnull(row[nota_col]):
                # Agregar la nota y los créditos a las listas correspondientes
                notas_estudiante.append(row[nota_col])
                creditos_estudiante.append(row[creditos_col])
        # Calcular el promedio ponderado para el semestre actual
        if len(notas_estudiante) > 0:
            promedio_semestre = np.average(notas_estudiante, weights=creditos_estudiante)
        else:
            # Si el estudiante no cursó ninguna materia, asignar promedio cero
            promedio_semestre = 0
        # Agregar el promedio del semestre a la lista de promedios
        promedios_semestre.append(promedio_semestre)

    # Agregar la lista de promedios por semestre al DataFrame
    industrial['PROMEDIO_CUATRO'] = promedios_semestre

    # Calcular métricas por semestre
    industrial['CAR_CUATRO'] = industrial[VECES_INDUSTRIAL_CUATRO].apply(lambda x: (x > 1).sum(), axis=1)
    industrial['NAC_CUATRO'] = industrial[VECES_INDUSTRIAL_CUATRO].apply(lambda x: (x > 0).sum(), axis=1)
    industrial['NAA_CUATRO'] = industrial[NOTAS_INDUSTRIAL_CUATRO].apply(lambda x: (x >= 30).sum(), axis=1)
    industrial['NAP_CUATRO'] = industrial['NAC_CUATRO'] - industrial['NAA_CUATRO']
    industrial['EPA_CUATRO'] = industrial.apply(lambda row: 1 if row['PROMEDIO_CUATRO'] < 30 or row['NAP_CUATRO'] >= 3 else 2, axis=1)

    # Construir NCC
    def calcular_creditos_cursados(row):
        creditos_cursados = 0
        for veces_col, creditos_col in zip(VECES_INDUSTRIAL_CUATRO, CREDITOS_INDUSTRIAL_CUATRO):
            if row[veces_col] > 0:
                creditos_cursados += row[creditos_col]
        return creditos_cursados
    industrial['NCC_CUATRO'] = industrial.apply(calcular_creditos_cursados, axis=1)

    # Construir NCA
    def calcular_creditos_aprobados(row):
        creditos_aprobados = 0
        for nota_col, creditos_col in zip(NOTAS_INDUSTRIAL_CUATRO, CREDITOS_INDUSTRIAL_CUATRO):
            if row[nota_col] >= 30:
                creditos_aprobados += row[creditos_col]
        return creditos_aprobados
    industrial['NCA_CUATRO'] = industrial.apply(calcular_creditos_aprobados, axis=1)

    # Construir NCP

    industrial['NCP_CUATRO'] = industrial['NCC_CUATRO'] - industrial['NCA_CUATRO']

    # Rendimiento CUATRO
    conditions = [(industrial['PROMEDIO_CUATRO'] >= 0) & (industrial['PROMEDIO_CUATRO'] < 30),
                (industrial['PROMEDIO_CUATRO'] >= 30) & (industrial['PROMEDIO_CUATRO'] < 40),
                (industrial['PROMEDIO_CUATRO'] >= 40) & (industrial['PROMEDIO_CUATRO'] < 45),
                (industrial['PROMEDIO_CUATRO'] >= 45) & (industrial['PROMEDIO_CUATRO'] < 50)]
    values = [1, 2, 3, 4]
    industrial['RENDIMIENTO_CUATRO'] = pd.Series(pd.cut(industrial['PROMEDIO_CUATRO'], bins=[0, 30, 40, 45, 50], labels=values))

    """# QUINTO SEMESTRE INDUSTRIAL"""

    # Lista industrial quinto semestre

    NOTAS_INDUSTRIAL_CINCO = ['NOTA_METODOLOGIA', 'NOTA_FISICA_TRES', 'NOTA_CONTABILIDAD', 'NOTA_PROCESOSM', 'NOTA_ADMINISTRACION', 'NOTA_LENGUA_UNO', 'NOTA_EI_UNO', 'NOTA_EI_DOS']
    VECES_INDUSTRIAL_CINCO = ['VECES_METODOLOGIA', 'VECES_FISICA_TRES', 'VECES_CONTABILIDAD', 'VECES_PROCESOSM', 'VECES_ADMINISTRACION', 'VECES_LENGUA_UNO', 'VECES_EI_UNO', 'VECES_EI_DOS']
    CREDITOS_INDUSTRIAL_CINCO = ['CREDITOS_METODOLOGIA', 'CREDITOS_FISICA_TRES', 'CREDITOS_CONTABILIDAD', 'CREDITOS_PROCESOSM', 'CREDITOS_ADMINISTRACION', 'CREDITOS_LENGUA_UNO', 'CREDITOS_EI_UNO', 'CREDITOS_EI_DOS']

    promedios_semestre = []

    # Iterar sobre cada estudiante
    for index, row in industrial.iterrows():
        notas_estudiante = []
        creditos_estudiante = []
        # Iterar sobre las materias del semestre
        for nota_col, veces_col, creditos_col in zip(NOTAS_INDUSTRIAL_CINCO, VECES_INDUSTRIAL_CINCO, CREDITOS_INDUSTRIAL_CINCO):
            # Verificar si el estudiante cursó la materia al menos una vez y si tiene un promedio registrado
            if row[veces_col] > 0 and not pd.isnull(row[nota_col]):
                # Agregar la nota y los créditos a las listas correspondientes
                notas_estudiante.append(row[nota_col])
                creditos_estudiante.append(row[creditos_col])
        # Calcular el promedio ponderado para el semestre actual
        if len(notas_estudiante) > 0:
            promedio_semestre = np.average(notas_estudiante, weights=creditos_estudiante)
        else:
            # Si el estudiante no cursó ninguna materia, asignar promedio cero
            promedio_semestre = 0
        # Agregar el promedio del semestre a la lista de promedios
        promedios_semestre.append(promedio_semestre)

    # Agregar la lista de promedios por semestre al DataFrame
    industrial['PROMEDIO_CINCO'] = promedios_semestre

    # Calcular métricas por semestre
    industrial['CAR_CINCO'] = industrial[VECES_INDUSTRIAL_CINCO].apply(lambda x: (x > 1).sum(), axis=1)
    industrial['NAC_CINCO'] = industrial[VECES_INDUSTRIAL_CINCO].apply(lambda x: (x > 0).sum(), axis=1)
    industrial['NAA_CINCO'] = industrial[NOTAS_INDUSTRIAL_CINCO].apply(lambda x: (x >= 30).sum(), axis=1)
    industrial['NAP_CINCO'] = industrial['NAC_CINCO'] - industrial['NAA_CINCO']
    industrial['EPA_CINCO'] = industrial.apply(lambda row: 1 if row['PROMEDIO_CINCO'] < 30 or row['NAP_CINCO'] >= 3 else 2, axis=1)

    # Construir NCC
    def calcular_creditos_cursados(row):
        creditos_cursados = 0
        for veces_col, creditos_col in zip(VECES_INDUSTRIAL_CINCO, CREDITOS_INDUSTRIAL_CINCO):
            if row[veces_col] > 0:
                creditos_cursados += row[creditos_col]
        return creditos_cursados
    industrial['NCC_CINCO'] = industrial.apply(calcular_creditos_cursados, axis=1)

    # Construir NCA
    def calcular_creditos_aprobados(row):
        creditos_aprobados = 0
        for nota_col, creditos_col in zip(NOTAS_INDUSTRIAL_CINCO, CREDITOS_INDUSTRIAL_CINCO):
            if row[nota_col] >= 30:
                creditos_aprobados += row[creditos_col]
        return creditos_aprobados
    industrial['NCA_CINCO'] = industrial.apply(calcular_creditos_aprobados, axis=1)

    # Construir NCP

    industrial['NCP_CINCO'] = industrial['NCC_CINCO'] - industrial['NCA_CINCO']

    # Rendimiento CINCO
    conditions = [(industrial['PROMEDIO_CINCO'] >= 0) & (industrial['PROMEDIO_CINCO'] < 30),
                (industrial['PROMEDIO_CINCO'] >= 30) & (industrial['PROMEDIO_CINCO'] < 40),
                (industrial['PROMEDIO_CINCO'] >= 40) & (industrial['PROMEDIO_CINCO'] < 45),
                (industrial['PROMEDIO_CINCO'] >= 45) & (industrial['PROMEDIO_CINCO'] < 50)]
    values = [1, 2, 3, 4]
    industrial['RENDIMIENTO_CINCO'] = pd.Series(pd.cut(industrial['PROMEDIO_CINCO'], bins=[0, 30, 40, 45, 50], labels=values))

    """# SEXTO SEMESTRE INDUSTRIAL"""

    #Lista industrial sexto semestre

    NOTAS_INDUSTRIAL_SEIS = ['NOTA_ECONOMIA_DOS', 'NOTA_PLINEAL', 'NOTA_DERECHO', 'NOTA_IECONOMICA', 'NOTA_DISENO', 'NOTA_METODOS', 'NOTA_SEGURIDAD', 'NOTA_EI_TRES']
    VECES_INDUSTRIAL_SEIS = ['VECES_ECONOMIA_DOS', 'VECES_PLINEAL', 'VECES_DERECHO', 'VECES_IECONOMICA', 'VECES_DISENO', 'VECES_METODOS', 'VECES_SEGURIDAD', 'VECES_EI_TRES']
    CREDITOS_INDUSTRIAL_SEIS = ['CREDITOS_ECONOMIA_DOS', 'CREDITOS_PLINEAL', 'CREDITOS_DERECHO', 'CREDITOS_IECONOMICA', 'CREDITOS_DISENO', 'CREDITOS_METODOS', 'CREDITOS_SEGURIDAD', 'CREDITOS_EI_TRES']

    promedios_semestre = []

    # Iterar sobre cada estudiante
    for index, row in industrial.iterrows():
        notas_estudiante = []
        creditos_estudiante = []
        # Iterar sobre las materias del semestre
        for nota_col, veces_col, creditos_col in zip(NOTAS_INDUSTRIAL_SEIS, VECES_INDUSTRIAL_SEIS, CREDITOS_INDUSTRIAL_SEIS):
            # Verificar si el estudiante cursó la materia al menos una vez y si tiene un promedio registrado
            if row[veces_col] > 0 and not pd.isnull(row[nota_col]):
                # Agregar la nota y los créditos a las listas correspondientes
                notas_estudiante.append(row[nota_col])
                creditos_estudiante.append(row[creditos_col])
        # Calcular el promedio ponderado para el semestre actual
        if len(notas_estudiante) > 0:
            promedio_semestre = np.average(notas_estudiante, weights=creditos_estudiante)
        else:
            # Si el estudiante no cursó ninguna materia, asignar promedio cero
            promedio_semestre = 0
        # Agregar el promedio del semestre a la lista de promedios
        promedios_semestre.append(promedio_semestre)

    # Agregar la lista de promedios por semestre al DataFrame
    industrial['PROMEDIO_SEIS'] = promedios_semestre

    # Calcular métricas por semestre
    industrial['CAR_SEIS'] = industrial[VECES_INDUSTRIAL_SEIS].apply(lambda x: (x > 1).sum(), axis=1)
    industrial['NAC_SEIS'] = industrial[VECES_INDUSTRIAL_SEIS].apply(lambda x: (x > 0).sum(), axis=1)
    industrial['NAA_SEIS'] = industrial[NOTAS_INDUSTRIAL_SEIS].apply(lambda x: (x >= 30).sum(), axis=1)
    industrial['NAP_SEIS'] = industrial['NAC_SEIS'] - industrial['NAA_SEIS']
    industrial['EPA_SEIS'] = industrial.apply(lambda row: 1 if row['PROMEDIO_SEIS'] < 30 or row['NAP_SEIS'] >= 3 else 2, axis=1)

    # Construir NCC
    def calcular_creditos_cursados(row):
        creditos_cursados = 0
        for veces_col, creditos_col in zip(VECES_INDUSTRIAL_SEIS, CREDITOS_INDUSTRIAL_SEIS):
            if row[veces_col] > 0:
                creditos_cursados += row[creditos_col]
        return creditos_cursados
    industrial['NCC_SEIS'] = industrial.apply(calcular_creditos_cursados, axis=1)

    # Construir NCA
    def calcular_creditos_aprobados(row):
        creditos_aprobados = 0
        for nota_col, creditos_col in zip(NOTAS_INDUSTRIAL_SEIS, CREDITOS_INDUSTRIAL_SEIS):
            if row[nota_col] >= 30:
                creditos_aprobados += row[creditos_col]
        return creditos_aprobados
    industrial['NCA_SEIS'] = industrial.apply(calcular_creditos_aprobados, axis=1)

    # Construir NCP

    industrial['NCP_SEIS'] = industrial['NCC_SEIS'] - industrial['NCA_SEIS']

    # Rendimiento SEIS
    conditions = [(industrial['PROMEDIO_SEIS'] >= 0) & (industrial['PROMEDIO_SEIS'] < 30),
                (industrial['PROMEDIO_SEIS'] >= 30) & (industrial['PROMEDIO_SEIS'] < 40),
                (industrial['PROMEDIO_SEIS'] >= 40) & (industrial['PROMEDIO_SEIS'] < 45),
                (industrial['PROMEDIO_SEIS'] >= 45) & (industrial['PROMEDIO_SEIS'] < 50)]
    values = [1, 2, 3, 4]
    industrial['RENDIMIENTO_SEIS'] = pd.Series(pd.cut(industrial['PROMEDIO_SEIS'], bins=[0, 30, 40, 45, 50], labels=values))

    """# SEPTIMO SEMESTRE INDUSTRIAL"""

    #Lista industrial primer semestre

    NOTAS_INDUSTRIAL_SIETE = ['NOTA_EMPRENDIMIENTO', 'NOTA_GRAFOS', 'NOTA_CALIDAD_UNO', 'NOTA_MERCADOTECNIA', 'NOTA_ERGONOMIA', 'NOTA_HOMBRE', 'NOTA_EI_CUATRO', 'NOTA_EI_CINCO']
    VECES_INDUSTRIAL_SIETE = ['VECES_EMPRENDIMIENTO', 'VECES_GRAFOS', 'VECES_CALIDAD_UNO', 'VECES_MERCADOTECNIA', 'VECES_ERGONOMIA', 'VECES_HOMBRE', 'VECES_EI_CUATRO', 'VECES_EI_CINCO']
    CREDITOS_INDUSTRIAL_SIETE = ['CREDITOS_EMPRENDIMIENTO', 'CREDITOS_GRAFOS', 'CREDITOS_CALIDAD_UNO', 'CREDITOS_MERCADOTECNIA', 'CREDITOS_ERGONOMIA', 'CREDITOS_HOMBRE', 'CREDITOS_EI_CUATRO', 'CREDITOS_EI_CINCO']

    promedios_semestre = []

    # Iterar sobre cada estudiante
    for index, row in industrial.iterrows():
        notas_estudiante = []
        creditos_estudiante = []
        # Iterar sobre las materias del semestre
        for nota_col, veces_col, creditos_col in zip(NOTAS_INDUSTRIAL_SIETE, VECES_INDUSTRIAL_SIETE, CREDITOS_INDUSTRIAL_SIETE):
            # Verificar si el estudiante cursó la materia al menos una vez y si tiene un promedio registrado
            if row[veces_col] > 0 and not pd.isnull(row[nota_col]):
                # Agregar la nota y los créditos a las listas correspondientes
                notas_estudiante.append(row[nota_col])
                creditos_estudiante.append(row[creditos_col])
        # Calcular el promedio ponderado para el semestre actual
        if len(notas_estudiante) > 0:
            promedio_semestre = np.average(notas_estudiante, weights=creditos_estudiante)
        else:
            # Si el estudiante no cursó ninguna materia, asignar promedio cero
            promedio_semestre = 0
        # Agregar el promedio del semestre a la lista de promedios
        promedios_semestre.append(promedio_semestre)

    # Agregar la lista de promedios por semestre al DataFrame
    industrial['PROMEDIO_SIETE'] = promedios_semestre

    # Calcular métricas por semestre
    industrial['CAR_SIETE'] = industrial[VECES_INDUSTRIAL_SIETE].apply(lambda x: (x > 1).sum(), axis=1)
    industrial['NAC_SIETE'] = industrial[VECES_INDUSTRIAL_SIETE].apply(lambda x: (x > 0).sum(), axis=1)
    industrial['NAA_SIETE'] = industrial[NOTAS_INDUSTRIAL_SIETE].apply(lambda x: (x >= 30).sum(), axis=1)
    industrial['NAP_SIETE'] = industrial['NAC_SIETE'] - industrial['NAA_SIETE']
    industrial['EPA_SIETE'] = industrial.apply(lambda row: 1 if row['PROMEDIO_SIETE'] < 30 or row['NAP_SIETE'] >= 3 else 2, axis=1)

    # Construir NCC
    def calcular_creditos_cursados(row):
        creditos_cursados = 0
        for veces_col, creditos_col in zip(VECES_INDUSTRIAL_SIETE, CREDITOS_INDUSTRIAL_SIETE):
            if row[veces_col] > 0:
                creditos_cursados += row[creditos_col]
        return creditos_cursados
    industrial['NCC_SIETE'] = industrial.apply(calcular_creditos_cursados, axis=1)

    # Construir NCA
    def calcular_creditos_aprobados(row):
        creditos_aprobados = 0
        for nota_col, creditos_col in zip(NOTAS_INDUSTRIAL_SIETE, CREDITOS_INDUSTRIAL_SIETE):
            if row[nota_col] >= 30:
                creditos_aprobados += row[creditos_col]
        return creditos_aprobados
    industrial['NCA_SIETE'] = industrial.apply(calcular_creditos_aprobados, axis=1)

    # Construir NCP

    industrial['NCP_SIETE'] = industrial['NCC_SIETE'] - industrial['NCA_SIETE']

    # Rendimiento SIETE
    conditions = [(industrial['PROMEDIO_SIETE'] >= 0) & (industrial['PROMEDIO_SIETE'] < 30),
                (industrial['PROMEDIO_SIETE'] >= 30) & (industrial['PROMEDIO_SIETE'] < 40),
                (industrial['PROMEDIO_SIETE'] >= 40) & (industrial['PROMEDIO_SIETE'] < 45),
                (industrial['PROMEDIO_SIETE'] >= 45) & (industrial['PROMEDIO_SIETE'] < 50)]
    values = [1, 2, 3, 4]
    industrial['RENDIMIENTO_SIETE'] = pd.Series(pd.cut(industrial['PROMEDIO_SIETE'], bins=[0, 30, 40, 45, 50], labels=values))

    """# OCTAVO SEMESTRE INDUSTRIAL"""

    #Lista industrial primer semestre

    NOTAS_INDUSTRIAL_OCHO = ['NOTA_LOG_UNO', 'NOTA_GOPERACIONES', 'NOTA_CALIDAD_DOS', 'NOTA_GAMBIENTAL', 'NOTA_LENGUA_DOS', 'NOTA_CONTEXTO', 'NOTA_EI_SEIS', 'NOTA_EI_SIETE']
    VECES_INDUSTRIAL_OCHO = ['VECES_LOG_UNO', 'VECES_GOPERACIONES', 'VECES_CALIDAD_DOS', 'VECES_GAMBIENTAL', 'VECES_LENGUA_DOS', 'VECES_CONTEXTO', 'VECES_EI_SEIS', 'VECES_EI_SIETE']
    CREDITOS_INDUSTRIAL_OCHO = ['CREDITOS_LOG_UNO', 'CREDITOS_GOPERACIONES', 'CREDITOS_CALIDAD_DOS', 'CREDITOS_GAMBIENTAL', 'CREDITOS_LENGUA_DOS', 'CREDITOS_CONTEXTO', 'CREDITOS_EI_SEIS', 'CREDITOS_EI_SIETE']

    promedios_semestre = []

    # Iterar sobre cada estudiante
    for index, row in industrial.iterrows():
        notas_estudiante = []
        creditos_estudiante = []
        # Iterar sobre las materias del semestre
        for nota_col, veces_col, creditos_col in zip(NOTAS_INDUSTRIAL_OCHO, VECES_INDUSTRIAL_OCHO, CREDITOS_INDUSTRIAL_OCHO):
            # Verificar si el estudiante cursó la materia al menos una vez y si tiene un promedio registrado
            if row[veces_col] > 0 and not pd.isnull(row[nota_col]):
                # Agregar la nota y los créditos a las listas correspondientes
                notas_estudiante.append(row[nota_col])
                creditos_estudiante.append(row[creditos_col])
        # Calcular el promedio ponderado para el semestre actual
        if len(notas_estudiante) > 0:
            promedio_semestre = np.average(notas_estudiante, weights=creditos_estudiante)
        else:
            # Si el estudiante no cursó ninguna materia, asignar promedio cero
            promedio_semestre = 0
        # Agregar el promedio del semestre a la lista de promedios
        promedios_semestre.append(promedio_semestre)

    # Agregar la lista de promedios por semestre al DataFrame
    industrial['PROMEDIO_OCHO'] = promedios_semestre

    # Calcular métricas por semestre
    industrial['CAR_OCHO'] = industrial[VECES_INDUSTRIAL_OCHO].apply(lambda x: (x > 1).sum(), axis=1)
    industrial['NAC_OCHO'] = industrial[VECES_INDUSTRIAL_OCHO].apply(lambda x: (x > 0).sum(), axis=1)
    industrial['NAA_OCHO'] = industrial[NOTAS_INDUSTRIAL_OCHO].apply(lambda x: (x >= 30).sum(), axis=1)
    industrial['NAP_OCHO'] = industrial['NAC_OCHO'] - industrial['NAA_OCHO']
    industrial['EPA_OCHO'] = industrial.apply(lambda row: 1 if row['PROMEDIO_OCHO'] < 30 or row['NAP_OCHO'] >= 3 else 2, axis=1)

    # Construir NCC
    def calcular_creditos_cursados(row):
        creditos_cursados = 0
        for veces_col, creditos_col in zip(VECES_INDUSTRIAL_OCHO, CREDITOS_INDUSTRIAL_OCHO):
            if row[veces_col] > 0:
                creditos_cursados += row[creditos_col]
        return creditos_cursados
    industrial['NCC_OCHO'] = industrial.apply(calcular_creditos_cursados, axis=1)

    # Construir NCA
    def calcular_creditos_aprobados(row):
        creditos_aprobados = 0
        for nota_col, creditos_col in zip(NOTAS_INDUSTRIAL_OCHO, CREDITOS_INDUSTRIAL_OCHO):
            if row[nota_col] >= 30:
                creditos_aprobados += row[creditos_col]
        return creditos_aprobados
    industrial['NCA_OCHO'] = industrial.apply(calcular_creditos_aprobados, axis=1)

    # Construir NCP

    industrial['NCP_OCHO'] = industrial['NCC_OCHO'] - industrial['NCA_OCHO']

    # Rendimiento OCHO
    conditions = [(industrial['PROMEDIO_OCHO'] >= 0) & (industrial['PROMEDIO_OCHO'] < 30),
                (industrial['PROMEDIO_OCHO'] >= 30) & (industrial['PROMEDIO_OCHO'] < 40),
                (industrial['PROMEDIO_OCHO'] >= 40) & (industrial['PROMEDIO_OCHO'] < 45),
                (industrial['PROMEDIO_OCHO'] >= 45) & (industrial['PROMEDIO_OCHO'] < 50)]
    values = [1, 2, 3, 4]
    industrial['RENDIMIENTO_OCHO'] = pd.Series(pd.cut(industrial['PROMEDIO_OCHO'], bins=[0, 30, 40, 45, 50], labels=values))

    """# NOVENO SEMESTRE INDUSTRIAL"""

    #Lista industrial primer semestre

    NOTAS_INDUSTRIAL_NUEVE = ['NOTA_GRADO_UNO', 'NOTA_LOG_DOS', 'NOTA_DECISION', 'NOTA_PRODUCCION', 'NOTA_FINANZAS', 'NOTA_GIT', 'NOTA_GTH', 'NOTA_HISTORIA']
    VECES_INDUSTRIAL_NUEVE = ['VECES_GRADO_UNO', 'VECES_LOG_DOS', 'VECES_DECISION', 'VECES_PRODUCCION', 'VECES_FINANZAS', 'VECES_GIT', 'VECES_GTH', 'VECES_HISTORIA']
    CREDITOS_INDUSTRIAL_NUEVE = ['CREDITOS_GRADO_UNO', 'CREDITOS_LOG_DOS', 'CREDITOS_DECISION', 'CREDITOS_PRODUCCION', 'CREDITOS_FINANZAS', 'CREDITOS_GIT', 'CREDITOS_GTH', 'CREDITOS_HISTORIA']

    promedios_semestre = []

    # Iterar sobre cada estudiante
    for index, row in industrial.iterrows():
        notas_estudiante = []
        creditos_estudiante = []
        # Iterar sobre las materias del semestre
        for nota_col, veces_col, creditos_col in zip(NOTAS_INDUSTRIAL_NUEVE, VECES_INDUSTRIAL_NUEVE, CREDITOS_INDUSTRIAL_NUEVE):
            # Verificar si el estudiante cursó la materia al menos una vez y si tiene un promedio registrado
            if row[veces_col] > 0 and not pd.isnull(row[nota_col]):
                # Agregar la nota y los créditos a las listas correspondientes
                notas_estudiante.append(row[nota_col])
                creditos_estudiante.append(row[creditos_col])
        # Calcular el promedio ponderado para el semestre actual
        if len(notas_estudiante) > 0:
            promedio_semestre = np.average(notas_estudiante, weights=creditos_estudiante)
        else:
            # Si el estudiante no cursó ninguna materia, asignar promedio cero
            promedio_semestre = 0
        # Agregar el promedio del semestre a la lista de promedios
        promedios_semestre.append(promedio_semestre)

    # Agregar la lista de promedios por semestre al DataFrame
    industrial['PROMEDIO_NUEVE'] = promedios_semestre

    # Calcular métricas por semestre
    industrial['CAR_NUEVE'] = industrial[VECES_INDUSTRIAL_NUEVE].apply(lambda x: (x > 1).sum(), axis=1)
    industrial['NAC_NUEVE'] = industrial[VECES_INDUSTRIAL_NUEVE].apply(lambda x: (x > 0).sum(), axis=1)
    industrial['NAA_NUEVE'] = industrial[NOTAS_INDUSTRIAL_NUEVE].apply(lambda x: (x >= 30).sum(), axis=1)
    industrial['NAP_NUEVE'] = industrial['NAC_NUEVE'] - industrial['NAA_NUEVE']
    industrial['EPA_NUEVE'] = industrial.apply(lambda row: 1 if row['PROMEDIO_NUEVE'] < 30 or row['NAP_NUEVE'] >= 3 else 2, axis=1)

    # Construir NCC
    def calcular_creditos_cursados(row):
        creditos_cursados = 0
        for veces_col, creditos_col in zip(VECES_INDUSTRIAL_NUEVE, CREDITOS_INDUSTRIAL_NUEVE):
            if row[veces_col] > 0:
                creditos_cursados += row[creditos_col]
        return creditos_cursados
    industrial['NCC_NUEVE'] = industrial.apply(calcular_creditos_cursados, axis=1)

    # Construir NCA
    def calcular_creditos_aprobados(row):
        creditos_aprobados = 0
        for nota_col, creditos_col in zip(NOTAS_INDUSTRIAL_NUEVE, CREDITOS_INDUSTRIAL_NUEVE):
            if row[nota_col] >= 30:
                creditos_aprobados += row[creditos_col]
        return creditos_aprobados
    industrial['NCA_NUEVE'] = industrial.apply(calcular_creditos_aprobados, axis=1)

    # Construir NCP

    industrial['NCP_NUEVE'] = industrial['NCC_NUEVE'] - industrial['NCA_NUEVE']

    # Rendimiento NUEVE
    conditions = [(industrial['PROMEDIO_NUEVE'] >= 0) & (industrial['PROMEDIO_NUEVE'] < 30),
                (industrial['PROMEDIO_NUEVE'] >= 30) & (industrial['PROMEDIO_NUEVE'] < 40),
                (industrial['PROMEDIO_NUEVE'] >= 40) & (industrial['PROMEDIO_NUEVE'] < 45),
                (industrial['PROMEDIO_NUEVE'] >= 45) & (industrial['PROMEDIO_NUEVE'] < 50)]
    values = [1, 2, 3, 4]
    industrial['RENDIMIENTO_NUEVE'] = pd.Series(pd.cut(industrial['PROMEDIO_NUEVE'], bins=[0, 30, 40, 45, 50], labels=values))

    """# DECIMO SEMESTRE INDUSTRIAL"""

    #Lista industrial primer semestre

    NOTAS_INDUSTRIAL_DIEZ = ['NOTA_GRADO_DOS', 'NOTA_LOG_TRES', 'NOTA_SIMULACION', 'NOTA_FORMULACION', 'NOTA_GERENCIA', 'NOTA_LENGUA_TRES', 'NOTA_EI_OCHO', 'NOTA_EI_NUEVE']
    VECES_INDUSTRIAL_DIEZ = ['VECES_GRADO_DOS', 'VECES_LOG_TRES', 'VECES_SIMULACION', 'VECES_FORMULACION', 'VECES_GERENCIA', 'VECES_LENGUA_TRES', 'VECES_EI_OCHO', 'VECES_EI_NUEVE']
    CREDITOS_INDUSTRIAL_DIEZ = ['CREDITOS_GRADO_DOS', 'CREDITOS_LOG_TRES', 'CREDITOS_SIMULACION', 'CREDITOS_FORMULACION', 'CREDITOS_GERENCIA', 'CREDITOS_LENGUA_TRES', 'CREDITOS_EI_OCHO', 'CREDITOS_EI_NUEVE']

    promedios_semestre = []

    # Iterar sobre cada estudiante
    for index, row in industrial.iterrows():
        notas_estudiante = []
        creditos_estudiante = []
        # Iterar sobre las materias del semestre
        for nota_col, veces_col, creditos_col in zip(NOTAS_INDUSTRIAL_DIEZ, VECES_INDUSTRIAL_DIEZ, CREDITOS_INDUSTRIAL_DIEZ):
            # Verificar si el estudiante cursó la materia al menos una vez y si tiene un promedio registrado
            if row[veces_col] > 0 and not pd.isnull(row[nota_col]):
                # Agregar la nota y los créditos a las listas correspondientes
                notas_estudiante.append(row[nota_col])
                creditos_estudiante.append(row[creditos_col])
        # Calcular el promedio ponderado para el semestre actual
        if len(notas_estudiante) > 0:
            promedio_semestre = np.average(notas_estudiante, weights=creditos_estudiante)
        else:
            # Si el estudiante no cursó ninguna materia, asignar promedio cero
            promedio_semestre = 0
        # Agregar el promedio del semestre a la lista de promedios
        promedios_semestre.append(promedio_semestre)

    # Agregar la lista de promedios por semestre al DataFrame
    industrial['PROMEDIO_DIEZ'] = promedios_semestre

    # Calcular métricas por semestre
    industrial['CAR_DIEZ'] = industrial[VECES_INDUSTRIAL_DIEZ].apply(lambda x: (x > 1).sum(), axis=1)
    industrial['NAC_DIEZ'] = industrial[VECES_INDUSTRIAL_DIEZ].apply(lambda x: (x > 0).sum(), axis=1)
    industrial['NAA_DIEZ'] = industrial[NOTAS_INDUSTRIAL_DIEZ].apply(lambda x: (x >= 30).sum(), axis=1)
    industrial['NAP_DIEZ'] = industrial['NAC_DIEZ'] - industrial['NAA_DIEZ']
    industrial['EPA_DIEZ'] = industrial.apply(lambda row: 1 if row['PROMEDIO_DIEZ'] < 30 or row['NAP_DIEZ'] >= 3 else 2, axis=1)

    # Construir NCC
    def calcular_creditos_cursados(row):
        creditos_cursados = 0
        for veces_col, creditos_col in zip(VECES_INDUSTRIAL_DIEZ, CREDITOS_INDUSTRIAL_DIEZ):
            if row[veces_col] > 0:
                creditos_cursados += row[creditos_col]
        return creditos_cursados
    industrial['NCC_DIEZ'] = industrial.apply(calcular_creditos_cursados, axis=1)

    # Construir NCA
    def calcular_creditos_aprobados(row):
        creditos_aprobados = 0
        for nota_col, creditos_col in zip(NOTAS_INDUSTRIAL_DIEZ, CREDITOS_INDUSTRIAL_DIEZ):
            if row[nota_col] >= 30:
                creditos_aprobados += row[creditos_col]
        return creditos_aprobados
    industrial['NCA_DIEZ'] = industrial.apply(calcular_creditos_aprobados, axis=1)

    # Construir NCP

    industrial['NCP_DIEZ'] = industrial['NCC_DIEZ'] - industrial['NCA_DIEZ']

    # Rendimiento DIEZ
    conditions = [(industrial['PROMEDIO_DIEZ'] >= 0) & (industrial['PROMEDIO_DIEZ'] < 30),
                (industrial['PROMEDIO_DIEZ'] >= 30) & (industrial['PROMEDIO_DIEZ'] < 40),
                (industrial['PROMEDIO_DIEZ'] >= 40) & (industrial['PROMEDIO_DIEZ'] < 45),
                (industrial['PROMEDIO_DIEZ'] >= 45) & (industrial['PROMEDIO_DIEZ'] < 50)]
    values = [1, 2, 3, 4]
    industrial['RENDIMIENTO_DIEZ'] = pd.Series(pd.cut(industrial['PROMEDIO_DIEZ'], bins=[0, 30, 40, 45, 50], labels=values))

    # Obtén una lista de todas las columnas que comienzan con "RENDIMIENTO_"
    columnas_rendimiento = [col for col in industrial.columns if col.startswith('RENDIMIENTO_')]

    # Convertir columnas categóricas a numéricas
    industrial[columnas_rendimiento] = industrial[columnas_rendimiento].astype(float)

    # Reemplazar los valores vacíos por cero en estas columnas
    industrial[columnas_rendimiento] = industrial[columnas_rendimiento].fillna(0)

    #industrial.to_csv("industrialfinal.csv", sep=',', index=False)

    industrial = industrial.apply(pd.to_numeric)

    #En promedio a filtrar es el número mínimo que debe tener un estudiante como promedio de las notas que se toman como variables
    promedio_a_filtrar = 5
    año_de_filtro = 2011

    """# INGENIERIA INDUSTRIAL"""

    # Primer semestre ingeniería industrial
    industrial1 = industrial.loc[:, ["GENERO", "TIPO_COLEGIO", "LOCALIDAD_COLEGIO","CALENDARIO","MUNICIPIO",
                                    "DEPARTAMENTO", "PG_ICFES","CON_MAT_ICFES","APT_MAT_ICFES","FISICA_ICFES","QUIMICA_ICFES",
                                    "APT_VERB_ICFES","LITERATURA_ICFES","BIOLOGIA_ICFES","SOCIALES_ICFES","FILOSOFIA_ICFES",
                                    "IDIOMA_ICFES","LOCALIDAD","DISTANCIA","INSCRIPCION","ESTRATO","ANO_INGRESO","RENDIMIENTO_UNO","PROMEDIO_UNO"]]

    industrial1 = industrial1 = industrial1.loc[industrial1['ANO_INGRESO'] >= año_de_filtro]
    industrial1.to_csv("industrial1.csv", sep=';', index=False)


    # Segundo semestre ingeniería industrial
    industrial2 = industrial.loc[:, ["LOCALIDAD_COLEGIO", "PG_ICFES", "CON_MAT_ICFES", "FISICA_ICFES", "BIOLOGIA_ICFES",
                                    "IDIOMA_ICFES", "LOCALIDAD", "PROMEDIO_UNO", "CAR_UNO", "NCC_UNO", "NCA_UNO", "NCP_UNO", "NAC_UNO",
                                    "NAA_UNO", "NAP_UNO", "EPA_UNO", "CREDITOS_DIFERENCIAL", "ESTADO_FINAL", "NOTA_DIFERENCIAL",
                                    "VECES_DIFERENCIAL", "NOTA_DIBUJO", "VECES_DIBUJO", "CREDITOS_DIBUJO", "NOTA_QUIMICA", "VECES_QUIMICA",
                                    "CREDITOS_QUIMICA", "NOTA_CFJC", "VECES_CFJC", "CREDITOS_CFJC", "NOTA_TEXTOS", "VECES_TEXTOS",
                                    "CREDITOS_TEXTOS", "NOTA_SEMINARIO", "VECES_SEMINARIO", "CREDITOS_SEMINARIO", "NOTA_EE_UNO","VECES_EE_UNO",
                                    "CREDITOS_EE_UNO", "RENDIMIENTO_DOS","PROMEDIO_DOS"]]

    columnas_nota = [col for col in industrial2.columns if col.startswith('NOTA')]

    industrial2['Promedio_NOTA'] = industrial2[columnas_nota].mean(axis=1)
    industrial2['Promedio_NOTA']
    filas_a_eliminar = industrial2[industrial2['Promedio_NOTA'] < promedio_a_filtrar]

    industrial_filtrado = industrial2.drop(filas_a_eliminar.index)
    industrial_filtrado.drop(columns=['Promedio_NOTA'], inplace=True)
    industrial2 = industrial_filtrado

    industrial2.to_csv("industrial2.csv", sep=';', index=False)

    # Tercer semestre ingeniería industrial
    industrial3 = industrial.loc[:, ["NUMERO", "LOCALIDAD_COLEGIO", "PG_ICFES", "CON_MAT_ICFES", "FISICA_ICFES", "BIOLOGIA_ICFES",
                                    "IDIOMA_ICFES", "LOCALIDAD", "PROMEDIO_UNO", "CAR_UNO", "NCC_UNO", "NCP_UNO", "NAA_UNO", "NAP_UNO",
                                    "ESTADO_FINAL", "NOTA_DIFERENCIAL", "NOTA_DIBUJO", "NOTA_QUIMICA", "NOTA_CFJC", "NOTA_TEXTOS",
                                    "NOTA_SEMINARIO", "NOTA_EE_UNO", "PROMEDIO_DOS", "CAR_DOS", "NCC_DOS", "NCA_DOS", "NCP_DOS", "NAC_DOS",
                                    "NAA_DOS", "NAP_DOS", "EPA_DOS", "NOTA_ALGEBRA", "VECES_ALGEBRA", "CREDITOS_ALGEBRA", "NOTA_INTEGRAL",
                                    "VECES_INTEGRAL", "CREDITOS_INTEGRAL", "NOTA_FISICA_UNO", "VECES_FISICA_UNO", "CREDITOS_FISICA_UNO",
                                    "NOTA_MATERIALES", "VECES_MATERIALES", "CREDITOS_MATERIALES", "NOTA_DEMOCRACIA", "VECES_DEMOCRACIA",
                                    "CREDITOS_DEMOCRACIA", "NOTA_PBASICA", "VECES_PBASICA", "CREDITOS_PBASICA", "NOTA_EE_DOS",
                                    "VECES_EE_DOS", "CREDITOS_EE_DOS", "RENDIMIENTO_TRES","PROMEDIO_TRES"]]

    columnas_nota = [col for col in industrial3.columns if col.startswith('NOTA')]

    industrial3['Promedio_NOTA'] = industrial3[columnas_nota].mean(axis=1)
    industrial3['Promedio_NOTA']
    filas_a_eliminar = industrial3[industrial3['Promedio_NOTA'] < promedio_a_filtrar]

    industrial_filtrado = industrial3.drop(filas_a_eliminar.index)
    industrial_filtrado.drop(columns=['Promedio_NOTA'], inplace=True)
    industrial3 = industrial_filtrado
    industrial3.to_csv("industrial3.csv", sep=';', index=False)

    # Cuarto semestre ingeniería industrial
    industrial4 = industrial.loc[:, ["NUMERO", "PROMEDIO_UNO", "NAA_UNO", "NOTA_DIFERENCIAL", "NOTA_DIBUJO", "NOTA_TEXTOS",
                                    "NOTA_EE_UNO", "PROMEDIO_DOS", "NCC_DOS", "NCA_DOS", "NAA_DOS", "NOTA_ALGEBRA",
                                    "NOTA_INTEGRAL", "NOTA_MATERIALES", "NOTA_PBASICA", "NOTA_EE_DOS", "CAR_TRES", "NCC_TRES",
                                    "NCA_TRES", "NCP_TRES", "NAC_TRES", "NAA_TRES", "NAP_TRES", "EPA_TRES", "NOTA_MULTIVARIADO",
                                    "VECES_MULTIVARIADO", "CREDITOS_MULTIVARIADO", "NOTA_ESTADISTICA_UNO", "VECES_ESTADISTICA_UNO",
                                    "CREDITOS_ESTADISTICA_UNO", "NOTA_TERMODINAMICA", "VECES_TERMODINAMICA", "CREDITOS_TERMODINAMICA",
                                    "NOTA_TGS", "VECES_TGS", "CREDITOS_TGS", "NOTA_ETICA", "VECES_ETICA", "CREDITOS_ETICA",
                                    "NOTA_PORIENTADA","VECES_PORIENTADA", "CREDITOS_PORIENTADA", "NOTA_EE_TRES",
                                    "VECES_EE_TRES", "CREDITOS_EE_TRES", "RENDIMIENTO_CUATRO","PROMEDIO_CUATRO"]]

    columnas_nota = [col for col in industrial4.columns if col.startswith('NOTA')]

    industrial4['Promedio_NOTA'] = industrial4[columnas_nota].mean(axis=1)
    industrial4['Promedio_NOTA']
    filas_a_eliminar = industrial4[industrial4['Promedio_NOTA'] < promedio_a_filtrar]

    industrial_filtrado = industrial4.drop(filas_a_eliminar.index)
    industrial_filtrado.drop(columns=['Promedio_NOTA'], inplace=True)
    industrial4 = industrial_filtrado
    industrial4.to_csv("industrial4.csv", sep=';', index=False)

    # Quinto semestre ingeniería industrial
    industrial5 = industrial.loc[:, ["NUMERO", "PROMEDIO_UNO", "NOTA_EE_UNO", "PROMEDIO_DOS", "NOTA_ALGEBRA", "NOTA_INTEGRAL",
                                    "NOTA_MATERIALES", "NOTA_EE_DOS", "PROMEDIO_TRES", "NAA_TRES", "NOTA_MULTIVARIADO",
                                    "NOTA_ESTADISTICA_UNO", "NOTA_TERMODINAMICA", "NOTA_TGS", "NOTA_EE_TRES", "PROMEDIO_CUATRO",
                                    "CAR_CUATRO", "NCC_CUATRO", "NCA_CUATRO", "NCP_CUATRO", "NAC_CUATRO","NAA_CUATRO", "NAP_CUATRO",
                                    "EPA_CUATRO", "NOTA_ECONOMIA_UNO", "VECES_ECONOMIA_UNO", "CREDITOS_ECONOMIA_UNO",
                                    "NOTA_ECUACIONES", "VECES_ECUACIONES", "CREDITOS_ECUACIONES", "NOTA_ESTADISTICA_DOS",
                                    "VECES_ESTADISTICA_DOS", "CREDITOS_ESTADISTICA_DOS", "NOTA_FISICA_DOS", "VECES_FISICA_DOS",
                                    "CREDITOS_FISICA_DOS", "NOTA_MECANICA", "VECES_MECANICA", "CREDITOS_MECANICA", "NOTA_PROCESOSQ",
                                    "VECES_PROCESOSQ", "CREDITOS_PROCESOSQ", "NOTA_EE_CUATRO", "VECES_EE_CUATRO", "CREDITOS_EE_CUATRO",
                                    "RENDIMIENTO_CINCO","PROMEDIO_CINCO"]]

    columnas_nota = [col for col in industrial5.columns if col.startswith('NOTA')]

    industrial5['Promedio_NOTA'] = industrial5[columnas_nota].mean(axis=1)
    industrial5['Promedio_NOTA']
    filas_a_eliminar = industrial5[industrial5['Promedio_NOTA'] < promedio_a_filtrar]

    industrial_filtrado = industrial5.drop(filas_a_eliminar.index)
    industrial_filtrado.drop(columns=['Promedio_NOTA'], inplace=True)
    industrial5 = industrial_filtrado
    industrial5.to_csv("industrial5.csv", sep=';', index=False)


    # Sexto semestre ingeniería industrial
    industrial6 = industrial.loc[:, ["NUMERO", "PROMEDIO_UNO", "NOTA_EE_UNO", "PROMEDIO_DOS", "NOTA_ALGEBRA", "NOTA_INTEGRAL",
                                    "NOTA_MATERIALES", "NOTA_EE_DOS", "PROMEDIO_TRES", "NAA_TRES", "NOTA_MULTIVARIADO",
                                    "NOTA_TERMODINAMICA", "NOTA_ECONOMIA_UNO", "NOTA_ECUACIONES", "NOTA_ESTADISTICA_DOS",
                                    "NOTA_FISICA_DOS", "NOTA_MECANICA", "NOTA_PROCESOSQ", "NOTA_EE_CUATRO", "PROMEDIO_CINCO",
                                    "CAR_CINCO", "NCC_CINCO", "NCA_CINCO", "NCP_CINCO", "NAC_CINCO", "NAA_CINCO", "NAP_CINCO",
                                    "EPA_CINCO", "NOTA_METODOLOGIA", "VECES_METODOLOGIA", "CREDITOS_METODOLOGIA",
                                    "NOTA_FISICA_TRES", "VECES_FISICA_TRES", "CREDITOS_FISICA_TRES", "NOTA_CONTABILIDAD",
                                    "VECES_CONTABILIDAD", "CREDITOS_CONTABILIDAD", "NOTA_PROCESOSM", "VECES_PROCESOSM",
                                    "CREDITOS_PROCESOSM", "NOTA_ADMINISTRACION", "VECES_ADMINISTRACION", "CREDITOS_ADMINISTRACION",
                                    "NOTA_LENGUA_UNO", "VECES_LENGUA_UNO", "CREDITOS_LENGUA_UNO", "NOTA_EI_UNO", "VECES_EI_UNO",
                                    "CREDITOS_EI_UNO", "NOTA_EI_DOS", "VECES_EI_DOS", "CREDITOS_EI_DOS", "RENDIMIENTO_SEIS","PROMEDIO_SEIS"]]

    columnas_nota = [col for col in industrial6.columns if col.startswith('NOTA')]

    industrial6['Promedio_NOTA'] = industrial6[columnas_nota].mean(axis=1)
    industrial6['Promedio_NOTA']
    filas_a_eliminar = industrial6[industrial6['Promedio_NOTA'] < promedio_a_filtrar]

    industrial_filtrado = industrial6.drop(filas_a_eliminar.index)
    industrial_filtrado.drop(columns=['Promedio_NOTA'], inplace=True)
    industrial6 = industrial_filtrado
    industrial6.to_csv("industrial6.csv", sep=';', index=False)

    # Septimo semestre ingeniería industrial
    industrial7 = industrial.loc[:, ["NUMERO", "PROMEDIO_UNO", "PROMEDIO_DOS", "NOTA_MATERIALES", "NOTA_EE_DOS", "PROMEDIO_TRES",
                                    "NOTA_MULTIVARIADO", "NOTA_FISICA_DOS", "NOTA_EE_CUATRO", "PROMEDIO_CINCO", "NOTA_PROCESOSM",
                                    "NOTA_ADMINISTRACION", "NOTA_LENGUA_UNO", "NOTA_EI_UNO", "NOTA_EI_DOS", "PROMEDIO_SEIS",
                                    "CAR_SEIS", "NCC_SEIS", "NCA_SEIS", "NCP_SEIS", "NAC_SEIS", "NAA_SEIS", "NAP_SEIS", "EPA_SEIS",
                                    "NOTA_ECONOMIA_DOS", "VECES_ECONOMIA_DOS", "CREDITOS_ECONOMIA_DOS", "NOTA_PLINEAL", "VECES_PLINEAL",
                                    "CREDITOS_PLINEAL", "NOTA_DERECHO", "VECES_DERECHO", "CREDITOS_DERECHO", "NOTA_IECONOMICA",
                                    "VECES_IECONOMICA", "CREDITOS_IECONOMICA", "NOTA_DISENO", "VECES_DISENO", "CREDITOS_DISENO",
                                    "NOTA_METODOS", "VECES_METODOS", "CREDITOS_METODOS", "NOTA_SEGURIDAD", "VECES_SEGURIDAD",
                                    "CREDITOS_SEGURIDAD", "NOTA_EI_TRES", "VECES_EI_TRES", "CREDITOS_EI_TRES", "RENDIMIENTO_SIETE","PROMEDIO_SIETE"]]

    columnas_nota = [col for col in industrial7.columns if col.startswith('NOTA')]

    industrial7['Promedio_NOTA'] = industrial7[columnas_nota].mean(axis=1)
    industrial7['Promedio_NOTA']
    filas_a_eliminar = industrial7[industrial7['Promedio_NOTA'] < promedio_a_filtrar]

    industrial_filtrado = industrial7.drop(filas_a_eliminar.index)
    industrial_filtrado.drop(columns=['Promedio_NOTA'], inplace=True)
    industrial7 = industrial_filtrado
    industrial7.to_csv("industrial7.csv", sep=';', index=False)

    # Octavo semestre ingeniería industrial
    industrial8 = industrial.loc[:, ["NUMERO", "PROMEDIO_UNO", "PROMEDIO_DOS", "NOTA_EE_DOS", "PROMEDIO_TRES", "NOTA_MULTIVARIADO",
                                    "NOTA_FISICA_DOS", "NOTA_EE_CUATRO", "PROMEDIO_CINCO", "NOTA_PROCESOSM", "NOTA_ADMINISTRACION",
                                    "NOTA_LENGUA_UNO", "NOTA_EI_UNO", "NOTA_EI_DOS", "PROMEDIO_SEIS", "NAC_SEIS", "NOTA_PLINEAL",
                                    "NOTA_IECONOMICA", "NOTA_DISENO", "NOTA_METODOS", "NOTA_EI_TRES", "PROMEDIO_SIETE", "CAR_SIETE",
                                    "NCC_SIETE", "NCA_SIETE", "NCP_SIETE", "NAC_SIETE", "NAA_SIETE", "NAP_SIETE", "EPA_SIETE",
                                    "NOTA_EMPRENDIMIENTO", "VECES_EMPRENDIMIENTO", "CREDITOS_EMPRENDIMIENTO", "NOTA_GRAFOS",
                                    "VECES_GRAFOS", "CREDITOS_GRAFOS", "NOTA_CALIDAD_UNO", "VECES_CALIDAD_UNO", "CREDITOS_CALIDAD_UNO",
                                    "NOTA_MERCADOTECNIA", "VECES_MERCADOTECNIA", "CREDITOS_MERCADOTECNIA", "NOTA_ERGONOMIA",
                                    "VECES_ERGONOMIA", "CREDITOS_ERGONOMIA", "NOTA_HOMBRE", "VECES_HOMBRE", "CREDITOS_HOMBRE",
                                    "NOTA_EI_CUATRO", "VECES_EI_CUATRO", "CREDITOS_EI_CUATRO", "NOTA_EI_CINCO", "VECES_EI_CINCO",
                                    "CREDITOS_EI_CINCO", "RENDIMIENTO_OCHO","PROMEDIO_OCHO"]]

    columnas_nota = [col for col in industrial8.columns if col.startswith('NOTA')]

    industrial8['Promedio_NOTA'] = industrial8[columnas_nota].mean(axis=1)
    industrial8['Promedio_NOTA']
    filas_a_eliminar = industrial8[industrial8['Promedio_NOTA'] < promedio_a_filtrar]

    industrial_filtrado = industrial8.drop(filas_a_eliminar.index)
    industrial_filtrado.drop(columns=['Promedio_NOTA'], inplace=True)
    industrial8 = industrial_filtrado
    industrial8.to_csv("industrial8.csv", sep=';', index=False)

    # Noveno semestre ingeniería industrial
    industrial9 = industrial.loc[:, ["NUMERO", "PROMEDIO_DOS", "NOTA_EE_CUATRO", "PROMEDIO_CINCO", "NOTA_LENGUA_UNO", "PROMEDIO_SEIS",
                                    "NOTA_IECONOMICA", "PROMEDIO_SIETE", "NAA_SIETE", "NOTA_GRAFOS", "NOTA_CALIDAD_UNO", "NOTA_ERGONOMIA",
                                    "NOTA_EI_CINCO", "PROMEDIO_OCHO", "CAR_OCHO", "NCC_OCHO", "NCA_OCHO", "NCP_OCHO", "NAC_OCHO", "NAA_OCHO",
                                    "NAP_OCHO", "EPA_OCHO", "NOTA_LOG_UNO", "VECES_LOG_UNO", "CREDITOS_LOG_UNO", "NOTA_GOPERACIONES",
                                    "VECES_GOPERACIONES", "CREDITOS_GOPERACIONES", "NOTA_CALIDAD_DOS", "VECES_CALIDAD_DOS", "CREDITOS_CALIDAD_DOS",
                                    "NOTA_GAMBIENTAL", "VECES_GAMBIENTAL", "CREDITOS_GAMBIENTAL", "NOTA_LENGUA_DOS", "VECES_LENGUA_DOS",
                                    "CREDITOS_LENGUA_DOS", "NOTA_CONTEXTO", "VECES_CONTEXTO", "CREDITOS_CONTEXTO", "NOTA_EI_SEIS", "VECES_EI_SEIS",
                                    "CREDITOS_EI_SEIS", "NOTA_EI_SIETE", "VECES_EI_SIETE", "CREDITOS_EI_SIETE", "RENDIMIENTO_NUEVE","PROMEDIO_NUEVE"]]

    columnas_nota = [col for col in industrial9.columns if col.startswith('NOTA')]

    industrial9['Promedio_NOTA'] = industrial9[columnas_nota].mean(axis=1)
    industrial9['Promedio_NOTA']
    filas_a_eliminar = industrial9[industrial9['Promedio_NOTA'] < promedio_a_filtrar]

    industrial_filtrado = industrial9.drop(filas_a_eliminar.index)
    industrial_filtrado.drop(columns=['Promedio_NOTA'], inplace=True)
    industrial9 = industrial_filtrado
    industrial9.to_csv("industrial9.csv", sep=';', index=False)

    # Decimo semestre ingeniería industrial
    industrial10 = industrial.loc[:, ["NUMERO", "PROMEDIO_CINCO", "PROMEDIO_SEIS", "NOTA_IECONOMICA", "PROMEDIO_SIETE", "NOTA_GRAFOS",
                                    "PROMEDIO_OCHO", "NCC_OCHO", "NOTA_LOG_UNO", "NOTA_CALIDAD_DOS", "NOTA_LENGUA_DOS", "PROMEDIO_NUEVE",
                                    "CAR_NUEVE", "NCC_NUEVE", "NCA_NUEVE", "NCP_NUEVE", "NAC_NUEVE", "NAA_NUEVE", "NAP_NUEVE", "EPA_NUEVE",
                                    "NOTA_GRADO_UNO", "VECES_GRADO_UNO", "CREDITOS_GRADO_UNO", "NOTA_LOG_DOS", "VECES_LOG_DOS", "CREDITOS_LOG_DOS",
                                    "NOTA_DECISION", "VECES_DECISION", "CREDITOS_DECISION", "NOTA_PRODUCCION", "VECES_PRODUCCION",
                                    "CREDITOS_PRODUCCION", "NOTA_FINANZAS", "VECES_FINANZAS", "CREDITOS_FINANZAS", "NOTA_GIT", "VECES_GIT",
                                    "CREDITOS_GIT", "NOTA_GTH", "VECES_GTH", "CREDITOS_GTH", "NOTA_HISTORIA", "VECES_HISTORIA","CREDITOS_HISTORIA", "RENDIMIENTO_DIEZ"
                                    ,"PROMEDIO_DIEZ"]]

    columnas_nota = [col for col in industrial10.columns if col.startswith('NOTA')]

    industrial10['Promedio_NOTA'] = industrial10[columnas_nota].mean(axis=1)
    industrial10['Promedio_NOTA']
    filas_a_eliminar = industrial10[industrial10['Promedio_NOTA'] < promedio_a_filtrar]

    industrial_filtrado = industrial10.drop(filas_a_eliminar.index)
    industrial_filtrado.drop(columns=['Promedio_NOTA'], inplace=True)
    industrial10 = industrial_filtrado
    industrial10.to_csv("industrial10.csv", sep=';', index=False)

 # Guardar resultados
    resultado_path = "backup-industrial.csv"
    industrial.to_csv(resultado_path, sep=';', index=False)    
    return resultado_path

@app.post("/procesar_archivos/")
async def procesar_archivos_endpoint(archivo_base: UploadFile = File(...)):
    archivo_base_path = 'temp_archivo_base.csv'
    #archivo_municipios_path = 'temp_archivo_municipios.csv'
    
    with open(archivo_base_path, "wb") as f:
        f.write(archivo_base.file.read())
    
    #with open(archivo_municipios_path, "wb") as f:
    #    f.write(archivo_municipios.file.read())
    
    resultado_path = procesar_archivos(archivo_base_path)
    
    # Eliminar archivos temporales
    os.remove(archivo_base_path)
    #os.remove(archivo_municipios_path)
    
    return FileResponse(resultado_path, media_type='text/csv', filename="backup-industrial.csv")