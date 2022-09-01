from datetime import datetime
import pandas as pd
import numpy as np

def diff_minutes(start,end,input_format:str="%Y-%m-%d %H:%M:%S"):
    """
    Calcula la diferencia en minutos entre dos fechas
    Argumentos:
        - start: str = Fecha de inicio
        - end: str = Fecha de salida
        - input_format: str = Formato de la fecha de entrada y salida. El valor por defecto es: "%Y-%m-%d %H:%M:%S"
    Salida:
        - minutos de diferencia (float)
        """
    start_norm = datetime.strptime(start,input_format)
    end_norm = datetime.strptime(end,input_format)
    minutes_diff = (end_norm - start_norm).total_seconds() / 60.0
    return minutes_diff

def resume_col(df,col):
    """
    Resumen de variables categóricas
    Entrada:
    - df: Dataframe
    - col: Columna del dataframe
    Salida
    - Resumen de cada categoría (conteo y porcentaje)
    """
    resume_count = df[col].value_counts().reset_index().rename({col:"CONTEO","index":col},axis=1)
    resume_porc = df[col].value_counts(normalize=True).reset_index().rename({col:"PORCENTAJE","index":col},axis=1)
    resume_porc["PORCENTAJE"] = resume_porc["PORCENTAJE"].apply(lambda x: str(round(x*100,3))+"%")
    resume = resume_count.merge(resume_porc,on=col,how="inner")
    return resume

def get_outliers(df):
    """
    Entrada:
    - df float: Entrada numérica
    Salida
    - tuple: (Outliers, Not Outliers)
    """
    q1=df.quantile(0.25)
    q3=df.quantile(0.75)
    IQR=q3-q1
    r_sup = q3 + 1.5*IQR
    r_inf = q1 - 1.5*IQR
    outliers = df[((df<r_inf) | (df>r_sup))]
    not_outliers = df[~((df<r_inf) | (df>r_sup))]
    return outliers, not_outliers

def temporada_alta(input_date,input_format="%Y-%m-%d %H:%M:%S"):
    """
    Retorna la temporada, siendo 1 temporada alta y 0 temporada baja.
    Entrada:
        - input_date: str = Campo de fecha
        - input_format:str = Formato de la fecha de entrada
    Salidas:
        - {0,1} en tipo int
    """
    date_fmt = datetime.strptime(input_date,input_format).strftime("%Y-%m-%d")
    year = datetime.strptime(input_date,input_format).strftime("%Y")
    if date_fmt>=f"{year}-12-15" and date_fmt <=f"{year}-12-31":
        return 1
    elif date_fmt>=f"{year}-01-01" and date_fmt <=f"{year}-03-03":
        return 1
    elif date_fmt>=f"{year}-07-15" and date_fmt <=f"{year}-07-31":
        return 1
    elif date_fmt>=f"{year}-09-11" and date_fmt <=f"{year}-09-30":
        return 1
    else:
        return 0

def date2date(input_date,input_format="%Y-%m-%d %H:%M:%S"):
    """
    Normalización de la fecha
    Entrada:
        - input_date: str = Campo de fecha
        - input_format: str = Formato de la fecha de entrada
    Salida:
        - Fecha estandarizada en el formato '%Y-%m-%d' 
    """
    return datetime.strptime(input_date,input_format).strftime("%Y-%m-%d")

def retraso(x,minutos:float=15.0):
    """
    Retorna si un vuelo tuvo retraso, siendo 1 retraso y 0 dentro del margen aceptable.
    Entrada:
        - x:float = Campo de entrada (minutos)
        - minutos:float = Parámetro a definir cuando es considerado un retraso
    Salida:
        - {0,1} en tipo int"""
    if x > minutos:
        return 1
    else:
        return 0

def periodo_dia(input_date,input_format="%Y-%m-%d %H:%M:%S"):
    """
    Retorna el momento del día (mañana, tarde y noche)
    Entrada:
        - input_date: str = Campo de fecha
        - input_format: str = Formato de la fecha de entrada
    Salida
        - Momento del día: str {'mañana', 'tarde' o 'noche')
    """
    time = datetime.strptime(input_date,input_format).strftime("%H:%M")
    if time >= "05:00" and time <= "11:59":
        return "mañana"
    elif time >= "12:00" and time <= "18:59":
        return "tarde"
    else:
        return "noche"