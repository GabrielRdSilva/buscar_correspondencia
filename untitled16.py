# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 12:19:16 2023

@author: gabriel.rodrigues
"""
import PyPDF2
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import re

pytesseract.pytesseract.tesseract_cmd = R'C:\Users\gabriel.rodrigues\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def convert_page_to_jpg(pdf_path, page_number, page_last_number, output_path):
    
    
    def buscar_padrao10(nome_cliente10, texto_extraido):
        match = re.search(texto_extraido, nome_cliente10)
        if match:
            return 5
        else:
            return 0
    def buscar_padrao1(texto_padrao1, texto_extraido):
        match = re.search(texto_extraido, texto_padrao1)
        if match:
            return 5
        else:
            return 0
    def buscar_padrao2(texto_padrao2, texto_extraido):
        match = re.search(texto_extraido, texto_padrao2)
        if match:
            return 5
        else:
            return 0
    def buscar_padrao3(texto_padrao3, texto_extraido):
        match = re.search(texto_extraido, texto_padrao3)
        if match:
            return 5
        else:
            return 0
    def buscar_padrao4(texto_padrao4, texto_extraido):
        match = re.search(texto_extraido, texto_padrao4)
        if match:
            return 5
        else:
            return 0
    
    texto_padrao1= 'TERCEIRA'
    texto_padrao2= 'QUARTA'
    texto_padrao3= 'QUINTA'
    texto_padrao4= 'SEXTA'
    nome_cliente10 = 'JOAO PAULO BORGES MOITA'
      
    
    
    
    
    
    while page_number <= page_last_number:
            i=0
            images = convert_from_path(pdf_path, first_page=page_number, last_page=page_number)
            if images:
                nome_ok0 = 0
                nome_ok1 = 0
                nome_ok2 = 0
                nome_ok3 = 0
                nome_ok4 = 0
                while (i < page_last_number) and (nome_ok0 == 0 or nome_ok1 == 0 or nome_ok2 == 0 or nome_ok3 == 0 or nome_ok4 == 0):
                    image = images[i]
                    image.save(output_path, "JPEG")
                    imagem = Image.open(output_path)
                    texto_extraido = pytesseract.image_to_string(imagem)
                    variavel_verifi0 = buscar_padrao10(nome_cliente10, texto_extraido)
                    if variavel_verifi0 == 5:
                        nome_ok0 = 2 
                    variavel_verifi1 = buscar_padrao1(texto_padrao1, texto_extraido)
                    if variavel_verifi1 == 5:
                        nome_ok1 = 2
                    variavel_verifi2 = buscar_padrao2(texto_padrao2, texto_extraido)
                    if variavel_verifi2 == 5:
                        nome_ok2 = 2
                    variavel_verifi3 = buscar_padrao3(texto_padrao3, texto_extraido)
                    if variavel_verifi3 == 5:
                        nome_ok3 = 2
                    variavel_verifi4 = buscar_padrao4(texto_padrao4, texto_extraido)
                    if variavel_verifi4 == 5:
                        nome_ok4 = 2
                    i=i+1
                if nome_ok0 == 2 and nome_ok1 == 2 and nome_ok2 == 2 and nome_ok3 == 2 and nome_ok4 == 2:
                    return 1
                else:
                    return 0
         


pdf_file = r'C:\Users\gabriel.rodrigues\Desktop\teste 2\exclsuive\bloco 1\apartamento 1\cota 1\ok2.pdf'  # Substitua pelo caminho do seu arquivo PDF
page_number = 1  # Substitua pelo número da página que você deseja converter
termo = '.pdf'
termo2 = 'image'
output_file = pdf_file.replace(termo, termo2)
pdfFileObj = open(pdf_file, 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)

page_last_number = int(len(pdfReader.pages))
success = convert_page_to_jpg(pdf_file, page_number, page_last_number, output_file)

if success == 1:
    print('encontrado')
    print('quantidade de paginas' + str(page_last_number))
else:
    print('não compativel')
    
    
    
    