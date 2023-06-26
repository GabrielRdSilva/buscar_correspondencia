# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 12:59:49 2023

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
    nova_lista.append(valor1)
    valor3 = str(valor2)
    nova_lista.append(str(valor3.replace('.0','')))

print(nova_lista.sort())
print(len(nova_lista))

conjunto = set(nova_lista)
if 'nan' in conjunto:
    print('------------------------------------------------------')
    print('tem')

# Gera o conteúdo do arquivo IN
conteudo = '\n'.join(nova_lista)

# Salva o conteúdo no arquivo IN
with open('dados.in', 'w') as arquivo:
    arquivo.write(conteudo)