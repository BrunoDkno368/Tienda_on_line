import os

def guardar_csv(df, nombre_archivo):
    base_dir = os.path.dirname(os.path.dirname(__file__))  # raíz del proyecto
    output_dir = os.path.join(base_dir, "outputs")

    # Crear carpeta si no existe
    os.makedirs(output_dir, exist_ok=True)

    ruta_salida = os.path.join(output_dir, nombre_archivo)
    df.to_csv(ruta_salida, index=False)

    print(f"✅ Archivo guardado en: {ruta_salida}")