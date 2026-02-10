from cargar_datos import*
from transforamciones import*
from analisis import*
from exportar import guardar_csv

def main ():

    #cargar datos
    ordenes= cargar_ordenes(r'C:\Users\Bruno\Desktop\ETL visual studio\proy reales\tienda online\data\ordenes.csv')
    clientes= cargar_clientes (r'C:\Users\Bruno\Desktop\ETL visual studio\proy reales\tienda online\data\clientes.csv')
    items= cargar_items(r'C:\Users\Bruno\Desktop\ETL visual studio\proy reales\tienda online\data\items_orden.csv')
    productos= cargar_productos(r'C:\Users\Bruno\Desktop\ETL visual studio\proy reales\tienda online\data\productos.csv')
    
    df = unir_tablas(ordenes, clientes, items, productos)
    df = calcular_metricas(df)

        # Guardar dataset final limpio
    guardar_csv(df, "dataset_ventas_limpio.csv")

        # Análisis
    ventas_mes = ventas_por_mes(df)
    ventas_categoria = ventas_por_categoria(df)
    top_prod = top_productos(df)
    top_cli = top_clientes(df)

        # Guardar resultados
    guardar_csv(ventas_mes, "ventas_por_mes.csv")
    guardar_csv(ventas_categoria, "ventas_por_categoria.csv")
    guardar_csv(top_prod, "top_productos.csv")
    guardar_csv(top_cli, "top_clientes.csv")

if __name__ == "__main__":
    main()