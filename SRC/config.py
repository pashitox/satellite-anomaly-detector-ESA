# config.py
from pathlib import Path
import time

class Config:
    BASE_DIR = Path("../DATA")  # Ruta base donde están tus datos
    MISSIONS = ["ESA-Mission1", "ESA-Mission2", "ESA-Mission3"]  # Nombres de las misiones
    FILE_MAP = {
        'anomalies': 'anomaly_types.csv',
        'channels': 'channels.csv',
        'labels': 'labels.csv',
        'telecommands': 'telecommands.csv',
        'events': 'events.csv'
    }

    @classmethod
    def setup_paths(cls):
        start_time = time.time()
        print("\n🔧 [CONFIG] Iniciando configuración de rutas...")
        print(f"📁 Directorio base: {cls.BASE_DIR.resolve()}")
        print(f"🛰 Misiones disponibles: {', '.join(cls.MISSIONS)}")

        if not cls.BASE_DIR.exists():
            print("❌ [ERROR] El directorio base no existe. Verifica la ruta.")
            return False

        print(f"✅ [CONFIG] Rutas configuradas correctamente en {time.time() - start_time:.2f} segundos.\n")
        return True
