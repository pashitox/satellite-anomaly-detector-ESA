"""
Módulo load_data.py - Versión definitiva
Guarda este archivo en: C:\Users\JMGY-\Documents\Advance-data-analitic\5.5 PROYECTO NASA\SRC\
"""

import pandas as pd
from pathlib import Path
import warnings

def load_mission_data(mission_name='ESA-Mission2', date_range=None):
    """Función principal para cargar datos de anomalías"""
    try:
        # 1. Configuración de rutas
        base_path = Path(r"C:\Users\JMGY-\Documents\Advance-data-analitic\5.5 PROYECTO NASA\DATA")
        mission_path = base_path / mission_name / mission_name
        
        # 2. Carga de archivos esenciales
        labels = pd.read_csv(
            mission_path / 'labels.csv',
            parse_dates=['StartTime', 'EndTime'],
            usecols=['ID', 'Channel', 'StartTime', 'EndTime']
        )
        
        anomalies = pd.read_csv(
            mission_path / 'anomaly_types.csv',
            usecols=['ID', 'Category', 'Dimensionality']
        )

        # 3. Combinación de datos
        merged = pd.merge(labels, anomalies, on='ID', how='left')
        
        # 4. Cálculo de duración
        merged['Duration'] = (merged['EndTime'] - merged['StartTime']).dt.total_seconds() / 3600
        
        # 5. Filtrado por fecha
        if date_range:
            mask = (merged['StartTime'] >= pd.to_datetime(date_range[0])) & \
                   (merged['StartTime'] <= pd.to_datetime(date_range[1]))
            merged = merged[mask].copy()
            
        return merged
    
    except Exception as e:
        warnings.warn(f"Error en load_mission_data: {str(e)}")
        raise

# Verificación interna del módulo
if __name__ == "__main__":
    print("🔍 Prueba interna del módulo load_data.py")
    test_data = load_mission_data()
    print(f"Datos de prueba cargados: {len(test_data)} registros")