import pandas as pd
import numpy as np
import glob
import csv
import os



#electronica = pd.read_csv(archivo_base_path, sep=',')
#municipios = pd.read_csv(archivo_municipios_path, sep=',')

#merged_df = pd.merge(electronica, municipios, on='MUNICIPIO')
#merged_df = merged_df.drop(columns=['MUNICIPIO'])
#merged_df = merged_df.rename(columns={'NUM_MUNI': 'MUNICIPIO'})
#electronica = merged_df

ruta_archivo = 'C:/Users/User/Desktop/udistrital/electronica_sin_variables.csv'
electronica = pd.read_csv(ruta_archivo, sep=',')

#ruta_archivo_2 = 'C:/Users/User/Desktop/udistrital/municipios_ud.csv'
#municipios = pd.read_csv(ruta_archivo_2, sep=',')


#electronica['DISTANCIA'] = np.where(((electronica['LOCALIDAD'] == 'TEUSAQUILLO') | (electronica['LOCALIDAD'] == 'CHAPINERO') | (electronica['LOCALIDAD'] == 'SANTA FE')) , '1' , np.nan)
#electronica['DISTANCIA'] = np.where(((electronica['LOCALIDAD'] == 'LOS MARTIRES')|(electronica['LOCALIDAD'] == 'LA CANDELARIA')|(electronica['LOCALIDAD'] == 'PUENTE ARANDA')), '2' , electronica['DISTANCIA'])
#electronica['DISTANCIA'] = np.where(((electronica['LOCALIDAD'] == 'BARRIOS UNIDOS')|(electronica['LOCALIDAD'] == 'RAFAEL URIBE URIBE')|(electronica['LOCALIDAD'] == 'ANTONIO NARINO')|(electronica['LOCALIDAD'] == 'ENGATIVA')|(electronica['LOCALIDAD'] == 'KENNEDY')), '3' , electronica['DISTANCIA'])
#electronica['DISTANCIA'] = np.where(((electronica['LOCALIDAD'] == 'FONTIBON')|(electronica['LOCALIDAD'] == 'SAN CRISTOBAL')), '4' , electronica['DISTANCIA'])
#electronica['DISTANCIA'] = np.where(((electronica['LOCALIDAD'] == 'USAQUEN')|(electronica['LOCALIDAD'] == 'BOSA')|(electronica['LOCALIDAD'] == 'SUBA')|(electronica['LOCALIDAD'] == 'TUNJUELITO')|(electronica['LOCALIDAD'] == 'CIUDAD BOLIVAR')), '5' , electronica['DISTANCIA'])
#electronica['DISTANCIA'] = np.where(((electronica['LOCALIDAD'] == 'USME')|(electronica['LOCALIDAD'] == 'FUERA DE BOGOTA')|(electronica['LOCALIDAD'] == 'SOACHA')|(electronica['LOCALIDAD'] == 'SUMAPAZ')), '6' , electronica['DISTANCIA'])
#electronica['DISTANCIA'] = np.where(((electronica['LOCALIDAD'] == 'NO REGISTRA')|(electronica['LOCALIDAD'] == 'SIN LOCALIDAD')), '7' , electronica['DISTANCIA'])

electronica['GENERO'] = electronica['GENERO'].replace({'MASCULINO': 0, 'FEMENINO': 1})
electronica['TIPO_COLEGIO'] = electronica['TIPO_COLEGIO'].replace({'NO REGISTRA': 0, 'OFICIAL': 1, 'NO OFICIAL':2})
electronica['LOCALIDAD_COLEGIO'] = electronica['LOCALIDAD_COLEGIO'].replace({'NO REGISTRA': 0, 'USAQUEN': 1, 'CHAPINERO': 2, 'SANTAFE': 3, 'SANTA FE': 3, 'SAN CRISTOBAL': 4, 'USME': 5, 'TUNJUELITO': 6, 'BOSA': 7, 'KENNEDY': 8, 'FONTIBON': 9, 'ENGATIVA': 10, 'SUBA': 11, 'BARRIOS UNIDOS': 12, 'TEUSAQUILLO': 13, 'LOS MARTIRES': 14, 'ANTONIO NARINO': 15, 'PUENTE ARANDA': 16, 'LA CANDELARIA': 17, 'RAFAEL URIBE URIBE': 18, 'RAFAEL URIBE': 18, 'CIUDAD BOLIVAR': 19, 'FUERA DE BOGOTA': 20, 'SIN LOCALIDAD': 21, 'SOACHA':20})
electronica['CALENDARIO'] = electronica['CALENDARIO'].replace({'NO REGISTRA': 0,'O': 0, 'A': 1, 'B': 2, 'F': 3})
electronica['DEPARTAMENTO'] = electronica['DEPARTAMENTO'].replace({'NO REGISTRA': 0, 'AMAZONAS': 1, 'ANTIOQUIA': 2,'ARAUCA': 3, 'ATLANTICO': 4, 'BOGOTA': 5, 'BOLIVAR': 6, 'BOYACA': 7, 'CALDAS': 8, 'CAQUETA': 9, 'CASANARE': 10, 'CAUCA': 11, 'CESAR': 12, 'CHOCO': 13, 'CORDOBA': 14, 'CUNDINAMARCA': 15, 'GUAINIA': 16, 'GUAVIARE': 17, 'HUILA': 18, 'LA GUAJIRA': 19, 'MAGDALENA':20, 'META': 21, 'NARINO': 22, 'NORTE SANTANDER': 23, 'PUTUMAYO': 24, 'QUINDIO': 25, 'RISARALDA': 26, 'SAN ANDRES Y PROVIDENCIA': 27, 'SANTANDER': 28, 'SUCRE': 29, 'TOLIMA': 30, 'VALLE': 31, 'VAUPES': 32, 'VICHADA': 33})
electronica['LOCALIDAD'] = electronica['LOCALIDAD'].replace({'NO REGISTRA': 0, 'USAQUEN': 1, 'CHAPINERO': 2, 'SANTA FE': 3, 'SAN CRISTOBAL': 4, 'USME': 5, 'TUNJUELITO': 6, 'BOSA': 7, 'KENNEDY': 8, 'FONTIBON': 9, 'ENGATIVA': 10, 'SUBA': 11, 'BARRIOS UNIDOS': 12, 'TEUSAQUILLO': 13, 'LOS MARTIRES': 14, 'ANTONIO NARINO': 15, 'PUENTE ARANDA': 16, 'LA CANDELARIA': 17, 'RAFAEL URIBE URIBE': 18, 'CIUDAD BOLIVAR': 19, 'FUERA DE BOGOTA': 20, 'SIN LOCALIDAD': 20, 'SOACHA': 20, 'SUMAPAZ': 20})
electronica['INSCRIPCION'] = electronica['INSCRIPCION'].replace({'NO REGISTRA': 0, 'BENEFICIARIOS LEY 1081 DE 2006': 1, 'BENEFICIARIOS LEY 1084 DE 2006': 2, 'CONVENIO ANDRES BELLO': 3, 'DESPLAZADOS': 4, 'INDIGENAS': 5, 'MEJORES BACHILLERES COL. DISTRITAL OFICIAL': 6, 'MINORIAS ETNICAS Y CULTURALES': 7, 'MOVILIDAD ACADEMICA INTERNACIONAL': 8, 'NORMAL': 9, 'TRANSFERENCIA EXTERNA': 10, 'TRANSFERENCIA INTERNA': 11,})
electronica['ESTADO_FINAL'] = electronica['ESTADO_FINAL'].replace({'ABANDONO': 1, 'ACTIVO': 2, 'APLAZO': 3, 'CANCELADO': 4, 'EGRESADO': 5, 'INACTIVO': 6, 'MOVILIDAD': 7, 'N.A.': 8, 'NO ESTUDIANTE AC004': 9, 'NO SUP. PRUEBA ACAD.': 10, 'PRUEBA AC Y ACTIVO': 11, 'PRUEBA ACAD': 12, 'RETIRADO': 13, 'TERMINO MATERIAS': 14, 'TERMINO Y MATRICULO': 15, 'VACACIONES': 16})
electronica['MUNICIPIO'] = electronica['MUNICIPIO'].replace({"NO REGISTRA": 0, "ACACIAS": 1, "AGUACHICA": 2, "AGUAZUL": 3, "ALBAN": 4, "ALBAN (SAN JOSE)": 5, "ALVARADO": 6, "ANAPOIMA": 7, "ANOLAIMA": 8, "APARTADO": 9, "ARAUCA": 10, "ARBELAEZ": 11, "ARMENIA": 12, "ATACO": 13, "BARRANCABERMEJA": 14, "BARRANQUILLA": 15, "BELEN DE LOS ANDAQUIES": 16, "BOAVITA": 17, "BOGOTA": 18, "BOJACA": 19, "BOLIVAR": 20, "BUCARAMANGA": 21, "BUENAVENTURA": 22, "CABUYARO": 23, "CACHIPAY": 24, "CAICEDONIA": 25, "CAJAMARCA": 26, "CAJICA": 27, "CALAMAR": 28, "CALARCA": 29, "CALI": 30, "CAMPOALEGRE": 31, "CAPARRAPI": 32, "CAQUEZA": 33, "CARTAGENA": 34, "CASTILLA LA NUEVA": 35, "CERETE": 36, "CHAPARRAL": 37, "CHARALA": 38, "CHIA": 39, "CHIPAQUE": 40, "CHIQUINQUIRA": 41, "CHOACHI": 42, "CHOCONTA": 43, "CIENAGA": 44, "CIRCASIA": 45, "COGUA": 46, "CONTRATACION": 47, "COTA": 48, "CUCUTA": 49, "CUMARAL": 50, "CUMBAL": 51, "CURITI": 52, "CURUMANI": 53, "DUITAMA": 54, "EL BANCO": 55, "EL CARMEN DE BOLIVAR": 56, "EL COLEGIO": 57, "EL CHARCO": 58, "EL DORADO": 59, "EL PASO": 60, "EL ROSAL": 61, "ESPINAL": 62, "FACATATIVA": 63, "FLORENCIA": 64, "FLORIDABLANCA": 65, "FOMEQUE": 66, "FONSECA": 67, "FORTUL": 68, "FOSCA": 69, "FUNZA": 70, "FUSAGASUGA": 71, "GACHETA": 72, "GALERAS (NUEVA GRANADA)": 73, "GAMA": 74, "GARAGOA": 75, "GARZON": 76, "GIGANTE": 77, "GIRARDOT": 78, "GRANADA": 79, "GUACHUCAL": 80, "GUADUAS": 81, "GUAITARILLA": 82, "GUAMO": 83, "GUASCA": 84, "GUATEQUE": 85, "GUAYATA": 86, "GUTIERREZ": 87, "IBAGUE": 88, "INIRIDA": 89, "INZA": 90, "IPIALES": 91, "ITSMINA": 92, "JENESANO": 93, "LA CALERA": 94, "LA DORADA": 95, "LA MESA": 96, "LA PLATA": 97, "LA UVITA": 98, "LA VEGA": 99, "LIBANO": 100, "LOS PATIOS": 101, "MACANAL": 102, "MACHETA": 103, "MADRID": 104, "MAICAO": 105, "MALAGA": 106, "MANAURE BALCON DEL 12": 107, "MANIZALES": 108, "MARIQUITA": 109, "MEDELLIN": 110, "MEDINA": 111, "MELGAR": 112, "MITU": 113, "MOCOA": 114, "MONTERIA": 115, "MONTERREY": 116, "MOSQUERA": 117, "NATAGAIMA": 118, "NEIVA": 119, "NEMOCON": 120, "OCANA": 121, "ORITO": 122, "ORTEGA": 123, "PACHO": 124, "PAEZ (BELALCAZAR)": 125, "PAICOL": 126, "PAILITAS": 127, "PAIPA": 128, "PALERMO": 129, "PALMIRA": 130, "PAMPLONA": 131, "PANDI": 132, "PASCA": 133, "PASTO": 134, "PAZ DE ARIPORO": 135, "PAZ DE RIO": 136, "PITALITO": 137, "POPAYAN": 138, "PUENTE NACIONAL": 139, "PUERTO ASIS": 140, "PUERTO BOYACA": 141, "PUERTO LOPEZ": 142, "PUERTO SALGAR": 143, "PURIFICACION": 144, "QUETAME": 145, "QUIBDO": 146, "RAMIRIQUI": 147, "RICAURTE": 148, "RIOHACHA": 149, "RIVERA": 150, "SABOYA": 151, "SAHAGUN": 152, "SALDAÑA": 153, "SAMACA": 154, "SAMANA": 155, "SAN AGUSTIN": 156, "SAN ANDRES": 157, "SAN BERNARDO": 158, "SAN EDUARDO": 159, "SAN FRANCISCO": 160, "SAN GIL": 161, "SAN JOSE DEL FRAGUA": 162, "SAN JOSE DEL GUAVIARE": 163, "SAN LUIS DE PALENQUE": 164, "SAN MARCOS": 165, "SAN MARTIN": 166, "SANDONA": 167, "SAN VICENTE DEL CAGUAN": 168, "SANTA MARTA": 169, "SANTA SOFIA": 170, "SESQUILE": 171, "SIBATE": 172, "SIBUNDOY": 173, "SILVANIA": 174, "SIMIJACA": 175, "SINCE": 176, "SINCELEJO": 177, "SOACHA": 178, "SOATA": 179, "SOCORRO": 180, "SOGAMOSO": 181, "SOLEDAD": 182, "SOPO": 183, "SORACA": 184, "SOTAQUIRA": 185, "SUAITA": 186, "SUBACHOQUE": 187, "SUESCA": 188, "SUPATA": 189, "SUTAMARCHAN": 190, "SUTATAUSA": 191, "TABIO": 192, "TAMESIS": 193, "TARQUI": 194, "TAUSA": 195, "TENA": 196, "TENJO": 197, "TESALIA": 198, "TIBANA": 199, "TIMANA": 200, "TOCANCIPA": 201, "TUBARA": 202, "TULUA": 203, "TUMACO": 204, "TUNJA": 205, "TURBACO": 206, "TURMEQUE": 207, "UBATE": 208, "UMBITA": 209, "UNE": 210, "VALLEDUPAR": 211, "VELEZ": 212, "VENADILLO": 213, "VENECIA (OSPINA PEREZ)": 214, "VILLA DE LEYVA": 215, "VILLAHERMOSA": 216, "VILLANUEVA": 217, "VILLAPINZON": 218, "VILLAVICENCIO": 219, "VILLETA": 220, "YACOPI": 221, "YOPAL": 222, "ZIPACON": 223, "ZIPAQUIRA": 224})

electronica = electronica.apply(pd.to_numeric)

# Recorrer todas las columnas que comienzan con "CREDITOS_"
for columna in electronica.columns:
    if columna.startswith('CREDITOS_'):
        # Obtener el valor distinto de cero en la columna
        otro_valor = electronica.loc[electronica[columna] != 0, columna].iloc[0]
        # Reemplazar ceros por el otro valor
        electronica[columna] = electronica[columna].replace(0, otro_valor)



"""#PRIMER SEMESTRE electronica"""

# Lista para variables de NOTA
NOTAS_electronica_UNO = ['NOTA_DIF', 'NOTA_FIS_UNO', 'NOTA_CFJC', 'NOTA_TEXTOS', 'NOTA_SEM', 'NOTA_PROGB']

VECES_electronica_UNO = ['VECES_DIF', 'VECES_FIS_UNO', 'VECES_CFJC', 'VECES_TEXTOS', 'VECES_SEM', 'VECES_PROGB']

CREDITOS_electronica_UNO = ['CREDITOS_DIF', 'CREDITOS_FIS_UNO', 'CREDITOS_CFJC', 'CREDITOS_TEXTOS', 'CREDITOS_SEM', 'CREDITOS_PROGB']
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in electronica.iterrows():
    notas_estudiante = []
    creditos_estudiante = []

    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_electronica_UNO, VECES_electronica_UNO, CREDITOS_electronica_UNO):
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
electronica['PROMEDIO_UNO'] = promedios_semestre

# Calcular métricas por semestre
electronica['CAR_UNO'] = electronica[VECES_electronica_UNO].apply(lambda x: (x > 1).sum(), axis=1)
electronica['NAC_UNO'] = electronica[VECES_electronica_UNO].apply(lambda x: (x > 0).sum(), axis=1)
electronica['NAA_UNO'] = electronica[NOTAS_electronica_UNO].apply(lambda x: (x >= 30).sum(), axis=1)
electronica['NAP_UNO'] = electronica['NAC_UNO'] - electronica['NAA_UNO']
electronica['EPA_UNO'] = electronica.apply(lambda row: 1 if row['PROMEDIO_UNO'] < 30 or row['NAP_UNO'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_electronica_UNO, CREDITOS_electronica_UNO):
        if row[veces_col] > 0:
            creditos_cursados += row[creditos_col]
    return creditos_cursados

electronica['NCC_UNO'] = electronica.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_electronica_UNO, CREDITOS_electronica_UNO):
        if row[nota_col] >= 30:
            creditos_aprobados += row[creditos_col]
    return creditos_aprobados

electronica['NCA_UNO'] = electronica.apply(calcular_creditos_aprobados, axis=1)


# Construir NCP

electronica['NCP_UNO'] = electronica['NCC_UNO'] - electronica['NCA_UNO']

# Rendimiento UNO
conditions = [(electronica['PROMEDIO_UNO'] >= 0) & (electronica['PROMEDIO_UNO'] < 30),
(electronica['PROMEDIO_UNO'] >= 30) & (electronica['PROMEDIO_UNO'] < 40),
(electronica['PROMEDIO_UNO'] >= 40) & (electronica['PROMEDIO_UNO'] < 45),
(electronica['PROMEDIO_UNO'] >= 45) & (electronica['PROMEDIO_UNO'] < 50)]
values = [1, 2, 3, 4]
electronica['RENDIMIENTO_UNO'] = pd.Series(pd.cut(electronica['PROMEDIO_UNO'], bins=[0, 30, 40, 45, 50], labels=values))

"""# SEGUNDO SEMRESTRE electronica"""

NOTAS_electronica_DOS = ['NOTA_ALGEBRA', 'NOTA_INT', 'NOTA_HIST', 'NOTA_POO', 'NOTA_FIS_DOS', 'NOTA_CIR_UNO']

VECES_electronica_DOS = ['VECES_ALGEBRA', 'VECES_INT', 'VECES_HIST', 'VECES_POO', 'VECES_FIS_DOS', 'VECES_CIR_UNO']

CREDITOS_electronica_DOS = ['CREDITOS_ALGEBRA', 'CREDITOS_INT', 'CREDITOS_HIST', 'CREDITOS_POO', 'CREDITOS_FIS_DOS', 'CREDITOS_CIR_UNO']

promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in electronica.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_electronica_DOS, VECES_electronica_DOS, CREDITOS_electronica_DOS):
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
electronica['PROMEDIO_DOS'] = promedios_semestre

# Calcular métricas por semestre
electronica['CAR_DOS'] = electronica[VECES_electronica_DOS].apply(lambda x: (x > 1).sum(), axis=1)
electronica['NAC_DOS'] = electronica[VECES_electronica_DOS].apply(lambda x: (x > 0).sum(), axis=1)
electronica['NAA_DOS'] = electronica[NOTAS_electronica_DOS].apply(lambda x: (x >= 30).sum(), axis=1)
electronica['NAP_DOS'] = electronica['NAC_DOS'] - electronica['NAA_DOS']
electronica['EPA_DOS'] = electronica.apply(lambda row: 1 if row['PROMEDIO_DOS'] < 30 or row['NAP_DOS'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_electronica_DOS, CREDITOS_electronica_DOS):
        if row[veces_col] > 0:
            creditos_cursados += row[creditos_col]
    return creditos_cursados

electronica['NCC_DOS'] = electronica.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_electronica_DOS, CREDITOS_electronica_DOS):
        if row[nota_col] >= 30:
            creditos_aprobados += row[creditos_col]
    return creditos_aprobados

electronica['NCA_DOS'] = electronica.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

electronica['NCP_DOS'] = electronica['NCC_DOS'] - electronica['NCA_DOS']

# Rendimiento DOS
conditions = [(electronica['PROMEDIO_DOS'] >= 0) & (electronica['PROMEDIO_DOS'] < 30),
(electronica['PROMEDIO_DOS'] >= 30) & (electronica['PROMEDIO_DOS'] < 40),
(electronica['PROMEDIO_DOS'] >= 40) & (electronica['PROMEDIO_DOS'] < 45),
(electronica['PROMEDIO_DOS'] >= 45) & (electronica['PROMEDIO_DOS'] < 50)]
values = [1, 2, 3, 4]
electronica['RENDIMIENTO_DOS'] = pd.Series(pd.cut(electronica['PROMEDIO_DOS'], bins=[0, 30, 40, 45, 50], labels=values))

"""# TERCER SEMESTRE electronica"""

NOTAS_electronica_TRES = ['NOTA_EE_UNO', 'NOTA_DEM', 'NOTA_MULTI', 'NOTA_CIR_DOS', 'NOTA_FIS_TRES', 'NOTA_ECUA', 'NOTA_EL_UNO']

VECES_electronica_TRES = ['VECES_EE_UNO', 'VECES_DEM', 'VECES_MULTI', 'VECES_CIR_DOS', 'VECES_FIS_TRES', 'VECES_ECUA', 'VECES_EL_UNO']

CREDITOS_electronica_TRES = ['CREDITOS_EE_UNO', 'CREDITOS_DEM', 'CREDITOS_MULTI', 'CREDITOS_CIR_DOS', 'CREDITOS_FIS_TRES', 'CREDITOS_ECUA', 'CREDITOS_EL_UNO']

promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in electronica.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_electronica_TRES, VECES_electronica_TRES, CREDITOS_electronica_TRES):
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
electronica['PROMEDIO_TRES'] = promedios_semestre

# Calcular métricas por semestre
electronica['CAR_TRES'] = electronica[VECES_electronica_TRES].apply(lambda x: (x > 1).sum(), axis=1)
electronica['NAC_TRES'] = electronica[VECES_electronica_TRES].apply(lambda x: (x > 0).sum(), axis=1)
electronica['NAA_TRES'] = electronica[NOTAS_electronica_TRES].apply(lambda x: (x >= 30).sum(), axis=1)
electronica['NAP_TRES'] = electronica['NAC_TRES'] - electronica['NAA_TRES']
electronica['EPA_TRES'] = electronica.apply(lambda row: 1 if row['PROMEDIO_TRES'] < 30 or row['NAP_TRES'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_electronica_TRES, CREDITOS_electronica_TRES):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados
electronica['NCC_TRES'] = electronica.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_electronica_TRES, CREDITOS_electronica_TRES):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados
electronica['NCA_TRES'] = electronica.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

electronica['NCP_TRES'] = electronica['NCC_TRES'] - electronica['NCA_TRES']

# Rendimiento TRES
conditions = [(electronica['PROMEDIO_TRES'] >= 0) & (electronica['PROMEDIO_TRES'] < 30),
(electronica['PROMEDIO_TRES'] >= 30) & (electronica['PROMEDIO_TRES'] < 40),
(electronica['PROMEDIO_TRES'] >= 40) & (electronica['PROMEDIO_TRES'] < 45),
(electronica['PROMEDIO_TRES'] >= 45) & (electronica['PROMEDIO_TRES'] < 50)]
values = [1, 2, 3, 4]
electronica['RENDIMIENTO_TRES'] = pd.Series(pd.cut(electronica['PROMEDIO_TRES'], bins=[0, 30, 40, 45, 50], labels=values))

"""# CUARTO SEMESTRE electronica"""

NOTAS_electronica_CUATRO = ['NOTA_L_UNO', 'NOTA_PYE_UNO', 'NOTA_VARCOM', 'NOTA_EL_DOS', 'NOTA_PROGAPL', 'NOTA_CAMPOS', 'NOTA_FCD']

VECES_electronica_CUATRO = ['VECES_L_UNO', 'VECES_PYE_UNO', 'VECES_VARCOM', 'VECES_EL_DOS', 'VECES_PROGAPL', 'VECES_CAMPOS', 'VECES_FCD']

CREDITOS_electronica_CUATRO = ['CREDITOS_L_UNO', 'CREDITOS_PYE_UNO', 'CREDITOS_VARCOM', 'CREDITOS_EL_DOS', 'CREDITOS_PROGAPL', 'CREDITOS_CAMPOS', 'CREDITOS_FCD']

promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in electronica.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_electronica_CUATRO, VECES_electronica_CUATRO, CREDITOS_electronica_CUATRO):
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
electronica['PROMEDIO_CUATRO'] = promedios_semestre

# Calcular métricas por semestre
electronica['CAR_CUATRO'] = electronica[VECES_electronica_CUATRO].apply(lambda x: (x > 1).sum(), axis=1)
electronica['NAC_CUATRO'] = electronica[VECES_electronica_CUATRO].apply(lambda x: (x > 0).sum(), axis=1)
electronica['NAA_CUATRO'] = electronica[NOTAS_electronica_CUATRO].apply(lambda x: (x >= 30).sum(), axis=1)
electronica['NAP_CUATRO'] = electronica['NAC_CUATRO'] - electronica['NAA_CUATRO']
electronica['EPA_CUATRO'] = electronica.apply(lambda row: 1 if row['PROMEDIO_CUATRO'] < 30 or row['NAP_CUATRO'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_electronica_CUATRO, CREDITOS_electronica_CUATRO):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados
electronica['NCC_CUATRO'] = electronica.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_electronica_CUATRO, CREDITOS_electronica_CUATRO):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados
electronica['NCA_CUATRO'] = electronica.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

electronica['NCP_CUATRO'] = electronica['NCC_CUATRO'] - electronica['NCA_CUATRO']

# Rendimiento CUATRO
conditions = [(electronica['PROMEDIO_CUATRO'] >= 0) & (electronica['PROMEDIO_CUATRO'] < 30),
(electronica['PROMEDIO_CUATRO'] >= 30) & (electronica['PROMEDIO_CUATRO'] < 40),
(electronica['PROMEDIO_CUATRO'] >= 40) & (electronica['PROMEDIO_CUATRO'] < 45),
(electronica['PROMEDIO_CUATRO'] >= 45) & (electronica['PROMEDIO_CUATRO'] < 50)]
values = [1, 2, 3, 4]
electronica['RENDIMIENTO_CUATRO'] = pd.Series(pd.cut(electronica['PROMEDIO_CUATRO'], bins=[0, 30, 40, 45, 50], labels=values))

"""# QUINTO SEMESTRE electronica"""

# Lista electronica quinto semestre

NOTAS_electronica_CINCO = ['NOTA_EE_DOS', 'NOTA_ONDAS', 'NOTA_FOU', 'NOTA_TFM', 'NOTA_EL_TRES', 'NOTA_ADMICRO']

VECES_electronica_CINCO = ['VECES_EE_DOS', 'VECES_ONDAS', 'VECES_FOU', 'VECES_TFM', 'VECES_EL_TRES', 'VECES_ADMICRO']

CREDITOS_electronica_CINCO = ['CREDITOS_EE_DOS', 'CREDITOS_ONDAS', 'CREDITOS_FOU', 'CREDITOS_TFM', 'CREDITOS_EL_TRES', 'CREDITOS_ADMICRO']

promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in electronica.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_electronica_CINCO, VECES_electronica_CINCO, CREDITOS_electronica_CINCO):
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
electronica['PROMEDIO_CINCO'] = promedios_semestre

# Calcular métricas por semestre
electronica['CAR_CINCO'] = electronica[VECES_electronica_CINCO].apply(lambda x: (x > 1).sum(), axis=1)
electronica['NAC_CINCO'] = electronica[VECES_electronica_CINCO].apply(lambda x: (x > 0).sum(), axis=1)
electronica['NAA_CINCO'] = electronica[NOTAS_electronica_CINCO].apply(lambda x: (x >= 30).sum(), axis=1)
electronica['NAP_CINCO'] = electronica['NAC_CINCO'] - electronica['NAA_CINCO']
electronica['EPA_CINCO'] = electronica.apply(lambda row: 1 if row['PROMEDIO_CINCO'] < 30 or row['NAP_CINCO'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_electronica_CINCO, CREDITOS_electronica_CINCO):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados
electronica['NCC_CINCO'] = electronica.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_electronica_CINCO, CREDITOS_electronica_CINCO):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados
electronica['NCA_CINCO'] = electronica.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

electronica['NCP_CINCO'] = electronica['NCC_CINCO'] - electronica['NCA_CINCO']

# Rendimiento CINCO
conditions = [(electronica['PROMEDIO_CINCO'] >= 0) & (electronica['PROMEDIO_CINCO'] < 30),
(electronica['PROMEDIO_CINCO'] >= 30) & (electronica['PROMEDIO_CINCO'] < 40),
(electronica['PROMEDIO_CINCO'] >= 40) & (electronica['PROMEDIO_CINCO'] < 45),
(electronica['PROMEDIO_CINCO'] >= 45) & (electronica['PROMEDIO_CINCO'] < 50)]
values = [1, 2, 3, 4]
electronica['RENDIMIENTO_CINCO'] = pd.Series(pd.cut(electronica['PROMEDIO_CINCO'], bins=[0, 30, 40, 45, 50], labels=values))

"""# SEXTO SEMESTRE electronica"""

NOTAS_electronica_SEIS = ['NOTA_L_DOS', 'NOTA_EE_TRES', 'NOTA_COMANA', 'NOTA_MOYGE', 'NOTA_DDM', 'NOTAS_SYS', 'NOTA_CCON']

VECES_electronica_SEIS = ['VECES_L_DOS', 'VECES_EE_TRES', 'VECES_COMANA', 'VECES_COYGE', 'VECES_DDM', 'VECES_SYS', 'VECES_CCON']

CREDITOS_electronica_SEIS = ['CREDITOS_L_DOS', 'CREDITOS_EE_TRES', 'CREDITOS_COMANA', 'CREDITOS_COYGE', 'CREDITOS_DDM', 'CREDITOS_SYS', 'CREDITOS_CCON']

promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in electronica.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_electronica_SEIS, VECES_electronica_SEIS, CREDITOS_electronica_SEIS):
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
electronica['PROMEDIO_SEIS'] = promedios_semestre

# Calcular métricas por semestre
electronica['CAR_SEIS'] = electronica[VECES_electronica_SEIS].apply(lambda x: (x > 1).sum(), axis=1)
electronica['NAC_SEIS'] = electronica[VECES_electronica_SEIS].apply(lambda x: (x > 0).sum(), axis=1)
electronica['NAA_SEIS'] = electronica[NOTAS_electronica_SEIS].apply(lambda x: (x >= 30).sum(), axis=1)
electronica['NAP_SEIS'] = electronica['NAC_SEIS'] - electronica['NAA_SEIS']
electronica['EPA_SEIS'] = electronica.apply(lambda row: 1 if row['PROMEDIO_SEIS'] < 30 or row['NAP_SEIS'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_electronica_SEIS, CREDITOS_electronica_SEIS):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados
electronica['NCC_SEIS'] = electronica.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_electronica_SEIS, CREDITOS_electronica_SEIS):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados

electronica['NCA_SEIS'] = electronica.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

electronica['NCP_SEIS'] = electronica['NCC_SEIS'] - electronica['NCA_SEIS']

# Rendimiento SEIS
conditions = [(electronica['PROMEDIO_SEIS'] >= 0) & (electronica['PROMEDIO_SEIS'] < 30),
(electronica['PROMEDIO_SEIS'] >= 30) & (electronica['PROMEDIO_SEIS'] < 40),
(electronica['PROMEDIO_SEIS'] >= 40) & (electronica['PROMEDIO_SEIS'] < 45),
(electronica['PROMEDIO_SEIS'] >= 45) & (electronica['PROMEDIO_SEIS'] < 50)]
values = [1, 2, 3, 4]
electronica['RENDIMIENTO_SEIS'] = pd.Series(pd.cut(electronica['PROMEDIO_SEIS'], bins=[0, 30, 40, 45, 50], labels=values))

"""# SEPTIMO SEMESTRE electronica"""

#Lista electronica primer semestre

NOTAS_electronica_SIETE = ['NOTA_L_TRES', 'NOTA_COMDIG', 'NOTA_FDS', 'NOTA_HSE', 'NOTA_SISDIN', 'NOTA_ELECPOT', 'NOTA_ECO']

VECES_electronica_SIETE = ['VECES_L_TRES', 'VECES_COMDIG', 'VECES_FDS', 'VECES_HSE', 'VECES_SISDIN', 'VECES_ELECPOT', 'VECES_ECO']

CREDITOS_electronica_SIETE = ['CREDITOS_L_TRES', 'CREDITOS_COMDIG', 'CREDITOS_FDS', 'CREDITOS_HSE', 'CREDITOS_SISDIN', 'CREDITOS_ELECPOT', 'CREDITOS_ECO']

promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in electronica.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_electronica_SIETE, VECES_electronica_SIETE, CREDITOS_electronica_SIETE):
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
electronica['PROMEDIO_SIETE'] = promedios_semestre

# Calcular métricas por semestre
electronica['CAR_SIETE'] = electronica[VECES_electronica_SIETE].apply(lambda x: (x > 1).sum(), axis=1)
electronica['NAC_SIETE'] = electronica[VECES_electronica_SIETE].apply(lambda x: (x > 0).sum(), axis=1)
electronica['NAA_SIETE'] = electronica[NOTAS_electronica_SIETE].apply(lambda x: (x >= 30).sum(), axis=1)
electronica['NAP_SIETE'] = electronica['NAC_SIETE'] - electronica['NAA_SIETE']
electronica['EPA_SIETE'] = electronica.apply(lambda row: 1 if row['PROMEDIO_SIETE'] < 30 or row['NAP_SIETE'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_electronica_SIETE, CREDITOS_electronica_SIETE):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados

electronica['NCC_SIETE'] = electronica.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_electronica_SIETE, CREDITOS_electronica_SIETE):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados

electronica['NCA_SIETE'] = electronica.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

electronica['NCP_SIETE'] = electronica['NCC_SIETE'] - electronica['NCA_SIETE']

# Rendimiento SIETE
conditions = [(electronica['PROMEDIO_SIETE'] >= 0) & (electronica['PROMEDIO_SIETE'] < 30),
(electronica['PROMEDIO_SIETE'] >= 30) & (electronica['PROMEDIO_SIETE'] < 40),
(electronica['PROMEDIO_SIETE'] >= 40) & (electronica['PROMEDIO_SIETE'] < 45),
(electronica['PROMEDIO_SIETE'] >= 45) & (electronica['PROMEDIO_SIETE'] < 50)]
values = [1, 2, 3, 4]
electronica['RENDIMIENTO_SIETE'] = pd.Series(pd.cut(electronica['PROMEDIO_SIETE'], bins=[0, 30, 40, 45, 50], labels=values))

"""# OCTAVO SEMESTRE electronica"""

NOTAS_electronica_OCHO = ['NOTA_TELEC_UNO', 'NOTA_TELEMA_UNO', 'NOTA_C_UNO', 'NOTA_INSIND', 'NOTA_BIOING_UNO', 'NOTA_INGECO', 'NOTA_STG', 'NOTAS_BDATOS']

VECES_electronica_OCHO = ['VECES_TELEC_UNO', 'VECES_TELEMA_UNO', 'VECES_C_UNO', 'VECES_INSIND', 'VECES_BIOING_UNO', 'VECES_INGECO', 'VECES_STG', 'VECES_BDATOS']

CREDITOS_electronica_OCHO = ['CREDITOS_TELEC_UNO', 'CREDITOS_TELEMA_UNO', 'CREDITOS_C_UNO', 'CREDITOS_INSIND', 'CREDITOS_BIOING_UNO', 'CREDITOS_INGECO', 'CREDITOS_STG', 'CREDITOS_BDATOS']

promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in electronica.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_electronica_OCHO, VECES_electronica_OCHO, CREDITOS_electronica_OCHO):
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
electronica['PROMEDIO_OCHO'] = promedios_semestre

# Calcular métricas por semestre
electronica['CAR_OCHO'] = electronica[VECES_electronica_OCHO].apply(lambda x: (x > 1).sum(), axis=1)
electronica['NAC_OCHO'] = electronica[VECES_electronica_OCHO].apply(lambda x: (x > 0).sum(), axis=1)
electronica['NAA_OCHO'] = electronica[NOTAS_electronica_OCHO].apply(lambda x: (x >= 30).sum(), axis=1)
electronica['NAP_OCHO'] = electronica['NAC_OCHO'] - electronica['NAA_OCHO']
electronica['EPA_OCHO'] = electronica.apply(lambda row: 1 if row['PROMEDIO_OCHO'] < 30 or row['NAP_OCHO'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_electronica_OCHO, CREDITOS_electronica_OCHO):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados

electronica['NCC_OCHO'] = electronica.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_electronica_OCHO, CREDITOS_electronica_OCHO):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados
electronica['NCA_OCHO'] = electronica.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

electronica['NCP_OCHO'] = electronica['NCC_OCHO'] - electronica['NCA_OCHO']

# Rendimiento OCHO
conditions = [(electronica['PROMEDIO_OCHO'] >= 0) & (electronica['PROMEDIO_OCHO'] < 30),
(electronica['PROMEDIO_OCHO'] >= 30) & (electronica['PROMEDIO_OCHO'] < 40),
(electronica['PROMEDIO_OCHO'] >= 40) & (electronica['PROMEDIO_OCHO'] < 45),
(electronica['PROMEDIO_OCHO'] >= 45) & (electronica['PROMEDIO_OCHO'] < 50)]
values = [1, 2, 3, 4]
electronica['RENDIMIENTO_OCHO'] = pd.Series(pd.cut(electronica['PROMEDIO_OCHO'], bins=[0, 30, 40, 45, 50], labels=values))

"""# NOVENO SEMESTRE electronica"""

NOTAS_electronica_NUEVE = ['NOTA_EI_IA', 'NOTA_EI_IIA', 'NOTA_EI_IIIA', 'NOTA_TRABGRAD', 'NOTA_TV', 'NOTA_FGEP']

VECES_electronica_NUEVE = ['VECES_EI_IA', 'VECES_EI_IIA', 'VECES_EI_IIIA', 'VECES_TRABGRAD', 'VECES_TV', 'VECES_FGEP']

CREDITOS_electronica_NUEVE = ['CREDITOS_EI_IA', 'CREDITOS_EI_IIA', 'CREDITOS_EI_IIIA', 'CREDITOS_TRABGRAD', 'CREDITOS_TV', 'CREDITOS_FGEP']

promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in electronica.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_electronica_NUEVE, VECES_electronica_NUEVE, CREDITOS_electronica_NUEVE):
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
electronica['PROMEDIO_NUEVE'] = promedios_semestre

# Calcular métricas por semestre
electronica['CAR_NUEVE'] = electronica[VECES_electronica_NUEVE].apply(lambda x: (x > 1).sum(), axis=1)
electronica['NAC_NUEVE'] = electronica[VECES_electronica_NUEVE].apply(lambda x: (x > 0).sum(), axis=1)
electronica['NAA_NUEVE'] = electronica[NOTAS_electronica_NUEVE].apply(lambda x: (x >= 30).sum(), axis=1)
electronica['NAP_NUEVE'] = electronica['NAC_NUEVE'] - electronica['NAA_NUEVE']
electronica['EPA_NUEVE'] = electronica.apply(lambda row: 1 if row['PROMEDIO_NUEVE'] < 30 or row['NAP_NUEVE'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_electronica_NUEVE, CREDITOS_electronica_NUEVE):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados
electronica['NCC_NUEVE'] = electronica.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_electronica_NUEVE, CREDITOS_electronica_NUEVE):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados
electronica['NCA_NUEVE'] = electronica.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

electronica['NCP_NUEVE'] = electronica['NCC_NUEVE'] - electronica['NCA_NUEVE']

# Rendimiento NUEVE
conditions = [(electronica['PROMEDIO_NUEVE'] >= 0) & (electronica['PROMEDIO_NUEVE'] < 30),
(electronica['PROMEDIO_NUEVE'] >= 30) & (electronica['PROMEDIO_NUEVE'] < 40),
(electronica['PROMEDIO_NUEVE'] >= 40) & (electronica['PROMEDIO_NUEVE'] < 45),
(electronica['PROMEDIO_NUEVE'] >= 45) & (electronica['PROMEDIO_NUEVE'] < 50)]
values = [1, 2, 3, 4]
electronica['RENDIMIENTO_NUEVE'] = pd.Series(pd.cut(electronica['PROMEDIO_NUEVE'], bins=[0, 30, 40, 45, 50], labels=values))

"""# DECIMO SEMESTRE electronica"""

NOTAS_electronica_DIEZ = ['NOTA_EI_IB', 'NOTA_EI_IIB', 'NOTA_EI_IIIB', 'NOTA_EE_CUATRO', 'NOTA_EYB', 'NOTA_ELEC_IND', 'NOTA_TGDOS']

VECES_electronica_DIEZ = ['VECES_EI_IB', 'VECES_EI_IIB', 'VECES_EI_IIIB', 'VECES_EE_CUATRO', 'VECES_EYB', 'VECES_ELEC_IND', 'VECES_TGDOS']

CREDITOS_electronica_DIEZ = ['CREDITOS_EI_IB', 'CREDITOS_EI_IIB', 'CREDITOS_EI_IIIB', 'CREDITOS_EE_CUATRO', 'CREDITOS_EYB', 'CREDITOS_ELEC_IND', 'CREDITOS_TGDOS']

promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in electronica.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_electronica_DIEZ, VECES_electronica_DIEZ, CREDITOS_electronica_DIEZ):
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
electronica['PROMEDIO_DIEZ'] = promedios_semestre

# Calcular métricas por semestre
electronica['CAR_DIEZ'] = electronica[VECES_electronica_DIEZ].apply(lambda x: (x > 1).sum(), axis=1)
electronica['NAC_DIEZ'] = electronica[VECES_electronica_DIEZ].apply(lambda x: (x > 0).sum(), axis=1)
electronica['NAA_DIEZ'] = electronica[NOTAS_electronica_DIEZ].apply(lambda x: (x >= 30).sum(), axis=1)
electronica['NAP_DIEZ'] = electronica['NAC_DIEZ'] - electronica['NAA_DIEZ']
electronica['EPA_DIEZ'] = electronica.apply(lambda row: 1 if row['PROMEDIO_DIEZ'] < 30 or row['NAP_DIEZ'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_electronica_DIEZ, CREDITOS_electronica_DIEZ):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados

electronica['NCC_DIEZ'] = electronica.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_electronica_DIEZ, CREDITOS_electronica_DIEZ):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados

electronica['NCA_DIEZ'] = electronica.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

electronica['NCP_DIEZ'] = electronica['NCC_DIEZ'] - electronica['NCA_DIEZ']

# Rendimiento DIEZ
conditions = [(electronica['PROMEDIO_DIEZ'] >= 0) & (electronica['PROMEDIO_DIEZ'] < 30),
(electronica['PROMEDIO_DIEZ'] >= 30) & (electronica['PROMEDIO_DIEZ'] < 40),
(electronica['PROMEDIO_DIEZ'] >= 40) & (electronica['PROMEDIO_DIEZ'] < 45),
(electronica['PROMEDIO_DIEZ'] >= 45) & (electronica['PROMEDIO_DIEZ'] < 50)]
values = [1, 2, 3, 4]
electronica['RENDIMIENTO_DIEZ'] = pd.Series(pd.cut(electronica['PROMEDIO_DIEZ'], bins=[0, 30, 40, 45, 50], labels=values))

# Obtén una lista de todas las columnas que comienzan con "RENDIMIENTO_"
columnas_rendimiento = [col for col in electronica.columns if col.startswith('RENDIMIENTO_')]

# Convertir columnas categóricas a numéricas
electronica[columnas_rendimiento] = electronica[columnas_rendimiento].astype(float)

# Reemplazar los valores vacíos por cero en estas columnas
electronica[columnas_rendimiento] = electronica[columnas_rendimiento].fillna(0)
electronica = electronica.applymap(lambda x: -x if isinstance(x, (int, float)) and x < 0 else x)

electronica = electronica.apply(pd.to_numeric)
electronica.to_csv("electronica.csv", sep=';', index=False)

#------------------------------CSV POR SEMESTRES--------------------------------------------------------#
#------------------------------CSV POR SEMESTRES--------------------------------------------------------#

#En promedio a filtrar es el número mínimo que debe tener un estudiante como promedio de las notas que se toman como variables
año_de_filtro = 2011

"""# INGENIERIA electronica"""

# Primer semestre ingeniería electronica
electronica1 = electronica.loc[:, ['CON_MAT_ICFES', 'IDIOMA_ICFES', 'LOCALIDAD_COLEGIO', 'BIOLOGIA_ICFES', 'QUIMICA_ICFES', 'PG_ICFES', 
    'LITERATURA_ICFES', 'ANO_INGRESO', 'FILOSOFIA_ICFES', 'APT_VERB_ICFES', 'FISICA_ICFES', 'MUNICIPIO', 
    'GENERO', 'APT_MAT_ICFES', 'LOCALIDAD', 'DEPARTAMENTO', 'SOCIALES_ICFES', 'ESTRATO', 'CALENDARIO', 
    'TIPO_COLEGIO', 'DISTANCIA', 'INSCRIPCION', 'CORTE_INGRESO',"RENDIMIENTO_UNO","PROMEDIO_UNO"]]

electronica1 = electronica1 = electronica1.loc[electronica1['ANO_INGRESO'] >= año_de_filtro]
electronica1.to_csv("electronica1.csv", sep=';', index=False)


# Segundo semestre ingeniería electronica
electronica2 = electronica.loc[:, ['PROMEDIO_UNO','NOTA_DIF','CON_MAT_ICFES','EPA_UNO','FISICA_ICFES','PG_ICFES','NOTA_PROGB','NOTA_FIS_UNO','BIOLOGIA_ICFES','IDIOMA_ICFES','LITERATURA_ICFES','NCP_UNO','NOTA_TEXTOS','NOTA_CFJC','NAP_UNO','NOTA_SEM','NCC_UNO','GENERO','LOCALIDAD','VECES_TEXTOS','NAA_UNO','NCA_UNO','VECES_DIF','VECES_SEM','NAC_UNO','CAR_UNO','QUIMICA_ICFES','VECES_CFJC','VECES_FIS_UNO','VECES_PROGB', "RENDIMIENTO_DOS","PROMEDIO_DOS"]]

#Se deja solo rendimientos del 1 al 4
electronica2 = electronica2[electronica2['RENDIMIENTO_DOS'].isin([1, 2, 3, 4])]

electronica2.to_csv("electronica2.csv", sep=';', index=False)

# Tercer semestre ingeniería electronica
electronica3 = electronica.loc[:, ['PROMEDIO_DOS','PG_ICFES','BIOLOGIA_ICFES','NAA_DOS','FISICA_ICFES','NOTA_INT','PROMEDIO_UNO','VECES_INT','NCA_DOS','NOTA_FIS_DOS','CON_MAT_ICFES','CAR_DOS','VECES_CIR_UNO','NOTA_HIST','NOTA_FIS_UNO','NOTA_DIF','NOTA_CIR_UNO','NCP_UNO','LITERATURA_ICFES','EPA_DOS','NAP_UNO','NAP_DOS','NOTA_ALGEBRA','NOTA_CFJC','NOTA_TEXTOS','NCC_DOS','VECES_FIS_DOS','NOTA_PROGB','VECES_HIST','VECES_ALGEBRA','NOTA_POO','EPA_UNO','IDIOMA_ICFES','NAC_DOS','NCP_DOS','VECES_POO','CREDITOS_POO','CREDITOS_INT','CREDITOS_HIST','CREDITOS_FIS_DOS','CREDITOS_CIR_UNO','CREDITOS_ALGEBRA', "RENDIMIENTO_TRES","PROMEDIO_TRES"]]

#Se deja solo rendimientos del 1 al 4
electronica3 = electronica3[electronica3['RENDIMIENTO_TRES'].isin([1, 2, 3, 4])]
electronica3.to_csv("electronica3.csv", sep=';', index=False)

# Cuarto semestre ingeniería electronica
electronica4 = electronica.loc[:, ['PROMEDIO_TRES','PROMEDIO_DOS','NOTA_INT','NCA_DOS','NCA_TRES','NOTA_FIS_DOS','PG_ICFES','NOTA_FIS_TRES','BIOLOGIA_ICFES','VECES_FIS_TRES','CON_MAT_ICFES','PROMEDIO_UNO','FISICA_ICFES','NOTA_EL_UNO','NOTA_DEM','NAA_TRES','VECES_INT','NAA_DOS','NOTA_CIR_DOS','VECES_CIR_DOS','NAC_TRES','NAP_TRES','NCC_TRES','EPA_TRES','CAR_TRES','VECES_EL_UNO','VECES_MULTI','NCP_TRES','NOTA_EE_UNO','VECES_DEM','VECES_ECUA','NOTA_ECUA','CAR_DOS','NOTA_MULTI','CREDITOS_MULTI','CREDITOS_FIS_TRES','CREDITOS_EL_UNO', "RENDIMIENTO_CUATRO","PROMEDIO_CUATRO"]]

#Se deja solo rendimientos del 1 al 4
electronica4 = electronica4[electronica4['RENDIMIENTO_CUATRO'].isin([1, 2, 3, 4])]
electronica4.to_csv("electronica4.csv", sep=';', index=False)

# Quinto semestre ingeniería electronica
electronica5 = electronica.loc[:, ['PROMEDIO_TRES','PG_ICFES','NOTA_FIS_DOS','NOTA_EL_DOS','NOTA_CAMPOS','NOTA_FCD','FISICA_ICFES','VECES_FCD','BIOLOGIA_ICFES','CON_MAT_ICFES','NOTA_PROGAPL','PROMEDIO_CUATRO','NOTA_VARCOM','NCA_TRES','NOTA_INT','NCP_CUATRO','NCA_CUATRO','NAP_CUATRO','NOTA_PYE_UNO','NCC_CUATRO','NOTA_FIS_TRES','NAC_CUATRO','NCA_DOS','VECES_PYE_UNO','VECES_PROGAPL','NAA_CUATRO','VECES_FIS_TRES','VECES_EL_DOS','VECES_VARCOM','NOTA_L_UNO','CAR_CUATRO','PROMEDIO_DOS','VECES_L_UNO','EPA_CUATRO','PROMEDIO_UNO','VECES_CAMPOS','CREDITOS_FCD','CREDITOS_VARCOM','CREDITOS_CAMPOS','CREDITOS_L_UNO','CREDITOS_PROGAPL','CREDITOS_PYE_UNO',"RENDIMIENTO_CINCO",'PROMEDIO_CINCO']]

#Se deja solo rendimientos del 1 al 4
electronica5 = electronica5[electronica5['RENDIMIENTO_CINCO'].isin([1, 2, 3, 4])]
electronica5.to_csv("electronica5.csv", sep=';', index=False)


# Sexto semestre ingeniería electronica
electronica6 = electronica.loc[:, ['NOTA_EE_DOS','NCC_CINCO','NOTA_ADMICRO','PROMEDIO_TRES','NOTA_FCD','NAP_CINCO','NOTA_VARCOM','NOTA_TFM','PROMEDIO_CINCO','VECES_ADMICRO','PG_ICFES','CON_MAT_ICFES','FISICA_ICFES','NAC_CINCO','NCA_CINCO','NOTA_EL_DOS','PROMEDIO_CUATRO','NOTA_ONDAS','EPA_CINCO','NOTA_CAMPOS','BIOLOGIA_ICFES','VECES_FOU','VECES_ONDAS','NOTA_EL_TRES','CAR_CINCO','NCP_CINCO','NAA_CINCO','NOTA_FOU','VECES_EL_TRES','VECES_TFM','NOTA_PROGAPL','NOTA_FIS_DOS','VECES_EE_DOS','VECES_FCD','CREDITOS_FOU','CREDITOS_EL_TRES','CREDITOS_EE_DOS','CREDITOS_ADMICRO', "RENDIMIENTO_SEIS","PROMEDIO_SEIS"]]

#Se deja solo rendimientos del 1 al 4
electronica6 = electronica6[electronica6['RENDIMIENTO_SEIS'].isin([1, 2, 3, 4])]
electronica6.to_csv("electronica6.csv", sep=';', index=False)

# Septimo semestre ingeniería electronica
electronica7 = electronica.loc[:, ['PROMEDIO_TRES','NOTA_TFM','NOTA_VARCOM','NOTA_COMANA','CON_MAT_ICFES','PROMEDIO_CINCO','NOTA_CCON','VECES_ADMICRO','VECES_COMANA','VECES_DDM','PROMEDIO_SEIS','PG_ICFES','NAC_SEIS','NAA_SEIS','NOTA_MOYGE','NOTAS_SYS','NOTA_ADMICRO','NOTA_FCD','NOTA_L_DOS','NCP_SEIS','VECES_L_DOS','CAR_SEIS','VECES_SYS','NOTA_DDM','NCC_CINCO','NCA_SEIS','NAP_SEIS','NAP_CINCO','NOTA_EE_TRES','NCC_SEIS','EPA_SEIS','VECES_COYGE','NOTA_EE_DOS','VECES_CCON','CREDITOS_SYS','CREDITOS_EE_TRES','VECES_EE_TRES','CREDITOS_COYGE', "RENDIMIENTO_SIETE","PROMEDIO_SIETE"]]

#Se deja solo rendimientos del 1 al 4
electronica7 = electronica7[electronica7['RENDIMIENTO_SIETE'].isin([1, 2, 3, 4])]
electronica7.to_csv("electronica7.csv", sep=';', index=False)

# Octavo semestre ingeniería electronica
electronica8 = electronica.loc[:, ['NOTA_SISDIN','NOTA_ELECPOT','PROMEDIO_SIETE','PROMEDIO_TRES','NOTA_COMDIG','NOTA_FDS','NOTA_VARCOM','CON_MAT_ICFES','NOTA_TFM','PROMEDIO_SEIS','NCC_SIETE','NOTA_COMANA','NAA_SIETE','NOTA_ECO','NCA_SIETE','VECES_COMANA','PG_ICFES','VECES_ELECPOT','NOTA_CCON','VECES_COMDIG','VECES_ADMICRO','NOTA_L_TRES','NCP_SIETE','PROMEDIO_CINCO','NAC_SIETE','CAR_SIETE','NOTA_HSE','NAP_SIETE','VECES_ECO','VECES_FDS','VECES_SISDIN','EPA_SIETE','VECES_DDM','VECES_L_TRES','CREDITOS_ELECPOT','VECES_HSE', "RENDIMIENTO_OCHO","PROMEDIO_OCHO"]]

#Se deja solo rendimientos del 1 al 4
electronica8 = electronica8[electronica8['RENDIMIENTO_OCHO'].isin([1, 2, 3, 4])]
electronica8.to_csv("electronica8.csv", sep=';', index=False)

# Noveno semestre ingeniería electronica
electronica9 = electronica.loc[:, ['NOTA_STG','PROMEDIO_SEIS','NOTA_C_UNO','NOTA_FDS','PROMEDIO_OCHO','NOTA_ELECPOT','NOTA_INSIND','NOTA_SISDIN','NAP_OCHO','NOTA_INGECO','NOTA_TFM','NOTA_VARCOM','NOTA_TELEC_UNO','NAC_OCHO','NOTA_TELEMA_UNO','VECES_STG','CON_MAT_ICFES','NCA_OCHO','NCC_OCHO','PROMEDIO_SIETE','PROMEDIO_TRES','CAR_OCHO','NOTA_COMDIG','NOTAS_BDATOS','NCP_OCHO','NAA_OCHO','NOTA_BIOING_UNO','NCC_SIETE','EPA_OCHO','VECES_INSIND','VECES_BDATOS','VECES_TELEC_UNO','VECES_INGECO','VECES_C_UNO','VECES_BIOING_UNO','VECES_TELEMA_UNO','CREDITOS_STG','CREDITOS_BIOING_UNO','CREDITOS_C_UNO','CREDITOS_INGECO','CREDITOS_TELEC_UNO','CREDITOS_BDATOS','CREDITOS_TELEMA_UNO','CREDITOS_INSIND', "RENDIMIENTO_NUEVE","PROMEDIO_NUEVE"]]

#Se deja solo rendimientos del 1 al 4
electronica9 = electronica9[electronica9['RENDIMIENTO_NUEVE'].isin([1, 2, 3, 4])]
electronica9.to_csv("electronica9.csv", sep=';', index=False)

# Decimo semestre ingeniería electronica
electronica10 = electronica.loc[:, ['NOTA_STG','PROMEDIO_SEIS','NOTA_C_UNO','NOTA_FDS','PROMEDIO_OCHO','NOTA_ELECPOT','NOTA_INSIND','NOTA_SISDIN','NAP_OCHO','NOTA_INGECO','NOTA_TFM','NOTA_EI_IA','VECES_EI_IA','CREDITOS_EI_IA','NOTA_EI_IIA','VECES_EI_IIA','CREDITOS_EI_IIA','NOTA_EI_IIIA','VECES_EI_IIIA','CREDITOS_EI_IIIA','NOTA_TRABGRAD','VECES_TRABGRAD','CREDITOS_TRABGRAD','NOTA_TV','VECES_TV','CREDITOS_TV','NOTA_FGEP','VECES_FGEP','CREDITOS_FGEP','PROMEDIO_NUEVE','CAR_NUEVE','NCC_NUEVE','NCA_NUEVE','NCP_NUEVE','NAC_NUEVE','NAA_NUEVE','NAP_NUEVE','EPA_NUEVE','RENDIMIENTO_DIEZ','PROMEDIO_DIEZ']]

#Se deja solo rendimientos del 1 al 4
electronica10 = electronica10[electronica10['RENDIMIENTO_DIEZ'].isin([1, 2, 3, 4])]
electronica10.to_csv("electronica10.csv", sep=';', index=False)

#Archivos electronica por año

#Año 1 electronica
electronicaAnio1 = electronica.loc[:, ["CON_MAT_ICFES","QUIMICA_ICFES","PG_ICFES","FISICA_ICFES","IDIOMA_ICFES","BIOLOGIA_ICFES","GENERO","LOCALIDAD","LITERATURA_ICFES","PROMEDIO_UNO",
              "NOTA_DIF","EPA_UNO","NOTA_PROGB","NOTA_FIS_UNO","NCP_UNO","NOTA_TEXTOS","NOTA_CFJC","NAP_UNO","PROMEDIO_TRES"]]

electronicaAnio1 = electronicaAnio1[electronicaAnio1['PROMEDIO_TRES'] > 0]
electronicaAnio1.to_csv("electronicaAnio1.csv", sep=';', index=False)

#Año 2 electronica
electronicaAnio2 = electronica.loc[:, ["CON_MAT_ICFES","QUIMICA_ICFES","PG_ICFES","FISICA_ICFES","IDIOMA_ICFES","BIOLOGIA_ICFES","GENERO","LOCALIDAD","LITERATURA_ICFES","PROMEDIO_UNO",
              "NOTA_DIF","EPA_UNO","NOTA_PROGB","NOTA_FIS_UNO","NCP_UNO","NOTA_TEXTOS","NOTA_CFJC","NAP_UNO","PROMEDIO_DOS","NAA_DOS","NOTA_INT",
              "VECES_INT","NCA_DOS","NOTA_FIS_DOS","CAR_DOS","PROMEDIO_TRES","NCA_TRES","NOTA_FIS_TRES","NOTA_EL_UNO","VECES_FIS_TRES","NOTA_DEM","PROMEDIO_CINCO"]]

electronicaAnio2 = electronicaAnio2[electronicaAnio2['PROMEDIO_CINCO'] > 0]
electronicaAnio2.to_csv("electronicaAnio2.csv", sep=';', index=False)

#Año 3 electronica
electronicaAnio3 = electronica.loc[:, ["CON_MAT_ICFES","QUIMICA_ICFES","PG_ICFES","FISICA_ICFES","IDIOMA_ICFES","BIOLOGIA_ICFES","GENERO","LOCALIDAD","LITERATURA_ICFES","PROMEDIO_UNO",
              "NOTA_DIF","EPA_UNO","NOTA_PROGB","NOTA_FIS_UNO","NCP_UNO","NOTA_TEXTOS","NOTA_CFJC","NAP_UNO","PROMEDIO_DOS","NAA_DOS","NOTA_INT",
              "VECES_INT","NCA_DOS","NOTA_FIS_DOS","CAR_DOS","PROMEDIO_TRES","NCA_TRES","NOTA_FIS_TRES","NOTA_EL_UNO","VECES_FIS_TRES","NOTA_DEM",
              "PROMEDIO_CUATRO","NOTA_EL_DOS","NOTA_CAMPOS","NOTA_FCD","VECES_FCD","NOTA_PROGAPL","NOTA_VARCOM","NCP_CUATRO","PROMEDIO_CINCO","NOTA_EE_DOS","NCC_CINCO","NOTA_ADMICRO","NAP_CINCO",
              "NOTA_TFM","VECES_ADMICRO","NAC_CINCO","PROMEDIO_SEIS","NOTA_COMANA","NOTA_MOYGE","NOTA_CCON","VECES_COMANA","VECES_DDM","NOTAS_SYS",
              "PROMEDIO_SIETE","NOTA_SISDIN","NOTA_ELECPOT","NOTA_COMDIG","NOTA_FDS","NCC_SIETE","PROMEDIO_OCHO","NOTA_STG","NOTA_C_UNO","NOTA_INSIND","NAP_OCHO","NOTA_INGECO","PROMEDIO_NUEVE"]]

electronicaAnio3 = electronicaAnio3[electronicaAnio3['PROMEDIO_NUEVE'] > 0]
electronicaAnio3.to_csv("electronicaAnio3.csv", sep=';', index=False)