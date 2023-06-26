import PyPDF2
import re
import os

def extrair_nome_cliente(caminho_pdf):
    with open(caminho_pdf, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        primeira_pagina = pdf_reader.pages[0]
        texto = primeira_pagina.extract_text()

        # Expressão regular para encontrar padrões de nome do cliente
        padrao_nome_cliente = r"Cessionário:(.*?)\n"

        # Procurar o padrão no texto
        match = re.search(padrao_nome_cliente, texto)

        if match:
            nome_cliente = match.group(1)
            return nome_cliente
        else:
            return None
        
def extrair_nome_empre(caminho_pdf):
    with open(caminho_pdf, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        primeira_pagina = pdf_reader.pages[0]
        texto = primeira_pagina.extract_text()

        # Expressão regular para encontrar padrões de nome do cliente
        padrao_nome_empre = r"QuanƟdadedePontos:(.*?)PrazodoContrato:"

        # Procurar o padrão no texto
        match = re.search(padrao_nome_empre, texto)

        if match:
            nome_empre = match.group(1)
            return nome_empre
        else:
            return None

diretorio = R'W:\ARQUIVOS-GNA\PUBLICA\Pub. Coordenação SALA\CONTRAKTOR\Vigente_\arquivozip\0007'
pastas = os.listdir(diretorio)
i=1
for pasta in pastas:
    
    nome_arq =  pasta + '\Documento Assinado.pdf'
    caminho_arquivo_pdf = os.path.join(diretorio, nome_arq)
    nome_cliente = extrair_nome_cliente(caminho_arquivo_pdf)
    nome_empre = extrair_nome_empre(caminho_arquivo_pdf)
    
    caminho_antigo = os.path.join(diretorio, pasta)
    
    if nome_cliente and nome_empre:
        i2=str(i)
        novo_nome_pasta = i2 +'-'+ nome_cliente +'-'+  nome_empre
        caminho_novo = os.path.join(diretorio, novo_nome_pasta)
        os.rename(caminho_antigo, caminho_novo)
        i=i+1