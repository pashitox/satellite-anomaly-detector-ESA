import os
import pandas as pd
import joblib

# Cargar modelo desde ruta completa
ruta_modelo = r"C:\Users\JMGY-\Documents\Advance-data-analitic\5.5 PROYECTO NASA\MODELS\modelo_ganador_xgb.joblib"
modelo = joblib.load(ruta_modelo)
print("✅ Modelo cargado correctamente")

# Asegurar carpeta de reporte
os.makedirs("reports", exist_ok=True)

# Cargar datos nuevos
ruta_csv = r"C:\Users\JMGY-\Documents\Advance-data-analitic\5.5 PROYECTO NASA\NOTEBOOK\data\nuevos_eventos.csv"
if os.path.exists(ruta_csv):
    nuevos_datos = pd.read_csv(ruta_csv)

    # Reordenar columnas al orden usado en entrenamiento
    columnas = ['Subclass', 'Category', 'Dimensionality', 'Locality', 'Length']
    nuevos_datos = nuevos_datos[columnas]

    # Aplicar predicción
    predicciones = modelo.predict(nuevos_datos)
    resultados = pd.DataFrame({
        "Index_origen": nuevos_datos.index,
        "Predicción": predicciones
    })

    # Guardar resultado
    salida = "reports/predicciones_nuevas.csv"
    resultados.to_csv(salida, index=False)
    print(f"✅ Predicciones guardadas en: {salida}")
else:
    print("❌ El archivo data/nuevos_eventos.csv no existe")