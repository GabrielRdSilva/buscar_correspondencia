# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 11:57:44 2023

@author: gabriel.rodrigues
"""
import os
from tika import parser
diretorio = R'C:\Users\gabriel.rodrigues\Desktop\teste 2'
pastas = set(os.listdir(diretorio))
print(pastas)  
for pasta in pastas:
    nome_arq =  pasta + '\Documento Assinado.pdf'
    caminho_pdf = os.path.join(diretorio, nome_arq)
    
    parsed_pdf = parser.from_file(caminho_pdf)
    texto = parsed_pdf['content']
    print(texto)
    print(type(texto))
    break
 