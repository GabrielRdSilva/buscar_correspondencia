# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 13:43:09 2023

@author: gabriel.rodrigues
"""
import os
import pandas as pd






diretorio = R'C:\Users\gabriel.rodrigues\Desktop\teste 2'
empreendimentos = set(os.listdir(diretorio))
conjunto_arquivos = set()

for bloco in empreendimentos:
    diretorio1 = os.path.join(diretorio, bloco)
    blocos = set(os.listdir(diretorio1))
    
    for apartamento in blocos:
        diretorio2 = os.path.join(diretorio1, apartamento)
        apartamentos = set(os.listdir(diretorio2)) 
        for cota in apartamentos:
            diretorio3 = os.path.join(diretorio2, cota)
            cotas = set(os.listdir(diretorio3)) 
            
            for contrato in cotas:
            
                diretorio4 = os.path.join(diretorio3, contrato)
                contratos = os.listdir(diretorio4)
                for arquivo in contratos:
                    
                    diretorio5 = os.path.join(diretorio4, arquivo)
                    teste2 = arquivo.split('.')
                    teste3 = teste2[-1]
                    
                    if teste3 == 'pdf':
                        conjunto_arquivos.add(diretorio5)
                        continue
                        
                    else:
                        arquivos = os.listdir(diretorio5)
                        
                        for documento in arquivos:
                            diretorio6 = os.path.join(diretorio5, documento)
                            teste20 = documento.split('.')
                            teste30 = teste20[-1]
                            
                            if teste30 == 'pdf':
                                conjunto_arquivos.add(diretorio6)
print(conjunto_arquivos)  
with open('arquivo.in', 'w') as arquivo:
    for elemento in conjunto_arquivos:
        arquivo.write(elemento + '\n')
    


                              
# lista = list(conjunto_arquivos)
# df = pd.DataFrame({'local do arquivo': lista})
# df.to_excel('local_arquivo_teste.xlsx', index=False)                            
                    
                            
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    

