import pandas as pd
import numpy as np
import glob
import csv
import os



#catastral = pd.read_csv(archivo_base_path, sep=',')
#municipios = pd.read_csv(archivo_municipios_path, sep=',')

#merged_df = pd.merge(catastral, municipios, on='MUNICIPIO')
#merged_df = merged_df.drop(columns=['MUNICIPIO'])
#merged_df = merged_df.rename(columns={'NUM_MUNI': 'MUNICIPIO'})
#catastral = merged_df

ruta_archivo = 'C:/Users/User/Desktop/udistrital/catastral_sin_variables.csv'
catastral = pd.read_csv(ruta_archivo, sep=',')

#ruta_archivo_2 = 'C:/Users/User/Desktop/udistrital/municipios_ud.csv'
#municipios = pd.read_csv(ruta_archivo_2, sep=',')


#catastral['DISTANCIA'] = np.where(((catastral['LOCALIDAD'] == 'TEUSAQUILLO') | (catastral['LOCALIDAD'] == 'CHAPINERO') | (catastral['LOCALIDAD'] == 'SANTA FE')) , '1' , np.nan)
#catastral['DISTANCIA'] = np.where(((catastral['LOCALIDAD'] == 'LOS MARTIRES')|(catastral['LOCALIDAD'] == 'LA CANDELARIA')|(catastral['LOCALIDAD'] == 'PUENTE ARANDA')), '2' , catastral['DISTANCIA'])
#catastral['DISTANCIA'] = np.where(((catastral['LOCALIDAD'] == 'BARRIOS UNIDOS')|(catastral['LOCALIDAD'] == 'RAFAEL URIBE URIBE')|(catastral['LOCALIDAD'] == 'ANTONIO NARINO')|(catastral['LOCALIDAD'] == 'ENGATIVA')|(catastral['LOCALIDAD'] == 'KENNEDY')), '3' , catastral['DISTANCIA'])
#catastral['DISTANCIA'] = np.where(((catastral['LOCALIDAD'] == 'FONTIBON')|(catastral['LOCALIDAD'] == 'SAN CRISTOBAL')), '4' , catastral['DISTANCIA'])
#catastral['DISTANCIA'] = np.where(((catastral['LOCALIDAD'] == 'USAQUEN')|(catastral['LOCALIDAD'] == 'BOSA')|(catastral['LOCALIDAD'] == 'SUBA')|(catastral['LOCALIDAD'] == 'TUNJUELITO')|(catastral['LOCALIDAD'] == 'CIUDAD BOLIVAR')), '5' , catastral['DISTANCIA'])
#catastral['DISTANCIA'] = np.where(((catastral['LOCALIDAD'] == 'USME')|(catastral['LOCALIDAD'] == 'FUERA DE BOGOTA')|(catastral['LOCALIDAD'] == 'SOACHA')|(catastral['LOCALIDAD'] == 'SUMAPAZ')), '6' , catastral['DISTANCIA'])
#catastral['DISTANCIA'] = np.where(((catastral['LOCALIDAD'] == 'NO REGISTRA')|(catastral['LOCALIDAD'] == 'SIN LOCALIDAD')), '7' , catastral['DISTANCIA'])

catastral['GENERO'] = catastral['GENERO'].replace({'MASCULINO': 0, 'FEMENINO': 1})
catastral['TIPO_COLEGIO'] = catastral['TIPO_COLEGIO'].replace({'NO REGISTRA': 0, 'OFICIAL': 1, 'NO OFICIAL':2})
catastral['LOCALIDAD_COLEGIO'] = catastral['LOCALIDAD_COLEGIO'].replace({'NO REGISTRA': 0, 'USAQUEN': 1, 'CHAPINERO': 2, 'SANTAFE': 3, 'SANTA FE': 3, 'SAN CRISTOBAL': 4, 'USME': 5, 'TUNJUELITO': 6, 'BOSA': 7, 'KENNEDY': 8, 'FONTIBON': 9, 'ENGATIVA': 10, 'SUBA': 11, 'BARRIOS UNIDOS': 12, 'TEUSAQUILLO': 13, 'LOS MARTIRES': 14, 'ANTONIO NARINO': 15, 'PUENTE ARANDA': 16, 'LA CANDELARIA': 17, 'RAFAEL URIBE URIBE': 18, 'RAFAEL URIBE': 18, 'CIUDAD BOLIVAR': 19, 'FUERA DE BOGOTA': 20, 'SIN LOCALIDAD': 21, 'SOACHA':20})
catastral['CALENDARIO'] = catastral['CALENDARIO'].replace({'NO REGISTRA': 0,'O': 0, 'A': 1, 'B': 2, 'F': 3})
catastral['DEPARTAMENTO'] = catastral['DEPARTAMENTO'].replace({'NO REGISTRA': 0, 'AMAZONAS': 1, 'ANTIOQUIA': 2,'ARAUCA': 3, 'ATLANTICO': 4, 'BOGOTA': 5, 'BOLIVAR': 6, 'BOYACA': 7, 'CALDAS': 8, 'CAQUETA': 9, 'CASANARE': 10, 'CAUCA': 11, 'CESAR': 12, 'CHOCO': 13, 'CORDOBA': 14, 'CUNDINAMARCA': 15, 'GUAINIA': 16, 'GUAVIARE': 17, 'HUILA': 18, 'LA GUAJIRA': 19, 'MAGDALENA':20, 'META': 21, 'NARINO': 22, 'NORTE SANTANDER': 23, 'PUTUMAYO': 24, 'QUINDIO': 25, 'RISARALDA': 26, 'SAN ANDRES Y PROVIDENCIA': 27, 'SANTANDER': 28, 'SUCRE': 29, 'TOLIMA': 30, 'VALLE': 31, 'VAUPES': 32, 'VICHADA': 33})
catastral['LOCALIDAD'] = catastral['LOCALIDAD'].replace({'NO REGISTRA': 0, 'USAQUEN': 1, 'CHAPINERO': 2, 'SANTA FE': 3, 'SAN CRISTOBAL': 4, 'USME': 5, 'TUNJUELITO': 6, 'BOSA': 7, 'KENNEDY': 8, 'FONTIBON': 9, 'ENGATIVA': 10, 'SUBA': 11, 'BARRIOS UNIDOS': 12, 'TEUSAQUILLO': 13, 'LOS MARTIRES': 14, 'ANTONIO NARINO': 15, 'PUENTE ARANDA': 16, 'LA CANDELARIA': 17, 'RAFAEL URIBE URIBE': 18, 'CIUDAD BOLIVAR': 19, 'FUERA DE BOGOTA': 20, 'SIN LOCALIDAD': 20, 'SOACHA': 20, 'SUMAPAZ': 20})
catastral['INSCRIPCION'] = catastral['INSCRIPCION'].replace({'NO REGISTRA': 0, 'BENEFICIARIOS LEY 1081 DE 2006': 1, 'BENEFICIARIOS LEY 1084 DE 2006': 2, 'CONVENIO ANDRES BELLO': 3, 'DESPLAZADOS': 4, 'INDIGENAS': 5, 'MEJORES BACHILLERES COL. DISTRITAL OFICIAL': 6, 'MINORIAS ETNICAS Y CULTURALES': 7, 'MOVILIDAD ACADEMICA INTERNACIONAL': 8, 'NORMAL': 9, 'TRANSFERENCIA EXTERNA': 10, 'TRANSFERENCIA INTERNA': 11,})
catastral['ESTADO_FINAL'] = catastral['ESTADO_FINAL'].replace({'ABANDONO': 1, 'ACTIVO': 2, 'APLAZO': 3, 'CANCELADO': 4, 'EGRESADO': 5, 'INACTIVO': 6, 'MOVILIDAD': 7, 'N.A.': 8, 'NO ESTUDIANTE AC004': 9, 'NO SUP. PRUEBA ACAD.': 10, 'PRUEBA AC Y ACTIVO': 11, 'PRUEBA ACAD': 12, 'RETIRADO': 13, 'TERMINO MATERIAS': 14, 'TERMINO Y MATRICULO': 15, 'VACACIONES': 16})
catastral['MUNICIPIO'] = catastral['MUNICIPIO'].replace({"NO REGISTRA": 0, "ACACIAS": 1, "AGUACHICA": 2, "AGUAZUL": 3, "ALBAN": 4, "ALBAN (SAN JOSE)": 5, "ALVARADO": 6, "ANAPOIMA": 7, "ANOLAIMA": 8, "APARTADO": 9, "ARAUCA": 10, "ARBELAEZ": 11, "ARMENIA": 12, "ATACO": 13, "BARRANCABERMEJA": 14, "BARRANQUILLA": 15, "BELEN DE LOS ANDAQUIES": 16, "BOAVITA": 17, "BOGOTA": 18, "BOJACA": 19, "BOLIVAR": 20, "BUCARAMANGA": 21, "BUENAVENTURA": 22, "CABUYARO": 23, "CACHIPAY": 24, "CAICEDONIA": 25, "CAJAMARCA": 26, "CAJICA": 27, "CALAMAR": 28, "CALARCA": 29, "CALI": 30, "CAMPOALEGRE": 31, "CAPARRAPI": 32, "CAQUEZA": 33, "CARTAGENA": 34, "CASTILLA LA NUEVA": 35, "CERETE": 36, "CHAPARRAL": 37, "CHARALA": 38, "CHIA": 39, "CHIPAQUE": 40, "CHIQUINQUIRA": 41, "CHOACHI": 42, "CHOCONTA": 43, "CIENAGA": 44, "CIRCASIA": 45, "COGUA": 46, "CONTRATACION": 47, "COTA": 48, "CUCUTA": 49, "CUMARAL": 50, "CUMBAL": 51, "CURITI": 52, "CURUMANI": 53, "DUITAMA": 54, "EL BANCO": 55, "EL CARMEN DE BOLIVAR": 56, "EL COLEGIO": 57, "EL CHARCO": 58, "EL DORADO": 59, "EL PASO": 60, "EL ROSAL": 61, "ESPINAL": 62, "FACATATIVA": 63, "FLORENCIA": 64, "FLORIDABLANCA": 65, "FOMEQUE": 66, "FONSECA": 67, "FORTUL": 68, "FOSCA": 69, "FUNZA": 70, "FUSAGASUGA": 71, "GACHETA": 72, "GALERAS (NUEVA GRANADA)": 73, "GAMA": 74, "GARAGOA": 75, "GARZON": 76, "GIGANTE": 77, "GIRARDOT": 78, "GRANADA": 79, "GUACHUCAL": 80, "GUADUAS": 81, "GUAITARILLA": 82, "GUAMO": 83, "GUASCA": 84, "GUATEQUE": 85, "GUAYATA": 86, "GUTIERREZ": 87, "IBAGUE": 88, "INIRIDA": 89, "INZA": 90, "IPIALES": 91, "ITSMINA": 92, "JENESANO": 93, "LA CALERA": 94, "LA DORADA": 95, "LA MESA": 96, "LA PLATA": 97, "LA UVITA": 98, "LA VEGA": 99, "LIBANO": 100, "LOS PATIOS": 101, "MACANAL": 102, "MACHETA": 103, "MADRID": 104, "MAICAO": 105, "MALAGA": 106, "MANAURE BALCON DEL 12": 107, "MANIZALES": 108, "MARIQUITA": 109, "MEDELLIN": 110, "MEDINA": 111, "MELGAR": 112, "MITU": 113, "MOCOA": 114, "MONTERIA": 115, "MONTERREY": 116, "MOSQUERA": 117, "NATAGAIMA": 118, "NEIVA": 119, "NEMOCON": 120, "OCANA": 121, "ORITO": 122, "ORTEGA": 123, "PACHO": 124, "PAEZ (BELALCAZAR)": 125, "PAICOL": 126, "PAILITAS": 127, "PAIPA": 128, "PALERMO": 129, "PALMIRA": 130, "PAMPLONA": 131, "PANDI": 132, "PASCA": 133, "PASTO": 134, "PAZ DE ARIPORO": 135, "PAZ DE RIO": 136, "PITALITO": 137, "POPAYAN": 138, "PUENTE NACIONAL": 139, "PUERTO ASIS": 140, "PUERTO BOYACA": 141, "PUERTO LOPEZ": 142, "PUERTO SALGAR": 143, "PURIFICACION": 144, "QUETAME": 145, "QUIBDO": 146, "RAMIRIQUI": 147, "RICAURTE": 148, "RIOHACHA": 149, "RIVERA": 150, "SABOYA": 151, "SAHAGUN": 152, "SALDAÑA": 153, "SAMACA": 154, "SAMANA": 155, "SAN AGUSTIN": 156, "SAN ANDRES": 157, "SAN BERNARDO": 158, "SAN EDUARDO": 159, "SAN FRANCISCO": 160, "SAN GIL": 161, "SAN JOSE DEL FRAGUA": 162, "SAN JOSE DEL GUAVIARE": 163, "SAN LUIS DE PALENQUE": 164, "SAN MARCOS": 165, "SAN MARTIN": 166, "SANDONA": 167, "SAN VICENTE DEL CAGUAN": 168, "SANTA MARTA": 169, "SANTA SOFIA": 170, "SESQUILE": 171, "SIBATE": 172, "SIBUNDOY": 173, "SILVANIA": 174, "SIMIJACA": 175, "SINCE": 176, "SINCELEJO": 177, "SOACHA": 178, "SOATA": 179, "SOCORRO": 180, "SOGAMOSO": 181, "SOLEDAD": 182, "SOPO": 183, "SORACA": 184, "SOTAQUIRA": 185, "SUAITA": 186, "SUBACHOQUE": 187, "SUESCA": 188, "SUPATA": 189, "SUTAMARCHAN": 190, "SUTATAUSA": 191, "TABIO": 192, "TAMESIS": 193, "TARQUI": 194, "TAUSA": 195, "TENA": 196, "TENJO": 197, "TESALIA": 198, "TIBANA": 199, "TIMANA": 200, "TOCANCIPA": 201, "TUBARA": 202, "TULUA": 203, "TUMACO": 204, "TUNJA": 205, "TURBACO": 206, "TURMEQUE": 207, "UBATE": 208, "UMBITA": 209, "UNE": 210, "VALLEDUPAR": 211, "VELEZ": 212, "VENADILLO": 213, "VENECIA (OSPINA PEREZ)": 214, "VILLA DE LEYVA": 215, "VILLAHERMOSA": 216, "VILLANUEVA": 217, "VILLAPINZON": 218, "VILLAVICENCIO": 219, "VILLETA": 220, "YACOPI": 221, "YOPAL": 222, "ZIPACON": 223, "ZIPAQUIRA": 224})

catastral = catastral.apply(pd.to_numeric)

# Recorrer todas las columnas que comienzan con "CREDITOS_"
for columna in catastral.columns:
    if columna.startswith('CREDITOS_'):
        # Obtener el valor distinto de cero en la columna
        otro_valor = catastral.loc[catastral[columna] != 0, columna].iloc[0]
        # Reemplazar ceros por el otro valor
        catastral[columna] = catastral[columna].replace(0, otro_valor)



"""#PRIMER SEMESTRE catastral"""

# Lista para variables de NOTA
NOTAS_catastral_UNO = [
    'NOTA_DIF', 'NOTA_TEXTOS', 'NOTA_SEM', 'NOTA_HIST',
    'NOTA_ALGEBRA', 'NOTA_CD&C', 'NOTA_DITO'
]

# Lista para variables de VECES
VECES_catastral_UNO = [
    'VECES_DIF', 'VECES_TEXTOS', 'VECES_SEM', 'VECES_HIST',
    'VECES_ALGEBRA', 'VECES_CD&C', 'VECES_DITO'
]

# Lista para variables de CREDITOS
CREDITOS_catastral_UNO = [
    'CREDITOS_DIF', 'CREDITOS_TEXTOS', 'CREDITOS_SEM', 'CREDITOS_HIST',
    'CREDITOS_ALGEBRA', 'CREDITOS_CD&C', 'CREDITOS_DITO'
]

promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in catastral.iterrows():
    notas_estudiante = []
    creditos_estudiante = []

    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_catastral_UNO, VECES_catastral_UNO, CREDITOS_catastral_UNO):
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
catastral['PROMEDIO_UNO'] = promedios_semestre

# Calcular métricas por semestre
catastral['CAR_UNO'] = catastral[VECES_catastral_UNO].apply(lambda x: (x > 1).sum(), axis=1)
catastral['NAC_UNO'] = catastral[VECES_catastral_UNO].apply(lambda x: (x > 0).sum(), axis=1)
catastral['NAA_UNO'] = catastral[NOTAS_catastral_UNO].apply(lambda x: (x >= 30).sum(), axis=1)
catastral['NAP_UNO'] = catastral['NAC_UNO'] - catastral['NAA_UNO']
catastral['EPA_UNO'] = catastral.apply(lambda row: 1 if row['PROMEDIO_UNO'] < 30 or row['NAP_UNO'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_catastral_UNO, CREDITOS_catastral_UNO):
        if row[veces_col] > 0:
            creditos_cursados += row[creditos_col]
    return creditos_cursados

catastral['NCC_UNO'] = catastral.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_catastral_UNO, CREDITOS_catastral_UNO):
        if row[nota_col] >= 30:
            creditos_aprobados += row[creditos_col]
    return creditos_aprobados

catastral['NCA_UNO'] = catastral.apply(calcular_creditos_aprobados, axis=1)


# Construir NCP

catastral['NCP_UNO'] = catastral['NCC_UNO'] - catastral['NCA_UNO']

# Rendimiento UNO
conditions = [(catastral['PROMEDIO_UNO'] >= 0) & (catastral['PROMEDIO_UNO'] < 30),
(catastral['PROMEDIO_UNO'] >= 30) & (catastral['PROMEDIO_UNO'] < 40),
(catastral['PROMEDIO_UNO'] >= 40) & (catastral['PROMEDIO_UNO'] < 45),
(catastral['PROMEDIO_UNO'] >= 45) & (catastral['PROMEDIO_UNO'] < 50)]
values = [1, 2, 3, 4]
catastral['RENDIMIENTO_UNO'] = pd.Series(pd.cut(catastral['PROMEDIO_UNO'], bins=[0, 30, 40, 45, 50], labels=values))

"""# SEGUNDO SEMRESTRE catastral"""

# Lista catastral segundo semestre
# Lista para variables de NOTA
NOTAS_catastral_DOS = [
    'NOTA_PROGB', 'NOTA_FIS_UNO', 'NOTA_INT', 'NOTA_EYB',
    'NOTA_ASES', 'NOTA_TOP'
]

# Lista para variables de VECES
VECES_catastral_DOS = [
    'VECES_PROGB', 'VECES_FIS_UNO', 'VECES_INT', 'VECES_EYB',
    'VECES_ASES', 'VECES_TOP'
]

# Lista para variables de CREDITOS
CREDITOS_catastral_DOS = [
    'CREDITOS_PROGB', 'CREDITOS_FIS_UNO', 'CREDITOS_INT', 'CREDITOS_EYB',
    'CREDITOS_ASES', 'CREDITOS_TOP'
]

catastral.columns

promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in catastral.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_catastral_DOS, VECES_catastral_DOS, CREDITOS_catastral_DOS):
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
catastral['PROMEDIO_DOS'] = promedios_semestre

# Calcular métricas por semestre
catastral['CAR_DOS'] = catastral[VECES_catastral_DOS].apply(lambda x: (x > 1).sum(), axis=1)
catastral['NAC_DOS'] = catastral[VECES_catastral_DOS].apply(lambda x: (x > 0).sum(), axis=1)
catastral['NAA_DOS'] = catastral[NOTAS_catastral_DOS].apply(lambda x: (x >= 30).sum(), axis=1)
catastral['NAP_DOS'] = catastral['NAC_DOS'] - catastral['NAA_DOS']
catastral['EPA_DOS'] = catastral.apply(lambda row: 1 if row['PROMEDIO_DOS'] < 30 or row['NAP_DOS'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_catastral_DOS, CREDITOS_catastral_DOS):
        if row[veces_col] > 0:
            creditos_cursados += row[creditos_col]
    return creditos_cursados

catastral['NCC_DOS'] = catastral.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_catastral_DOS, CREDITOS_catastral_DOS):
        if row[nota_col] >= 30:
            creditos_aprobados += row[creditos_col]
    return creditos_aprobados

catastral['NCA_DOS'] = catastral.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

catastral['NCP_DOS'] = catastral['NCC_DOS'] - catastral['NCA_DOS']

# Rendimiento DOS
conditions = [(catastral['PROMEDIO_DOS'] >= 0) & (catastral['PROMEDIO_DOS'] < 30),
(catastral['PROMEDIO_DOS'] >= 30) & (catastral['PROMEDIO_DOS'] < 40),
(catastral['PROMEDIO_DOS'] >= 40) & (catastral['PROMEDIO_DOS'] < 45),
(catastral['PROMEDIO_DOS'] >= 45) & (catastral['PROMEDIO_DOS'] < 50)]
values = [1, 2, 3, 4]
catastral['RENDIMIENTO_DOS'] = pd.Series(pd.cut(catastral['PROMEDIO_DOS'], bins=[0, 30, 40, 45, 50], labels=values))

"""# TERCER SEMESTRE catastral"""

# Lista catastral tercer semestre

# Lista para variables de NOTA
NOTAS_catastral_TRES = [
    'NOTA_CFJC', 'NOTA_POO', 'NOTA_FIS_DOS', 'NOTA_MULTI',
    'NOTA_ECUA', 'NOTA_FOTO', 'NOTA_SUELOS'
]

# Lista para variables de VECES
VECES_catastral_TRES = [
    'VECES_CFJC', 'VECES_POO', 'VECES_FIS_DOS', 'VECES_MULTI',
    'VECES_ECUA', 'VECES_FOTO', 'VECES_SUELOS'
]

# Lista para variables de CREDITOS
CREDITOS_catastral_TRES = [
    'CREDITOS_CFJC', 'CREDITOS_POO', 'CREDITOS_FIS_DOS', 'CREDITOS_MULTI',
    'CREDITOS_ECUA', 'CREDITOS_FOTO', 'CREDITOS_SUELOS'
]

catastral.columns
promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in catastral.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_catastral_TRES, VECES_catastral_TRES, CREDITOS_catastral_TRES):
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
catastral['PROMEDIO_TRES'] = promedios_semestre

# Calcular métricas por semestre
catastral['CAR_TRES'] = catastral[VECES_catastral_TRES].apply(lambda x: (x > 1).sum(), axis=1)
catastral['NAC_TRES'] = catastral[VECES_catastral_TRES].apply(lambda x: (x > 0).sum(), axis=1)
catastral['NAA_TRES'] = catastral[NOTAS_catastral_TRES].apply(lambda x: (x >= 30).sum(), axis=1)
catastral['NAP_TRES'] = catastral['NAC_TRES'] - catastral['NAA_TRES']
catastral['EPA_TRES'] = catastral.apply(lambda row: 1 if row['PROMEDIO_TRES'] < 30 or row['NAP_TRES'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_catastral_TRES, CREDITOS_catastral_TRES):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados
catastral['NCC_TRES'] = catastral.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_catastral_TRES, CREDITOS_catastral_TRES):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados
catastral['NCA_TRES'] = catastral.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

catastral['NCP_TRES'] = catastral['NCC_TRES'] - catastral['NCA_TRES']

# Rendimiento TRES
conditions = [(catastral['PROMEDIO_TRES'] >= 0) & (catastral['PROMEDIO_TRES'] < 30),
(catastral['PROMEDIO_TRES'] >= 30) & (catastral['PROMEDIO_TRES'] < 40),
(catastral['PROMEDIO_TRES'] >= 40) & (catastral['PROMEDIO_TRES'] < 45),
(catastral['PROMEDIO_TRES'] >= 45) & (catastral['PROMEDIO_TRES'] < 50)]
values = [1, 2, 3, 4]
catastral['RENDIMIENTO_TRES'] = pd.Series(pd.cut(catastral['PROMEDIO_TRES'], bins=[0, 30, 40, 45, 50], labels=values))

"""# CUARTO SEMESTRE catastral"""

#Lista catastral cuarto semestre

# Lista para variables de NOTA
NOTAS_catastral_CUATRO = [
    'NOTA_L_UNO', 'NOTA_FIS_TRES', 'NOTA_CCON', 'NOTA_PROB',
    'NOTA_GEOGEO', 'NOTA_PRII', 'NOTA_GH&F'
]

# Lista para variables de VECES
VECES_catastral_CUATRO = [
    'VECES_L_UNO', 'VECES_FIS_TRES', 'VECES_CCON', 'VECES_PROB',
    'VECES_GEOGEO', 'VECES_PRII', 'VECES_GH&F'
]

# Lista para variables de CREDITOS
CREDITOS_catastral_CUATRO = [
    'CREDITOS_L_UNO', 'CREDITOS_FIS_TRES', 'CREDITOS_CCON', 'CREDITOS_PROB',
    'CREDITOS_GEOGEO', 'CREDITOS_PRII', 'CREDITOS_GH&F'
]

promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in catastral.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_catastral_CUATRO, VECES_catastral_CUATRO, CREDITOS_catastral_CUATRO):
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
catastral['PROMEDIO_CUATRO'] = promedios_semestre

# Calcular métricas por semestre
catastral['CAR_CUATRO'] = catastral[VECES_catastral_CUATRO].apply(lambda x: (x > 1).sum(), axis=1)
catastral['NAC_CUATRO'] = catastral[VECES_catastral_CUATRO].apply(lambda x: (x > 0).sum(), axis=1)
catastral['NAA_CUATRO'] = catastral[NOTAS_catastral_CUATRO].apply(lambda x: (x >= 30).sum(), axis=1)
catastral['NAP_CUATRO'] = catastral['NAC_CUATRO'] - catastral['NAA_CUATRO']
catastral['EPA_CUATRO'] = catastral.apply(lambda row: 1 if row['PROMEDIO_CUATRO'] < 30 or row['NAP_CUATRO'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_catastral_CUATRO, CREDITOS_catastral_CUATRO):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados
catastral['NCC_CUATRO'] = catastral.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_catastral_CUATRO, CREDITOS_catastral_CUATRO):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados
catastral['NCA_CUATRO'] = catastral.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

catastral['NCP_CUATRO'] = catastral['NCC_CUATRO'] - catastral['NCA_CUATRO']

# Rendimiento CUATRO
conditions = [(catastral['PROMEDIO_CUATRO'] >= 0) & (catastral['PROMEDIO_CUATRO'] < 30),
(catastral['PROMEDIO_CUATRO'] >= 30) & (catastral['PROMEDIO_CUATRO'] < 40),
(catastral['PROMEDIO_CUATRO'] >= 40) & (catastral['PROMEDIO_CUATRO'] < 45),
(catastral['PROMEDIO_CUATRO'] >= 45) & (catastral['PROMEDIO_CUATRO'] < 50)]
values = [1, 2, 3, 4]
catastral['RENDIMIENTO_CUATRO'] = pd.Series(pd.cut(catastral['PROMEDIO_CUATRO'], bins=[0, 30, 40, 45, 50], labels=values))

"""# QUINTO SEMESTRE catastral"""

# Lista catastral quinto semestre

# Lista para variables de NOTA
NOTAS_catastral_CINCO = [
    'NOTA_ECO_UNO', 'NOTA_ME', 'NOTA_EST', 'NOTA_AGEO',
    'NOTA_BD', 'NOTA_CARTO', 'NOTAS_SISC'
]

# Lista para variables de VECES
VECES_catastral_CINCO = [
    'VECES_ECO_UNO', 'VECES_ME', 'VECES_EST', 'VECES_AGEO',
    'VECES_BD', 'VECES_CARTO', 'VECES_SISC'
]

# Lista para variables de CREDITOS
CREDITOS_catastral_CINCO = [
    'CREDITOS_ECO_UNO', 'CREDITOS_ME', 'CREDITOS_EST', 'CREDITOS_AGEO',
    'CREDITOS_BD', 'CREDITOS_CARTO', 'CREDITOS_SISC'
]

promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in catastral.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_catastral_CINCO, VECES_catastral_CINCO, CREDITOS_catastral_CINCO):
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
catastral['PROMEDIO_CINCO'] = promedios_semestre

# Calcular métricas por semestre
catastral['CAR_CINCO'] = catastral[VECES_catastral_CINCO].apply(lambda x: (x > 1).sum(), axis=1)
catastral['NAC_CINCO'] = catastral[VECES_catastral_CINCO].apply(lambda x: (x > 0).sum(), axis=1)
catastral['NAA_CINCO'] = catastral[NOTAS_catastral_CINCO].apply(lambda x: (x >= 30).sum(), axis=1)
catastral['NAP_CINCO'] = catastral['NAC_CINCO'] - catastral['NAA_CINCO']
catastral['EPA_CINCO'] = catastral.apply(lambda row: 1 if row['PROMEDIO_CINCO'] < 30 or row['NAP_CINCO'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_catastral_CINCO, CREDITOS_catastral_CINCO):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados
catastral['NCC_CINCO'] = catastral.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_catastral_CINCO, CREDITOS_catastral_CINCO):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados
catastral['NCA_CINCO'] = catastral.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

catastral['NCP_CINCO'] = catastral['NCC_CINCO'] - catastral['NCA_CINCO']

# Rendimiento CINCO
conditions = [(catastral['PROMEDIO_CINCO'] >= 0) & (catastral['PROMEDIO_CINCO'] < 30),
(catastral['PROMEDIO_CINCO'] >= 30) & (catastral['PROMEDIO_CINCO'] < 40),
(catastral['PROMEDIO_CINCO'] >= 40) & (catastral['PROMEDIO_CINCO'] < 45),
(catastral['PROMEDIO_CINCO'] >= 45) & (catastral['PROMEDIO_CINCO'] < 50)]
values = [1, 2, 3, 4]
catastral['RENDIMIENTO_CINCO'] = pd.Series(pd.cut(catastral['PROMEDIO_CINCO'], bins=[0, 30, 40, 45, 50], labels=values))

"""# SEXTO SEMESTRE catastral"""

#Lista catastral sexto semestre

# Lista para variables de NOTA
NOTAS_catastral_SEIS = [
    'NOTA_EE_UNO', 'NOTA_L_DOS', 'NOTA_HSE', 'NOTA_INGECO',
    'NOTA_GEO_FIS', 'NOTA_SIG', 'NOTA_LEGIC'
]

# Lista para variables de VECES
VECES_catastral_SEIS = [
    'VECES_EE_UNO', 'VECES_L_DOS', 'VECES_HSE', 'VECES_INGECO',
    'VECES_GEO_FIS', 'VECES_SIG', 'VECES_LEGIC'
]

# Lista para variables de CREDITOS
CREDITOS_catastral_SEIS = [
    'CREDITOS_EE_UNO', 'CREDITOS_L_DOS', 'CREDITOS_HSE', 'CREDITOS_INGECO',
    'CREDITOS_GEO_FIS', 'CREDITOS_SIG', 'CREDITOS_LEGIC'
]

promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in catastral.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_catastral_SEIS, VECES_catastral_SEIS, CREDITOS_catastral_SEIS):
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
catastral['PROMEDIO_SEIS'] = promedios_semestre

# Calcular métricas por semestre
catastral['CAR_SEIS'] = catastral[VECES_catastral_SEIS].apply(lambda x: (x > 1).sum(), axis=1)
catastral['NAC_SEIS'] = catastral[VECES_catastral_SEIS].apply(lambda x: (x > 0).sum(), axis=1)
catastral['NAA_SEIS'] = catastral[NOTAS_catastral_SEIS].apply(lambda x: (x >= 30).sum(), axis=1)
catastral['NAP_SEIS'] = catastral['NAC_SEIS'] - catastral['NAA_SEIS']
catastral['EPA_SEIS'] = catastral.apply(lambda row: 1 if row['PROMEDIO_SEIS'] < 30 or row['NAP_SEIS'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_catastral_SEIS, CREDITOS_catastral_SEIS):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados
catastral['NCC_SEIS'] = catastral.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_catastral_SEIS, CREDITOS_catastral_SEIS):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados

catastral['NCA_SEIS'] = catastral.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

catastral['NCP_SEIS'] = catastral['NCC_SEIS'] - catastral['NCA_SEIS']

# Rendimiento SEIS
conditions = [(catastral['PROMEDIO_SEIS'] >= 0) & (catastral['PROMEDIO_SEIS'] < 30),
(catastral['PROMEDIO_SEIS'] >= 30) & (catastral['PROMEDIO_SEIS'] < 40),
(catastral['PROMEDIO_SEIS'] >= 40) & (catastral['PROMEDIO_SEIS'] < 45),
(catastral['PROMEDIO_SEIS'] >= 45) & (catastral['PROMEDIO_SEIS'] < 50)]
values = [1, 2, 3, 4]
catastral['RENDIMIENTO_SEIS'] = pd.Series(pd.cut(catastral['PROMEDIO_SEIS'], bins=[0, 30, 40, 45, 50], labels=values))

"""# SEPTIMO SEMESTRE catastral"""

#Lista catastral primer semestre

# Lista para variables de NOTA
NOTAS_catastral_SIETE = [
    'NOTA_EI_UNO', 'NOTA_EI_DOS', 'NOTA_GEO_SAL', 'NOTA_PDI',
    'NOTA_PROCC', 'NOTA_AVAP', 'NOTA_ECONOMET'
]

# Lista para variables de VECES
VECES_catastral_SIETE = [
    'VECES_EI_UNO', 'VECES_EI_DOS', 'VECES_GEO_SAL', 'VECES_PDI',
    'VECES_PROCC', 'VECES_AVAP', 'VECES_ECONOMET'
]

# Lista para variables de CREDITOS
CREDITOS_catastral_SIETE = [
    'CREDITOS_EI_UNO', 'CREDITOS_EI_DOS', 'CREDITOS_GEO_SAL', 'CREDITOS_PDI',
    'CREDITOS_PROCC', 'CREDITOS_AVAP', 'CREDITOS_ECONOMET'
]

promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in catastral.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_catastral_SIETE, VECES_catastral_SIETE, CREDITOS_catastral_SIETE):
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
catastral['PROMEDIO_SIETE'] = promedios_semestre

# Calcular métricas por semestre
catastral['CAR_SIETE'] = catastral[VECES_catastral_SIETE].apply(lambda x: (x > 1).sum(), axis=1)
catastral['NAC_SIETE'] = catastral[VECES_catastral_SIETE].apply(lambda x: (x > 0).sum(), axis=1)
catastral['NAA_SIETE'] = catastral[NOTAS_catastral_SIETE].apply(lambda x: (x >= 30).sum(), axis=1)
catastral['NAP_SIETE'] = catastral['NAC_SIETE'] - catastral['NAA_SIETE']
catastral['EPA_SIETE'] = catastral.apply(lambda row: 1 if row['PROMEDIO_SIETE'] < 30 or row['NAP_SIETE'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_catastral_SIETE, CREDITOS_catastral_SIETE):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados

catastral['NCC_SIETE'] = catastral.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_catastral_SIETE, CREDITOS_catastral_SIETE):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados

catastral['NCA_SIETE'] = catastral.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

catastral['NCP_SIETE'] = catastral['NCC_SIETE'] - catastral['NCA_SIETE']

# Rendimiento SIETE
conditions = [(catastral['PROMEDIO_SIETE'] >= 0) & (catastral['PROMEDIO_SIETE'] < 30),
(catastral['PROMEDIO_SIETE'] >= 30) & (catastral['PROMEDIO_SIETE'] < 40),
(catastral['PROMEDIO_SIETE'] >= 40) & (catastral['PROMEDIO_SIETE'] < 45),
(catastral['PROMEDIO_SIETE'] >= 45) & (catastral['PROMEDIO_SIETE'] < 50)]
values = [1, 2, 3, 4]
catastral['RENDIMIENTO_SIETE'] = pd.Series(pd.cut(catastral['PROMEDIO_SIETE'], bins=[0, 30, 40, 45, 50], labels=values))

"""# OCTAVO SEMESTRE catastral"""

#Lista catastral primer semestre

# Lista para variables de NOTA
NOTAS_catastral_OCHO = [
    'NOTA_L_TRES', 'NOTA_EI_TRES', 'NOTA_EI_CUATRO', 'NOTA_FGEP',
    'NOTA_FOTOD', 'NOTA_AVAM'
]

# Lista para variables de VECES
VECES_catastral_OCHO = [
    'VECES_L_TRES', 'VECES_EI_TRES', 'VECES_EI_CUATRO', 'VECES_FGEP',
    'VECES_FOTOD', 'VECES_AVAM'
]

# Lista para variables de CREDITOS
CREDITOS_catastral_OCHO = [
    'CREDITOS_L_TRES', 'CREDITOS_EI_TRES', 'CREDITOS_EI_CUATRO', 'CREDITOS_FGEP',
    'CREDITOS_FOTOD', 'CREDITOS_AVAM'
]

promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in catastral.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_catastral_OCHO, VECES_catastral_OCHO, CREDITOS_catastral_OCHO):
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
catastral['PROMEDIO_OCHO'] = promedios_semestre

# Calcular métricas por semestre
catastral['CAR_OCHO'] = catastral[VECES_catastral_OCHO].apply(lambda x: (x > 1).sum(), axis=1)
catastral['NAC_OCHO'] = catastral[VECES_catastral_OCHO].apply(lambda x: (x > 0).sum(), axis=1)
catastral['NAA_OCHO'] = catastral[NOTAS_catastral_OCHO].apply(lambda x: (x >= 30).sum(), axis=1)
catastral['NAP_OCHO'] = catastral['NAC_OCHO'] - catastral['NAA_OCHO']
catastral['EPA_OCHO'] = catastral.apply(lambda row: 1 if row['PROMEDIO_OCHO'] < 30 or row['NAP_OCHO'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_catastral_OCHO, CREDITOS_catastral_OCHO):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados

catastral['NCC_OCHO'] = catastral.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_catastral_OCHO, CREDITOS_catastral_OCHO):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados
catastral['NCA_OCHO'] = catastral.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

catastral['NCP_OCHO'] = catastral['NCC_OCHO'] - catastral['NCA_OCHO']

# Rendimiento OCHO
conditions = [(catastral['PROMEDIO_OCHO'] >= 0) & (catastral['PROMEDIO_OCHO'] < 30),
(catastral['PROMEDIO_OCHO'] >= 30) & (catastral['PROMEDIO_OCHO'] < 40),
(catastral['PROMEDIO_OCHO'] >= 40) & (catastral['PROMEDIO_OCHO'] < 45),
(catastral['PROMEDIO_OCHO'] >= 45) & (catastral['PROMEDIO_OCHO'] < 50)]
values = [1, 2, 3, 4]
catastral['RENDIMIENTO_OCHO'] = pd.Series(pd.cut(catastral['PROMEDIO_OCHO'], bins=[0, 30, 40, 45, 50], labels=values))

"""# NOVENO SEMESTRE catastral"""

#Lista catastral primer semestre
# Lista para variables de NOTA
NOTAS_catastral_NUEVE = [
    'NOTA_EI_CINCO', 'NOTA_EE_DOS', 'NOTA_EI_SEIS', 'NOTA_ORD_TER',
    'NOTA_TG_UNO'
]

# Lista para variables de VECES
VECES_catastral_NUEVE = [
    'VECES_EI_CINCO', 'VECES_EE_DOS', 'VECES_EI_SEIS', 'VECES_ORD_TER',
    'VECES_TG_UNO'
]

# Lista para variables de CREDITOS
CREDITOS_catastral_NUEVE = [
    'CREDITOS_EI_CINCO', 'CREDITOS_EE_DOS', 'CREDITOS_EI_SEIS', 'CREDITOS_ORD_TER',
    'CREDITOS_TG_UNO'
]

promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in catastral.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_catastral_NUEVE, VECES_catastral_NUEVE, CREDITOS_catastral_NUEVE):
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
catastral['PROMEDIO_NUEVE'] = promedios_semestre

# Calcular métricas por semestre
catastral['CAR_NUEVE'] = catastral[VECES_catastral_NUEVE].apply(lambda x: (x > 1).sum(), axis=1)
catastral['NAC_NUEVE'] = catastral[VECES_catastral_NUEVE].apply(lambda x: (x > 0).sum(), axis=1)
catastral['NAA_NUEVE'] = catastral[NOTAS_catastral_NUEVE].apply(lambda x: (x >= 30).sum(), axis=1)
catastral['NAP_NUEVE'] = catastral['NAC_NUEVE'] - catastral['NAA_NUEVE']
catastral['EPA_NUEVE'] = catastral.apply(lambda row: 1 if row['PROMEDIO_NUEVE'] < 30 or row['NAP_NUEVE'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_catastral_NUEVE, CREDITOS_catastral_NUEVE):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados
catastral['NCC_NUEVE'] = catastral.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_catastral_NUEVE, CREDITOS_catastral_NUEVE):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados
catastral['NCA_NUEVE'] = catastral.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

catastral['NCP_NUEVE'] = catastral['NCC_NUEVE'] - catastral['NCA_NUEVE']

# Rendimiento NUEVE
conditions = [(catastral['PROMEDIO_NUEVE'] >= 0) & (catastral['PROMEDIO_NUEVE'] < 30),
(catastral['PROMEDIO_NUEVE'] >= 30) & (catastral['PROMEDIO_NUEVE'] < 40),
(catastral['PROMEDIO_NUEVE'] >= 40) & (catastral['PROMEDIO_NUEVE'] < 45),
(catastral['PROMEDIO_NUEVE'] >= 45) & (catastral['PROMEDIO_NUEVE'] < 50)]
values = [1, 2, 3, 4]
catastral['RENDIMIENTO_NUEVE'] = pd.Series(pd.cut(catastral['PROMEDIO_NUEVE'], bins=[0, 30, 40, 45, 50], labels=values))

"""# DECIMO SEMESTRE catastral"""

#Lista catastral primer semestre

# Lista para variables de NOTA
NOTAS_catastral_DIEZ = [
    'NOTA_EE_TRES', 'NOTA_VAL', 'NOTA_PLADES', 'NOTA_TG_DOS'
]

# Lista para variables de VECES
VECES_catastral_DIEZ = [
    'VECES_EE_TRES', 'VECES_VAL', 'VECES_PLADES', 'VECES_TG_DOS'
]

# Lista para variables de CREDITOS
CREDITOS_catastral_DIEZ = [
    'CREDITOS_EE_TRES', 'CREDITOS_VAL', 'CREDITOS_PLADES', 'CREDITOS_TG_DOS'
]

promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in catastral.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_catastral_DIEZ, VECES_catastral_DIEZ, CREDITOS_catastral_DIEZ):
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
catastral['PROMEDIO_DIEZ'] = promedios_semestre

# Calcular métricas por semestre
catastral['CAR_DIEZ'] = catastral[VECES_catastral_DIEZ].apply(lambda x: (x > 1).sum(), axis=1)
catastral['NAC_DIEZ'] = catastral[VECES_catastral_DIEZ].apply(lambda x: (x > 0).sum(), axis=1)
catastral['NAA_DIEZ'] = catastral[NOTAS_catastral_DIEZ].apply(lambda x: (x >= 30).sum(), axis=1)
catastral['NAP_DIEZ'] = catastral['NAC_DIEZ'] - catastral['NAA_DIEZ']
catastral['EPA_DIEZ'] = catastral.apply(lambda row: 1 if row['PROMEDIO_DIEZ'] < 30 or row['NAP_DIEZ'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_catastral_DIEZ, CREDITOS_catastral_DIEZ):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados

catastral['NCC_DIEZ'] = catastral.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_catastral_DIEZ, CREDITOS_catastral_DIEZ):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados

catastral['NCA_DIEZ'] = catastral.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

catastral['NCP_DIEZ'] = catastral['NCC_DIEZ'] - catastral['NCA_DIEZ']

# Rendimiento DIEZ
conditions = [(catastral['PROMEDIO_DIEZ'] >= 0) & (catastral['PROMEDIO_DIEZ'] < 30),
(catastral['PROMEDIO_DIEZ'] >= 30) & (catastral['PROMEDIO_DIEZ'] < 40),
(catastral['PROMEDIO_DIEZ'] >= 40) & (catastral['PROMEDIO_DIEZ'] < 45),
(catastral['PROMEDIO_DIEZ'] >= 45) & (catastral['PROMEDIO_DIEZ'] < 50)]
values = [1, 2, 3, 4]
catastral['RENDIMIENTO_DIEZ'] = pd.Series(pd.cut(catastral['PROMEDIO_DIEZ'], bins=[0, 30, 40, 45, 50], labels=values))

# Obtén una lista de todas las columnas que comienzan con "RENDIMIENTO_"
columnas_rendimiento = [col for col in catastral.columns if col.startswith('RENDIMIENTO_')]

# Convertir columnas categóricas a numéricas
catastral[columnas_rendimiento] = catastral[columnas_rendimiento].astype(float)

# Reemplazar los valores vacíos por cero en estas columnas
catastral[columnas_rendimiento] = catastral[columnas_rendimiento].fillna(0)
catastral = catastral.applymap(lambda x: -x if isinstance(x, (int, float)) and x < 0 else x)

catastral = catastral.apply(pd.to_numeric)
catastral.to_csv("catastral.csv", sep=';', index=False)

#------------------------------CSV POR SEMESTRES--------------------------------------------------------#
#------------------------------CSV POR SEMESTRES--------------------------------------------------------#

#En promedio a filtrar es el número mínimo que debe tener un estudiante como promedio de las notas que se toman como variables
año_de_filtro = 2011

"""# INGENIERIA catastral"""

# Primer semestre ingeniería catastral
catastral1 = catastral.loc[:, ['CON_MAT_ICFES', 'IDIOMA_ICFES', 'LOCALIDAD_COLEGIO', 'BIOLOGIA_ICFES', 'QUIMICA_ICFES', 'PG_ICFES', 
    'LITERATURA_ICFES', 'ANO_INGRESO', 'FILOSOFIA_ICFES', 'APT_VERB_ICFES', 'FISICA_ICFES', 'MUNICIPIO', 
    'GENERO', 'APT_MAT_ICFES', 'LOCALIDAD', 'DEPARTAMENTO', 'SOCIALES_ICFES', 'ESTRATO', 'CALENDARIO', 
    'TIPO_COLEGIO', 'DISTANCIA', 'INSCRIPCION', 'CORTE_INGRESO',"RENDIMIENTO_UNO","PROMEDIO_UNO"]]

catastral1 = catastral1 = catastral1.loc[catastral1['ANO_INGRESO'] >= año_de_filtro]
catastral1.to_csv("catastral1.csv", sep=';', index=False)


# Segundo semestre ingeniería catastral
catastral2 = catastral.loc[:, ['NOTA_ALGEBRA', 'NOTA_DITO', 'NOTA_TEXTOS', 'NOTA_CD&C', 'NCA_UNO', 'NAA_UNO', 
    'BIOLOGIA_ICFES', 'NOTA_HIST', 'QUIMICA_ICFES', 'NOTA_SEM', 'FILOSOFIA_ICFES', 
    'IDIOMA_ICFES', 'LITERATURA_ICFES', 'NOTA_DIF', 'CON_MAT_ICFES', 'NAP_UNO', 
    'VECES_HIST', 'VECES_ALGEBRA', 'NCP_UNO', 'GENERO', 'EPA_UNO', 'VECES_DIF', 
    'VECES_DITO', 'VECES_SEM', 'VECES_CD&C', 'VECES_TEXTOS', 'CAR_UNO', 'LOCALIDAD', 
    'NAC_UNO', 'CREDITOS_DIF', 'NCC_UNO', 'CREDITOS_TEXTOS', 'CREDITOS_SEM', 
    'CREDITOS_ALGEBRA','PROMEDIO_UNO', "RENDIMIENTO_DOS","PROMEDIO_DOS"]]

#Se deja solo rendimientos del 1 al 4
catastral2 = catastral2[catastral2['RENDIMIENTO_DOS'].isin([1, 2, 3, 4])]

catastral2.to_csv("catastral2.csv", sep=';', index=False)

# Tercer semestre ingeniería catastral
catastral3 = catastral.loc[:, ['EPA_DOS', 'NOTA_TOP', 'NOTA_PROGB', 'NOTA_FIS_UNO', 'NOTA_HIST', 'LITERATURA_ICFES', 
    'NOTA_INT', 'VECES_TOP', 'NCA_UNO', 'IDIOMA_ICFES', 'NAP_UNO', 'VECES_HIST', 'NOTA_EYB', 
    'NOTA_DIF', 'BIOLOGIA_ICFES', 'NCP_UNO', 'NOTA_DITO', 'NAA_DOS', 'NCA_DOS', 'CAR_DOS', 
    'NOTA_SEM', 'VECES_PROGB', 'VECES_INT', 'CON_MAT_ICFES', 'VECES_ALGEBRA', 'NAC_DOS', 
    'NAA_UNO', 'NAP_DOS', 'NOTA_ALGEBRA', 'NOTA_CD&C', 'NCP_DOS', 'NOTA_ASES', 'NCC_DOS', 
    'VECES_FIS_UNO', 'NOTA_TEXTOS', 'QUIMICA_ICFES', 'FILOSOFIA_ICFES', 'VECES_ASES', 
    'GENERO', 'VECES_EYB', 'CREDITOS_ASES', 'CREDITOS_EYB', 
    'CREDITOS_FIS_UNO', 'CREDITOS_PROGB', 'CREDITOS_TOP','PROMEDIO_DOS','PROMEDIO_UNO','CREDITOS_INT', "RENDIMIENTO_TRES","PROMEDIO_TRES"]]

#Se deja solo rendimientos del 1 al 4
catastral3 = catastral3[catastral3['RENDIMIENTO_TRES'].isin([1, 2, 3, 4])]
catastral3.to_csv("catastral3.csv", sep=';', index=False)

# Cuarto semestre ingeniería catastral
catastral4 = catastral.loc[:, ['NOTA_DIF', 'NOTA_SUELOS', 'NOTA_POO', 'NOTA_FIS_DOS', 'NOTA_TOP', 'NOTA_EYB', 
    'IDIOMA_ICFES', 'NOTA_HIST', 'NOTA_ECUA', 'NOTA_PROGB', 'LITERATURA_ICFES', 
    'NCA_TRES', 'NOTA_FOTO', 'NOTA_FIS_UNO', 'NOTA_CFJC', 'VECES_SUELOS', 'EPA_TRES', 
    'NOTA_MULTI', 'NAP_TRES', 'VECES_POO', 'NOTA_INT', 'NAC_TRES', 'NAP_UNO', 'CAR_TRES', 
    'VECES_FOTO', 'NCC_TRES', 'NCA_UNO', 'NAA_TRES', 'VECES_MULTI', 'NCP_TRES', 
    'VECES_HIST', 'VECES_CFJC', 'VECES_ECUA', 'VECES_FIS_DOS', 'VECES_TOP', 'EPA_DOS', 
    'CREDITOS_ECUA', 'CREDITOS_FIS_DOS', 'CREDITOS_CFJC', 'CREDITOS_FOTO', 'CREDITOS_MULTI', 
    'CREDITOS_POO', 'CREDITOS_SUELOS','PROMEDIO_DOS','PROMEDIO_UNO','PROMEDIO_TRES', "RENDIMIENTO_CUATRO","PROMEDIO_CUATRO"]]

#Se deja solo rendimientos del 1 al 4
catastral4 = catastral4[catastral4['RENDIMIENTO_CUATRO'].isin([1, 2, 3, 4])]
catastral4.to_csv("catastral4.csv", sep=';', index=False)

# Quinto semestre ingeniería catastral
catastral5 = catastral.loc[:, ['NOTA_GEOGEO', 'NOTA_TOP', 'NCA_CUATRO', 'NOTA_SUELOS', 'NOTA_POO', 'NOTA_PRII', 
    'NOTA_FOTO', 'EPA_CUATRO', 'LITERATURA_ICFES', 'NOTA_PROGB', 'NOTA_PROB', 'NOTA_ECUA', 
    'NOTA_CFJC', 'NOTA_FIS_UNO', 'NCC_CUATRO', 'NOTA_L_UNO', 'NAA_CUATRO', 'NAC_CUATRO', 
    'NCP_CUATRO', 'NOTA_CCON', 'IDIOMA_ICFES', 'VECES_FIS_TRES', 'VECES_GEOGEO', 'VECES_PROB', 
    'NOTA_HIST', 'VECES_GH&F', 'VECES_L_UNO', 'VECES_PRII', 'NOTA_FIS_DOS', 'VECES_SUELOS', 
    'NOTA_GH&F', 'NOTA_FIS_TRES', 'NOTA_EYB', 'NOTA_DIF', 'NCA_TRES', 'NAP_CUATRO', 'VECES_CCON', 
    'CAR_CUATRO', 'CREDITOS_L_UNO', 'CREDITOS_CCON', 'CREDITOS_PROB', 
    'CREDITOS_PRII','PROMEDIO_DOS','PROMEDIO_UNO','PROMEDIO_TRES','PROMEDIO_CUATRO', 'CREDITOS_GH&F', 'CREDITOS_GEOGEO', 'CREDITOS_FIS_TRES',
    "RENDIMIENTO_CINCO",'PROMEDIO_CINCO']]

#Se deja solo rendimientos del 1 al 4
catastral5 = catastral5[catastral5['RENDIMIENTO_CINCO'].isin([1, 2, 3, 4])]
catastral5.to_csv("catastral5.csv", sep=';', index=False)


# Sexto semestre ingeniería catastral
catastral6 = catastral.loc[:, ['NOTA_SUELOS', 'NOTAS_SISC', 'NOTA_TOP', 'NOTA_GEOGEO', 'NOTA_POO', 'VECES_BD', 'NOTA_ME', 
    'NOTA_ECUA', 'CAR_CINCO', 'NOTA_PROGB', 'NOTA_FOTO', 'NOTA_CARTO', 'LITERATURA_ICFES', 
    'VECES_CARTO', 'NOTA_CFJC', 'VECES_SISC', 'NCA_CUATRO', 'NOTA_PROB', 'NOTA_AGEO', 'NOTA_BD', 
    'NOTA_PRII', 'NOTA_ECO_UNO', 'VECES_ME', 'VECES_EST', 'NAC_CINCO', 'NCA_CINCO', 'NCC_CINCO', 
    'EPA_CINCO', 'EPA_CUATRO', 'NAP_CINCO', 'NAA_CINCO', 'VECES_ECO_UNO', 'VECES_AGEO', 'NOTA_EST', 
    'NCP_CINCO','PROMEDIO_DOS','PROMEDIO_UNO','PROMEDIO_TRES','PROMEDIO_CUATRO','PROMEDIO_CINCO','CREDITOS_ECO_UNO', 'CREDITOS_EST', 'CREDITOS_BD', 'CREDITOS_AGEO', 
    'CREDITOS_ME', 'CREDITOS_SISC', 'CREDITOS_CARTO', "RENDIMIENTO_SEIS","PROMEDIO_SEIS"]]

#Se deja solo rendimientos del 1 al 4
catastral6 = catastral6[catastral6['RENDIMIENTO_SEIS'].isin([1, 2, 3, 4])]
catastral6.to_csv("catastral6.csv", sep=';', index=False)

# Septimo semestre ingeniería catastral
catastral7 = catastral.loc[:, ['NOTA_GEO_FIS', 'NOTA_L_DOS', 'NOTA_ECUA', 'CAR_CINCO', 'NOTA_CARTO', 'NOTA_LEGIC', 'NOTA_GEOGEO', 
    'NOTA_POO', 'NOTA_CFJC', 'NOTA_INGECO', 'VECES_L_DOS', 'NOTA_SUELOS', 'NOTA_FOTO', 'NAA_SEIS', 
    'NCA_SEIS', 'NOTA_HSE', 'NOTA_SIG', 'NOTA_ME', 'NOTA_EE_UNO', 'NOTA_PROGB', 'CAR_SEIS', 
    'VECES_CARTO', 'NOTA_TOP', 'LITERATURA_ICFES', 'VECES_EE_UNO', 'NOTAS_SISC', 'NCP_SEIS', 
    'VECES_BD', 'NCC_SEIS', 'NAP_SEIS', 'VECES_GEO_FIS', 'VECES_SIG', 'NAC_SEIS', 'EPA_SEIS', 
    'VECES_INGECO','PROMEDIO_DOS','PROMEDIO_UNO','PROMEDIO_CINCO','PROMEDIO_CUATRO','PROMEDIO_SEIS', 'VECES_LEGIC', 'CREDITOS_GEO_FIS', 'CREDITOS_L_DOS', 'CREDITOS_EE_UNO', 
    'CREDITOS_INGECO', 'CREDITOS_LEGIC', 'VECES_HSE', 'CREDITOS_SIG', "RENDIMIENTO_SIETE","PROMEDIO_SIETE"]]

catastral7 = catastral7[catastral7 ['RENDIMIENTO_SIETE'].isin([1, 2, 3, 4])]
catastral7.to_csv("catastral7.csv", sep=';', index=False)

# Octavo semestre ingeniería catastral
catastral8 = catastral.loc[:, ['NOTA_L_DOS', 'NOTA_ECONOMET', 'NOTA_AVAP', 'CAR_CINCO', 'NOTA_POO', 'NOTA_ECUA', 'NOTA_FOTO',
    'NOTA_GEOGEO', 'NOTA_EI_UNO', 'VECES_ECONOMET', 'NOTA_PDI', 'NOTA_INGECO', 'NOTA_CFJC', 
    'NOTA_CARTO', 'NOTA_SUELOS', 'NOTA_EI_DOS', 'NAC_SIETE', 'NCA_SIETE', 'NAP_SIETE', 'NAA_SIETE', 
    'VECES_PDI', 'VECES_EI_UNO', 'NOTA_LEGIC', 'NCC_SIETE', 'VECES_EI_DOS', 'VECES_GEO_SAL', 
    'CAR_SIETE', 'VECES_AVAP', 'VECES_L_DOS', 'NOTA_PROCC', 'NCP_SIETE', 'NOTA_GEO_SAL', 'EPA_SIETE', 
    'NOTA_GEO_FIS','PROMEDIO_DOS','PROMEDIO_CINCO','PROMEDIO_SEIS','PROMEDIO_SIETE', 'VECES_PROCC', 'CREDITOS_AVAP', 'CREDITOS_EI_DOS', 'CREDITOS_ECONOMET', 
    'CREDITOS_EI_UNO', 'CREDITOS_PDI', 'CREDITOS_PROCC', 'CREDITOS_GEO_SAL', "RENDIMIENTO_OCHO","PROMEDIO_OCHO"]]

#Se deja solo rendimientos del 1 al 4
catastral8 = catastral8[catastral8['RENDIMIENTO_OCHO'].isin([1, 2, 3, 4])]
catastral8.to_csv("catastral8.csv", sep=';', index=False)

# Noveno semestre ingeniería catastral
catastral9 = catastral.loc[:, ['NOTA_FOTO', 'NOTA_POO', 'NOTA_L_DOS', 'NOTA_FOTOD', 'NOTA_AVAM', 'NOTA_AVAP', 'NOTA_EI_CUATRO',
    'NOTA_L_TRES', 'NOTA_EI_UNO', 'NOTA_ECONOMET', 'NOTA_FGEP', 'NOTA_ECUA', 'NOTA_GEOGEO', 'NOTA_EI_TRES',
    'NCC_OCHO', 'VECES_FGEP', 'NAC_OCHO', 'VECES_FOTOD', 'NAA_OCHO', 'CAR_CINCO', 'CAR_OCHO', 
    'VECES_EI_CUATRO', 'VECES_L_TRES', 'NCP_OCHO', 'NCA_OCHO', 'EPA_OCHO', 'VECES_AVAM', 'VECES_EI_TRES', 
    'NAP_OCHO', 'CREDITOS_L_TRES','PROMEDIO_CINCO','PROMEDIO_SEIS','PROMEDIO_SIETE','PROMEDIO_OCHO', 'CREDITOS_FOTOD', 'CREDITOS_FGEP', 'CREDITOS_EI_CUATRO', 
    'CREDITOS_AVAM', 'CREDITOS_EI_TRES', "RENDIMIENTO_NUEVE","PROMEDIO_NUEVE"]]

#Se deja solo rendimientos del 1 al 4
catastral9 = catastral9[catastral9['RENDIMIENTO_NUEVE'].isin([1, 2, 3, 4])]
catastral9.to_csv("catastral9.csv", sep=';', index=False)

# Decimo semestre ingeniería catastral
catastral10 = catastral.loc[:, ['NOTA_TG_UNO', 'NOTA_L_DOS', 'NOTA_AVAP', 'NOTA_EI_CINCO', 'NOTA_ECONOMET', 'NOTA_AVAM', 'NOTA_FOTO',
    'NOTA_FGEP', 'NOTA_EI_SEIS', 'NOTA_EE_DOS', 'NOTA_ECUA', 'NOTA_EI_UNO', 'NOTA_L_TRES', 'NOTA_GEOGEO',
    'NOTA_ORD_TER', 'NCC_NUEVE', 'NOTA_POO', 'NCA_NUEVE', 'NAC_NUEVE', 'NAA_NUEVE', 'VECES_EE_DOS', 
    'NOTA_FOTOD', 'VECES_EI_CINCO', 'VECES_ORD_TER', 'NOTA_EI_CUATRO', 'VECES_TG_UNO', 'EPA_NUEVE', 
    'VECES_EI_SEIS','PROMEDIO_CINCO','PROMEDIO_SEIS','PROMEDIO_SIETE','PROMEDIO_NUEVE', 'NCP_NUEVE', 'NAP_NUEVE', 'CREDITOS_EI_CINCO', 'CREDITOS_TG_UNO', 'CREDITOS_ORD_TER',
    'CREDITOS_EI_SEIS', 'CREDITOS_EE_DOS', "RENDIMIENTO_DIEZ","PROMEDIO_DIEZ"]]

#Se deja solo rendimientos del 1 al 4
catastral10 = catastral10[catastral10['RENDIMIENTO_DIEZ'].isin([1, 2, 3, 4])]
catastral10.to_csv("catastral10.csv", sep=';', index=False)

#Archivos catastral por año

#Año 1 catastral
catastralAnio1 = catastral.loc[:, ['CON_MAT_ICFES','IDIOMA_ICFES','BIOLOGIA_ICFES','GENERO','FILOSOFIA_ICFES','LOCALIDAD','LITERATURA_ICFES','QUIMICA_ICFES','PG_ICFES',
              'PROMEDIO_UNO','NOTA_ALGEBRA','NOTA_DITO','NOTA_TEXTOS','NOTA_CD&C','NCA_UNO','NAA_UNO','NOTA_HIST','NOTA_SEM',
              'NOTA_DIF','NAP_UNO','VECES_HIST','VECES_ALGEBRA','NCP_UNO','PROMEDIO_TRES']]

catastralAnio1 = catastralAnio1[catastralAnio1['PROMEDIO_TRES'] > 0]
catastralAnio1.to_csv("catastralAnio1.csv", sep=';', index=False)

#Año 2 catastral
catastralAnio2 = catastral.loc[:, ["CON_MAT_ICFES","IDIOMA_ICFES","BIOLOGIA_ICFES","GENERO","FILOSOFIA_ICFES","LOCALIDAD","LITERATURA_ICFES","QUIMICA_ICFES","PG_ICFES","PROMEDIO_UNO",
              "NOTA_ALGEBRA","NOTA_DITO","NOTA_TEXTOS","NOTA_CD&C","NCA_UNO","NAA_UNO","NOTA_HIST","NOTA_SEM","NOTA_DIF","NAP_UNO","VECES_HIST","VECES_ALGEBRA","NCP_UNO",
              "PROMEDIO_DOS","EPA_DOS","NOTA_TOP","NOTA_PROGB","NOTA_FIS_UNO","NOTA_INT","VECES_TOP","NOTA_EYB","PROMEDIO_TRES","NOTA_SUELOS","NOTA_POO","NOTA_FIS_DOS",
              "NOTA_ECUA","NCA_TRES","NOTA_FOTO","NOTA_CFJC","VECES_SUELOS","PROMEDIO_CINCO"]]

catastralAnio2 = catastralAnio2[catastralAnio2['PROMEDIO_CINCO'] > 0]
catastralAnio2.to_csv("catastralAnio2.csv", sep=';', index=False)

#Año 3 catastral
catastralAnio3 = catastral.loc[:, ["CON_MAT_ICFES","IDIOMA_ICFES","BIOLOGIA_ICFES","GENERO","FILOSOFIA_ICFES","LOCALIDAD","LITERATURA_ICFES","QUIMICA_ICFES","PG_ICFES","PROMEDIO_UNO",
              "NOTA_ALGEBRA","NOTA_DITO","NOTA_TEXTOS","NOTA_CD&C","NCA_UNO","NAA_UNO","NOTA_HIST","NOTA_SEM","NOTA_DIF","NAP_UNO","VECES_HIST","VECES_ALGEBRA","NCP_UNO",
              "PROMEDIO_DOS","EPA_DOS","NOTA_TOP","NOTA_PROGB","NOTA_FIS_UNO","NOTA_INT","VECES_TOP","NOTA_EYB","PROMEDIO_TRES","NOTA_SUELOS","NOTA_POO","NOTA_FIS_DOS",
              "NOTA_ECUA","NCA_TRES","NOTA_FOTO","NOTA_CFJC","VECES_SUELOS","PROMEDIO_CUATRO","NOTA_GEOGEO","NCA_CUATRO","NOTA_PRII","EPA_CUATRO",
              "NOTA_PROB","PROMEDIO_CINCO","NOTAS_SISC","VECES_BD","NOTA_ME","CAR_CINCO","NOTA_CARTO","VECES_CARTO","PROMEDIO_SEIS","NOTA_GEO_FIS","NOTA_L_DOS","NOTA_LEGIC",
              "NOTA_INGECO","VECES_L_DOS","PROMEDIO_SIETE","NOTA_ECONOMET","NOTA_AVAP","NOTA_EI_UNO","PROMEDIO_NUEVE"]]

catastralAnio3 = catastralAnio3[catastralAnio3['PROMEDIO_NUEVE'] > 0]
catastralAnio3.to_csv("catastralAnio3.csv", sep=';', index=False)
