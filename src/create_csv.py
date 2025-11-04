import os
import pandas as pd

def create_csv(df: pd.DataFrame, start_date: str, end_date: str) -> None:
    data_dir = '../data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Guardar el DataFrame en CSV
    csv_filename = f'{data_dir}/statcast_{start_date}_to_{end_date}.csv'
    df.to_csv(csv_filename, index=False)

    print(f"✓ Datos guardados en: {csv_filename}")
    print(f"Archivo creado con {len(df)} filas y {len(df.columns)} columnas")