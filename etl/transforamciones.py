import pandas as pd

def unir_tablas (ordenes,clientes, items, productos ):

    #unimos ordenes con clientes 
    df= ordenes.merge(clientes, on ='cliente_id',how='left')

    #uniro con items
    df= df.merge(items, on='orden_id', how='left')

    #unir con producto
    df=df.merge(productos, on='producto_id', how='left')

    return df

def calcular_metricas(df):
    df['ventas'] = df['cantidad']* df['precio_unitario']
    df['costo'] = df['cantidad']* df['costo_unitario']
    df['ganancia'] = df['ventas'] - df['costo']
    df['fecha_orden'] = pd.to_datetime(df['fecha_orden'], errors='coerce')
    df['margen_pct'] = (df['ganancia'] / df['ventas']) * 100
    df['mes'] = df['fecha_orden'].dt.to_period('M')

    return (df)

