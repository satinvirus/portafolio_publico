import pandas as pd
import os

def procesar_informe():
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

if __name__ == "__main__":
    procesar_informe()