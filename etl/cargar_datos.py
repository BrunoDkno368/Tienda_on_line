import pandas as pd

def cargar_clientes(ruta):
    df = pd.read_csv(ruta)
    df.columns = df.columns.str.strip().str.lower()
    return df

def cargar_productos(ruta):
    df = pd.read_csv(ruta)
    df.columns = df.columns.str.strip().str.lower()
    return df

def cargar_ordenes(ruta):
    df = pd.read_csv(ruta)
    df.columns = df.columns.str.strip().str.lower()
    return df

def cargar_items(ruta):
    df = pd.read_csv(ruta)
    df.columns = df.columns.str.strip().str.lower()
    return df