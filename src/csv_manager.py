import os
import pandas as pd
from typing import Optional

# ----- CSV Management Functions ----- #
def create_csv(df: pd.DataFrame, folder: str, start_year: int, end_year: Optional[int] = None) -> None:
    data_dir = '../data/' + folder
    if not os.path.exists(data_dir):
        os.makedirs(data_dir) # Create directory if it doesn't exist

    if end_year is None:
        csv_filename = f'{data_dir}/statcast_{start_year}.csv'
    else:
        csv_filename = f'{data_dir}/statcast_{start_year}_to_{end_year}.csv'

    df.to_csv(csv_filename, index=False)

    print(f"Datos guardados en: {csv_filename}")
    print(f"Archivo creado con {len(df)} filas y {len(df.columns)} columnas")

def read_csv(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path): # Check if file exists
        raise FileNotFoundError(f"El archivo {file_path} no existe.")
    
    df = pd.read_csv(file_path)
    print(f"Datos leídos desde: {file_path}")
    print(f"Archivo contiene {len(df)} filas y {len(df.columns)} columnas")
    return df

def append_csv(folder: str, start_year: int, end_year: int) -> pd.DataFrame:
    data_dir = '../data/' + folder
    all_files = []
    for year in range(start_year, end_year + 1):
        csv_filename = f'{data_dir}/statcast_{year}.csv'
        if os.path.exists(csv_filename):
            all_files.append(csv_filename)
    
    if not all_files:
        raise FileNotFoundError(f"No se encontraron archivos CSV en el directorio {data_dir}.")

    df_list = []
    for file in all_files: # Read each CSV and append to list
        df = pd.read_csv(file)
        df_list.append(df)
        print(f"Datos leídos desde: {file} con {len(df)} filas y {len(df.columns)} columnas")

    combined_df = pd.concat(df_list, ignore_index=True) # Combine all DataFrames
    print(f"Datos combinados: {len(combined_df)} filas y {len(combined_df.columns)} columnas en total")
    return combined_df