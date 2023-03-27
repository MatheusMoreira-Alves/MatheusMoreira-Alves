import pandas as pd
import time

# Lê o arquivo .csv em um DataFrame, utilizando a codificação ISO-8859-1 e o separador ";" e registrando o tempo de início;
def read_csv_file(file_path):
    print('Lendo o arquivo .csv...')

    start_time = time.time()
    df = pd.read_csv(file_path, sep=';', encoding='ISO-8859-1', low_memory=False)

    # Registra o tempo de fim da leitura do arquivo
    end_time = time.time()

    # Calcula o tempo total de leitura do arquivo
    read_time = end_time - start_time

    print(f'Tempo de leitura do arquivo: {read_time:.2f} segundos')

    return df
