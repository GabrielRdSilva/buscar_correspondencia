# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 08:23:08 2023

@author: gabriel.rodrigues
"""
import pytesseract
import PyPDF2
from PIL import Image
from pdf2image import convert_from_path
import re
import os
pytesseract.pytesseract.tesseract_cmd = R'C:\Users\gabriel.rodrigues\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def verificar_correspondencia(elemento):
    def buscar_texto(texto_extraido):
        termo = 'PROPOSTA DE COMPRA E VENDA'
        match = re.search(termo, texto_extraido)
        print('texto')
        if match:
            return 1
        else:
            return 0
    
    def buscar_nome(nome_cliente, texto_extraido):
        
        match = re.search(nome_cliente, texto_extraido)
        print('texto 2')
        if match:
            return 1
        else:
            return 0
    def buscar_cota(numero_cota, texto_extraido):
        padrao = r"Cota n(.*?)\n"
        match = re.search(padrao, texto_extraido)
        # padrao_buscado = 'Cota n2.: {}'.format(numero_cota)
        # match = re.search(padrao_buscado, texto_extraido)
        print(numero_cota)
        if match:
            nome_empre = match.group(1)
            lista = nome_empre.split(' ')
            print(lista)
            for trecho in lista:
                if trecho == numero_cota:
                    return 1
                else:
                    continue
        else:
           return 0  
   
        
    def buscar_caracter1(texto_extraido):
        termo = 'DE GARANTIA REAL'
        match = re.search(termo, texto_extraido)
        print('TERMO 4')
        if match:
            return 1
        else:
            return 0
        
    def buscar_caracter2(texto_extraido):
        termo = 'USULA QUINTA'
        match = re.search(termo, texto_extraido)
        print('TERMO 5')
        if match:
            return 1
        else:
            return 0
        
    
    i=0
    arquivo_pdf = open(elemento, 'rb')
    pdfReader = PyPDF2.PdfReader(arquivo_pdf)
    quantidade_paginas = int(len(pdfReader.pages))
    termo = '.pdf'
    termo2 = 'image'
    indicador1 = 0
    indicador2 = 0
    indicador3 = 0
    indicador4 = 0
    indicador5 = 0
    print(quantidade_paginas)
    while i < quantidade_paginas:
        print('pagina {}'.format(i+1))
        caminho_3 = R'{}'.format(elemento)
        images = convert_from_path(caminho_3, first_page=i, last_page=quantidade_paginas)
        
        caminho_imagem = elemento.replace(termo, termo2)
          
        if images:
            image = images[i]
            image.save(caminho_imagem, "JPEG")
            imagem = Image.open(caminho_imagem)
            texto_extraido = pytesseract.image_to_string(imagem)
            print(texto_extraido)
            i = i + 1
            if indicador1 == 0: 
                verificar_texto = buscar_texto(texto_extraido)
                if verificar_texto == 1:
                    indicador1 = indicador1 + 1
                    print('indicador 1 encontrada na pagina {}'.format(i))
                if indicador2 == 0:
                             
                    for i2 in range(0, len(lista), 2):
                           
                        nome_cliente = lista[i2]
                        
                        verificar_nome = buscar_nome(nome_cliente, texto_extraido)
                        
                        if verificar_nome == 1:
                            
                            indicador2 = indicador2 + 1
                            i3 = i2 +1
                            print('nome cliente encontrada na pagina {}'.format(i))
                            break
                    numero_cota = lista[i3]
                    if indicador3 == 0:
                        verificar_cota = buscar_cota(numero_cota, texto_extraido)
                        
                    if verificar_cota == 1:
                        indicador3 = indicador3 + 1
                        print('cota encontrada na pagina {}'.format(i))
                        continue
                        
                else:
                    numero_cota = lista[i3]
                    if indicador3 == 0:
                        
                        verificar_cota = buscar_cota(numero_cota, texto_extraido)
                        
                        if verificar_cota == 1:
                            indicador3 = indicador3 + 1
                            print('cota encontrada na pagina {}'.format(i))
                    if indicador4 == 0:
                       
                        verificar_caracter1 = buscar_caracter1(texto_extraido)
                        
                        if verificar_caracter1 == 1:
                            indicador4 = indicador4 + 1
                            print('indicador 4 encontrada na pagina {}'.format(i))
                    if indicador5 == 0:
                        verificar_caracter2 = buscar_caracter2(texto_extraido)
                        if verificar_caracter2 == 1:
                            print('indicador 5 encontrada na pagina {}'.format(i))
                            indicador5 = indicador5 + 1
                    if indicador3 > 0 and indicador4 > 0 and indicador5 > 0:
                                                              
                        return nome_cliente + numero_cota
                                
                    else:
                        continue
            else:
                continue
                    
        
        else:
            return None
    return None
    
                    
diretorio = R'C:\Users\gabriel.rodrigues\Desktop\teste 2'
empreendimentos = set(os.listdir(diretorio))
conjunto_arquivos = set()

lista = ['JOAO LUIZ DIAS ALBUQUERQUE','2','JOSE ILSON CAMARA BEZERRA','23','FRANCISCO DE LIMA FILHO','4']  
ok = len(lista) - 1  
         
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


for elemento in conjunto_arquivos:
    
    
    
    elemento_buscado = verificar_correspondencia(elemento)
    if elemento_buscado:
        print(elemento_buscado + 'encontrado no banco de dados')
    else:
        print(elemento + 'não faz parte da lista ')
    
    
    
    
    
    
    
    
    
    