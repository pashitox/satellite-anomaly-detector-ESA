import joblib
import pandas as pd

# 🔍 Cargamos modelo y encoder
modelo = joblib.load("modelo_ganador_xgb.joblib")
encoder_y = joblib.load("label_encoder_y.joblib")

# 📥 Cargar nuevas anomalías (sin columna 'Class')
nuevas_anomalias = pd.read_csv("processed/features_dataset.csv")  # ajusta path si usas otro archivo

# 💡 Codificar columnas categóricas igual que antes
from sklearn.preprocessing import LabelEncoder

for col in nuevas_anomalias.select_dtypes(include='object').columns:
    le_col = LabelEncoder()
    nuevas_anomalias[col] = le_col.fit_transform(nuevas_anomalias[col].astype(str))

# 🧠 Hacer predicción
predicciones_codificadas = modelo.predict(nuevas_anomalias)

# 🔁 Decodificar etiquetas
predicciones = encoder_y.inverse_transform(predicciones_codificadas)

# 📊 Mostrar resultados
print("\n🛰️ Predicciones reales sobre nuevas anomalías:")
print(predicciones[:20])  # mostramos los primeros 20 como ejemplo