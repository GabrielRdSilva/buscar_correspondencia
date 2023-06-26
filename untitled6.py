# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 11:22:00 2023

@author: gabriel.rodrigues
"""
from tika import parser
import PyPDF2
import re
import os 

def extrair_nome_cliente(caminho_pdf):
    raw = parser.from_file(caminho_pdf)
    texto = raw['content']

        # Expressão regular para encontrar padrões de nome do cliente
    padrao_nome_cliente = r"Nome:(.*?)\n"

        # Procurar o padrão no texto
    match = re.search(padrao_nome_cliente, texto)

    if match:
        nome_cliente = match.group(1)
        return nome_cliente
    else:
        return None
diretorio = R'C:\Users\gabriel.rodrigues\Desktop\teste 2'
pastas = os.listdir(diretorio) 

      
for pasta in pastas:
    
    
    nome_arq =  pasta + '\Documento Assinado.pdf'
    caminho_arquivo_pdf = os.path.join(diretorio, nome_arq)
    nome_cliente = extrair_nome_cliente(caminho_arquivo_pdf)
    
    
    
print(nome_cliente)    
 