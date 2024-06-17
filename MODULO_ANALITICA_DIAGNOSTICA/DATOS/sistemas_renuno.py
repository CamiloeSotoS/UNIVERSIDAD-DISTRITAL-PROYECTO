import pandas as pd
import numpy as np
import glob
import csv
import os



#sistemas = pd.read_csv(archivo_base_path, sep=',')
#municipios = pd.read_csv(archivo_municipios_path, sep=',')

#merged_df = pd.merge(sistemas, municipios, on='MUNICIPIO')
#merged_df = merged_df.drop(columns=['MUNICIPIO'])
#merged_df = merged_df.rename(columns={'NUM_MUNI': 'MUNICIPIO'})
#sistemas = merged_df

ruta_archivo = 'C:/Users/User/Desktop/udistrital/NUEVA_BD_ING_SISTEMAS.csv'
sistemas = pd.read_csv(ruta_archivo, sep=',')

#ruta_archivo_2 = 'C:/Users/User/Desktop/udistrital/municipios_ud.csv'
#municipios = pd.read_csv(ruta_archivo_2, sep=',')


#sistemas['DISTANCIA'] = np.where(((sistemas['LOCALIDAD'] == 'TEUSAQUILLO') | (sistemas['LOCALIDAD'] == 'CHAPINERO') | (sistemas['LOCALIDAD'] == 'SANTA FE')) , '1' , np.nan)
#sistemas['DISTANCIA'] = np.where(((sistemas['LOCALIDAD'] == 'LOS MARTIRES')|(sistemas['LOCALIDAD'] == 'LA CANDELARIA')|(sistemas['LOCALIDAD'] == 'PUENTE ARANDA')), '2' , sistemas['DISTANCIA'])
#sistemas['DISTANCIA'] = np.where(((sistemas['LOCALIDAD'] == 'BARRIOS UNIDOS')|(sistemas['LOCALIDAD'] == 'RAFAEL URIBE URIBE')|(sistemas['LOCALIDAD'] == 'ANTONIO NARINO')|(sistemas['LOCALIDAD'] == 'ENGATIVA')|(sistemas['LOCALIDAD'] == 'KENNEDY')), '3' , sistemas['DISTANCIA'])
#sistemas['DISTANCIA'] = np.where(((sistemas['LOCALIDAD'] == 'FONTIBON')|(sistemas['LOCALIDAD'] == 'SAN CRISTOBAL')), '4' , sistemas['DISTANCIA'])
#sistemas['DISTANCIA'] = np.where(((sistemas['LOCALIDAD'] == 'USAQUEN')|(sistemas['LOCALIDAD'] == 'BOSA')|(sistemas['LOCALIDAD'] == 'SUBA')|(sistemas['LOCALIDAD'] == 'TUNJUELITO')|(sistemas['LOCALIDAD'] == 'CIUDAD BOLIVAR')), '5' , sistemas['DISTANCIA'])
#sistemas['DISTANCIA'] = np.where(((sistemas['LOCALIDAD'] == 'USME')|(sistemas['LOCALIDAD'] == 'FUERA DE BOGOTA')|(sistemas['LOCALIDAD'] == 'SOACHA')|(sistemas['LOCALIDAD'] == 'SUMAPAZ')), '6' , sistemas['DISTANCIA'])
#sistemas['DISTANCIA'] = np.where(((sistemas['LOCALIDAD'] == 'NO REGISTRA')|(sistemas['LOCALIDAD'] == 'SIN LOCALIDAD')), '7' , sistemas['DISTANCIA'])

sistemas['GENERO'] = sistemas['GENERO'].replace({'MASCULINO': 0, 'FEMENINO': 1})
sistemas['TIPO_COLEGIO'] = sistemas['TIPO_COLEGIO'].replace({'NO REGISTRA': 0, 'OFICIAL': 1, 'NO OFICIAL':2})
sistemas['LOCALIDAD_COLEGIO'] = sistemas['LOCALIDAD_COLEGIO'].replace({'NO REGISTRA': 0, 'USAQUEN': 1, 'CHAPINERO': 2, 'SANTAFE': 3, 'SANTA FE': 3, 'SAN CRISTOBAL': 4, 'USME': 5, 'TUNJUELITO': 6, 'BOSA': 7, 'KENNEDY': 8, 'FONTIBON': 9, 'ENGATIVA': 10, 'SUBA': 11, 'BARRIOS UNIDOS': 12, 'TEUSAQUILLO': 13, 'LOS MARTIRES': 14, 'ANTONIO NARINO': 15, 'PUENTE ARANDA': 16, 'LA CANDELARIA': 17, 'RAFAEL URIBE URIBE': 18, 'RAFAEL URIBE': 18, 'CIUDAD BOLIVAR': 19, 'FUERA DE BOGOTA': 20, 'SIN LOCALIDAD': 21, 'SOACHA':20})
sistemas['CALENDARIO'] = sistemas['CALENDARIO'].replace({'NO REGISTRA': 0,'O': 0, 'A': 1, 'B': 2, 'F': 3})
sistemas['DEPARTAMENTO'] = sistemas['DEPARTAMENTO'].replace({'NO REGISTRA': 0, 'AMAZONAS': 1, 'ANTIOQUIA': 2,'ARAUCA': 3, 'ATLANTICO': 4, 'BOGOTA': 5, 'BOLIVAR': 6, 'BOYACA': 7, 'CALDAS': 8, 'CAQUETA': 9, 'CASANARE': 10, 'CAUCA': 11, 'CESAR': 12, 'CHOCO': 13, 'CORDOBA': 14, 'CUNDINAMARCA': 15, 'GUAINIA': 16, 'GUAVIARE': 17, 'HUILA': 18, 'LA GUAJIRA': 19, 'MAGDALENA':20, 'META': 21, 'NARINO': 22, 'NORTE SANTANDER': 23, 'PUTUMAYO': 24, 'QUINDIO': 25, 'RISARALDA': 26, 'SAN ANDRES Y PROVIDENCIA': 27, 'SANTANDER': 28, 'SUCRE': 29, 'TOLIMA': 30, 'VALLE': 31, 'VAUPES': 32, 'VICHADA': 33})
sistemas['LOCALIDAD'] = sistemas['LOCALIDAD'].replace({'NO REGISTRA': 0, 'USAQUEN': 1, 'CHAPINERO': 2, 'SANTA FE': 3, 'SAN CRISTOBAL': 4, 'USME': 5, 'TUNJUELITO': 6, 'BOSA': 7, 'KENNEDY': 8, 'FONTIBON': 9, 'ENGATIVA': 10, 'SUBA': 11, 'BARRIOS UNIDOS': 12, 'TEUSAQUILLO': 13, 'LOS MARTIRES': 14, 'ANTONIO NARINO': 15, 'PUENTE ARANDA': 16, 'LA CANDELARIA': 17, 'RAFAEL URIBE URIBE': 18, 'CIUDAD BOLIVAR': 19, 'FUERA DE BOGOTA': 20, 'SIN LOCALIDAD': 20, 'SOACHA': 20, 'SUMAPAZ': 20})
sistemas['INSCRIPCION'] = sistemas['INSCRIPCION'].replace({'NO REGISTRA': 0, 'BENEFICIARIOS LEY 1081 DE 2006': 1, 'BENEFICIARIOS LEY 1084 DE 2006': 2, 'CONVENIO ANDRES BELLO': 3, 'DESPLAZADOS': 4, 'INDIGENAS': 5, 'MEJORES BACHILLERES COL. DISTRITAL OFICIAL': 6, 'MINORIAS ETNICAS Y CULTURALES': 7, 'MOVILIDAD ACADEMICA INTERNACIONAL': 8, 'NORMAL': 9, 'TRANSFERENCIA EXTERNA': 10, 'TRANSFERENCIA INTERNA': 11,})
#sistemas['ESTADO_FINAL'] = sistemas['ESTADO_FINAL'].replace({'ABANDONO': 1, 'ACTIVO': 2, 'APLAZO': 3, 'CANCELADO': 4, 'EGRESADO': 5, 'INACTIVO': 6, 'MOVILIDAD': 7, 'N.A.': 8, 'NO ESTUDIANTE AC004': 9, 'NO SUP. PRUEBA ACAD.': 10, 'PRUEBA AC Y ACTIVO': 11, 'PRUEBA ACAD': 12, 'RETIRADO': 13, 'TERMINO MATERIAS': 14, 'TERMINO Y MATRICULO': 15, 'VACACIONES': 16})
sistemas['MUNICIPIO'] = sistemas['MUNICIPIO'].replace({"NO REGISTRA": 0, "ACACIAS": 1, "AGUACHICA": 2, "AGUAZUL": 3, "ALBAN": 4, "ALBAN (SAN JOSE)": 5, "ALVARADO": 6, "ANAPOIMA": 7, "ANOLAIMA": 8, "APARTADO": 9, "ARAUCA": 10, "ARBELAEZ": 11, "ARMENIA": 12, "ATACO": 13, "BARRANCABERMEJA": 14, "BARRANQUILLA": 15, "BELEN DE LOS ANDAQUIES": 16, "BOAVITA": 17, "BOGOTA": 18, "BOJACA": 19, "BOLIVAR": 20, "BUCARAMANGA": 21, "BUENAVENTURA": 22, "CABUYARO": 23, "CACHIPAY": 24, "CAICEDONIA": 25, "CAJAMARCA": 26, "CAJICA": 27, "CALAMAR": 28, "CALARCA": 29, "CALI": 30, "CAMPOALEGRE": 31, "CAPARRAPI": 32, "CAQUEZA": 33, "CARTAGENA": 34, "CASTILLA LA NUEVA": 35, "CERETE": 36, "CHAPARRAL": 37, "CHARALA": 38, "CHIA": 39, "CHIPAQUE": 40, "CHIQUINQUIRA": 41, "CHOACHI": 42, "CHOCONTA": 43, "CIENAGA": 44, "CIRCASIA": 45, "COGUA": 46, "CONTRATACION": 47, "COTA": 48, "CUCUTA": 49, "CUMARAL": 50, "CUMBAL": 51, "CURITI": 52, "CURUMANI": 53, "DUITAMA": 54, "EL BANCO": 55, "EL CARMEN DE BOLIVAR": 56, "EL COLEGIO": 57, "EL CHARCO": 58, "EL DORADO": 59, "EL PASO": 60, "EL ROSAL": 61, "ESPINAL": 62, "FACATATIVA": 63, "FLORENCIA": 64, "FLORIDABLANCA": 65, "FOMEQUE": 66, "FONSECA": 67, "FORTUL": 68, "FOSCA": 69, "FUNZA": 70, "FUSAGASUGA": 71, "GACHETA": 72, "GALERAS (NUEVA GRANADA)": 73, "GAMA": 74, "GARAGOA": 75, "GARZON": 76, "GIGANTE": 77, "GIRARDOT": 78, "GRANADA": 79, "GUACHUCAL": 80, "GUADUAS": 81, "GUAITARILLA": 82, "GUAMO": 83, "GUASCA": 84, "GUATEQUE": 85, "GUAYATA": 86, "GUTIERREZ": 87, "IBAGUE": 88, "INIRIDA": 89, "INZA": 90, "IPIALES": 91, "ITSMINA": 92, "JENESANO": 93, "LA CALERA": 94, "LA DORADA": 95, "LA MESA": 96, "LA PLATA": 97, "LA UVITA": 98, "LA VEGA": 99, "LIBANO": 100, "LOS PATIOS": 101, "MACANAL": 102, "MACHETA": 103, "MADRID": 104, "MAICAO": 105, "MALAGA": 106, "MANAURE BALCON DEL 12": 107, "MANIZALES": 108, "MARIQUITA": 109, "MEDELLIN": 110, "MEDINA": 111, "MELGAR": 112, "MITU": 113, "MOCOA": 114, "MONTERIA": 115, "MONTERREY": 116, "MOSQUERA": 117, "NATAGAIMA": 118, "NEIVA": 119, "NEMOCON": 120, "OCANA": 121, "ORITO": 122, "ORTEGA": 123, "PACHO": 124, "PAEZ (BELALCAZAR)": 125, "PAICOL": 126, "PAILITAS": 127, "PAIPA": 128, "PALERMO": 129, "PALMIRA": 130, "PAMPLONA": 131, "PANDI": 132, "PASCA": 133, "PASTO": 134, "PAZ DE ARIPORO": 135, "PAZ DE RIO": 136, "PITALITO": 137, "POPAYAN": 138, "PUENTE NACIONAL": 139, "PUERTO ASIS": 140, "PUERTO BOYACA": 141, "PUERTO LOPEZ": 142, "PUERTO SALGAR": 143, "PURIFICACION": 144, "QUETAME": 145, "QUIBDO": 146, "RAMIRIQUI": 147, "RICAURTE": 148, "RIOHACHA": 149, "RIVERA": 150, "SABOYA": 151, "SAHAGUN": 152, "SALDAÑA": 153, "SAMACA": 154, "SAMANA": 155, "SAN AGUSTIN": 156, "SAN ANDRES": 157, "SAN BERNARDO": 158, "SAN EDUARDO": 159, "SAN FRANCISCO": 160, "SAN GIL": 161, "SAN JOSE DEL FRAGUA": 162, "SAN JOSE DEL GUAVIARE": 163, "SAN LUIS DE PALENQUE": 164, "SAN MARCOS": 165, "SAN MARTIN": 166, "SANDONA": 167, "SAN VICENTE DEL CAGUAN": 168, "SANTA MARTA": 169, "SANTA SOFIA": 170, "SESQUILE": 171, "SIBATE": 172, "SIBUNDOY": 173, "SILVANIA": 174, "SIMIJACA": 175, "SINCE": 176, "SINCELEJO": 177, "SOACHA": 178, "SOATA": 179, "SOCORRO": 180, "SOGAMOSO": 181, "SOLEDAD": 182, "SOPO": 183, "SORACA": 184, "SOTAQUIRA": 185, "SUAITA": 186, "SUBACHOQUE": 187, "SUESCA": 188, "SUPATA": 189, "SUTAMARCHAN": 190, "SUTATAUSA": 191, "TABIO": 192, "TAMESIS": 193, "TARQUI": 194, "TAUSA": 195, "TENA": 196, "TENJO": 197, "TESALIA": 198, "TIBANA": 199, "TIMANA": 200, "TOCANCIPA": 201, "TUBARA": 202, "TULUA": 203, "TUMACO": 204, "TUNJA": 205, "TURBACO": 206, "TURMEQUE": 207, "UBATE": 208, "UMBITA": 209, "UNE": 210, "VALLEDUPAR": 211, "VELEZ": 212, "VENADILLO": 213, "VENECIA (OSPINA PEREZ)": 214, "VILLA DE LEYVA": 215, "VILLAHERMOSA": 216, "VILLANUEVA": 217, "VILLAPINZON": 218, "VILLAVICENCIO": 219, "VILLETA": 220, "YACOPI": 221, "YOPAL": 222, "ZIPACON": 223, "ZIPAQUIRA": 224})

sistemas = sistemas.apply(pd.to_numeric)

# Recorrer todas las columnas que comienzan con "CREDITOS_"
for columna in sistemas.columns:
    if columna.startswith('CREDITOS_'):
        # Obtener el valor distinto de cero en la columna
        otro_valor = sistemas.loc[sistemas[columna] != 0, columna].iloc[0]
        # Reemplazar ceros por el otro valor
        sistemas[columna] = sistemas[columna].replace(0, otro_valor)



"""#PRIMER SEMESTRE sistemas"""

#Lista sistemas primer semestre
NOTAS_sistemas_UNO= ['NOTA_DIFERENCIAL', 'NOTA_PROG_BASICA', 'NOTA_CATEDRA_FJC', 'NOTA_TEXTOS', 'NOTA_SEMINARIO', 'NOTA_CATEDRA_DEM', 'NOTA_CATEDRA_CON', 'NOTA_LOGICA', 'NOTA_EE_UNO']
VECES_sistemas_UNO= ['VECES_DIFERENCIAL', 'VECES_PROG_BASICA', 'VECES_CATEDRA_FJC', 'VECES_TEXTOS', 'VECES_SEMINARIO', 'VECES_CATEDRA_DEM', 'VECES_CATEDRA_CON', 'VECES_LOGICA', 'VECES_EE_UNO']
CREDITOS_sistemas_UNO= ['CREDITOS_DIFERENCIAL', 'CREDITOS_PROG_BASICA', 'CREDITOS_CATEDRA_FJC', 'CREDITOS_TEXTOS', 'CREDITOS_SEMINARIO', 'CREDITOS_CATEDRA_DEM', 'CREDITOS_CATEDRA_CON', 'CREDITOS_LOGICA', 'CREDITOS_EE_UNO']

promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in sistemas.iterrows():
    notas_estudiante = []
    creditos_estudiante = []

    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_sistemas_UNO, VECES_sistemas_UNO, CREDITOS_sistemas_UNO):
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
sistemas['PROMEDIO_UNO'] = promedios_semestre

# Calcular métricas por semestre
sistemas['CAR_UNO'] = sistemas[VECES_sistemas_UNO].apply(lambda x: (x > 1).sum(), axis=1)
sistemas['NAC_UNO'] = sistemas[VECES_sistemas_UNO].apply(lambda x: (x > 0).sum(), axis=1)
sistemas['NAA_UNO'] = sistemas[NOTAS_sistemas_UNO].apply(lambda x: (x >= 30).sum(), axis=1)
sistemas['NAP_UNO'] = sistemas['NAC_UNO'] - sistemas['NAA_UNO']
sistemas['EPA_UNO'] = sistemas.apply(lambda row: 1 if row['PROMEDIO_UNO'] < 30 or row['NAP_UNO'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_sistemas_UNO, CREDITOS_sistemas_UNO):
        if row[veces_col] > 0:
            creditos_cursados += row[creditos_col]
    return creditos_cursados

sistemas['NCC_UNO'] = sistemas.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_sistemas_UNO, CREDITOS_sistemas_UNO):
        if row[nota_col] >= 30:
            creditos_aprobados += row[creditos_col]
    return creditos_aprobados

sistemas['NCA_UNO'] = sistemas.apply(calcular_creditos_aprobados, axis=1)


# Construir NCP

sistemas['NCP_UNO'] = sistemas['NCC_UNO'] - sistemas['NCA_UNO']

# Rendimiento UNO
conditions = [(sistemas['PROMEDIO_UNO'] >= 0) & (sistemas['PROMEDIO_UNO'] < 30),
(sistemas['PROMEDIO_UNO'] >= 30) & (sistemas['PROMEDIO_UNO'] < 40),
(sistemas['PROMEDIO_UNO'] >= 40) & (sistemas['PROMEDIO_UNO'] < 45),
(sistemas['PROMEDIO_UNO'] >= 45) & (sistemas['PROMEDIO_UNO'] < 50)]
values = [1, 2, 3, 4]
sistemas['RENDIMIENTO_UNO'] = pd.Series(pd.cut(sistemas['PROMEDIO_UNO'], bins=[0, 30, 40, 45, 50], labels=values))

"""# SEGUNDO SEMRESTRE sistemas"""

# Lista sistemas segundo semestre
NOTAS_sistemas_DOS = ['NOTA_SEGUNDA_LENGUA_UNO', 'NOTA_EI_UNO', 'NOTA_FISICA_UNO', 'NOTA_INTEGRAL', 'NOTA_ALGEBRA', 'NOTA_PROG_ORIENTADA', 'NOTA_ETICA', 'NOTA_GT_UNO']
VECES_sistemas_DOS = ['VECES_SEGUNDA_LENGUA_UNO', 'VECES_EI_UNO', 'VECES_FISICA_UNO', 'VECES_INTEGRAL', 'VECES_ALGEBRA', 'VECES_PROG_ORIENTADA', 'VECES_ETICA', 'VECES_GT_UNO']
CREDITOS_sistemas_DOS = ['CREDITOS_SEGUNDA_LENGUA_UNO', 'CREDITOS_EI_UNO', 'CREDITOS_FISICA_UNO', 'CREDITOS_INTEGRAL', 'CREDITOS_ALGEBRA', 'CREDITOS_PROG_ORIENTADA', 'CREDITOS_ETICA', 'CREDITOS_GT_UNO']

sistemas.columns

promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in sistemas.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_sistemas_DOS, VECES_sistemas_DOS, CREDITOS_sistemas_DOS):
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
sistemas['PROMEDIO_DOS'] = promedios_semestre

# Calcular métricas por semestre
sistemas['CAR_DOS'] = sistemas[VECES_sistemas_DOS].apply(lambda x: (x > 1).sum(), axis=1)
sistemas['NAC_DOS'] = sistemas[VECES_sistemas_DOS].apply(lambda x: (x > 0).sum(), axis=1)
sistemas['NAA_DOS'] = sistemas[NOTAS_sistemas_DOS].apply(lambda x: (x >= 30).sum(), axis=1)
sistemas['NAP_DOS'] = sistemas['NAC_DOS'] - sistemas['NAA_DOS']
sistemas['EPA_DOS'] = sistemas.apply(lambda row: 1 if row['PROMEDIO_DOS'] < 30 or row['NAP_DOS'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_sistemas_DOS, CREDITOS_sistemas_DOS):
        if row[veces_col] > 0:
            creditos_cursados += row[creditos_col]
    return creditos_cursados

sistemas['NCC_DOS'] = sistemas.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_sistemas_DOS, CREDITOS_sistemas_DOS):
        if row[nota_col] >= 30:
            creditos_aprobados += row[creditos_col]
    return creditos_aprobados

sistemas['NCA_DOS'] = sistemas.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

sistemas['NCP_DOS'] = sistemas['NCC_DOS'] - sistemas['NCA_DOS']

# Rendimiento DOS
conditions = [(sistemas['PROMEDIO_DOS'] >= 0) & (sistemas['PROMEDIO_DOS'] < 30),
(sistemas['PROMEDIO_DOS'] >= 30) & (sistemas['PROMEDIO_DOS'] < 40),
(sistemas['PROMEDIO_DOS'] >= 40) & (sistemas['PROMEDIO_DOS'] < 45),
(sistemas['PROMEDIO_DOS'] >= 45) & (sistemas['PROMEDIO_DOS'] < 50)]
values = [1, 2, 3, 4]
sistemas['RENDIMIENTO_DOS'] = pd.Series(pd.cut(sistemas['PROMEDIO_DOS'], bins=[0, 30, 40, 45, 50], labels=values))

"""# TERCER SEMESTRE sistemas"""

# Lista sistemas tercer semestre

VECES_sistemas_TRES = ['VECES_SEGUNDA_LENGUA_DOS', 'VECES_EE_DOS', 'VECES_FISICA_DOS', 'VECES_MULTIVARIADO', 'VECES_ECUACIONES', 'VECES_TGS', 'VECES_PROG_AVANZADA']
NOTAS_sistemas_TRES = ['NOTA_SEGUNDA_LENGUA_DOS', 'NOTA_EE_DOS', 'NOTA_FISICA_DOS', 'NOTA_MULTIVARIADO', 'NOTA_ECUACIONES', 'NOTA_TGS', 'NOTA_PROG_AVANZADA']
CREDITOS_sistemas_TRES = ['CREDITOS_SEGUNDA_LENGUA_DOS', 'CREDITOS_EE_DOS', 'CREDITOS_FISICA_DOS', 'CREDITOS_MULTIVARIADO', 'CREDITOS_ECUACIONES', 'CREDITOS_TGS', 'CREDITOS_PROG_AVANZADA']

sistemas.columns
promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in sistemas.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_sistemas_TRES, VECES_sistemas_TRES, CREDITOS_sistemas_TRES):
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
sistemas['PROMEDIO_TRES'] = promedios_semestre

# Calcular métricas por semestre
sistemas['CAR_TRES'] = sistemas[VECES_sistemas_TRES].apply(lambda x: (x > 1).sum(), axis=1)
sistemas['NAC_TRES'] = sistemas[VECES_sistemas_TRES].apply(lambda x: (x > 0).sum(), axis=1)
sistemas['NAA_TRES'] = sistemas[NOTAS_sistemas_TRES].apply(lambda x: (x >= 30).sum(), axis=1)
sistemas['NAP_TRES'] = sistemas['NAC_TRES'] - sistemas['NAA_TRES']
sistemas['EPA_TRES'] = sistemas.apply(lambda row: 1 if row['PROMEDIO_TRES'] < 30 or row['NAP_TRES'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_sistemas_TRES, CREDITOS_sistemas_TRES):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados
sistemas['NCC_TRES'] = sistemas.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_sistemas_TRES, CREDITOS_sistemas_TRES):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados
sistemas['NCA_TRES'] = sistemas.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

sistemas['NCP_TRES'] = sistemas['NCC_TRES'] - sistemas['NCA_TRES']

# Rendimiento TRES
conditions = [(sistemas['PROMEDIO_TRES'] >= 0) & (sistemas['PROMEDIO_TRES'] < 30),
(sistemas['PROMEDIO_TRES'] >= 30) & (sistemas['PROMEDIO_TRES'] < 40),
(sistemas['PROMEDIO_TRES'] >= 40) & (sistemas['PROMEDIO_TRES'] < 45),
(sistemas['PROMEDIO_TRES'] >= 45) & (sistemas['PROMEDIO_TRES'] < 50)]
values = [1, 2, 3, 4]
sistemas['RENDIMIENTO_TRES'] = pd.Series(pd.cut(sistemas['PROMEDIO_TRES'], bins=[0, 30, 40, 45, 50], labels=values))

"""# CUARTO SEMESTRE sistemas"""

#Lista sistemas cuarto semestre

VECES_sistemas_CUATRO = ['VECES_SEGUNDA_LENGUA_TRES', 'VECES_HOMBRE', 'VECES_GT_DOS', 'VECES_MAT_ESP', 'VECES_MOD_PROG_UNO', 'VECES_A_SISTEMAS', 'VECES_METODOS_NUM', 'VECES_FUND_BASES', 'VECES_MAT_DIS']
NOTAS_sistemas_CUATRO = ['NOTA_SEGUNDA_LENGUA_TRES', 'NOTA_HOMBRE', 'NOTA_GT_DOS', 'NOTA_MAT_ESP', 'NOTA_MOD_PROG_UNO', 'NOTA_A_SISTEMAS', 'NOTA_METODOS_NUM', 'NOTA_FUND_BASES', 'NOTA_MAT_DIS']
CREDITOS_sistemas_CUATRO = ['CREDITOS_SEGUNDA_LENGUA_TRES', 'CREDITOS_HOMBRE', 'CREDITOS_GT_DOS', 'CREDITOS_MAT_ESP', 'CREDITOS_MOD_PROG_UNO', 'CREDITOS_A_SISTEMAS', 'CREDITOS_METODOS_NUM', 'CREDITOS_FUND_BASES', 'CREDITOS_MAT_DIS']

promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in sistemas.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_sistemas_CUATRO, VECES_sistemas_CUATRO, CREDITOS_sistemas_CUATRO):
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
sistemas['PROMEDIO_CUATRO'] = promedios_semestre

# Calcular métricas por semestre
sistemas['CAR_CUATRO'] = sistemas[VECES_sistemas_CUATRO].apply(lambda x: (x > 1).sum(), axis=1)
sistemas['NAC_CUATRO'] = sistemas[VECES_sistemas_CUATRO].apply(lambda x: (x > 0).sum(), axis=1)
sistemas['NAA_CUATRO'] = sistemas[NOTAS_sistemas_CUATRO].apply(lambda x: (x >= 30).sum(), axis=1)
sistemas['NAP_CUATRO'] = sistemas['NAC_CUATRO'] - sistemas['NAA_CUATRO']
sistemas['EPA_CUATRO'] = sistemas.apply(lambda row: 1 if row['PROMEDIO_CUATRO'] < 30 or row['NAP_CUATRO'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_sistemas_CUATRO, CREDITOS_sistemas_CUATRO):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados
sistemas['NCC_CUATRO'] = sistemas.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_sistemas_CUATRO, CREDITOS_sistemas_CUATRO):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados
sistemas['NCA_CUATRO'] = sistemas.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

sistemas['NCP_CUATRO'] = sistemas['NCC_CUATRO'] - sistemas['NCA_CUATRO']

# Rendimiento CUATRO
conditions = [(sistemas['PROMEDIO_CUATRO'] >= 0) & (sistemas['PROMEDIO_CUATRO'] < 30),
(sistemas['PROMEDIO_CUATRO'] >= 30) & (sistemas['PROMEDIO_CUATRO'] < 40),
(sistemas['PROMEDIO_CUATRO'] >= 40) & (sistemas['PROMEDIO_CUATRO'] < 45),
(sistemas['PROMEDIO_CUATRO'] >= 45) & (sistemas['PROMEDIO_CUATRO'] < 50)]
values = [1, 2, 3, 4]
sistemas['RENDIMIENTO_CUATRO'] = pd.Series(pd.cut(sistemas['PROMEDIO_CUATRO'], bins=[0, 30, 40, 45, 50], labels=values))

"""# QUINTO SEMESTRE sistemas"""

# Lista sistemas quinto semestre

VECES_sistemas_CINCO = ['VECES_EE_TRES', 'VECES_FISICA_TRES', 'VECES_ARQ_COMP', 'VECES_MOD_PROG_DOS', 'VECES_CIENCIAS_COMP_UNO', 'VECES_INV_OP_UNO', 'VECES_PROB']
NOTAS_sistemas_CINCO = ['NOTA_EE_TRES', 'NOTA_FISICA_TRES', 'NOTA_ARQ_COMP', 'NOTA_MOD_PROG_DOS', 'NOTA_CIENCIAS_COMP_UNO', 'NOTA_INV_OP_UNO', 'NOTA_PROB']
CREDITOS_sistemas_CINCO = ['CREDITOS_EE_TRES', 'CREDITOS_FISICA_TRES', 'CREDITOS_ARQ_COMP', 'CREDITOS_MOD_PROG_DOS', 'CREDITOS_CIENCIAS_COMP_UNO', 'CREDITOS_INV_OP_UNO', 'CREDITOS_PROB']

promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in sistemas.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_sistemas_CINCO, VECES_sistemas_CINCO, CREDITOS_sistemas_CINCO):
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
sistemas['PROMEDIO_CINCO'] = promedios_semestre

# Calcular métricas por semestre
sistemas['CAR_CINCO'] = sistemas[VECES_sistemas_CINCO].apply(lambda x: (x > 1).sum(), axis=1)
sistemas['NAC_CINCO'] = sistemas[VECES_sistemas_CINCO].apply(lambda x: (x > 0).sum(), axis=1)
sistemas['NAA_CINCO'] = sistemas[NOTAS_sistemas_CINCO].apply(lambda x: (x >= 30).sum(), axis=1)
sistemas['NAP_CINCO'] = sistemas['NAC_CINCO'] - sistemas['NAA_CINCO']
sistemas['EPA_CINCO'] = sistemas.apply(lambda row: 1 if row['PROMEDIO_CINCO'] < 30 or row['NAP_CINCO'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_sistemas_CINCO, CREDITOS_sistemas_CINCO):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados
sistemas['NCC_CINCO'] = sistemas.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_sistemas_CINCO, CREDITOS_sistemas_CINCO):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados
sistemas['NCA_CINCO'] = sistemas.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

sistemas['NCP_CINCO'] = sistemas['NCC_CINCO'] - sistemas['NCA_CINCO']

# Rendimiento CINCO
conditions = [(sistemas['PROMEDIO_CINCO'] >= 0) & (sistemas['PROMEDIO_CINCO'] < 30),
(sistemas['PROMEDIO_CINCO'] >= 30) & (sistemas['PROMEDIO_CINCO'] < 40),
(sistemas['PROMEDIO_CINCO'] >= 40) & (sistemas['PROMEDIO_CINCO'] < 45),
(sistemas['PROMEDIO_CINCO'] >= 45) & (sistemas['PROMEDIO_CINCO'] < 50)]
values = [1, 2, 3, 4]
sistemas['RENDIMIENTO_CINCO'] = pd.Series(pd.cut(sistemas['PROMEDIO_CINCO'], bins=[0, 30, 40, 45, 50], labels=values))

"""# SEXTO SEMESTRE sistemas"""

#Lista sistemas sexto semestre

VECES_sistemas_SEIS = ['VECES_HISTORIA_COL', 'VECES_GI_UNO', 'VECES_CIBERNETICA_UNO', 'VECES_REDES_COM_UNO', 'VECES_CIENCIAS_COMP_DOS', 'VECES_INV_OP_DOS', 'VECES_ESTADISTICA']
NOTAS_sistemas_SEIS = ['NOTA_HISTORIA_COL', 'NOTA_GI_UNO', 'NOTA_CIBERNETICA_UNO', 'NOTA_REDES_COM_UNO', 'NOTA_CIENCIAS_COMP_DOS', 'NOTA_INV_OP_DOS', 'NOTA_ESTADISTICA']
CREDITOS_sistemas_SEIS = ['CREDITOS_HISTORIA_COL', 'CREDITOS_GI_UNO', 'CREDITOS_CIBERNETICA_UNO', 'CREDITOS_REDES_COM_UNO', 'CREDITOS_CIENCIAS_COMP_DOS', 'CREDITOS_INV_OP_DOS', 'CREDITOS_ESTADISTICA']

promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in sistemas.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_sistemas_SEIS, VECES_sistemas_SEIS, CREDITOS_sistemas_SEIS):
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
sistemas['PROMEDIO_SEIS'] = promedios_semestre

# Calcular métricas por semestre
sistemas['CAR_SEIS'] = sistemas[VECES_sistemas_SEIS].apply(lambda x: (x > 1).sum(), axis=1)
sistemas['NAC_SEIS'] = sistemas[VECES_sistemas_SEIS].apply(lambda x: (x > 0).sum(), axis=1)
sistemas['NAA_SEIS'] = sistemas[NOTAS_sistemas_SEIS].apply(lambda x: (x >= 30).sum(), axis=1)
sistemas['NAP_SEIS'] = sistemas['NAC_SEIS'] - sistemas['NAA_SEIS']
sistemas['EPA_SEIS'] = sistemas.apply(lambda row: 1 if row['PROMEDIO_SEIS'] < 30 or row['NAP_SEIS'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_sistemas_SEIS, CREDITOS_sistemas_SEIS):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados
sistemas['NCC_SEIS'] = sistemas.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_sistemas_SEIS, CREDITOS_sistemas_SEIS):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados

sistemas['NCA_SEIS'] = sistemas.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

sistemas['NCP_SEIS'] = sistemas['NCC_SEIS'] - sistemas['NCA_SEIS']

# Rendimiento SEIS
conditions = [(sistemas['PROMEDIO_SEIS'] >= 0) & (sistemas['PROMEDIO_SEIS'] < 30),
(sistemas['PROMEDIO_SEIS'] >= 30) & (sistemas['PROMEDIO_SEIS'] < 40),
(sistemas['PROMEDIO_SEIS'] >= 40) & (sistemas['PROMEDIO_SEIS'] < 45),
(sistemas['PROMEDIO_SEIS'] >= 45) & (sistemas['PROMEDIO_SEIS'] < 50)]
values = [1, 2, 3, 4]
sistemas['RENDIMIENTO_SEIS'] = pd.Series(pd.cut(sistemas['PROMEDIO_SEIS'], bins=[0, 30, 40, 45, 50], labels=values))

"""# SEPTIMO SEMESTRE sistemas"""

#Lista sistemas primer semestre

VECES_sistemas_SIETE = ['VECES_EI_DOS', 'VECES_ECONOMIA', 'VECES_GT_TRES', 'VECES_CIBERNETICA_DOS', 'VECES_REDES_COM_DOS', 'VECES_INV_OP_TRES', 'VECES_F_ING_SOF', 'VECES_GI_DOS', 'VECES_FUND_IA']
NOTAS_sistemas_SIETE = ['NOTA_EI_DOS', 'NOTA_ECONOMIA', 'NOTA_GT_TRES', 'NOTA_CIBERNETICA_UDOS', 'NOTA_REDES_COM_DOS', 'NOTA_INV_OP_TRES', 'NOTA_F_ING_SOF', 'NOTA_GI_DOS', 'NOTA_FUND_IA']
CREDITOS_sistemas_SIETE = ['CREDITOS_EI_DOS', 'CREDITOS_ECONOMIA', 'CREDITOS_GT_TRES', 'CREDITOS_CIBERNETICA_DOS', 'CREDITOS_REDES_COM_DOS', 'CREDITOS_INV_OP_TRES', 'CREDITOS_F_ING_SOF', 'CREDITOS_GI_DOS', 'CREDITOS_FUND_IA']

promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in sistemas.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_sistemas_SIETE, VECES_sistemas_SIETE, CREDITOS_sistemas_SIETE):
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
sistemas['PROMEDIO_SIETE'] = promedios_semestre

# Calcular métricas por semestre
sistemas['CAR_SIETE'] = sistemas[VECES_sistemas_SIETE].apply(lambda x: (x > 1).sum(), axis=1)
sistemas['NAC_SIETE'] = sistemas[VECES_sistemas_SIETE].apply(lambda x: (x > 0).sum(), axis=1)
sistemas['NAA_SIETE'] = sistemas[NOTAS_sistemas_SIETE].apply(lambda x: (x >= 30).sum(), axis=1)
sistemas['NAP_SIETE'] = sistemas['NAC_SIETE'] - sistemas['NAA_SIETE']
sistemas['EPA_SIETE'] = sistemas.apply(lambda row: 1 if row['PROMEDIO_SIETE'] < 30 or row['NAP_SIETE'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_sistemas_SIETE, CREDITOS_sistemas_SIETE):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados

sistemas['NCC_SIETE'] = sistemas.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_sistemas_SIETE, CREDITOS_sistemas_SIETE):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados

sistemas['NCA_SIETE'] = sistemas.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

sistemas['NCP_SIETE'] = sistemas['NCC_SIETE'] - sistemas['NCA_SIETE']

# Rendimiento SIETE
conditions = [(sistemas['PROMEDIO_SIETE'] >= 0) & (sistemas['PROMEDIO_SIETE'] < 30),
(sistemas['PROMEDIO_SIETE'] >= 30) & (sistemas['PROMEDIO_SIETE'] < 40),
(sistemas['PROMEDIO_SIETE'] >= 40) & (sistemas['PROMEDIO_SIETE'] < 45),
(sistemas['PROMEDIO_SIETE'] >= 45) & (sistemas['PROMEDIO_SIETE'] < 50)]
values = [1, 2, 3, 4]
sistemas['RENDIMIENTO_SIETE'] = pd.Series(pd.cut(sistemas['PROMEDIO_SIETE'], bins=[0, 30, 40, 45, 50], labels=values))

"""# OCTAVO SEMESTRE sistemas"""

#Lista sistemas primer semestre

VECES_sistemas_OCHO = ['VECES_EI_OP_AI', 'VECES_EE_CUATRO', 'VECES_EI_OP_BI', 'VECES_ING_ECONOMICA', 'VECES_CIBERNETICA_TRES', 'VECES_REDES_COM_TRES', 'VECES_DIS_ARQ_SOFT']
NOTAS_sistemas_OCHO = ['NOTA_EI_OP_AI', 'NOTA_EE_CUATRO', 'NOTA_EI_OP_BI', 'NOTA_ING_ECONOMICA', 'NOTA_CIBERNETICA_TRES', 'NOTA_REDES_COM_TRES', 'NOTA_DIS_ARQ_SOFT']
CREDITOS_sistemas_OCHO = ['CREDITOS_EI_OP_AI', 'CREDITOS_EE_CUATRO', 'CREDITOS_EI_OP_BI', 'CREDITOS_ING_ECONOMICA', 'CREDITOS_CIBERNETICA_TRES', 'CREDITOS_REDES_COM_TRES', 'CREDITOS_DIS_ARQ_SOFT']

promedios_semestre = []

# Lista para almacenar los promedios del semestre
promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in sistemas.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_sistemas_OCHO, VECES_sistemas_OCHO, CREDITOS_sistemas_OCHO):
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
sistemas['PROMEDIO_OCHO'] = promedios_semestre

# Calcular métricas por semestre
sistemas['CAR_OCHO'] = sistemas[VECES_sistemas_OCHO].apply(lambda x: (x > 1).sum(), axis=1)
sistemas['NAC_OCHO'] = sistemas[VECES_sistemas_OCHO].apply(lambda x: (x > 0).sum(), axis=1)
sistemas['NAA_OCHO'] = sistemas[NOTAS_sistemas_OCHO].apply(lambda x: (x >= 30).sum(), axis=1)
sistemas['NAP_OCHO'] = sistemas['NAC_OCHO'] - sistemas['NAA_OCHO']
sistemas['EPA_OCHO'] = sistemas.apply(lambda row: 1 if row['PROMEDIO_OCHO'] < 30 or row['NAP_OCHO'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_sistemas_OCHO, CREDITOS_sistemas_OCHO):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados

sistemas['NCC_OCHO'] = sistemas.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_sistemas_OCHO, CREDITOS_sistemas_OCHO):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados
sistemas['NCA_OCHO'] = sistemas.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

sistemas['NCP_OCHO'] = sistemas['NCC_OCHO'] - sistemas['NCA_OCHO']

# Rendimiento OCHO
conditions = [(sistemas['PROMEDIO_OCHO'] >= 0) & (sistemas['PROMEDIO_OCHO'] < 30),
(sistemas['PROMEDIO_OCHO'] >= 30) & (sistemas['PROMEDIO_OCHO'] < 40),
(sistemas['PROMEDIO_OCHO'] >= 40) & (sistemas['PROMEDIO_OCHO'] < 45),
(sistemas['PROMEDIO_OCHO'] >= 45) & (sistemas['PROMEDIO_OCHO'] < 50)]
values = [1, 2, 3, 4]
sistemas['RENDIMIENTO_OCHO'] = pd.Series(pd.cut(sistemas['PROMEDIO_OCHO'], bins=[0, 30, 40, 45, 50], labels=values))

"""# NOVENO SEMESTRE sistemas"""

#Lista sistemas primer semestre

VECES_sistemas_NUEVE = ['VECES_EI_OP_AII', 'VECES_EI_OP_BII', 'VECES_EI_OP_CI', 'VECES_GES_CAL_VAL_SOFT', 'VECES_SIS_OP']
NOTAS_sistemas_NUEVE = ['NOTA_EI_OP_AII', 'NOTA_EI_OP_BII', 'NOTA_EI_OP_CI', 'NOTA_GES_CAL_VAL_SOFT', 'NOTA_SIS_OP']
CREDITOS_sistemas_NUEVE = ['CREDITOS_EI_OP_AII', 'CREDITOS_EI_OP_BII', 'CREDITOS_EI_OP_CI', 'CREDITOS_GES_CAL_VAL_SOFT', 'CREDITOS_SIS_OP']

promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in sistemas.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_sistemas_NUEVE, VECES_sistemas_NUEVE, CREDITOS_sistemas_NUEVE):
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
sistemas['PROMEDIO_NUEVE'] = promedios_semestre

# Calcular métricas por semestre
sistemas['CAR_NUEVE'] = sistemas[VECES_sistemas_NUEVE].apply(lambda x: (x > 1).sum(), axis=1)
sistemas['NAC_NUEVE'] = sistemas[VECES_sistemas_NUEVE].apply(lambda x: (x > 0).sum(), axis=1)
sistemas['NAA_NUEVE'] = sistemas[NOTAS_sistemas_NUEVE].apply(lambda x: (x >= 30).sum(), axis=1)
sistemas['NAP_NUEVE'] = sistemas['NAC_NUEVE'] - sistemas['NAA_NUEVE']
sistemas['EPA_NUEVE'] = sistemas.apply(lambda row: 1 if row['PROMEDIO_NUEVE'] < 30 or row['NAP_NUEVE'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_sistemas_NUEVE, CREDITOS_sistemas_NUEVE):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados
sistemas['NCC_NUEVE'] = sistemas.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_sistemas_NUEVE, CREDITOS_sistemas_NUEVE):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados
sistemas['NCA_NUEVE'] = sistemas.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

sistemas['NCP_NUEVE'] = sistemas['NCC_NUEVE'] - sistemas['NCA_NUEVE']

# Rendimiento NUEVE
conditions = [(sistemas['PROMEDIO_NUEVE'] >= 0) & (sistemas['PROMEDIO_NUEVE'] < 30),
(sistemas['PROMEDIO_NUEVE'] >= 30) & (sistemas['PROMEDIO_NUEVE'] < 40),
(sistemas['PROMEDIO_NUEVE'] >= 40) & (sistemas['PROMEDIO_NUEVE'] < 45),
(sistemas['PROMEDIO_NUEVE'] >= 45) & (sistemas['PROMEDIO_NUEVE'] < 50)]
values = [1, 2, 3, 4]
sistemas['RENDIMIENTO_NUEVE'] = pd.Series(pd.cut(sistemas['PROMEDIO_NUEVE'], bins=[0, 30, 40, 45, 50], labels=values))

"""# DECIMO SEMESTRE sistemas"""

#Lista sistemas primer semestre

NOTAS_sistemas_DIEZ = ['NOTA_GRADO_UNO', 'NOTA_EI_OP_AIII', 'NOTA_EI_OP_BIII', 'NOTA_EI_OP_CII', 'NOTA_EI_OP_DI', 'NOTA_FOGEP', 'NOTA_GRADO_DOS']
VECES_sistemas_DIEZ = ['VECES_GRADO_UNO', 'VECES_EI_OP_AIII', 'VECES_EI_OP_BIII', 'VECES_EI_OP_CII', 'VECES_EI_OP_DI', 'VECES_FOGEP', 'VECES_GRADO_DOS']
CREDITOS_sistemas_DIEZ = ['CREDITOS_GRADO_UNO', 'CREDITOS_EI_OP_AIII', 'CREDITOS_EI_OP_BIII', 'CREDITOS_EI_OP_CII', 'CREDITOS_EI_OP_DI', 'CREDITOS_FOGEP', 'CREDITOS_GRADO_DOS']

promedios_semestre = []

# Iterar sobre cada estudiante
for index, row in sistemas.iterrows():
    notas_estudiante = []
    creditos_estudiante = []
    
    # Iterar sobre las materias del semestre
    for nota_col, veces_col, creditos_col in zip(NOTAS_sistemas_DIEZ, VECES_sistemas_DIEZ, CREDITOS_sistemas_DIEZ):
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
sistemas['PROMEDIO_DIEZ'] = promedios_semestre

# Calcular métricas por semestre
sistemas['CAR_DIEZ'] = sistemas[VECES_sistemas_DIEZ].apply(lambda x: (x > 1).sum(), axis=1)
sistemas['NAC_DIEZ'] = sistemas[VECES_sistemas_DIEZ].apply(lambda x: (x > 0).sum(), axis=1)
sistemas['NAA_DIEZ'] = sistemas[NOTAS_sistemas_DIEZ].apply(lambda x: (x >= 30).sum(), axis=1)
sistemas['NAP_DIEZ'] = sistemas['NAC_DIEZ'] - sistemas['NAA_DIEZ']
sistemas['EPA_DIEZ'] = sistemas.apply(lambda row: 1 if row['PROMEDIO_DIEZ'] < 30 or row['NAP_DIEZ'] >= 3 else 2, axis=1)

# Construir NCC
def calcular_creditos_cursados(row):
    creditos_cursados = 0
    for veces_col, creditos_col in zip(VECES_sistemas_DIEZ, CREDITOS_sistemas_DIEZ):
      if row[veces_col] > 0:
        creditos_cursados += row[creditos_col]
    return creditos_cursados

sistemas['NCC_DIEZ'] = sistemas.apply(calcular_creditos_cursados, axis=1)

# Construir NCA
def calcular_creditos_aprobados(row):
    creditos_aprobados = 0
    for nota_col, creditos_col in zip(NOTAS_sistemas_DIEZ, CREDITOS_sistemas_DIEZ):
      if row[nota_col] >= 30:
        creditos_aprobados += row[creditos_col]
    return creditos_aprobados

sistemas['NCA_DIEZ'] = sistemas.apply(calcular_creditos_aprobados, axis=1)

# Construir NCP

sistemas['NCP_DIEZ'] = sistemas['NCC_DIEZ'] - sistemas['NCA_DIEZ']

# Rendimiento DIEZ
conditions = [(sistemas['PROMEDIO_DIEZ'] >= 0) & (sistemas['PROMEDIO_DIEZ'] < 30),
(sistemas['PROMEDIO_DIEZ'] >= 30) & (sistemas['PROMEDIO_DIEZ'] < 40),
(sistemas['PROMEDIO_DIEZ'] >= 40) & (sistemas['PROMEDIO_DIEZ'] < 45),
(sistemas['PROMEDIO_DIEZ'] >= 45) & (sistemas['PROMEDIO_DIEZ'] < 50)]
values = [1, 2, 3, 4]
sistemas['RENDIMIENTO_DIEZ'] = pd.Series(pd.cut(sistemas['PROMEDIO_DIEZ'], bins=[0, 30, 40, 45, 50], labels=values))

# Obtén una lista de todas las columnas que comienzan con "RENDIMIENTO_"
columnas_rendimiento = [col for col in sistemas.columns if col.startswith('RENDIMIENTO_')]

# Convertir columnas categóricas a numéricas
sistemas[columnas_rendimiento] = sistemas[columnas_rendimiento].astype(float)

# Reemplazar los valores vacíos por cero en estas columnas
sistemas[columnas_rendimiento] = sistemas[columnas_rendimiento].fillna(0)
sistemas = sistemas.applymap(lambda x: -x if isinstance(x, (int, float)) and x < 0 else x)

#sistemas.to_csv("sistemasfinal.csv", sep=',', index=False)

sistemas = sistemas.apply(pd.to_numeric)
sistemas.to_csv("sistemas.csv", sep=';', index=False)

    #sistemas.to_csv("sistemasfinal.csv", sep=',', index=False)

sistemas = sistemas.apply(pd.to_numeric)


#------------------------------CSV POR SEMESTRES--------------------------------------------------------#
#------------------------------CSV POR SEMESTRES--------------------------------------------------------#

#En promedio a filtrar es el número mínimo que debe tener un estudiante como promedio de las notas que se toman como variables
promedio_a_filtrar = 5
año_de_filtro = 2011

"""# INGENIERIA sistemas"""

# Primer semestre ingeniería sistemas
sistemas1 = sistemas.loc[:, ['CON_MAT_ICFES', 'IDIOMA_ICFES', 'LOCALIDAD_COLEGIO', 'BIOLOGIA_ICFES', 'QUIMICA_ICFES', 'PG_ICFES', 
    'LITERATURA_ICFES', 'ANO_INGRESO', 'FILOSOFIA_ICFES', 'APT_VERB_ICFES', 'FISICA_ICFES', 'MUNICIPIO', 
    'GENERO', 'APT_MAT_ICFES', 'LOCALIDAD', 'DEPARTAMENTO', 'SOCIALES_ICFES', 'ESTRATO', 'CALENDARIO', 
    'TIPO_COLEGIO', 'DISTANCIA', 'INSCRIPCION', 'CORTE_INGRESO',"RENDIMIENTO_UNO","PROMEDIO_UNO"]]

sistemas1 = sistemas1 = sistemas1.loc[sistemas1['ANO_INGRESO'] >= año_de_filtro]
sistemas1.to_csv("sistemas1.csv", sep=';', index=False)


# Segundo semestre ingeniería sistemas
sistemas2 = sistemas.loc[:, ['NOTA_DIFERENCIAL', 'NOTA_CATEDRA_DEM', 'NOTA_PROG_BASICA', 'NAA_UNO', 'CAR_UNO', 'NOTA_TEXTOS', 
    'NOTA_LOGICA', 'NOTA_SEMINARIO', 'VECES_LOGICA', 'NAC_UNO', 'NCC_UNO', 'NCA_UNO', 'IDIOMA_ICFES', 
    'VECES_CATEDRA_DEM', 'NOTA_EE_UNO', 'PG_ICFES', 'NAP_UNO', 'VECES_DIFERENCIAL', 'CON_MAT_ICFES', 
    'NOTA_CATEDRA_CON', 'VECES_EE_UNO', 'NOTA_CATEDRA_FJC', 'NCP_UNO', 'LOCALIDAD_COLEGIO', 'EPA_UNO', 
    'VECES_PROG_BASICA', 'BIOLOGIA_ICFES', 'LITERATURA_ICFES', 'VECES_TEXTOS', 'VECES_CATEDRA_CON', 
    'VECES_CATEDRA_FJC', 'VECES_SEMINARIO', 'QUIMICA_ICFES', 'CREDITOS_PROG_BASICA', 'CREDITOS_LOGICA', 
    'CREDITOS_CATEDRA_FJC','PROMEDIO_UNO', "RENDIMIENTO_DOS","PROMEDIO_DOS"]]

sistemas2 = sistemas2[sistemas2 ['RENDIMIENTO_DOS'].isin([1, 2, 3, 4])]
sistemas2.to_csv("sistemas2.csv", sep=';', index=False)

# Tercer semestre ingeniería sistemas
sistemas3 = sistemas.loc[:, ['NOTA_TGS', 'NOTA_PROG_AVANZADA', 'NOTA_FISICA_DOS', 'NOTA_MULTIVARIADO', 'NOTA_SEGUNDA_LENGUA_DOS', 
    'VECES_FISICA_DOS', 'NOTA_EE_DOS', 'VECES_PROG_AVANZADA', 'NAA_DOS', 'VECES_TGS', 'NCA_DOS', 
    'VECES_MULTIVARIADO', 'NOTA_ECUACIONES', 'NOTA_DIFERENCIAL', 'NAC_DOS', 'NCP_DOS', 
    'VECES_SEGUNDA_LENGUA_DOS', 'VECES_EE_DOS', 'VECES_ECUACIONES', 'PG_ICFES', 'NOTA_TEXTOS', 
    'CAR_DOS', 'NCC_DOS', 'NAP_DOS', 'NAP_UNO', 'NOTA_SEMINARIO', 'VECES_LOGICA', 'VECES_EE_UNO', 
    'NAA_UNO', 'VECES_DIFERENCIAL', 'VECES_CATEDRA_DEM', 'NCA_UNO', 'NOTA_CATEDRA_CON', 'NCC_UNO', 
    'NOTA_EE_UNO', 'NAC_UNO', 'NOTA_CATEDRA_DEM', 'NOTA_LOGICA', 'CAR_UNO', 'NOTA_PROG_BASICA', 
    'EPA_DOS', 'IDIOMA_ICFES', 'CON_MAT_ICFES', 'CREDITOS_EE_DOS', 'CREDITOS_ECUACIONES', 
    'CREDITOS_MULTIVARIADO', 'CREDITOS_TGS', 'CREDITOS_SEGUNDA_LENGUA_DOS', 
    'CREDITOS_FISICA_DOS','PROMEDIO_UNO','PROMEDIO_DOS', 'CREDITOS_PROG_AVANZADA', "RENDIMIENTO_TRES","PROMEDIO_TRES"]]

#Se deja solo rendimientos del 1 al 4
sistemas3 = sistemas3[sistemas3['RENDIMIENTO_TRES'].isin([1, 2, 3, 4])]
sistemas3.to_csv("sistemas3.csv", sep=';', index=False)

# Cuarto semestre ingeniería sistemas
sistemas4 = sistemas.loc[:, ['NOTA_METODOS_NUM', 'NOTA_A_SISTEMAS', 'NOTA_MOD_PROG_UNO', 'NOTA_MAT_DIS', 'NOTA_HOMBRE', 
    'NOTA_GT_DOS', 'VECES_A_SISTEMAS', 'VECES_HOMBRE', 'NCC_TRES', 'NAA_DOS', 'NAA_TRES', 
    'NOTA_FUND_BASES', 'NAC_TRES', 'NCA_TRES', 'NOTA_PROG_AVANZADA', 'VECES_MAT_DIS', 'VECES_MAT_ESP', 
    'NCA_DOS', 'NOTA_SEGUNDA_LENGUA_TRES', 'NOTA_DIFERENCIAL', 'NOTA_MAT_ESP', 'VECES_METODOS_NUM', 
    'EPA_TRES', 'NCP_TRES', 'NOTA_TGS', 'VECES_MULTIVARIADO', 'VECES_PROG_AVANZADA', 'NOTA_FISICA_DOS', 
    'VECES_MOD_PROG_UNO', 'VECES_FUND_BASES', 'NOTA_SEGUNDA_LENGUA_DOS', 'VECES_FISICA_DOS', 
    'VECES_SEGUNDA_LENGUA_TRES', 'VECES_GT_DOS', 'CAR_TRES', 'NOTA_MULTIVARIADO', 'NOTA_EE_DOS', 
    'NOTA_ECUACIONES', 'NAP_TRES', 'NAC_DOS', 'VECES_TGS', 'CREDITOS_MOD_PROG_UNO', 'CREDITOS_MAT_ESP', 
    'CREDITOS_A_SISTEMAS', 'CREDITOS_SEGUNDA_LENGUA_TRES', 'CREDITOS_METODOS_NUM', 'CREDITOS_MAT_DIS', 
    'CREDITOS_HOMBRE', 'CREDITOS_GT_DOS', 'CREDITOS_FUND_BASES','PROMEDIO_UNO','PROMEDIO_DOS', "RENDIMIENTO_CUATRO","PROMEDIO_CUATRO"]]

#Se deja solo rendimientos del 1 al 4
sistemas4 = sistemas4[sistemas4['RENDIMIENTO_CUATRO'].isin([1, 2, 3, 4])]
sistemas4.to_csv("sistemas4.csv", sep=';', index=False)

# Quinto semestre ingeniería sistemas
sistemas5 = sistemas.loc[:, ['NOTA_PROB', 'NOTA_CIENCIAS_COMP_UNO', 'NOTA_MOD_PROG_DOS', 'NOTA_ARQ_COMP', 'NOTA_INV_OP_UNO', 
    'NOTA_FISICA_TRES', 'VECES_INV_OP_UNO', 'VECES_PROB', 'NOTA_METODOS_NUM', 'NOTA_MOD_PROG_UNO', 
    'VECES_MOD_PROG_DOS', 'VECES_FISICA_TRES', 'NOTA_EE_TRES', 'VECES_CIENCIAS_COMP_UNO', 'VECES_ARQ_COMP', 
    'VECES_EE_TRES', 'NCC_CUATRO', 'NCA_CUATRO', 'NAP_CUATRO', 'NOTA_MAT_DIS', 'NOTA_A_SISTEMAS', 
    'NAC_TRES', 'NAA_DOS', 'VECES_A_SISTEMAS', 'NOTA_GT_DOS', 'CAR_CUATRO', 'NAA_CUATRO', 'NOTA_FUND_BASES', 
    'NCC_TRES', 'NOTA_HOMBRE', 'NCP_CUATRO', 'NAA_TRES', 'VECES_HOMBRE', 'NAC_CUATRO', 'EPA_CUATRO', 
    'CREDITOS_PROB', 'CREDITOS_INV_OP_UNO', 'PROMEDIO_CINCO', 'CREDITOS_EE_TRES', 'CREDITOS_MOD_PROG_DOS', 
    'CREDITOS_CIENCIAS_COMP_UNO', 'CREDITOS_FISICA_TRES','PROMEDIO_UNO','PROMEDIO_DOS','PROMEDIO_TRES', 'CREDITOS_ARQ_COMP',
    "RENDIMIENTO_CINCO"]]

#Se deja solo rendimientos del 1 al 4
sistemas5 = sistemas5[sistemas5['RENDIMIENTO_CINCO'].isin([1, 2, 3, 4])]
sistemas5.to_csv("sistemas5.csv", sep=';', index=False)


# Sexto semestre ingeniería sistemas
sistemas6 = sistemas.loc[:, ['NOTA_HISTORIA_COL', 'NOTA_ESTADISTICA', 'NOTA_CIBERNETICA_UNO', 'NOTA_INV_OP_DOS', 
    'NOTA_REDES_COM_UNO', 'NOTA_GI_UNO', 'VECES_HISTORIA_COL', 'VECES_CIBERNETICA_UNO', 
    'NOTA_CIENCIAS_COMP_DOS', 'VECES_REDES_COM_UNO', 'VECES_GI_UNO', 'VECES_ESTADISTICA', 
    'NOTA_MOD_PROG_DOS', 'VECES_CIENCIAS_COMP_DOS', 'VECES_INV_OP_DOS', 'CAR_CINCO', 
    'NOTA_METODOS_NUM', 'VECES_FISICA_TRES', 'NOTA_MOD_PROG_UNO', 'NOTA_PROB', 'NAC_CINCO', 
    'NOTA_ARQ_COMP', 'NOTA_CIENCIAS_COMP_UNO', 'NOTA_FISICA_TRES', 'NCA_CINCO', 'NCC_CINCO', 
    'NOTA_INV_OP_UNO', 'VECES_MOD_PROG_DOS', 'VECES_INV_OP_UNO', 'NCP_CINCO', 'NAA_CINCO', 
    'EPA_CINCO', 'NAP_CINCO', 'VECES_PROB', 'CREDITOS_ESTADISTICA', 'CREDITOS_HISTORIA_COL', 
    'CREDITOS_GI_UNO', 'CREDITOS_CIENCIAS_COMP_DOS', 'CREDITOS_INV_OP_DOS', 
    'CREDITOS_CIBERNETICA_UNO', 'CREDITOS_REDES_COM_UNO','PROMEDIO_UNO','PROMEDIO_DOS','PROMEDIO_TRES', "RENDIMIENTO_SEIS","PROMEDIO_SEIS"]]

#Se deja solo rendimientos del 1 al 4
sistemas6 = sistemas6[sistemas6['RENDIMIENTO_SEIS'].isin([1, 2, 3, 4])]
sistemas6.to_csv("sistemas6.csv", sep=';', index=False)

# Septimo semestre ingeniería sistemas
sistemas7 = sistemas.loc[:, ['NOTA_F_ING_SOF', 'NOTA_GT_TRES', 'NOTA_ECONOMIA', 'NOTA_EI_DOS', 'NOTA_REDES_COM_DOS', 
    'VECES_ECONOMIA', 'NOTA_CIBERNETICA_UDOS', 'NOTA_INV_OP_TRES', 'NOTA_INV_OP_DOS', 
    'NOTA_HISTORIA_COL', 'VECES_F_ING_SOF', 'VECES_REDES_COM_DOS', 'NOTA_METODOS_NUM', 
    'VECES_EI_DOS', 'VECES_CIBERNETICA_DOS', 'NOTA_ESTADISTICA', 'NCP_SEIS', 'NOTA_MOD_PROG_DOS', 
    'NOTA_GI_DOS', 'NOTA_FUND_IA', 'CAR_CINCO', 'VECES_GT_TRES', 'NOTA_CIENCIAS_COMP_DOS', 
    'VECES_CIENCIAS_COMP_DOS', 'NAP_SEIS', 'NAC_SEIS', 'NAA_SEIS', 'EPA_SEIS', 'CAR_SEIS', 
    'VECES_FUND_IA', 'VECES_GI_DOS', 'VECES_INV_OP_TRES', 'VECES_GI_UNO', 'VECES_HISTORIA_COL', 
    'VECES_INV_OP_DOS', 'VECES_CIBERNETICA_UNO', 'NOTA_GI_UNO', 'NOTA_CIBERNETICA_UNO', 'NCC_SEIS', 
    'NCA_SEIS', 'NOTA_REDES_COM_UNO', 'VECES_REDES_COM_UNO', 'VECES_ESTADISTICA', 'VECES_FISICA_TRES', 
    'CREDITOS_GI_DOS', 'CREDITOS_ECONOMIA', 'CREDITOS_INV_OP_TRES', 'CREDITOS_GT_TRES', 
    'CREDITOS_F_ING_SOF', 'CREDITOS_FUND_IA', 'CREDITOS_EI_DOS', 'CREDITOS_REDES_COM_DOS', 
    'CREDITOS_CIBERNETICA_DOS','PROMEDIO_UNO','PROMEDIO_DOS','PROMEDIO_TRES','PROMEDIO_CINCO', "RENDIMIENTO_SIETE","PROMEDIO_SIETE"]]

#Se deja solo rendimientos del 1 al 4
sistemas7 = sistemas7[sistemas7['RENDIMIENTO_SIETE'].isin([1, 2, 3, 4])]
sistemas7.to_csv("sistemas7.csv", sep=';', index=False)

# Octavo semestre ingeniería sistemas
sistemas8 = sistemas.loc[:, ['NOTA_DIS_ARQ_SOFT', 'NOTA_EI_OP_AI', 'NOTA_ING_ECONOMICA', 'NOTA_REDES_COM_TRES', 
    'NOTA_CIBERNETICA_TRES', 'VECES_EI_OP_AI', 'VECES_DIS_ARQ_SOFT', 'VECES_ING_ECONOMICA', 
    'VECES_EI_OP_BI', 'VECES_CIBERNETICA_TRES', 'NOTA_INV_OP_DOS', 'NOTA_F_ING_SOF', 
    'VECES_REDES_COM_TRES', 'NAP_SIETE', 'NOTA_GI_DOS', 'NOTA_EI_OP_BI', 'NOTA_INV_OP_TRES', 
    'NCA_SIETE', 'NOTA_REDES_COM_DOS', 'VECES_CIBERNETICA_DOS', 'NOTA_MOD_PROG_DOS', 'CAR_SIETE', 
    'NOTA_EI_DOS', 'NOTA_CIBERNETICA_UDOS', 'NAA_SIETE', 'NCC_SIETE', 'NOTA_ESTADISTICA', 
    'NOTA_GT_TRES', 'NOTA_HISTORIA_COL', 'VECES_REDES_COM_DOS', 'NCP_SEIS', 'NOTA_ECONOMIA', 
    'VECES_EI_DOS', 'NAC_SIETE', 'VECES_ECONOMIA', 'EPA_SIETE', 'NOTA_METODOS_NUM', 'NCP_SIETE', 
    'CREDITOS_CIBERNETICA_TRES', 'CREDITOS_EE_CUATRO', 'VECES_F_ING_SOF', 'NOTA_EE_CUATRO', 
    'CREDITOS_ING_ECONOMICA', 'CREDITOS_EI_OP_BI', 'CREDITOS_EI_OP_AI', 'CREDITOS_DIS_ARQ_SOFT', 
    'CREDITOS_REDES_COM_TRES','PROMEDIO_UNO','PROMEDIO_DOS','PROMEDIO_TRES','PROMEDIO_CINCO','PROMEDIO_SEIS', "RENDIMIENTO_OCHO","PROMEDIO_OCHO"]]

#Se deja solo rendimientos del 1 al 4
sistemas8 = sistemas8[sistemas8['RENDIMIENTO_OCHO'].isin([1, 2, 3, 4])]
sistemas8.to_csv("sistemas8.csv", sep=';', index=False)

# Noveno semestre ingeniería sistemas
sistemas9 = sistemas.loc[:, ['NOTA_EI_OP_AII', 'NOTA_GES_CAL_VAL_SOFT', 'NOTA_EI_OP_CI', 'NOTA_SIS_OP', 
    'VECES_EI_OP_AII', 'VECES_SIS_OP', 'NOTA_ING_ECONOMICA', 'VECES_EI_OP_CI', 
    'NAC_OCHO', 'VECES_GES_CAL_VAL_SOFT', 'VECES_EI_OP_AI', 'NOTA_REDES_COM_TRES', 
    'NCC_OCHO', 'NOTA_EI_OP_BII', 'VECES_EI_OP_BII', 'NOTA_EI_OP_AI', 'VECES_EI_OP_BI', 
    'CAR_OCHO', 'VECES_DIS_ARQ_SOFT', 'NOTA_CIBERNETICA_TRES', 'NAP_OCHO', 'NOTA_DIS_ARQ_SOFT', 
    'VECES_ING_ECONOMICA', 'EPA_OCHO', 'NCP_OCHO', 'NCA_OCHO', 'NAA_OCHO', 
    'CREDITOS_EI_OP_AII', 'CREDITOS_EI_OP_CI', 'CREDITOS_EI_OP_BII', 
    'CREDITOS_SIS_OP', 'CREDITOS_GES_CAL_VAL_SOFT','PROMEDIO_SIETE','PROMEDIO_TRES','PROMEDIO_CINCO','PROMEDIO_SEIS', "RENDIMIENTO_NUEVE","PROMEDIO_NUEVE"]]

#Se deja solo rendimientos del 1 al 4
sistemas9 = sistemas9[sistemas9['RENDIMIENTO_NUEVE'].isin([1, 2, 3, 4])]
sistemas9.to_csv("sistemas9.csv", sep=';', index=False)

# Decimo semestre ingeniería sistemas
sistemas10 = sistemas.loc[:, ['NOTA_FOGEP', 'NOTA_EI_OP_DI', 'NOTA_EI_OP_CII', 'NOTA_EI_OP_CI', 'NOTA_EI_OP_AIII', 
    'NOTA_ING_ECONOMICA', 'VECES_FOGEP', 'NOTA_GRADO_UNO', 'NOTA_GRADO_DOS', 
    'VECES_EI_OP_DI', 'NOTA_EI_OP_BIII', 'NCP_NUEVE', 'NOTA_GES_CAL_VAL_SOFT', 
    'NOTA_SIS_OP', 'VECES_EI_OP_BIII', 'VECES_GRADO_UNO', 'VECES_EI_OP_CII', 
    'NCA_NUEVE', 'NAC_OCHO', 'NAC_NUEVE', 'VECES_EI_OP_CI', 'VECES_GRADO_DOS', 
    'VECES_GES_CAL_VAL_SOFT', 'VECES_EI_OP_AIII', 'CAR_NUEVE', 'NCC_NUEVE', 'NAA_NUEVE', 
    'EPA_NUEVE', 'VECES_EI_OP_AII', 'NAP_NUEVE', 'VECES_SIS_OP', 'NOTA_EI_OP_AII', 
    'CREDITOS_GRADO_DOS', 'CREDITOS_EI_OP_AIII', 'CREDITOS_GRADO_UNO', 'CREDITOS_FOGEP', 
    'CREDITOS_EI_OP_DI', 'CREDITOS_EI_OP_CII','PROMEDIO_SIETE','PROMEDIO_TRES','PROMEDIO_CINCO','PROMEDIO_SEIS', 'CREDITOS_EI_OP_BIII', "RENDIMIENTO_DIEZ"
,"PROMEDIO_DIEZ"]]

#Se deja solo rendimientos del 1 al 4
sistemas10 = sistemas10[sistemas10['RENDIMIENTO_DIEZ'].isin([1, 2, 3, 4])]
sistemas10.to_csv("sistemas10.csv", sep=';', index=False)

#Archivos sistemas por año

#Año 1 sistemas
sistemasAnio1 = sistemas.loc[:, ['CON_MAT_ICFES','IDIOMA_ICFES','LOCALIDAD_COLEGIO','BIOLOGIA_ICFES','QUIMICA_ICFES','PG_ICFES','LITERATURA_ICFES',
  'PROMEDIO_UNO','NOTA_DIFERENCIAL','NOTA_CATEDRA_DEM','NOTA_PROG_BASICA','NAA_UNO','CAR_UNO','NOTA_TEXTOS','NOTA_LOGICA','NOTA_SEMINARIO',
  'VECES_LOGICA','NAC_UNO','NCC_UNO','NCA_UNO','VECES_CATEDRA_DEM','NOTA_EE_UNO','NAP_UNO','VECES_DIFERENCIAL',
  'NOTA_CATEDRA_CON','VECES_EE_UNO','PROMEDIO_TRES']]
sistemasAnio1 = sistemasAnio1[sistemasAnio1['PROMEDIO_TRES'] > 0]
sistemasAnio1.to_csv("sistemasAnio1.csv", sep=';', index=False)

#Año 2 sistemas
sistemasAnio2 = sistemas.loc[:, ['CON_MAT_ICFES','IDIOMA_ICFES','LOCALIDAD_COLEGIO','BIOLOGIA_ICFES','QUIMICA_ICFES','PG_ICFES','LITERATURA_ICFES',
  'PROMEDIO_UNO','NOTA_DIFERENCIAL','NOTA_CATEDRA_DEM','NOTA_PROG_BASICA','NAA_UNO','CAR_UNO','NOTA_TEXTOS','NOTA_LOGICA','NOTA_SEMINARIO',
  'VECES_LOGICA','NAC_UNO','NCC_UNO','NCA_UNO','VECES_CATEDRA_DEM','NOTA_EE_UNO','NAP_UNO','VECES_DIFERENCIAL',
  'NOTA_CATEDRA_CON','VECES_EE_UNO','PROMEDIO_DOS','NOTA_TGS','NOTA_PROG_AVANZADA','NOTA_FISICA_DOS','NOTA_MULTIVARIADO',
  'NOTA_SEGUNDA_LENGUA_DOS','VECES_FISICA_DOS','NOTA_EE_DOS','VECES_PROG_AVANZADA','NAA_DOS','VECES_TGS','NCA_DOS','VECES_MULTIVARIADO','NOTA_ECUACIONES','NAC_DOS',
  'NOTA_METODOS_NUM','NOTA_A_SISTEMAS','NOTA_MOD_PROG_UNO','NOTA_MAT_DIS','NOTA_HOMBRE','NOTA_GT_DOS','VECES_A_SISTEMAS','VECES_HOMBRE','NCC_TRES','NAA_TRES',
  'NOTA_FUND_BASES','NAC_TRES','PROMEDIO_CINCO']]

sistemasAnio2 = sistemasAnio2[sistemasAnio2['PROMEDIO_CINCO'] > 0]
sistemasAnio2.to_csv("sistemasAnio2.csv", sep=';', index=False)

#Año 3 sistemas
sistemasAnio3 = sistemas.loc[:, ['CON_MAT_ICFES','IDIOMA_ICFES','LOCALIDAD_COLEGIO','BIOLOGIA_ICFES','QUIMICA_ICFES','PG_ICFES','LITERATURA_ICFES',
  'PROMEDIO_UNO','NOTA_DIFERENCIAL','NOTA_CATEDRA_DEM','NOTA_PROG_BASICA','NAA_UNO','CAR_UNO','NOTA_TEXTOS','NOTA_LOGICA','NOTA_SEMINARIO',
  'VECES_LOGICA','NAC_UNO','NCC_UNO','NCA_UNO','VECES_CATEDRA_DEM','NOTA_EE_UNO','NAP_UNO','VECES_DIFERENCIAL',
  'NOTA_CATEDRA_CON','VECES_EE_UNO','PROMEDIO_DOS','NOTA_TGS','NOTA_PROG_AVANZADA','NOTA_FISICA_DOS',
  'NOTA_MULTIVARIADO','NOTA_SEGUNDA_LENGUA_DOS','VECES_FISICA_DOS','NOTA_EE_DOS','VECES_PROG_AVANZADA','NAA_DOS','VECES_TGS','NCA_DOS','VECES_MULTIVARIADO','NOTA_ECUACIONES',
  'NAC_DOS','NOTA_METODOS_NUM','NOTA_A_SISTEMAS','NOTA_MOD_PROG_UNO','NOTA_MAT_DIS','NOTA_HOMBRE','NOTA_GT_DOS','VECES_A_SISTEMAS',
  'VECES_HOMBRE','NCC_TRES','NAA_TRES','NOTA_FUND_BASES','NAC_TRES','PROMEDIO_TRES','NOTA_PROB','NOTA_CIENCIAS_COMP_UNO',
  'NOTA_MOD_PROG_DOS','NOTA_ARQ_COMP','NOTA_INV_OP_UNO','NOTA_FISICA_TRES','VECES_INV_OP_UNO','VECES_PROB','VECES_MOD_PROG_DOS','VECES_FISICA_TRES',
  'NOTA_HISTORIA_COL','NOTA_ESTADISTICA','NOTA_CIBERNETICA_UNO','NOTA_INV_OP_DOS','NOTA_REDES_COM_UNO','NOTA_GI_UNO','VECES_HISTORIA_COL','VECES_CIBERNETICA_UNO',
  'NOTA_CIENCIAS_COMP_DOS','VECES_REDES_COM_UNO','VECES_GI_UNO','VECES_ESTADISTICA','VECES_CIENCIAS_COMP_DOS','VECES_INV_OP_DOS','CAR_CINCO',
  'PROMEDIO_CINCO','NOTA_F_ING_SOF','NOTA_GT_TRES','NOTA_ECONOMIA','NOTA_EI_DOS','NOTA_REDES_COM_DOS','VECES_ECONOMIA','NOTA_CIBERNETICA_UDOS','NOTA_INV_OP_TRES',
  'VECES_F_ING_SOF','VECES_REDES_COM_DOS','VECES_EI_DOS','VECES_CIBERNETICA_DOS','NCP_SEIS','NOTA_GI_DOS','PROMEDIO_SEIS','NOTA_DIS_ARQ_SOFT','NOTA_EI_OP_AI',
  'NOTA_ING_ECONOMICA','NOTA_REDES_COM_TRES','NOTA_CIBERNETICA_TRES','VECES_EI_OP_AI','VECES_DIS_ARQ_SOFT','VECES_ING_ECONOMICA','VECES_EI_OP_BI',
  'VECES_CIBERNETICA_TRES','PROMEDIO_NUEVE']]

sistemasAnio3 = sistemasAnio3[sistemasAnio3['PROMEDIO_NUEVE'] > 0]
sistemasAnio3.to_csv("sistemasAnio3.csv", sep=';', index=False)