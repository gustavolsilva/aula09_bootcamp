import pandas as pd
import os
import glob

from utils_log import log_decorator

@log_decorator
# uma funcao de extract que le e consolida os json
def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    '''
    Funcao para extrair os dados dos arquivos json
    e consolidadar em um unico dataframe pandas
    '''
    arquivos_json = glob.glob(os.path.join(pasta, "*.json"))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

@log_decorator
# uma funcao que transforma
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Funcao de calculo de KPI de total de vendas
    criando uma coluna no dataframe
    '''
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

@log_decorator
# uma funcao que da load em csv ou parquet
def carregar_dados(df: pd.DataFrame, format_saida: list):
    '''
    Funcao para carregar os dados em um arquivo csv ou parquet
    '''
    for formato in format_saida:
        if formato == 'csv':
            df.to_csv("dados.csv", index=False)
        if formato == 'parquet':
            df.to_parquet("dados.parquet")

@log_decorator
def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_de_saida: list):
    data_frame = extrair_dados_e_consolidar(pasta=pasta)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_de_saida)  