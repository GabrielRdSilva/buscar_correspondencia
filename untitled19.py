# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 08:13:55 2023

@author: gabriel.rodrigues
"""

import pandas as pd

# Lê o arquivo Excel com as duas colunas
df = pd.read_excel(R'C:\Users\gabriel.rodrigues\Desktop\teste_teste.xlsx')

# Obtém as duas colunas do DataFrame
coluna1 = df['nome_cliente']
coluna2 = df['COTA']

# Cria uma nova lista intercalando as informações das colunas 1 e 2
nova_lista = []
for valor1, valor2 in zip(coluna1, coluna2):
    nova_lista.append(str(valor1))
    nova_lista.append(str(valor2).replace('.0', ''))

# Gera o conteúdo do arquivo IN
conteudo = '\n'.join(nova_lista)

# Salva o conteúdo no arquivo IN
with open('cliente_e_cota.in', 'w') as arquivo:
    arquivo.write(conteudo)