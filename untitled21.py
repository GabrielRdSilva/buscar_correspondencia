# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 09:14:29 2023

@author: gabriel.rodrigues
"""

lista = []

# Abre o arquivo IN
with open(R'C:\Users\gabriel.rodrigues\Desktop\python\cliente_e_cota.in', 'r') as arquivo:
    # Lê cada linha do arquivo
    for linha in arquivo:
        # Remove quebras de linha e espaços em branco extras
        linha = linha.strip()
        # Verifica se a linha não está vazia
        if linha:
            # Adiciona a linha à lista
            lista.append(linha)

# Imprime a lista
print(lista)