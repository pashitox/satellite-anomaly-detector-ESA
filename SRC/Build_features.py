import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Rutas de los archivos fuente
origen_1 = r"C:\Users\JMGY-\Documents\Advance-data-analitic\5.5 PROYECTO NASA\DATA\ESA-Mission1\ESA-Mission1\anomaly_types.csv"
origen_2 = r"C:\Users\JMGY-\Documents\Advance-data-analitic\5.5 PROYECTO NASA\DATA\ESA-Mission2\ESA-Mission2\anomaly_types.csv"
origen_3 = r"C:\Users\JMGY-\Documents\Advance-data-analitic\5.5 PROYECTO NASA\DATA\ESA-Mission3\ESA-Mission3\anomaly_types.csv"

# Leer y unir
dataframes = []
for path in [origen_1, origen_2, origen_3]:
    if os.path.exists(path):
        df = pd.read_csv(path)
        df['mission'] = os.path.basename(os.path.dirname(path))
        dataframes.append(df)

# Unimos todo
df_total = pd.concat(dataframes).reset_index(drop=True)

# Seleccionamos columnas clave
columnas_utiles = ['Class', 'Subclass', 'Category', 'Dimensionality', 'Locality', 'Length', 'mission']
df_total = df_total[columnas_utiles].dropna()

# Codificamos categóricas
for col in df_total.columns:
    if df_total[col].dtype == 'object':
        le = LabelEncoder()
        df_total[col] = le.fit_transform(df_total[col].astype(str))

# Guardamos
os.makedirs("processed", exist_ok=True)
df_total.to_csv("processed/features_dataset.csv", index=False)

print("✅ Dataset de features generado: processed/features_dataset.csv")