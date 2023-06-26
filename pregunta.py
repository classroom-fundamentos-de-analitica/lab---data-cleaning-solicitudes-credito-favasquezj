"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from re import match
from datetime import datetime

def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    df = df.dropna()

    df['sexo'] = [x.lower() for x in df['sexo']]
    df['tipo_de_emprendimiento'] = [x.lower() for x in df['tipo_de_emprendimiento']]
    df['idea_negocio'] = [x.lower().replace("_", " ").replace("-", " ") for x in df['idea_negocio']]
    df['barrio'] = [x.lower().replace("_", " ").replace("-", " ") for x in df['barrio']]
    df['línea_credito'] = [x.lower().replace("-", " ").replace("_", " ") for x in df['línea_credito']]
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(int)

    df['monto_del_credito'] = [float(x.strip("$").replace(",", "")) for x in df['monto_del_credito']]

    date_formats = ["%d/%m/%Y", "%Y/%m/%d"]
    df['fecha_de_beneficio'] = [parse_date(x, date_formats) for x in df['fecha_de_beneficio']]

    df = df.drop_duplicates()
    return df

def parse_date(date_str, date_formats):
    for fmt in date_formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            pass
    raise ValueError("Invalid date format: '{}'".format(date_str))
