# Función para exportar archivo en formato .CSV al directorio local.
import os

def guardar_archivo():
    try:
        ingreso_ruta = input('Copie y pegue el directorio donde guardar el archivo .CSV: ')
        ruta_archivo = f"{ingreso_ruta}"
        nombre_csv_salida = "comisiones_consolidadas.csv"
        ruta_salida_completa = os.path.join(ruta_archivo, nombre_csv_salida)
        df_final_limpio.to_csv(ruta_salida_completa, index=False, encoding='utf-8')
        mensaje = print('✅ ¡Archivo guardado exitosamente!')
        
    except Exception as e:
        mensaje = print('⚠️ No se pudo guardar el archivo por el siguiente error:')
        print(type(e))
    return mensaje
