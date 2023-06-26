# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 15:55:46 2023

@author: gabriel.rodrigues
"""

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
import pandas as pd
pytesseract.pytesseract.tesseract_cmd = R'C:\Users\gabriel.rodrigues\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def verificar_correspondencia(elemento):
    def buscar_texto(texto_extraido):
        termo = 'PROPOSTA DE COMPRA E VENDA'
        match = re.search(termo, texto_extraido)
        
        if match:
            return 1
        else:
            return 0
    
    def buscar_nome(nome_cliente, texto_extraido):
        
        match = re.search(nome_cliente, texto_extraido)
        
        if match:
            return 1
        else:
            return 0
    def buscar_cota(numero_cota, texto_extraido):
        padrao = r"UNIDADE AUTONOMA n?(.*?)\n"
        padrao2 = r"Cota n(.*?)\n"
        
        match = re.search(padrao, texto_extraido)
        match2 = re.search(padrao2, texto_extraido)
        cota_teste = str('0{}'.format(numero_cota))
       
        
        if match:
            nome_empre = match.group(1)
            lista = re.split(r',| ', nome_empre)
                      
            for trecho in lista:
                       
                if trecho == numero_cota:
                    return 1
                elif trecho == cota_teste:
                    return 1
                else:
                    continue
        elif match2:
            nome_empre = match2.group(1)
            lista = re.split(r',| ', nome_empre)
            for trecho in lista:
                               
                if trecho == numero_cota:
                    return 1
                elif trecho == cota_teste:
                    return 1
                else:
                    continue
        else:
           return 0  
   
        
    def buscar_caracter1(conjunto_palavras):
        termo = 'QUINTA'
        termo2 = 'extrajudicial'
        termo3 = 'honorarios'
        termo4 = 'advocaticios'
        
        for frase in conjunto_palavras:
            match = re.search(termo, frase)
            match2 = re.search(termo2, frase)
            match3 = re.search(termo3, frase)
            match4 = re.search(termo4, frase)
            if match:
                return 1
            elif match2:
                return 1
            elif match3:
                return 1
            elif match4:
                return 1
        return 0
        
    def buscar_caracter2(conjunto_palavras):
        termo = 'incorridos'
        termo2 = 'EXCLUSIVO'
        termo3 = '(cinco)'
        termo4 = 'Indivisibilidade'
        
        for frase in conjunto_palavras:
            match = re.search(termo, frase)
            match2 = re.search(termo2, frase)
            match3 = re.search(termo3, frase)
            match4 = re.search(termo4, frase)
            if match:
                return 1
            elif match2:
                return 1
            elif match3:
                return 1
            elif match4:
                return 1
        return 0
        
    
    i=0
    j=0
    i3=0
    caminho_3 = R'{}'.format(elemento)
    try:
        with open(caminho_3, "rb") as arquivo_pdf:
            # Faça algo com o arquivo
            pdfReader = PyPDF2.PdfReader(arquivo_pdf)
            quantidade_paginas = int(len(pdfReader.pages))
    except FileNotFoundError:
        # Lida com o erro de arquivo não encontrado
        return None
    termo = '.pdf'
    termo2 = 'image'
    indicador1 = 0
    indicador2 = 0
    indicador3 = 0
    indicador4 = 0
    indicador5 = 0
    verificar_texto = 0
    images = convert_from_path(caminho_3, first_page=0, last_page=quantidade_paginas)
    caminho_imagem = elemento.replace(termo, termo2)
    if quantidade_paginas < 10:
        return None
    while i < quantidade_paginas:
        if images:
            image = images[i]
            image.save(caminho_imagem, "JPEG")
            imagem = Image.open(caminho_imagem)
            texto_extraido = pytesseract.image_to_string(imagem)
            i = i + 1
            if indicador1 == 0:
                verificar_texto = buscar_texto(texto_extraido)
                if verificar_texto == 1:
                    indicador1 = indicador1 + 1
            if indicador2 == 0 and i <11:
                         
                for i2 in range(0, len(nova_lista), 2):
                       
                    nome_cliente = nova_lista[i2]
                    if nome_cliente != 'nan':
                        verificar_nome = buscar_nome(nome_cliente, texto_extraido)
                        
                        if verificar_nome == 1:
                            indicador2 = indicador2 + 1
                            i3 = i2 +1
            
                            numero_cota = nova_lista[i3]
                            verificar_cota = buscar_cota(numero_cota, texto_extraido)
                            if verificar_cota == 1:
                                indicador3 = indicador3 + 1
                                
                            break    
                    
            if indicador3 == 0 and indicador2 == 1:
                numero_cota = nova_lista[i3]
                verificar_cota = buscar_cota(numero_cota, texto_extraido)
                
                if verificar_cota == 1:
                    indicador3 = indicador3 + 1
                    
            
            if i > 5 and indicador2 == 0 and indicador3 == 0:
                os.remove(caminho_imagem) 
                return None
            conjunto_palavras = set(texto_extraido.split(' '))
            if indicador4 == 0:
                
                verificar_caracter1 = buscar_caracter1(conjunto_palavras)
                
                if verificar_caracter1 == 1:
                    indicador4 = indicador4 + 1
                    
            if indicador5 == 0:
                
                verificar_caracter2 = buscar_caracter2(conjunto_palavras)
                
                if verificar_caracter2 == 1:
                    
                    indicador5 = indicador5 + 1
            #print(verificar_texto, indicador1, indicador2, indicador3, indicador4, indicador5)        
            if indicador3 == 1 and indicador4 == 1 and indicador5 == 1 and indicador2 == 1:
                os.remove(caminho_imagem)                                      
                return nome_cliente +' - '+ numero_cota + ' - ' + str(quantidade_paginas)
                        
            else:
                
                continue
            
        else:
            i = i + 1
        if i > 10 and indicador2 == 1 and indicador3 == 0:
            if j < 5:
                i = 0
                i3 = i3 + 2
                j = j + 1
            else:
                if indicador3 == 0 and (indicador4 == 1 or indicador5 == 1) and indicador2 == 1:
                    os.remove(caminho_imagem)                                      
                    return nome_cliente +' - '+ 'verificar' + ' - ' + str(quantidade_paginas)
                else:
                    return None    
    os.remove(caminho_imagem)       
    return None
    
                    
diretorio = R'W:\ARQUIVOS-GNA\PUBLICA\Pub. Coordenação SALA\GAV Resorts Dropbox\Servidor GAV Resorts\SERVIDOR\CONTRATOS - SALINAS PARK RESORT\ATALAIA'
empreendimentos = set(os.listdir(diretorio))
conjunto_arquivos = set()
# Lê o arquivo Excel com as duas colunas
df = pd.read_excel(R'C:\Users\gabriel.rodrigues\Desktop\teste_teste.xlsx')
# Obtém as duas colunas do DataFrame
coluna1 = df['nome_cliente']
coluna2 = df['COTA']
lista_vazia = []
# Cria uma nova lista intercalando as informações das colunas 1 e 2
nova_lista = []
for valor1, valor2 in zip(coluna1, coluna2):
    nova_lista.append(str(valor1))
    valor3 = str(valor2)
    nova_lista.append(str(valor3.replace('.0',''))) 
         
for bloco in empreendimentos:
    diretorio1 = os.path.join(diretorio, bloco)
    blocos = set(os.listdir(diretorio1))
    
    for apartamento in blocos:
        diretorio2 = os.path.join(diretorio1, apartamento)
        apartamentos = set(os.listdir(diretorio2)) 
        for arquivo in apartamentos:
            buscar_erro = str(arquivo.lower())
            padrao_erro = '..pdf'
            match5 = re.search(padrao_erro, buscar_erro)
            if match5:
                encontrado = match5.group(0)
                lista_controle = list(encontrado)
                if lista_controle[0] == '.':
                    continue
                
                
            diretorio5 = os.path.join(diretorio2, arquivo)
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
contador = 1                              
print('possui {} documentos pdf para analisar'.format(len(conjunto_arquivos)))
for elemento in conjunto_arquivos:
    print('verificando o {}º arquivo '.format(contador))
    elemento_buscado = verificar_correspondencia(elemento)
    contador = contador + 1
    if elemento_buscado:
        lista1 =  elemento_buscado.split('-')
        
        #print(elemento_buscado + '\n encontrado no banco de dados \n')
        lista1.append('ENCONTRADO')
        lista_vazia.append(lista1)
    else:
        
        
        print(elemento + '\n não faz parte da lista \n')
    

  
dataframe = pd.DataFrame(lista_vazia, columns=['Nome', 'cota','quantidade de paginas', 'situacao']) 
dataframe.to_excel(R'C:\Users\gabriel.rodrigues\Desktop\lista_apos_busca_park.xlsx', index=False)     
        
        
        
    
    