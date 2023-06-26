# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 18:04:01 2023

@author: gabriel.rodrigues
"""

import pandas as pd

df = pd.read_excel(R'C:\Users\gabriel.rodrigues\Desktop\teste_teste.xlsx')

df = df.dropna(subset=['nome_cliente'], inplace=False)
df = df.dropna(subset=['COTA'], inplace=False)

with open('nome_cliente_arquivar.in', 'w') as arquivo:
    # Percorre as linhas do DataFrame
    for indice, linha in df.iterrows():
        # Escreve os valores das colunas no arquivo IN
        for valor in linha:
            arquivo.write(str(valor) + ' ')
        arquivo.write('\n')
