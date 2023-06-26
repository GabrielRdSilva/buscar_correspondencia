# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 16:15:24 2023

@author: gabriel.rodrigues
"""

import pandas as pd
lista_dados = []
elemento = 'ghjklljgdkkdkkdkdk ghjkl ghjkl - 5 '
lista1 =  elemento.split('-')
# Exemplo de lista com duas colunas
print(lista1)
lista_dados = lista_dados.append(lista1())

print(lista_dados)
# Criar um DataFrame a partir da lista
dataframe = pd.DataFrame(lista_dados, columns=['Nome', 'Idade'])

# Salvar o DataFrame em um arquivo Excel
dataframe.to_excel('caminho/do/arquivo.xlsx', index=False)