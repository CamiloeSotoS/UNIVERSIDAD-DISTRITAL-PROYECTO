import pandas as pd
import numpy as np
import glob
import csv
import os



#electrica = pd.read_csv(archivo_base_path, sep=',')
#municipios = pd.read_csv(archivo_municipios_path, sep=',')

#merged_df = pd.merge(electrica, municipios, on='MUNICIPIO')
#merged_df = merged_df.drop(columns=['MUNICIPIO'])
#merged_df = merged_df.rename(columns={'NUM_MUNI': 'MUNICIPIO'})
#electrica = merged_df

ruta_archivo = 'C:/Users/User/Desktop/udistrital/electrica_sin_variables.csv'
electrica = pd.read_csv(ruta_archivo, sep=',')

#ruta_archivo_2 = 'C:/Users/User/Desktop/udistrital/municipios_ud.csv'
#municipios = pd.read_csv(ruta_archivo_2, sep=',')


#electrica['DISTANCIA'] = np.where(((electrica['LOCALIDAD'] == 'TEUSAQUILLO') | (electrica['LOCALIDAD'] == 'CHAPINERO') | (electrica['LOCALIDAD'] == 'SANTA FE')) , '1' , np.nan)
#electrica['DISTANCIA'] = np.where(((electrica['LOCALIDAD'] == 'LOS MARTIRES')|(electrica['LOCALIDAD'] == 'LA CANDELARIA')|(electrica['LOCALIDAD'] == 'PUENTE ARANDA')), '2' , electrica['DISTANCIA'])
#electrica['DISTANCIA'] = np.where(((electrica['LOCALIDAD'] == 'BARRIOS UNIDOS')|(electrica['LOCALIDAD'] == 'RAFAEL URIBE URIBE')|(electrica['LOCALIDAD'] == 'ANTONIO NARINO')|(electrica['LOCALIDAD'] == 'ENGATIVA')|(electrica['LOCALIDAD'] == 'KENNEDY')), '3' , electrica['DISTANCIA'])
#electrica['DISTANCIA'] = np.where(((electrica['LOCALIDAD'] == 'FONTIBON')|(electrica['LOCALIDAD'] == 'SAN CRISTOBAL')), '4' , electrica['DISTANCIA'])
#electrica['DISTANCIA'] = np.where(((electrica['LOCALIDAD'] == 'USAQUEN')|(electrica['LOCALIDAD'] == 'BOSA')|(electrica['LOCALIDAD'] == 'SUBA')|(electrica['LOCALIDAD'] == 'TUNJUELITO')|(electrica['LOCALIDAD'] == 'CIUDAD BOLIVAR')), '5' , electrica['DISTANCIA'])
#electrica['DISTANCIA'] = np.where(((electrica['LOCALIDAD'] == 'USME')|(electrica['LOCALIDAD'] == 'FUERA DE BOGOTA')|(electrica['LOCALIDAD'] == 'SOACHA')|(electrica['LOCALIDAD'] == 'SUMAPAZ')), '6' , electrica['DISTANCIA'])
#electrica['DISTANCIA'] = np.where(((electrica['LOCALIDAD'] == 'NO REGISTRA')|(electrica['LOCALIDAD'] == 'SIN LOCALIDAD')), '7' , electrica['DISTANCIA'])

electrica['GENERO'] = electrica['GENERO'].replace({'MASCULINO': 0, 'FEMENINO': 1})
electrica['TIPO_COLEGIO'] = electrica['TIPO_COLEGIO'].replace({'NO REGISTRA': 0, 'OFICIAL': 1, 'NO OFICIAL':2})
electrica['LOCALIDAD_COLEGIO'] = electrica['LOCALIDAD_COLEGIO'].replace({'NO REGISTRA': 0, 'USAQUEN': 1, 'CHAPINERO': 2, 'SANTAFE': 3, 'SANTA FE': 3, 'SAN CRISTOBAL': 4, 'USME': 5, 'TUNJUELITO': 6, 'BOSA': 7, 'KENNEDY': 8, 'FONTIBON': 9, 'ENGATIVA': 10, 'SUBA': 11, 'BARRIOS UNIDOS': 12, 'TEUSAQUILLO': 13, 'LOS MARTIRES': 14, 'ANTONIO NARINO': 15, 'PUENTE ARANDA': 16, 'LA CANDELARIA': 17, 'RAFAEL URIBE URIBE': 18, 'RAFAEL URIBE': 18, 'CIUDAD BOLIVAR': 19, 'FUERA DE BOGOTA': 20, 'SIN LOCALIDAD': 21, 'SOACHA':20})
electrica['CALENDARIO'] = electrica['CALENDARIO'].replace({'NO REGISTRA': 0,'O': 0, 'A': 1, 'B': 2, 'F': 3})
electrica['DEPARTAMENTO'] = electrica['DEPARTAMENTO'].replace({'NO REGISTRA': 0, 'AMAZONAS': 1, 'ANTIOQUIA': 2,'ARAUCA': 3, 'ATLANTICO': 4, 'BOGOTA': 5, 'BOLIVAR': 6, 'BOYACA': 7, 'CALDAS': 8, 'CAQUETA': 9, 'CASANARE': 10, 'CAUCA': 11, 'CESAR': 12, 'CHOCO': 13, 'CORDOBA': 14, 'CUNDINAMARCA': 15, 'GUAINIA': 16, 'GUAVIARE': 17, 'HUILA': 18, 'LA GUAJIRA': 19, 'MAGDALENA':20, 'META': 21, 'NARINO': 22, 'NORTE SANTANDER': 23, 'PUTUMAYO': 24, 'QUINDIO': 25, 'RISARALDA': 26, 'SAN ANDRES Y PROVIDENCIA': 27, 'SANTANDER': 28, 'SUCRE': 29, 'TOLIMA': 30, 'VALLE': 31, 'VAUPES': 32, 'VICHADA': 33})
electrica['LOCALIDAD'] = electrica['LOCALIDAD'].replace({'NO REGISTRA': 0, 'USAQUEN': 1, 'CHAPINERO': 2, 'SANTA FE': 3, 'SAN CRISTOBAL': 4, 'USME': 5, 'TUNJUELITO': 6, 'BOSA': 7, 'KENNEDY': 8, 'FONTIBON': 9, 'ENGATIVA': 10, 'SUBA': 11, 'BARRIOS UNIDOS': 12, 'TEUSAQUILLO': 13, 'LOS MARTIRES': 14, 'ANTONIO NARINO': 15, 'PUENTE ARANDA': 16, 'LA CANDELARIA': 17, 'RAFAEL URIBE URIBE': 18, 'CIUDAD BOLIVAR': 19, 'FUERA DE BOGOTA': 20, 'SIN LOCALIDAD': 20, 'SOACHA': 20, 'SUMAPAZ': 20})
electrica['INSCRIPCION'] = electrica['INSCRIPCION'].replace({'NO REGISTRA': 0, 'BENEFICIARIOS LEY 1081 DE 2006': 1, 'BENEFICIARIOS LEY 1084 DE 2006': 2, 'CONVENIO ANDRES BELLO': 3, 'DESPLAZADOS': 4, 'INDIGENAS': 5, 'MEJORES BACHILLERES COL. DISTRITAL OFICIAL': 6, 'MINORIAS ETNICAS Y CULTURALES': 7, 'MOVILIDAD ACADEMICA INTERNACIONAL': 8, 'NORMAL': 9, 'TRANSFERENCIA EXTERNA': 10, 'TRANSFERENCIA INTERNA': 11,})
electrica['ESTADO_FINAL'] = electrica['ESTADO_FINAL'].replace({'ABANDONO': 1, 'ACTIVO': 2, 'APLAZO': 3, 'CANCELADO': 4, 'EGRESADO': 5, 'INACTIVO': 6, 'MOVILIDAD': 7, 'N.A.': 8, 'NO ESTUDIANTE AC004': 9, 'NO SUP. PRUEBA ACAD.': 10, 'PRUEBA AC Y ACTIVO': 11, 'PRUEBA ACAD': 12, 'RETIRADO': 13, 'TERMINO MATERIAS': 14, 'TERMINO Y MATRICULO': 15, 'VACACIONES': 16})
electrica['MUNICIPIO'] = electrica['MUNICIPIO'].replace({"NO REGISTRA": 0, "ACACIAS": 1, "AGUACHICA": 2, "AGUAZUL": 3, "ALBAN": 4, "ALBAN (SAN JOSE)": 5, "ALVARADO": 6, "ANAPOIMA": 7, "ANOLAIMA": 8, "APARTADO": 9, "ARAUCA": 10, "ARBELAEZ": 11, "ARMENIA": 12, "ATACO": 13, "BARRANCABERMEJA": 14, "BARRANQUILLA": 15, "BELEN DE LOS ANDAQUIES": 16, "BOAVITA": 17, "BOGOTA": 18, "BOJACA": 19, "BOLIVAR": 20, "BUCARAMANGA": 21, "BUENAVENTURA": 22, "CABUYARO": 23, "CACHIPAY": 24, "CAICEDONIA": 25, "CAJAMARCA": 26, "CAJICA": 27, "CALAMAR": 28, "CALARCA": 29, "CALI": 30, "CAMPOALEGRE": 31, "CAPARRAPI": 32, "CAQUEZA": 33, "CARTAGENA": 34, "CASTILLA LA NUEVA": 35, "CERETE": 36, "CHAPARRAL": 37, "CHARALA": 38, "CHIA": 39, "CHIPAQUE": 40, "CHIQUINQUIRA": 41, "CHOACHI": 42, "CHOCONTA": 43, "CIENAGA": 44, "CIRCASIA": 45, "COGUA": 46, "CONTRATACION": 47, "COTA": 48, "CUCUTA": 49, "CUMARAL": 50, "CUMBAL": 51, "CURITI": 52, "CURUMANI": 53, "DUITAMA": 54, "EL BANCO": 55, "EL CARMEN DE BOLIVAR": 56, "EL COLEGIO": 57, "EL CHARCO": 58, "EL DORADO": 59, "EL PASO": 60, "EL ROSAL": 61, "ESPINAL": 62, "FACATATIVA": 63, "FLORENCIA": 64, "FLORIDABLANCA": 65, "FOMEQUE": 66, "FONSECA": 67, "FORTUL": 68, "FOSCA": 69, "FUNZA": 70, "FUSAGASUGA": 71, "GACHETA": 72, "GALERAS (NUEVA GRANADA)": 73, "GAMA": 74, "GARAGOA": 75, "GARZON": 76, "GIGANTE": 77, "GIRARDOT": 78, "GRANADA": 79, "GUACHUCAL": 80, "GUADUAS": 81, "GUAITARILLA": 82, "GUAMO": 83, "GUASCA": 84, "GUATEQUE": 85, "GUAYATA": 86, "GUTIERREZ": 87, "IBAGUE": 88, "INIRIDA": 89, "INZA": 90, "IPIALES": 91, "ITSMINA": 92, "JENESANO": 93, "LA CALERA": 94, "LA DORADA": 95, "LA MESA": 96, "LA PLATA": 97, "LA UVITA": 98, "LA VEGA": 99, "LIBANO": 100, "LOS PATIOS": 101, "MACANAL": 102, "MACHETA": 103, "MADRID": 104, "MAICAO": 105, "MALAGA": 106, "MANAURE BALCON DEL 12": 107, "MANIZALES": 108, "MARIQUITA": 109, "MEDELLIN": 110, "MEDINA": 111, "MELGAR": 112, "MITU": 113, "MOCOA": 114, "MONTERIA": 115, "MONTERREY": 116, "MOSQUERA": 117, "NATAGAIMA": 118, "NEIVA": 119, "NEMOCON": 120, "OCANA": 121, "ORITO": 122, "ORTEGA": 123, "PACHO": 124, "PAEZ (BELALCAZAR)": 125, "PAICOL": 126, "PAILITAS": 127, "PAIPA": 128, "PALERMO": 129, "PALMIRA": 130, "PAMPLONA": 131, "PANDI": 132, "PASCA": 133, "PASTO": 134, "PAZ DE ARIPORO": 135, "PAZ DE RIO": 136, "PITALITO": 137, "POPAYAN": 138, "PUENTE NACIONAL": 139, "PUERTO ASIS": 140, "PUERTO BOYACA": 141, "PUERTO LOPEZ": 142, "PUERTO SALGAR": 143, "PURIFICACION": 144, "QUETAME": 145, "QUIBDO": 146, "RAMIRIQUI": 147, "RICAURTE": 148, "RIOHACHA": 149, "RIVERA": 150, "SABOYA": 151, "SAHAGUN": 152, "SALDAÑA": 153, "SAMACA": 154, "SAMANA": 155, "SAN AGUSTIN": 156, "SAN ANDRES": 157, "SAN BERNARDO": 158, "SAN EDUARDO": 159, "SAN FRANCISCO": 160, "SAN GIL": 161, "SAN JOSE DEL FRAGUA": 162, "SAN JOSE DEL GUAVIARE": 163, "SAN LUIS DE PALENQUE": 164, "SAN MARCOS": 165, "SAN MARTIN": 166, "SANDONA": 167, "SAN VICENTE DEL CAGUAN": 168, "SANTA MARTA": 169, "SANTA SOFIA": 170, "SESQUILE": 171, "SIBATE": 172, "SIBUNDOY": 173, "SILVANIA": 174, "SIMIJACA": 175, "SINCE": 176, "SINCELEJO": 177, "SOACHA": 178, "SOATA": 179, "SOCORRO": 180, "SOGAMOSO": 181, "SOLEDAD": 182, "SOPO": 183, "SORACA": 184, "SOTAQUIRA": 185, "SUAITA": 186, "SUBACHOQUE": 187, "SUESCA": 188, "SUPATA": 189, "SUTAMARCHAN": 190, "SUTATAUSA": 191, "TABIO": 192, "TAMESIS": 193, "TARQUI": 194, "TAUSA": 195, "TENA": 196, "TENJO": 197, "TESALIA": 198, "TIBANA": 199, "TIMANA": 200, "TOCANCIPA": 201, "TUBARA": 202, "TULUA": 203, "TUMACO": 204, "TUNJA": 205, "TURBACO": 206, "TURMEQUE": 207, "UBATE": 208, "UMBITA": 209, "UNE": 210, "VALLEDUPAR": 211, "VELEZ": 212, "VENADILLO": 213, "VENECIA (OSPINA PEREZ)": 214, "VILLA DE LEYVA": 215, "VILLAHERMOSA": 216, "VILLANUEVA": 217, "VILLAPINZON": 218, "VILLAVICENCIO": 219, "VILLETA": 220, "YACOPI": 221, "YOPAL": 222, "ZIPACON": 223, "ZIPAQUIRA": 224})

electrica = electrica.apply(pd.to_numeric)

# Recorrer todas las columnas que comienzan con "CREDITOS_"
for columna in electrica.columns:
    if columna.startswith('CREDITOS_'):
        # Obtener el valor distinto de cero en la columna
        otro_valor = electrica.loc[electrica[columna] != 0, columna].iloc[0]
        # Reemplazar ceros por el otro valor
        electrica[columna] = electrica[columna].replace(0, otro_valor)



"""#PRIMER SEMESTRE electrica"""

# Lista para variables de NOTA
NOTAS_electrica_UNO = ['NOTA_DIF', 'NOTA_FIS_UNO', 'NOTA_CFJC', 'NOTA_TEXTOS', 'NOTA_SEM', 'NOTA_PROGB', 'NOTA_ALGEBRA']

VECES_electrica_UNO = ['VECES_DIF', 'VECES_FIS_UNO', 'VECES_CFJC', 'VECES_TEXTOS', 'VECES_SEM', 'VECES_PROGB', 'VECES_ALGEBRA']

CREDITOS_electrica_UNO = ['CREDITOS_DIF', 'CREDITOS_FIS_UNO', 'CREDITOS_CFJC', 'CREDITOS_TEXTOS', 'CREDITOS_SEM', 'CREDITOS_PROGB', 'CREDITOS_ALGEBRA']

promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in electrica.iterrows():
    notas_estudiante = []
    creditos_estudiante = []

    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_electrica_UNO, VECES_electrica_UNO, CREDITOS_electrica_UNO):
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
electrica['PROMEDIO_UNO'] = promedios_semestre

# Calcular métricas por semestre
electrica['CAR_UNO'] = electrica[VECES_electrica_UNO].apply(lambda x: (x > 1).sum(), axis=1)
electrica['NAC_UNO'] = electrica[VECES_electrica_UNO].apply(lambda x: (x > 0).sum(), axis=1)
electrica['NAA_UNO'] = electrica[NOTAS_electrica_UNO].apply(lambda x: (x >= 30).sum(), axis=1)
electrica['NAP_UNO'] = electrica['NAC_UNO'] - electrica['NAA_UNO']
electrica['EPA_UNO'] = electrica.apply(lambda row: 1 if row['PROMEDIO_UNO'] < 30 or row['NAP_UNO'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_electrica_UNO, CREDITOS_electrica_UNO):
        if row[veces_col] > 0:
            creditos_cursados += row[creditos_col]
    return creditos_cursados

electrica['NCC_UNO'] = electrica.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_electrica_UNO, CREDITOS_electrica_UNO):
        if row[nota_col] >= 30:
            creditos_aprobados += row[creditos_col]
    return creditos_aprobados

electrica['NCA_UNO'] = electrica.apply(calcular_creditos_aprobados, axis=1)


# Construir NCP

electrica['NCP_UNO'] = electrica['NCC_UNO'] - electrica['NCA_UNO']

# Rendimiento UNO
conditions = [(electrica['PROMEDIO_UNO'] >= 0) & (electrica['PROMEDIO_UNO'] < 30),
(electrica['PROMEDIO_UNO'] >= 30) & (electrica['PROMEDIO_UNO'] < 40),
(electrica['PROMEDIO_UNO'] >= 40) & (electrica['PROMEDIO_UNO'] < 45),
(electrica['PROMEDIO_UNO'] >= 45) & (electrica['PROMEDIO_UNO'] < 50)]
values = [1, 2, 3, 4]
electrica['RENDIMIENTO_UNO'] = pd.Series(pd.cut(electrica['PROMEDIO_UNO'], bins=[0, 30, 40, 45, 50], labels=values))

"""# SEGUNDO SEMRESTRE electrica"""

NOTAS_electrica_DOS = ['NOTA_INT', 'NOTA_DEM', 'NOTA_POO', 'NOTA_FIS_DOS', 'NOTA_CIR_UNO', 'NOTA_EYB', 'NOTA_HCI']

VECES_electrica_DOS = ['VECES_INT', 'VECES_DEM', 'VECES_POO', 'VECES_FIS_DOS', 'VECES_CIR_UNO', 'VECES_EYB', 'VECES_HCI']

CREDITOS_electrica_DOS = ['CREDITOS_INT', 'CREDITOS_DEM', 'CREDITOS_POO', 'CREDITOS_FIS_DOS', 'CREDITOS_CIR_UNO', 'CREDITOS_EYB', 'CREDITOS_HCI']

promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in electrica.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_electrica_DOS, VECES_electrica_DOS, CREDITOS_electrica_DOS):
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
electrica['PROMEDIO_DOS'] = promedios_semestre

# Calcular métricas por semestre
electrica['CAR_DOS'] = electrica[VECES_electrica_DOS].apply(lambda x: (x > 1).sum(), axis=1)
electrica['NAC_DOS'] = electrica[VECES_electrica_DOS].apply(lambda x: (x > 0).sum(), axis=1)
electrica['NAA_DOS'] = electrica[NOTAS_electrica_DOS].apply(lambda x: (x >= 30).sum(), axis=1)
electrica['NAP_DOS'] = electrica['NAC_DOS'] - electrica['NAA_DOS']
electrica['EPA_DOS'] = electrica.apply(lambda row: 1 if row['PROMEDIO_DOS'] < 30 or row['NAP_DOS'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_electrica_DOS, CREDITOS_electrica_DOS):
        if row[veces_col] > 0:
            creditos_cursados += row[creditos_col]
    return creditos_cursados

electrica['NCC_DOS'] = electrica.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_electrica_DOS, CREDITOS_electrica_DOS):
        if row[nota_col] >= 30:
            creditos_aprobados += row[creditos_col]
    return creditos_aprobados

electrica['NCA_DOS'] = electrica.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

electrica['NCP_DOS'] = electrica['NCC_DOS'] - electrica['NCA_DOS']

# Rendimiento DOS
conditions = [(electrica['PROMEDIO_DOS'] >= 0) & (electrica['PROMEDIO_DOS'] < 30),
(electrica['PROMEDIO_DOS'] >= 30) & (electrica['PROMEDIO_DOS'] < 40),
(electrica['PROMEDIO_DOS'] >= 40) & (electrica['PROMEDIO_DOS'] < 45),
(electrica['PROMEDIO_DOS'] >= 45) & (electrica['PROMEDIO_DOS'] < 50)]
values = [1, 2, 3, 4]
electrica['RENDIMIENTO_DOS'] = pd.Series(pd.cut(electrica['PROMEDIO_DOS'], bins=[0, 30, 40, 45, 50], labels=values))

"""# TERCER SEMESTRE electrica"""

NOTAS_electrica_TRES = ['NOTA_MULTI', 'NOTA_CIR_DOS', 'NOTA_FIS_TRES', 'NOTA_ECUA', 'NOTA_EL_UNO', 'NOTA_TERMO']

VECES_electrica_TRES = ['VECES_MULTI', 'VECES_CIR_DOS', 'VECES_FIS_TRES', 'VECES_ECUA', 'VECES_EL_UNO', 'VECES_TERMO']

CREDITOS_electrica_TRES = ['CREDITOS_MULTI', 'CREDITOS_CIR_DOS', 'CREDITOS_FIS_TRES', 'CREDITOS_ECUA', 'CREDITOS_EL_UNO', 'CREDITOS_TERMO']

promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in electrica.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_electrica_TRES, VECES_electrica_TRES, CREDITOS_electrica_TRES):
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
electrica['PROMEDIO_TRES'] = promedios_semestre

# Calcular métricas por semestre
electrica['CAR_TRES'] = electrica[VECES_electrica_TRES].apply(lambda x: (x > 1).sum(), axis=1)
electrica['NAC_TRES'] = electrica[VECES_electrica_TRES].apply(lambda x: (x > 0).sum(), axis=1)
electrica['NAA_TRES'] = electrica[NOTAS_electrica_TRES].apply(lambda x: (x >= 30).sum(), axis=1)
electrica['NAP_TRES'] = electrica['NAC_TRES'] - electrica['NAA_TRES']
electrica['EPA_TRES'] = electrica.apply(lambda row: 1 if row['PROMEDIO_TRES'] < 30 or row['NAP_TRES'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_electrica_TRES, CREDITOS_electrica_TRES):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados
electrica['NCC_TRES'] = electrica.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_electrica_TRES, CREDITOS_electrica_TRES):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados
electrica['NCA_TRES'] = electrica.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

electrica['NCP_TRES'] = electrica['NCC_TRES'] - electrica['NCA_TRES']

# Rendimiento TRES
conditions = [(electrica['PROMEDIO_TRES'] >= 0) & (electrica['PROMEDIO_TRES'] < 30),
(electrica['PROMEDIO_TRES'] >= 30) & (electrica['PROMEDIO_TRES'] < 40),
(electrica['PROMEDIO_TRES'] >= 40) & (electrica['PROMEDIO_TRES'] < 45),
(electrica['PROMEDIO_TRES'] >= 45) & (electrica['PROMEDIO_TRES'] < 50)]
values = [1, 2, 3, 4]
electrica['RENDIMIENTO_TRES'] = pd.Series(pd.cut(electrica['PROMEDIO_TRES'], bins=[0, 30, 40, 45, 50], labels=values))

"""# CUARTO SEMESTRE electrica"""

NOTAS_electrica_CUATRO = ['NOTA_MPI', 'NOTA_PYE', 'NOTA_ELD', 'NOTA_EL_DOS', 'NOTA_CIR_TRES', 'NOTA_GEE', 'NOTA_ME']

VECES_electrica_CUATRO = ['VECES_MPI', 'VECES_PYE', 'VECES_ELD', 'VECES_EL_DOS', 'VECES_CIR_TRES', 'VECES_GEE', 'VECES_ME']

CREDITOS_electrica_CUATRO = ['CREDITOS_MPI', 'CREDITOS_PYE', 'CREDITOS_ELD', 'CREDITOS_EL_DOS', 'CREDITOS_CIR_TRES', 'CREDITOS_GEE', 'CREDITOS_ME']


promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in electrica.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_electrica_CUATRO, VECES_electrica_CUATRO, CREDITOS_electrica_CUATRO):
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
electrica['PROMEDIO_CUATRO'] = promedios_semestre

# Calcular métricas por semestre
electrica['CAR_CUATRO'] = electrica[VECES_electrica_CUATRO].apply(lambda x: (x > 1).sum(), axis=1)
electrica['NAC_CUATRO'] = electrica[VECES_electrica_CUATRO].apply(lambda x: (x > 0).sum(), axis=1)
electrica['NAA_CUATRO'] = electrica[NOTAS_electrica_CUATRO].apply(lambda x: (x >= 30).sum(), axis=1)
electrica['NAP_CUATRO'] = electrica['NAC_CUATRO'] - electrica['NAA_CUATRO']
electrica['EPA_CUATRO'] = electrica.apply(lambda row: 1 if row['PROMEDIO_CUATRO'] < 30 or row['NAP_CUATRO'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_electrica_CUATRO, CREDITOS_electrica_CUATRO):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados
electrica['NCC_CUATRO'] = electrica.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_electrica_CUATRO, CREDITOS_electrica_CUATRO):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados
electrica['NCA_CUATRO'] = electrica.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

electrica['NCP_CUATRO'] = electrica['NCC_CUATRO'] - electrica['NCA_CUATRO']

# Rendimiento CUATRO
conditions = [(electrica['PROMEDIO_CUATRO'] >= 0) & (electrica['PROMEDIO_CUATRO'] < 30),
(electrica['PROMEDIO_CUATRO'] >= 30) & (electrica['PROMEDIO_CUATRO'] < 40),
(electrica['PROMEDIO_CUATRO'] >= 40) & (electrica['PROMEDIO_CUATRO'] < 45),
(electrica['PROMEDIO_CUATRO'] >= 45) & (electrica['PROMEDIO_CUATRO'] < 50)]
values = [1, 2, 3, 4]
electrica['RENDIMIENTO_CUATRO'] = pd.Series(pd.cut(electrica['PROMEDIO_CUATRO'], bins=[0, 30, 40, 45, 50], labels=values))

"""# QUINTO SEMESTRE electrica"""

# Lista electrica quinto semestre

NOTAS_electrica_CINCO = ['NOTA_EE_UNO', 'NOTA_IYM', 'NOTA_ASD', 'NOTA_CEM', 'NOTA_INSE', 'NOTA_GENH', 'NOTA_IO_UNO']

VECES_electrica_CINCO = ['VECES_EE_UNO', 'VECES_IYM', 'VECES_ASD', 'VECES_CEM', 'VECES_INSE', 'VECES_GENH', 'VECES_IO_UNO']

CREDITOS_electrica_CINCO = ['CREDITOS_EE_UNO', 'CREDITOS_IYM', 'CREDITOS_ASD', 'CREDITOS_CEM', 'CREDITOS_INSE', 'CREDITOS_GENH', 'CREDITOS_IO_UNO']

promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in electrica.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_electrica_CINCO, VECES_electrica_CINCO, CREDITOS_electrica_CINCO):
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
electrica['PROMEDIO_CINCO'] = promedios_semestre

# Calcular métricas por semestre
electrica['CAR_CINCO'] = electrica[VECES_electrica_CINCO].apply(lambda x: (x > 1).sum(), axis=1)
electrica['NAC_CINCO'] = electrica[VECES_electrica_CINCO].apply(lambda x: (x > 0).sum(), axis=1)
electrica['NAA_CINCO'] = electrica[NOTAS_electrica_CINCO].apply(lambda x: (x >= 30).sum(), axis=1)
electrica['NAP_CINCO'] = electrica['NAC_CINCO'] - electrica['NAA_CINCO']
electrica['EPA_CINCO'] = electrica.apply(lambda row: 1 if row['PROMEDIO_CINCO'] < 30 or row['NAP_CINCO'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_electrica_CINCO, CREDITOS_electrica_CINCO):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados
electrica['NCC_CINCO'] = electrica.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_electrica_CINCO, CREDITOS_electrica_CINCO):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados
electrica['NCA_CINCO'] = electrica.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

electrica['NCP_CINCO'] = electrica['NCC_CINCO'] - electrica['NCA_CINCO']

# Rendimiento CINCO
conditions = [(electrica['PROMEDIO_CINCO'] >= 0) & (electrica['PROMEDIO_CINCO'] < 30),
(electrica['PROMEDIO_CINCO'] >= 30) & (electrica['PROMEDIO_CINCO'] < 40),
(electrica['PROMEDIO_CINCO'] >= 40) & (electrica['PROMEDIO_CINCO'] < 45),
(electrica['PROMEDIO_CINCO'] >= 45) & (electrica['PROMEDIO_CINCO'] < 50)]
values = [1, 2, 3, 4]
electrica['RENDIMIENTO_CINCO'] = pd.Series(pd.cut(electrica['PROMEDIO_CINCO'], bins=[0, 30, 40, 45, 50], labels=values))

"""# SEXTO SEMESTRE electrica"""

NOTAS_electrica_SEIS = ['NOTA_INGECO', 'NOTA_DDP', 'NOTA_IO_DOS', 'NOTA_CONEM', 'NOTA_TDE', 'NOTAS_RDC', 'NOTA_CTRL']

VECES_electrica_SEIS = ['VECES_INGECO', 'VECES_DDP', 'VECES_IO_DOS', 'VECES_CONEM', 'VECES_TDE', 'VECES_RDC', 'VECES_CTRL']

CREDITOS_electrica_SEIS = ['CREDITOS_INGECO', 'CREDITOS_DDP', 'CREDITOS_IO_DOS', 'CREDITOS_CONEM', 'CREDITOS_TDE', 'CREDITOS_RDC', 'CREDITOS_CTRL']


promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in electrica.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_electrica_SEIS, VECES_electrica_SEIS, CREDITOS_electrica_SEIS):
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
electrica['PROMEDIO_SEIS'] = promedios_semestre

# Calcular métricas por semestre
electrica['CAR_SEIS'] = electrica[VECES_electrica_SEIS].apply(lambda x: (x > 1).sum(), axis=1)
electrica['NAC_SEIS'] = electrica[VECES_electrica_SEIS].apply(lambda x: (x > 0).sum(), axis=1)
electrica['NAA_SEIS'] = electrica[NOTAS_electrica_SEIS].apply(lambda x: (x >= 30).sum(), axis=1)
electrica['NAP_SEIS'] = electrica['NAC_SEIS'] - electrica['NAA_SEIS']
electrica['EPA_SEIS'] = electrica.apply(lambda row: 1 if row['PROMEDIO_SEIS'] < 30 or row['NAP_SEIS'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_electrica_SEIS, CREDITOS_electrica_SEIS):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados
electrica['NCC_SEIS'] = electrica.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_electrica_SEIS, CREDITOS_electrica_SEIS):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados

electrica['NCA_SEIS'] = electrica.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

electrica['NCP_SEIS'] = electrica['NCC_SEIS'] - electrica['NCA_SEIS']

# Rendimiento SEIS
conditions = [(electrica['PROMEDIO_SEIS'] >= 0) & (electrica['PROMEDIO_SEIS'] < 30),
(electrica['PROMEDIO_SEIS'] >= 30) & (electrica['PROMEDIO_SEIS'] < 40),
(electrica['PROMEDIO_SEIS'] >= 40) & (electrica['PROMEDIO_SEIS'] < 45),
(electrica['PROMEDIO_SEIS'] >= 45) & (electrica['PROMEDIO_SEIS'] < 50)]
values = [1, 2, 3, 4]
electrica['RENDIMIENTO_SEIS'] = pd.Series(pd.cut(electrica['PROMEDIO_SEIS'], bins=[0, 30, 40, 45, 50], labels=values))

"""# SEPTIMO SEMESTRE electrica"""

#Lista electrica primer semestre

NOTAS_electrica_SIETE = ['NOTA_L_UNO', 'NOTA_EI_UNO', 'NOTA_ECO', 'NOTA_AUTO', 'NOTA_MAQEL', 'NOTA_ELECPOT', 'NOTA_ASP']

VECES_electrica_SIETE = ['VECES_L_UNO', 'VECES_EI_UNO', 'VECES_ECO', 'VECES_AUTO', 'VECES_MAQEL', 'VECES_ELECPOT', 'VECES_ASP']

CREDITOS_electrica_SIETE = ['CREDITOS_L_UNO', 'CREDITOS_EI_UNO', 'CREDITOS_ECO', 'CREDITOS_AUTO', 'CREDITOS_MAQEL', 'CREDITOS_ELECPOT', 'CREDITOS_ASP']

promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in electrica.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_electrica_SIETE, VECES_electrica_SIETE, CREDITOS_electrica_SIETE):
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
electrica['PROMEDIO_SIETE'] = promedios_semestre

# Calcular métricas por semestre
electrica['CAR_SIETE'] = electrica[VECES_electrica_SIETE].apply(lambda x: (x > 1).sum(), axis=1)
electrica['NAC_SIETE'] = electrica[VECES_electrica_SIETE].apply(lambda x: (x > 0).sum(), axis=1)
electrica['NAA_SIETE'] = electrica[NOTAS_electrica_SIETE].apply(lambda x: (x >= 30).sum(), axis=1)
electrica['NAP_SIETE'] = electrica['NAC_SIETE'] - electrica['NAA_SIETE']
electrica['EPA_SIETE'] = electrica.apply(lambda row: 1 if row['PROMEDIO_SIETE'] < 30 or row['NAP_SIETE'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_electrica_SIETE, CREDITOS_electrica_SIETE):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados

electrica['NCC_SIETE'] = electrica.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_electrica_SIETE, CREDITOS_electrica_SIETE):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados

electrica['NCA_SIETE'] = electrica.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

electrica['NCP_SIETE'] = electrica['NCC_SIETE'] - electrica['NCA_SIETE']

# Rendimiento SIETE
conditions = [(electrica['PROMEDIO_SIETE'] >= 0) & (electrica['PROMEDIO_SIETE'] < 30),
(electrica['PROMEDIO_SIETE'] >= 30) & (electrica['PROMEDIO_SIETE'] < 40),
(electrica['PROMEDIO_SIETE'] >= 40) & (electrica['PROMEDIO_SIETE'] < 45),
(electrica['PROMEDIO_SIETE'] >= 45) & (electrica['PROMEDIO_SIETE'] < 50)]
values = [1, 2, 3, 4]
electrica['RENDIMIENTO_SIETE'] = pd.Series(pd.cut(electrica['PROMEDIO_SIETE'], bins=[0, 30, 40, 45, 50], labels=values))

"""# OCTAVO SEMESTRE electrica"""

NOTAS_electrica_OCHO = ['NOTA_EI_DOS', 'NOTA_L_DOS', 'NOTA_HIST', 'NOTA_CCON', 'NOTA_FGEP', 'NOTA_SUBEL', 'NOTA_AIELEC']

VECES_electrica_OCHO = ['VECES_EI_DOS', 'VECES_L_DOS', 'VECES_HIST', 'VECES_CCON', 'VECES_FGEP', 'VECES_SUBEL', 'VECES_AIELEC']

CREDITOS_electrica_OCHO = ['CREDITOS_EI_DOS', 'CREDITOS_L_DOS', 'CREDITOS_HIST', 'CREDITOS_CCON', 'CREDITOS_FGEP', 'CREDITOS_SUBEL', 'CREDITOS_AIELEC']

promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in electrica.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_electrica_OCHO, VECES_electrica_OCHO, CREDITOS_electrica_OCHO):
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
electrica['PROMEDIO_OCHO'] = promedios_semestre

# Calcular métricas por semestre
electrica['CAR_OCHO'] = electrica[VECES_electrica_OCHO].apply(lambda x: (x > 1).sum(), axis=1)
electrica['NAC_OCHO'] = electrica[VECES_electrica_OCHO].apply(lambda x: (x > 0).sum(), axis=1)
electrica['NAA_OCHO'] = electrica[NOTAS_electrica_OCHO].apply(lambda x: (x >= 30).sum(), axis=1)
electrica['NAP_OCHO'] = electrica['NAC_OCHO'] - electrica['NAA_OCHO']
electrica['EPA_OCHO'] = electrica.apply(lambda row: 1 if row['PROMEDIO_OCHO'] < 30 or row['NAP_OCHO'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_electrica_OCHO, CREDITOS_electrica_OCHO):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados

electrica['NCC_OCHO'] = electrica.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_electrica_OCHO, CREDITOS_electrica_OCHO):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados
electrica['NCA_OCHO'] = electrica.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

electrica['NCP_OCHO'] = electrica['NCC_OCHO'] - electrica['NCA_OCHO']

# Rendimiento OCHO
conditions = [(electrica['PROMEDIO_OCHO'] >= 0) & (electrica['PROMEDIO_OCHO'] < 30),
(electrica['PROMEDIO_OCHO'] >= 30) & (electrica['PROMEDIO_OCHO'] < 40),
(electrica['PROMEDIO_OCHO'] >= 40) & (electrica['PROMEDIO_OCHO'] < 45),
(electrica['PROMEDIO_OCHO'] >= 45) & (electrica['PROMEDIO_OCHO'] < 50)]
values = [1, 2, 3, 4]
electrica['RENDIMIENTO_OCHO'] = pd.Series(pd.cut(electrica['PROMEDIO_OCHO'], bins=[0, 30, 40, 45, 50], labels=values))

"""# NOVENO SEMESTRE electrica"""

NOTAS_electrica_NUEVE = ['NOTA_EI_TRES', 'NOTA_L_TRES', 'NOTA_EE_DOS', 'NOTA_EI_CUATRO', 'NOTA_HSE', 'NOTA_ADMIN', 'NOTA_PROTELEC', 'NOTA_TGUNO']

VECES_electrica_NUEVE = ['VECES_EI_TRES', 'VECES_L_TRES', 'VECES_EE_DOS', 'VECES_EI_CUATRO', 'VECES_HSE', 'VECES_ADMIN', 'VECES_PROTELEC', 'VECES_TGUNO']

CREDITOS_electrica_NUEVE = ['CREDITOS_EI_TRES', 'CREDITOS_L_TRES', 'CREDITOS_EE_DOS', 'CREDITOS_EI_CUATRO', 'CREDITOS_HSE', 'CREDITOS_ADMIN', 'CREDITOS_PROTELEC', 'CREDITOS_TGUNO']

promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in electrica.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_electrica_NUEVE, VECES_electrica_NUEVE, CREDITOS_electrica_NUEVE):
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
electrica['PROMEDIO_NUEVE'] = promedios_semestre

# Calcular métricas por semestre
electrica['CAR_NUEVE'] = electrica[VECES_electrica_NUEVE].apply(lambda x: (x > 1).sum(), axis=1)
electrica['NAC_NUEVE'] = electrica[VECES_electrica_NUEVE].apply(lambda x: (x > 0).sum(), axis=1)
electrica['NAA_NUEVE'] = electrica[NOTAS_electrica_NUEVE].apply(lambda x: (x >= 30).sum(), axis=1)
electrica['NAP_NUEVE'] = electrica['NAC_NUEVE'] - electrica['NAA_NUEVE']
electrica['EPA_NUEVE'] = electrica.apply(lambda row: 1 if row['PROMEDIO_NUEVE'] < 30 or row['NAP_NUEVE'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_electrica_NUEVE, CREDITOS_electrica_NUEVE):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados
electrica['NCC_NUEVE'] = electrica.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_electrica_NUEVE, CREDITOS_electrica_NUEVE):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados
electrica['NCA_NUEVE'] = electrica.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

electrica['NCP_NUEVE'] = electrica['NCC_NUEVE'] - electrica['NCA_NUEVE']

# Rendimiento NUEVE
conditions = [(electrica['PROMEDIO_NUEVE'] >= 0) & (electrica['PROMEDIO_NUEVE'] < 30),
(electrica['PROMEDIO_NUEVE'] >= 30) & (electrica['PROMEDIO_NUEVE'] < 40),
(electrica['PROMEDIO_NUEVE'] >= 40) & (electrica['PROMEDIO_NUEVE'] < 45),
(electrica['PROMEDIO_NUEVE'] >= 45) & (electrica['PROMEDIO_NUEVE'] < 50)]
values = [1, 2, 3, 4]
electrica['RENDIMIENTO_NUEVE'] = pd.Series(pd.cut(electrica['PROMEDIO_NUEVE'], bins=[0, 30, 40, 45, 50], labels=values))

"""# DECIMO SEMESTRE electrica"""

NOTAS_electrica_DIEZ = ['NOTA_EE_TRES', 'NOTA_EI_CINCO', 'NOTA_EI_SEIS', 'NOTA_TGDOS']

VECES_electrica_DIEZ = ['VECES_EE_TRES', 'VECES_EI_CINCO', 'VECES_EI_SEIS', 'VECES_TGDOS']

CREDITOS_electrica_DIEZ = ['CREDITOS_EE_TRES', 'CREDITOS_EI_CINCO', 'CREDITOS_EI_SEIS', 'CREDITOS_TGDOS']


promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in electrica.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_electrica_DIEZ, VECES_electrica_DIEZ, CREDITOS_electrica_DIEZ):
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
electrica['PROMEDIO_DIEZ'] = promedios_semestre

# Calcular métricas por semestre
electrica['CAR_DIEZ'] = electrica[VECES_electrica_DIEZ].apply(lambda x: (x > 1).sum(), axis=1)
electrica['NAC_DIEZ'] = electrica[VECES_electrica_DIEZ].apply(lambda x: (x > 0).sum(), axis=1)
electrica['NAA_DIEZ'] = electrica[NOTAS_electrica_DIEZ].apply(lambda x: (x >= 30).sum(), axis=1)
electrica['NAP_DIEZ'] = electrica['NAC_DIEZ'] - electrica['NAA_DIEZ']
electrica['EPA_DIEZ'] = electrica.apply(lambda row: 1 if row['PROMEDIO_DIEZ'] < 30 or row['NAP_DIEZ'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_electrica_DIEZ, CREDITOS_electrica_DIEZ):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados

electrica['NCC_DIEZ'] = electrica.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_electrica_DIEZ, CREDITOS_electrica_DIEZ):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados

electrica['NCA_DIEZ'] = electrica.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

electrica['NCP_DIEZ'] = electrica['NCC_DIEZ'] - electrica['NCA_DIEZ']

# Rendimiento DIEZ
conditions = [(electrica['PROMEDIO_DIEZ'] >= 0) & (electrica['PROMEDIO_DIEZ'] < 30),
(electrica['PROMEDIO_DIEZ'] >= 30) & (electrica['PROMEDIO_DIEZ'] < 40),
(electrica['PROMEDIO_DIEZ'] >= 40) & (electrica['PROMEDIO_DIEZ'] < 45),
(electrica['PROMEDIO_DIEZ'] >= 45) & (electrica['PROMEDIO_DIEZ'] < 50)]
values = [1, 2, 3, 4]
electrica['RENDIMIENTO_DIEZ'] = pd.Series(pd.cut(electrica['PROMEDIO_DIEZ'], bins=[0, 30, 40, 45, 50], labels=values))

# Obtén una lista de todas las columnas que comienzan con "RENDIMIENTO_"
columnas_rendimiento = [col for col in electrica.columns if col.startswith('RENDIMIENTO_')]

# Convertir columnas categóricas a numéricas
electrica[columnas_rendimiento] = electrica[columnas_rendimiento].astype(float)

# Reemplazar los valores vacíos por cero en estas columnas
electrica[columnas_rendimiento] = electrica[columnas_rendimiento].fillna(0)
electrica = electrica.applymap(lambda x: -x if isinstance(x, (int, float)) and x < 0 else x)

electrica = electrica.apply(pd.to_numeric)
electrica.to_csv("electrica.csv", sep=';', index=False)


#------------------------------CSV POR SEMESTRES--------------------------------------------------------#
#------------------------------CSV POR SEMESTRES--------------------------------------------------------#

#En promedio a filtrar es el número mínimo que debe tener un estudiante como promedio de las notas que se toman como variables
año_de_filtro = 2011

"""# INGENIERIA electrica"""

# Primer semestre ingeniería electrica
electrica1 = electrica.loc[:, ['CON_MAT_ICFES', 'IDIOMA_ICFES', 'LOCALIDAD_COLEGIO', 'BIOLOGIA_ICFES', 'QUIMICA_ICFES', 'PG_ICFES', 
    'LITERATURA_ICFES', 'ANO_INGRESO', 'FILOSOFIA_ICFES', 'APT_VERB_ICFES', 'FISICA_ICFES', 'MUNICIPIO', 
    'GENERO', 'APT_MAT_ICFES', 'LOCALIDAD', 'DEPARTAMENTO', 'SOCIALES_ICFES', 'ESTRATO', 'CALENDARIO', 
    'TIPO_COLEGIO', 'DISTANCIA', 'INSCRIPCION', 'CORTE_INGRESO',"RENDIMIENTO_UNO","PROMEDIO_UNO"]]

electrica1 = electrica1 = electrica1.loc[electrica1['ANO_INGRESO'] >= año_de_filtro]
electrica1.to_csv("electrica1.csv", sep=';', index=False)


# Segundo semestre ingeniería electrica
electrica2 = electrica.loc[:, ['RENDIMIENTO_DOS','NOTA_POO','NOTA_INT','NOTA_FIS_DOS','NOTA_EYB','NOTA_DEM','NOTA_CIR_UNO','NOTA_HCI','VECES_INT','VECES_FIS_DOS','PROMEDIO_UNO','PG_ICFES','NCA_UNO','EPA_UNO','NAP_UNO','NCP_UNO','IDIOMA_ICFES','VECES_POO','NAA_UNO','VECES_CIR_UNO','VECES_EYB','VECES_DEM','CAR_UNO','QUIMICA_ICFES','ANO_INGRESO','GENERO','NCC_UNO','VECES_HCI','BIOLOGIA_ICFES','NAC_UNO','APT_VERB_ICFES','PROMEDIO_DOS','FILOSOFIA_ICFES','FISICA_ICFES','CREDITOS_HCI']]

#Se deja solo rendimientos del 1 al 4
electrica2 = electrica2[electrica2['RENDIMIENTO_DOS'].isin([1, 2, 3, 4])]
electrica2.to_csv("electrica2.csv", sep=';', index=False)

# Tercer semestre ingeniería electrica
electrica3 = electrica.loc[:, ['NOTA_ECUA','NOTA_TERMO','NOTA_CIR_DOS','NOTA_FIS_DOS','NOTA_EL_UNO','VECES_ECUA','NOTA_FIS_TRES','NOTA_MULTI','NCP_DOS','PROMEDIO_DOS','NCA_DOS','VECES_TERMO','VECES_EL_UNO','VECES_MULTI','VECES_CIR_DOS','NAA_DOS','NAP_DOS','EPA_DOS','VECES_CIR_UNO','VECES_FIS_TRES','NOTA_INT','NOTA_POO','NOTA_EYB','NOTA_HCI','NOTA_CIR_UNO','NCC_DOS','NAC_DOS','NOTA_DEM','VECES_FIS_DOS','VECES_INT','VECES_POO','CAR_DOS','CREDITOS_MULTI','CREDITOS_FIS_TRES','CREDITOS_CIR_DOS','CREDITOS_TERMO','CREDITOS_EL_UNO','CREDITOS_ECUA', "RENDIMIENTO_TRES","PROMEDIO_TRES"]]

#Se deja solo rendimientos del 1 al 4
electrica3 = electrica3[electrica3['RENDIMIENTO_TRES'].isin([1, 2, 3, 4])]
electrica3.to_csv("electrica3.csv", sep=';', index=False)

# Cuarto semestre ingeniería electrica
electrica4 = electrica.loc[:, ['NOTA_EL_DOS','NOTA_MPI','NOTA_ME','NOTA_PYE','NOTA_ELD','VECES_ME','VECES_EL_DOS','NOTA_GEE','NOTA_CIR_TRES','VECES_PYE','PROMEDIO_DOS','VECES_ECUA','NCP_TRES','NOTA_ECUA','VECES_MPI','PROMEDIO_TRES','VECES_CIR_TRES','VECES_ELD','NOTA_CIR_DOS','NAP_TRES','NAC_TRES','NAA_TRES','NOTA_TERMO','NOTA_EL_UNO','NOTA_MULTI','VECES_GEE','NCA_TRES','CAR_TRES','NCP_DOS','NCC_TRES','NCA_DOS','EPA_TRES','VECES_TERMO','NOTA_FIS_TRES','NOTA_FIS_DOS','CREDITOS_CIR_TRES','CREDITOS_EL_DOS','CREDITOS_ELD','CREDITOS_PYE','CREDITOS_MPI','CREDITOS_ME','CREDITOS_GEE', "RENDIMIENTO_CUATRO","PROMEDIO_CUATRO"]]

columnas_nota = [col for col in electrica4.columns if col.startswith('NOTA')]

#Se deja solo rendimientos del 1 al 4
electrica4 = electrica4[electrica4['RENDIMIENTO_CUATRO'].isin([1, 2, 3, 4])]
electrica4.to_csv("electrica4.csv", sep=';', index=False)

# Quinto semestre ingeniería electrica
electrica5 = electrica.loc[:, ['NOTA_ASD','NOTA_CEM','NOTA_IO_UNO','NOTA_INSE','NOTA_IYM','NOTA_EE_UNO','NOTA_GENH','VECES_CEM','NOTA_EL_DOS','VECES_IYM','VECES_INSE','PROMEDIO_CUATRO','NOTA_MPI','VECES_EE_UNO','VECES_ASD','NAA_CUATRO','NOTA_GEE','NOTA_ME','NCC_CUATRO','NOTA_PYE','NCA_CUATRO','NOTA_CIR_TRES','NOTA_ELD','VECES_GENH','NCP_CUATRO','VECES_EL_DOS','VECES_IO_UNO','VECES_ME','CAR_CUATRO','NAP_CUATRO','NAC_CUATRO','EPA_CUATRO','VECES_PYE','CREDITOS_ASD','CREDITOS_IYM','CREDITOS_IO_UNO','CREDITOS_INSE','CREDITOS_GENH','CREDITOS_EE_UNO','CREDITOS_CEM',"RENDIMIENTO_CINCO",'PROMEDIO_CINCO']]

#Se deja solo rendimientos del 1 al 4
electrica5 = electrica5[electrica5['RENDIMIENTO_CINCO'].isin([1, 2, 3, 4])]
electrica5.to_csv("electrica5.csv", sep=';', index=False)


# Sexto semestre ingeniería electrica
electrica6 = electrica.loc[:, ['NOTA_INGECO','NOTA_DDP','NOTA_CTRL','NOTA_CONEM','NOTA_TDE','VECES_INGECO','PROMEDIO_CUATRO','VECES_IO_DOS','VECES_DDP','NAC_CINCO','NOTAS_RDC','VECES_CTRL','VECES_RDC','NOTA_IO_DOS','VECES_CONEM','NOTA_EL_DOS','VECES_CEM','VECES_TDE','NCP_CINCO','NCC_CINCO','NOTA_GENH','EPA_CINCO','VECES_INSE','NOTA_ASD','NCA_CINCO','NAA_CINCO','NOTA_INSE','NOTA_IO_UNO','NOTA_IYM','PROMEDIO_CINCO','VECES_IYM','CAR_CINCO','NOTA_CEM','NAP_CINCO','CREDITOS_TDE','CREDITOS_IO_DOS','CREDITOS_INGECO','NOTA_EE_UNO','CREDITOS_CONEM','CREDITOS_RDC','CREDITOS_DDP','CREDITOS_CTRL', "RENDIMIENTO_SEIS","PROMEDIO_SEIS"]]

#Se deja solo rendimientos del 1 al 4
electrica6 = electrica6[electrica6['RENDIMIENTO_SEIS'].isin([1, 2, 3, 4])]
electrica6.to_csv("electrica6.csv", sep=';', index=False)

# Septimo semestre ingeniería electrica
electrica7 = electrica.loc[:, ['VECES_ECO','NOTA_L_UNO','NOTA_ASP','NOTA_ELECPOT','NOTA_ECO','NOTA_MAQEL','VECES_ASP','NAC_CINCO','NOTA_AUTO','NOTA_DDP','NOTAS_RDC','VECES_ELECPOT','VECES_AUTO','VECES_MAQEL','NCC_SEIS','NCA_SEIS','VECES_IO_DOS','NAC_SEIS','NOTA_CONEM','NOTA_CTRL','NAA_SEIS','NOTA_EI_UNO','NOTA_INGECO','NCP_SEIS','PROMEDIO_SEIS','PROMEDIO_CUATRO','NOTA_TDE','EPA_SEIS','VECES_DDP','VECES_EI_UNO','NAP_SEIS','VECES_L_UNO','CAR_SEIS','CREDITOS_MAQEL','CREDITOS_EI_UNO','CREDITOS_AUTO','VECES_INGECO','CREDITOS_L_UNO','CREDITOS_ASP','CREDITOS_ELECPOT','CREDITOS_ECO', "RENDIMIENTO_SIETE","PROMEDIO_SIETE"]]

#Se deja solo rendimientos del 1 al 4
electrica7 = electrica7[electrica7['RENDIMIENTO_SIETE'].isin([1, 2, 3, 4])]
electrica7.to_csv("electrica7.csv", sep=';', index=False)

# Octavo semestre ingeniería electrica
electrica8 = electrica.loc[:, ['NOTA_FGEP','NOTA_HIST','NOTA_CCON','NOTA_L_DOS','NOTA_AIELEC','NOTA_SUBEL','VECES_SUBEL','VECES_FGEP','VECES_L_DOS','VECES_HIST','NOTA_L_UNO','PROMEDIO_SIETE','VECES_CCON','NOTA_EI_DOS','NOTA_ELECPOT','NAC_CINCO','NCC_SIETE','NAA_SIETE','EPA_SIETE','NOTA_AUTO','NOTA_MAQEL','VECES_AIELEC','VECES_ECO','NOTA_ECO','NOTA_ASP','NAP_SIETE','NAC_SIETE','NCA_SIETE','VECES_ASP','CAR_SIETE','NCP_SIETE','VECES_EI_DOS','CREDITOS_EI_DOS','CREDITOS_AIELEC','CREDITOS_SUBEL','CREDITOS_L_DOS','CREDITOS_HIST','CREDITOS_FGEP','CREDITOS_CCON', "RENDIMIENTO_OCHO","PROMEDIO_OCHO"]]

#Se deja solo rendimientos del 1 al 4
electrica8 = electrica8[electrica8['RENDIMIENTO_OCHO'].isin([1, 2, 3, 4])]
electrica8.to_csv("electrica8.csv", sep=';', index=False)

# Noveno semestre ingeniería electrica
electrica9 = electrica.loc[:, ['NOTA_L_TRES','NOTA_HSE','NOTA_ADMIN','NOTA_TGUNO','VECES_HSE','NOTA_EI_TRES','NOTA_EE_DOS','NOTA_PROTELEC','NCC_OCHO','VECES_L_TRES','VECES_PROTELEC','CAR_OCHO','VECES_ADMIN','PROMEDIO_SIETE','NOTA_L_UNO','NOTA_L_DOS','VECES_EI_TRES','PROMEDIO_OCHO','NOTA_EI_CUATRO','VECES_EE_DOS','VECES_TGUNO','NAA_OCHO','NOTA_AIELEC','NCA_OCHO','NOTA_CCON','VECES_L_DOS','VECES_FGEP','NOTA_FGEP','EPA_OCHO','NOTA_HIST','NAC_OCHO','NOTA_SUBEL','NCP_OCHO','VECES_HIST','VECES_EI_CUATRO','VECES_SUBEL','CREDITOS_EE_DOS','CREDITOS_EI_TRES','CREDITOS_PROTELEC','CREDITOS_L_TRES','NAP_OCHO','CREDITOS_TGUNO','VECES_CCON','CREDITOS_ADMIN','CREDITOS_EI_CUATRO','CREDITOS_HSE', "RENDIMIENTO_NUEVE","PROMEDIO_NUEVE"]]

#Se deja solo rendimientos del 1 al 4
electrica9 = electrica9[electrica9['RENDIMIENTO_NUEVE'].isin([1, 2, 3, 4])]
electrica9.to_csv("electrica9.csv", sep=';', index=False)

# Decimo semestre ingeniería electrica
electrica10 = electrica.loc[:, ['NOTA_L_TRES','NOTA_HSE','NOTA_ADMIN','NOTA_TGUNO','VECES_HSE','NOTA_EI_TRES','NOTA_EE_DOS','NOTA_PROTELEC','NCC_OCHO','VECES_L_TRES','VECES_PROTELEC','CAR_OCHO','VECES_ADMIN','PROMEDIO_SIETE','NOTA_L_UNO','NOTA_L_DOS','VECES_EI_TRES','PROMEDIO_OCHO','NOTA_EI_CUATRO','VECES_EE_DOS','VECES_TGUNO','NAA_OCHO','NOTA_AIELEC','NCA_OCHO','NOTA_CCON','VECES_L_DOS','VECES_FGEP','NOTA_FGEP','EPA_OCHO','NOTA_HIST','NAC_OCHO','NOTA_SUBEL','NCP_OCHO','VECES_HIST','VECES_EI_CUATRO','VECES_SUBEL','CREDITOS_EE_DOS','CREDITOS_EI_TRES','CREDITOS_PROTELEC','CREDITOS_L_TRES','NAP_OCHO','CREDITOS_TGUNO','VECES_CCON','CREDITOS_ADMIN','CREDITOS_EI_CUATRO','CREDITOS_HSE','NOTA_EI_CINCO','NOTA_TGDOS','NOTA_EI_SEIS','NOTA_EE_TRES','NCC_NUEVE','VECES_EI_CINCO','PROMEDIO_NUEVE','NCA_NUEVE','NAC_NUEVE','NAA_NUEVE','CAR_NUEVE','CREDITOS_EI_CINCO','CREDITOS_EE_TRES','NCP_NUEVE','CREDITOS_EI_SEIS','VECES_TGDOS','NAP_NUEVE','EPA_NUEVE','RENDIMIENTO_DIEZ','PROMEDIO_DIEZ']]

#Se deja solo rendimientos del 1 al 4
electrica10 = electrica10[electrica10['RENDIMIENTO_DIEZ'].isin([1, 2, 3, 4])]
electrica10.to_csv("electrica10.csv", sep=';', index=False)

#Archivos electrica por año

#Año 1 electrica
electricaAnio1 = electrica.loc[:, ['IDIOMA_ICFES','PG_ICFES','FISICA_ICFES','ANO_INGRESO','APT_VERB_ICFES','QUIMICA_ICFES','FILOSOFIA_ICFES','GENERO','BIOLOGIA_ICFES','PROMEDIO_UNO','NOTA_POO','NOTA_INT','NOTA_FIS_DOS','NOTA_EYB','NOTA_DEM','NOTA_CIR_UNO','NOTA_HCI','VECES_INT','VECES_FIS_DOS','PROMEDIO_TRES']]

electricaAnio1 = electricaAnio1[electricaAnio1['PROMEDIO_TRES'] > 0]
electricaAnio1.to_csv("electricaAnio1.csv", sep=';', index=False)

#Año 2 electrica
electricaAnio2 = electrica.loc[:, ["IDIOMA_ICFES","PG_ICFES","FISICA_ICFES","ANO_INGRESO","APT_VERB_ICFES","QUIMICA_ICFES","FILOSOFIA_ICFES","GENERO","BIOLOGIA_ICFES","PROMEDIO_UNO",
              "NOTA_POO","NOTA_INT","NOTA_FIS_DOS","NOTA_EYB","NOTA_DEM","NOTA_CIR_UNO","NOTA_HCI","VECES_INT","VECES_FIS_DOS","PROMEDIO_DOS",
              "NOTA_ECUA","NOTA_TERMO","NOTA_CIR_DOS","NOTA_EL_UNO","VECES_ECUA","NOTA_FIS_TRES","NOTA_MULTI","NCP_DOS","NCA_DOS","VECES_TERMO","NOTA_EL_DOS","NOTA_MPI","NOTA_ME",
              "NOTA_PYE","NOTA_ELD","VECES_ME","VECES_EL_DOS","NOTA_GEE","NOTA_CIR_TRES","VECES_PYE","PROMEDIO_CINCO"]]

electricaAnio2 = electricaAnio2[electricaAnio2['PROMEDIO_CINCO'] > 0]
electricaAnio2.to_csv("electricaAnio2.csv", sep=';', index=False)

#Año 3 electrica
electricaAnio3 = electrica.loc[:, ["IDIOMA_ICFES","PG_ICFES","FISICA_ICFES","ANO_INGRESO","APT_VERB_ICFES","QUIMICA_ICFES","FILOSOFIA_ICFES","GENERO","BIOLOGIA_ICFES","PROMEDIO_UNO","NOTA_POO",
              "NOTA_INT","NOTA_FIS_DOS","NOTA_EYB","NOTA_DEM","NOTA_CIR_UNO","NOTA_HCI","VECES_INT","VECES_FIS_DOS","PROMEDIO_DOS","NOTA_ECUA","NOTA_TERMO",
              "NOTA_CIR_DOS","NOTA_EL_UNO","VECES_ECUA","NOTA_FIS_TRES","NOTA_MULTI","NCP_DOS","NCA_DOS","VECES_TERMO","NOTA_EL_DOS","NOTA_MPI","NOTA_ME","NOTA_PYE","NOTA_ELD","VECES_ME","VECES_EL_DOS",
              "NOTA_GEE","NOTA_CIR_TRES","VECES_PYE","PROMEDIO_CUATRO","NOTA_ASD","NOTA_CEM","NOTA_IO_UNO","NOTA_INSE","NOTA_IYM","NOTA_EE_UNO","NOTA_GENH","VECES_CEM",
              "VECES_IYM","VECES_INSE","NOTA_INGECO","NOTA_DDP","NOTA_CTRL","NOTA_CONEM","NOTA_TDE","VECES_INGECO","VECES_IO_DOS","VECES_DDP","NAC_CINCO","NOTAS_RDC","VECES_ECO","NOTA_L_UNO",
              "NOTA_ASP","NOTA_ELECPOT","NOTA_ECO","NOTA_MAQEL","VECES_ASP","NOTA_AUTO","PROMEDIO_SIETE","NOTA_FGEP","NOTA_HIST","NOTA_CCON","NOTA_L_DOS","NOTA_AIELEC","NOTA_SUBEL","VECES_SUBEL",
              "VECES_FGEP","VECES_L_DOS","VECES_HIST","NOTA_L_TRES","NOTA_HSE","NOTA_ADMIN","NOTA_TGUNO","VECES_HSE","NOTA_EI_TRES","NOTA_EE_DOS","NOTA_PROTELEC","NCC_OCHO","VECES_L_TRES","VECES_PROTELEC",
              "CAR_OCHO","VECES_ADMIN","PROMEDIO_NUEVE"]]

electricaAnio3 = electricaAnio3[electricaAnio3['PROMEDIO_NUEVE'] > 0]
electricaAnio3.to_csv("electricaAnio3.csv", sep=';', index=False)