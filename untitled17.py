# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 14:02:49 2023

@author: gabriel.rodrigues
"""
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import re

pytesseract.pytesseract.tesseract_cmd = R'C:\Users\gabriel.rodrigues\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def convert_page_to_jpg(pdf_path, page_number, output_path):
    images = convert_from_path(pdf_path, first_page=page_number, last_page=30)
    if images:
        image = images[20]
        image.save(output_path, "JPEG")
        return True
    return False
pdf_file = R"C:\Users\gabriel.rodrigues\Desktop\teste 2\exclsuive\bloco 1\apartamento 1\cota 1\ok.Pdf"  # Substitua pelo caminho do seu arquivo PDF
page_number = 1  # Substitua pelo número da página que você deseja converter
output_file = R"C:\Users\gabriel.rodrigues\Desktop\teste 2\exclsuive\bloco 1\apartamento 1\cota 1\ok.jpg"  # Substitua pelo caminho de saída para a imagem JPG

success = convert_page_to_jpg(pdf_file, page_number, output_file)

imagem_jpg = R"C:\Users\gabriel.rodrigues\Desktop\teste 2\exclsuive\bloco 1\apartamento 1\cota 1\ok.jpg"  # Substitua pelo caminho da sua imagem JPG
imagem = Image.open(imagem_jpg)

texto_extraido = pytesseract.image_to_string(imagem)

conjunto = set(texto_extraido.split(' '))


termo = 'SEXTA'
for frase in conjunto:
    match = re.search(termo, frase)
    if match:
        print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;; encontrado ;;;;;;;;;;;;;;;;;;;;;;;')
        break
    