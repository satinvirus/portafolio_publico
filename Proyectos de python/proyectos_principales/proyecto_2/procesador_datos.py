import pandas as pd
import os

ruta_actual = os.path.dirname(__file__)
ruta_plantilla = os.path.join(ruta_actual, 'plantilla_dashboard.html')


def procesar_informe_prueba1():
    print("Iniciando pipeline de datos...")

    #carga de datos
    df = pd.read_csv('lecturas.csv')

    #purificacion

    #filtro de valores que sen mayores a 0 & menores a 100
    datos_limpios = df[(df['valor'] > 0) & (df['valor'] <100)]

    #filtro 2 valores mayores a 10

    datos_limpios = datos_limpios[datos_limpios['voltaje'] > 10]

    #se añade la funciond de promedio
    promedio = datos_limpios['valor'].mean()

    #se imprime un mensaje de finalizacion y se añade el valor final del promedio

    print(f"datos procesados. promedio:{promedio:.2f}")

    #se exporta un archivo nuevo .csv con los datos ya filtrados
    datos_limpios.to_csv('datos_finales.csv', index=False)
    print("Archivo generado")




def procesar_informe():
    print("🚀 Iniciando Pipeline de Datos...")
    
    # 1. Cargar y Limpiar los datos
    df = pd.read_csv('lecturas.csv')
    datos_limpios = df[(df['valor'] > 0) & (df['valor'] < 100)]
    datos_limpios = datos_limpios[datos_limpios['voltaje'] > 10]
    
    promedio = datos_limpios['valor'].mean()
    print(f"✅ Datos limpios. Promedio: {promedio:.2f}")
    
    # 2. Preparar datos para JavaScript
    # Convertimos las columnas a listas de Python para que JS las entienda
    fechas_js = str(datos_limpios['fecha'].tolist())
    valores_js = str(datos_limpios['valor'].tolist())
    promedio_texto = f"{promedio:.2f} unidades"
    
    # 3. Leer la plantilla HTML
    with open(ruta_plantilla, 'r', encoding='utf-8') as archivo_html:
        html_contenido = archivo_html.read()
        
    # 4. Inyectar los datos en el HTML
    html_final = html_contenido.replace('{{FECHAS}}', fechas_js)
    html_final = html_final.replace('{{VALORES}}', valores_js)
    html_final = html_final.replace('{{PROMEDIO}}', promedio_texto)
    
    # 5. Generar el Dashboard final
    with open('reporte_final.html', 'w', encoding='utf-8') as archivo_final:
        archivo_final.write(html_final)
        
    print("📁 ¡Éxito! Abre 'reporte_final.html' para ver tu gráfica interactiva.")




if __name__ == "__main__":
    procesar_informe()