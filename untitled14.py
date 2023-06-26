# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 10:55:48 2023

@author: gabriel.rodrigues
"""
import PyPDF3

# with open(R'C:\Users\gabriel.rodrigues\Desktop\teste 2\exclsuive\bloco 1\apartamento 1\cota 1\ok.pdf', 'rb') as arquivo_pdf:
#     leitor_pdf = PyPDF3.PdfFileReader(arquivo_pdf)
#     num_paginas = leitor_pdf.numPages

# for num_pagina in range(num_paginas):
#     pagina = leitor_pdf.getPage(num_pagina)
#     texto = pagina.extract_text()
#     print(f'Texto da página {num_pagina + 1}:')
#     print(texto)
#     print()
    
    
def extrair_texto_primeira_pagina(caminho_pdf):
    pdfFileObj = open(caminho_pdf, 'rb')
    pdfReader = PyPDF3.PdfFileReader(pdfFileObj)
    pagina = pdfReader.getPage(1)
    texto = pagina.extractText()
    return texto
        # pdf_reader = PyPDF3.PdfFileReader(pdf_file)
        # pagina = pdf_reader.getPage(1)
        # texto = pagina.extractText()
        # return texto
       # pagina = pdf_reader.getPage(1)
        # texto = pdf_reader.extractText()
        # if texto:
        #     return texto
        # else:
        #     return 1



caminho_arquivo_pdf = R'C:\Users\gabriel.rodrigues\Desktop\teste 2\exclsuive\bloco 1\apartamento 1\cota 1\ok.pdf'
texto_extraido = extrair_texto_primeira_pagina(caminho_arquivo_pdf)


print(texto_extraido)
    