def ventas_por_mes (df):
    return df.groupby ('mes')['ventas'].sum().reset_index()

def ventas_por_categoria (df):
    return df.groupby ('categoria')['ventas'].sum().sort_values(ascending=False).reset_index()

def top_productos (df, n=5):
    return( df.groupby('nombre_producto')['ganancia']
           .sum().sort_values(ascending=False)
           .head(n).reset_index())

def top_clientes (df, n=5):
    return(df.groupby('nombre')['ventas']
           .sum().sort_values(ascending= False)
           .head(n).reset_index())    

def ventas_por_canal(df):
    return df.groupby('canal_ventas')['ventas'].sum().reset_index()