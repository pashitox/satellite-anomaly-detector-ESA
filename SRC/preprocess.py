import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class SatelliteDataCleaner(BaseEstimator, TransformerMixin):
    """
    Pipeline de limpieza para datos satelitales:
    - Manejo de valores atípicos
    - Codificación de características
    - Normalización temporal
    """
    
    def __init__(self, max_value=1e6, time_freq='5T'):
        self.max_value = max_value
        self.time_freq = time_freq
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Copia profunda para evitar warnings
        X = X.copy()
        
        # 1. Limpieza de valores extremos
        X['Value'] = np.where(
            X['Value'].abs() > self.max_value,
            np.nan,
            X['Value']
        )
        
        # 2. Codificación de canales (one-hot para <10 categorías)
        channel_counts = X['Channel'].value_counts()
        common_channels = channel_counts[channel_counts > 100].index
        X['Channel'] = np.where(
            X['Channel'].isin(common_channels),
            X['Channel'],
            'OTHER'
        )
        
        # 3. Muestreo temporal uniforme
        X = X.set_index('Timestamp')
        X = X.groupby('Channel').resample(self.time_freq).mean().reset_index()
        
        # 4. Interpolación inteligente
        for channel in X['Channel'].unique():
            mask = X['Channel'] == channel
            X.loc[mask, 'Value'] = X.loc[mask, 'Value'].interpolate(
                method='time',
                limit_direction='both'
            )
        
        return X.dropna()

def add_engineering_features(df):
    """Añade características avanzadas para detección de anomalías"""
    df = df.copy()
    
    # 1. Diferencias temporales
    df['Value_diff'] = df.groupby('Channel')['Value'].diff()
    
    # 2. Media móvil (para detectar derivas)
    df['Rolling_avg'] = df.groupby('Channel')['Value'].transform(
        lambda x: x.rolling(window=12, min_periods=1).mean()
    )
    
    # 3. Componentes de Fourier (para patrones periódicos)
    for channel in df['Channel'].unique()[:3]:  # Solo canales principales
        vals = df.loc[df['Channel'] == channel, 'Value'].values
        if len(vals) > 10:
            df.loc[df['Channel'] == channel, 'Fourier_1'] = np.fft.fft(vals).real[:len(vals)]
    
    return df

def clean_telemetry(df):
    """
    Versión simplificada para compatibilidad
    """
    import pandas as pd
    df = df.copy()
    
    # 1. Limpieza básica
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df = df.dropna(subset=['Timestamp', 'Value'])
    
    # 2. Filtrado de valores extremos
    df = df[(df['Value'].abs() < 1e6)]
    
    return df.reset_index(drop=True)