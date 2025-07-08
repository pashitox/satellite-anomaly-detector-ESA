# === main.py ===
if __name__ == "__main__":
    import warnings
    warnings.filterwarnings("ignore")

    print("🔧 Configurando proyecto...")
    config = Config()

    loader = DataLoader()
    data = loader.load_all_missions()

    preproc = DataPreprocessor()
    
    # Preprocesar anomalies de ESA-Mission1
    anomalies_df = data['ESA-Mission1'].get('anomalies')
    if anomalies_df is not None:
        df_processed = preproc.preprocess_anomalies(anomalies_df)
        preproc.save_artifacts("./artifacts")
    else:
        print("❌ No se encontró dataset 'anomalies' en ESA-Mission1")

    # Preparar datos para entrenar modelo
    labels_df = data['ESA-Mission1'].get('labels')
    if labels_df is not None and df_processed is not None:

        # Crear una columna target de ejemplo (categorías codificadas)
        df_processed['target'] = labels_df.iloc[:, 0].astype('category').cat.codes

        # 🔍 Eliminar columnas con tipo object (como 'ID')
        for col in df_processed.columns:
            if df_processed[col].dtype == 'object':
                print(f"🔎 Eliminando columna no numérica: {col}")
                df_processed.drop(columns=[col], inplace=True)

        # Separar variables predictoras y objetivo
        X = df_processed.drop(columns=['target'])
        y = df_processed['target']

        # Entrenar modelo
        trainer = ModelTrainer()
        trainer.train(X, y)

    else:
        print("❌ Datos insuficientes para entrenamiento")

