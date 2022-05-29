from numpy import int64, integer
import pandas as pd
import requests
from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d")
fiis = []

def request(url,param):
    """
    Faz request no site e puxa a tabela para o pandas.
    """
    r = requests.get(f"{url}", headers={'User-Agent':'Mozzila/5.0'})
    df_list = pd.read_html(r.text)
    df = df_list[param]
    return df

def point_remove(df,list_columns):
    """
    Formatação de colunas, removendo a string monetária.
    """
    df_stage = df
    for columns in list_columns:
        df_stage[columns] = df_stage[columns].replace(',', '.', regex=True)
        df_stage[columns] = df_stage[columns].replace('[^.0-9\-]', '', regex=True).astype(float)
    return df_stage

def value_import(df,code):
    """ 
    Medidas importantes para avaliar um fii sendo guardadas em um dicionário e posteriormente
    guardadas em uma lista.
    """
    result = {}
    result["Papel"] = code
    result["Mediana"] = df["Dividendo"].median()
    result["Desvio"] = df["Dividendo"].std()
    result["Cotacao"] = df["Cotação base"].iloc[0]
    fiis.append(result)
    return fiis

def market_rule():
    """
    Regra de negócio aplicada para a estratégia utilizada e lista geral com todos os fiis.
    """
    df = request("https://www.fundamentus.com.br/fii_resultado.php",0)
    df.drop(columns=['Segmento', 'Cotação','FFO Yield', 'Valor de Mercado', 'Preço do m2', 'Aluguel por m2', 'Cap Rate', 'Vacância Média'], inplace=True)
    df['Liquidez'] = df['Liquidez'].replace('[.,]','', regex=True).astype('int64')
    df = df.loc[df['Liquidez'] >= 200000]
    df = df.loc[df['P/VP'] <= 100]
    df['P/VP'] = df['P/VP']/100
    return df

df = market_rule()

for codes in df['Papel']:
    """
    Request no site com informações dos últimos dividendos pagos para avaliação de métricas
    utilizamos o for para pergamos informações dos últimos 10 meses de todos os fiis puxados
    da fundamentus.
    """
    dataframe = request(f"https://fiis.com.br/{codes}/",1)
    dataframe = point_remove(dataframe, ["Dividendo"])
    resultado = value_import(dataframe, codes)

# Último tratamento e regra de negócio para ser enviada ao sheets e 
# posteriomente feita a sua análise
tabela_fiis=pd.DataFrame(data=fiis)
df_final = df.join((tabela_fiis.set_index('Papel')), lsuffix="_left", on='Papel')
df_final['Cotacao'] = df_final['Cotacao'].replace('[^,.0-9\-]', '', regex=True)
df_final = df_final.loc[df_final['Desvio'] <= 0.25]
df_final.to_excel(f'result-{date}.xlsx', index=False)