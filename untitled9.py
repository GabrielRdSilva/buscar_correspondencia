# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 17:24:52 2023

@author: gabriel.rodrigues
"""

from tika import parser
import re
import PyPDF2

def buscar_nome(caminho_pdf,nome_cliente):
    raw = parser.from_file(caminho_pdf)
    texto = raw['content']
    match = re.search(nome_cliente, texto)
    if match:
        return nome_cliente
    else:
        return None
    
def buscar_padrao1(texto1, i):
    i2 = 0
    
    
    with open(caminho_pdf, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        while i2 < i:
            pagina = pdf_reader.pages[i2]
            texto = pagina.extract_text()
            match = re.search(texto1, texto)
            i2 = i2 + 1
    
            if match:
                i2 = i
                return 1
             
       
def buscar_padrao2(texto2, i):
    i2 = 0
    
    
    with open(caminho_pdf, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        while i2 < i:
            pagina = pdf_reader.pages[i2]
            texto = pagina.extract_text()
            match = re.search(texto2, texto)
            i2 = i2 + 1
    
            if match:
                i2 = i
                return 2  
def buscar_padrao3(texto3, i):
    i2 = 0
    
    
    with open(caminho_pdf, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        while i2 < i:
            pagina = pdf_reader.pages[i2]
            texto = pagina.extract_text()
            match = re.search(texto3, texto)
            i2 = i2 + 1
    
            if match:
                i2 = i
                return 3
def buscar_padrao4(texto4, i):
    i2 = 0
    
    
    with open(caminho_pdf, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        while i2 < i:
            pagina = pdf_reader.pages[i2]
            texto = pagina.extract_text()
            match = re.search(texto4, texto)
            i2 = i2 + 1
    
            if match:
                i2 = i
                return 4              
    #FRANCISCO DE LIMA FILHO
    
    
texto_padrao1= 'QUARTA'
texto_padrao2= 'TERCEIRA'
texto_padrao3= 'QUINTA'
texto_padrao4= 'SEXTA'

caminho_pdf = R'C:\Users\gabriel.rodrigues\Desktop\teste 2\exclsuive\bloco 1\apartamento 1\cota 1\ok.pdf'
texto_extraido = buscar_nome(caminho_pdf, str(input()))
pdfFileObj = open(caminho_pdf, 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
paginas = len(pdfReader.pages)
if texto_extraido: 
    print(texto_extraido + 'chegou aqui')
    variavel_verifi1 = buscar_padrao1(texto_padrao1, paginas)
    print(variavel_verifi1)
    variavel_verifi2 = buscar_padrao2(texto_padrao2, paginas)
    print(variavel_verifi2)
    variavel_verifi3 = buscar_padrao3(texto_padrao3, paginas)
    variavel_verifi4 = buscar_padrao4(texto_padrao4, paginas)
    if variavel_verifi1 == 1:
        if variavel_verifi2 == 2: 
            if variavel_verifi3 == 3: 
                if variavel_verifi4 == 4: 
                    print('provavelmente esta completo')
                else:
                    print('incompleto verificar')
            else:
                print('incompleto verificar')   
        else:
            print('incompleto verificar')   
    else:
        print('incompleto verificar')            

        
        
        
        
        
        
        
        
        
        
        
        