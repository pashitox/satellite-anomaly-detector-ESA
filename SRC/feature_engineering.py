# === src/feature_engineering.py ===
import pandas as pd
from datetime import timedelta

def parse_timestamp_column(df, column_name='timestamp'):
    """Convierte la columna timestamp a tipo datetime si no lo está."""
    if column_name in df.columns:
        if not pd.api.types.is_datetime64_any_dtype(df[column_name]):
            df[column_name] = pd.to_datetime(df[column_name], errors='coerce')
    return df


def merge_events_and_commands(anomalies_df, events_df=None, commands_df=None, window=60):
    """
    Funde eventos y comandos cercanos temporalmente a las anomalías.
    
    Parámetros:
    - anomalies_df: DataFrame con anomalías. Debe tener columna 'timestamp'
    - events_df: DataFrame con eventos (opcional). Debe tener columna 'timestamp'
    - commands_df: DataFrame con telecommands (opcional). Debe tener columna 'timestamp'
    - window: int (segundos) ± ventana para buscar coincidencias

    Retorna:
    - anomalies_enriched: DataFrame con columnas nuevas sobre eventos y comandos cercanos
    """
    anomalies_df = parse_timestamp_column(anomalies_df, 'timestamp')
    
    if events_df is not None:
        events_df = parse_timestamp_column(events_df, 'timestamp')
        anomalies_df['near_event'] = anomalies_df['timestamp'].apply(
            lambda ts: ((events_df['timestamp'] >= ts - timedelta(seconds=window)) &
                        (events_df['timestamp'] <= ts + timedelta(seconds=window))).any()
        )
    else:
        anomalies_df['near_event'] = False
    
    if commands_df is not None:
        commands_df = parse_timestamp_column(commands_df, 'timestamp')
        anomalies_df['near_command'] = anomalies_df['timestamp'].apply(
            lambda ts: ((commands_df['timestamp'] >= ts - timedelta(seconds=window)) &
                        (commands_df['timestamp'] <= ts + timedelta(seconds=window))).any()
        )
    else:
        anomalies_df['near_command'] = False

    return anomalies_df
