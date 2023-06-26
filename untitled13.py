# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 10:40:55 2023

@author: gabriel.rodrigues
"""
import re
import os
import pandas as pd

diretorio = R'W:\ARQUIVOS-GNA\PUBLICA\Pub. Coordenação SALA\GAV Resorts Dropbox\Servidor GAV Resorts\SERVIDOR'
empreendimentos = set(os.listdir(diretorio))
conjunto_arquivos = set()
# Lê o arquivo Excel com as

for bloco in empreendimentos:
    
    if bloco == 'desktop.ini' or bloco == 'DISTRATO CANCELADO PARA JURIDICO - EXCLUIR DEPOIS' or bloco == 'EMPREENDIMENTOS':
        continue
    if bloco == 'PORTO ALTO RESORTS' or bloco == 'RASCUNHOS - CONTRATOS PREMIUM' or bloco == 'TIME SHARE':
        continue
    diretorio1 = os.path.join(diretorio, bloco)
    blocos = set(os.listdir(diretorio1))
    
    for apartamento in blocos:
        diretorio2 = os.path.join(diretorio1, apartamento)
        apartamentos = set(os.listdir(diretorio2)) 
        for cota in apartamentos:
            diretorio3 = os.path.join(diretorio2, cota)
            cotas = set(os.listdir(diretorio3)) 
            for arquivo in cotas:
                buscar_erro = str(arquivo.lower())
                padrao_erro = '..pdf'
                match5 = re.search(padrao_erro, buscar_erro)
                if match5:
                    encontrado = match5.group(0)
                    lista_controle = list(encontrado)
                    if lista_controle[0] == '.':
                        continue
                if arquivo == 'Documentos - Atalho.lnk':
                    continue
                    
                diretorio5 = os.path.join(diretorio3, arquivo)
                teste2 = arquivo.split('.')
                teste3 = teste2[-1]
                
                if teste3.lower() == 'pdf':
                    conjunto_arquivos.add(diretorio5)
                    
                    continue
                    
                else:
                    
                    arquivos = os.listdir(diretorio5)
                    
                    for documento in arquivos:
                        buscar_erro = str(documento.lower())
                        padrao_erro = '..pdf'
                        match5 = re.search(padrao_erro, buscar_erro)
                        if match5:
                            encontrado = match5.group(0)
                            lista_controle = list(encontrado)
                            if lista_controle[0] == '.':
                                continue
                            
                        diretorio6 = os.path.join(diretorio5, documento)    
                        teste20 = documento.split('.')
                        teste30 = teste20[-1]
                        
                        if teste30.lower() == 'pdf':
                            conjunto_arquivos.add(diretorio6) 
                        
dataframe = pd.DataFrame(conjunto_arquivos, columns=['caminho_arquivo']) 
dataframe.to_excel(R'C:\Users\gabriel.rodrigues\Desktop\lista_caminhos.xlsx', index=False)                          
                        
                        
                        
                        
                        
                        
                        
                        