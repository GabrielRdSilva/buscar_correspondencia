
import PyPDF2


def extrair_texto_primeira_pagina(caminho_pdf):
    with open(caminho_pdf, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        primeira_pagina = pdf_reader.pages[3]
        texto = primeira_pagina.extract_text()
        return texto



caminho_arquivo_pdf = R'C:\Users\gabriel.rodrigues\Desktop\teste 2\park\bloco 1 - Copia\apartamento 1 - Copia - Copia\cota 1 - Copia - Copia - Copia\okok\ok.pdf'
texto_extraido = extrair_texto_primeira_pagina(caminho_arquivo_pdf)


print(texto_extraido)


