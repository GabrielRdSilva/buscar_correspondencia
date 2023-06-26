import PyPDF2
import re
import os
from tika import parser

def extrair_nome_cliente(caminho_pdf): 
    raw = parser.from_file(caminho_pdf)
    texto = raw['content']

    # Expressão regular para encontrar padrões de nome do cliente
    padrao_nome_cliente = r"Nome:(.*?)\n"

    # Procurar o padrão no texto
    match = re.search(padrao_nome_cliente, texto)

    if match:
        nome_cliente = match.group(1)
        return nome_cliente
    else:
        return None
    
def extrair_nome_empre(caminho_pdf):
    raw = parser.from_file(caminho_pdf)
    texto = raw['content']

    # Expressão regular para encontrar padrões de nome do cliente
    padrao_nome_empre = r"EMPREENDIMENTO:(.*?)\n"

    # Procurar o padrão no texto
    match = re.search(padrao_nome_empre, texto)

    if match:
        nome_empre = match.group(1)
        return nome_empre
    else:
        return None
def extrair_nome_cota(caminho_pdf):
    raw = parser.from_file(caminho_pdf)
    texto = raw['content']

    # Expressão regular para encontrar padrões de nome do cliente
    padrao_nome_cota = r"TERMO DE VERIFICAÇÃO DE(.*?)\n"

    # Procurar o padrão no texto
    match = re.search(padrao_nome_cota, texto)

    if match:
        nome_cota = match.group(1)
        return nome_cota
    else:
        return None
        

diretorio = R'C:\Users\gabriel.rodrigues\Desktop\teste 2'
pastas = set(os.listdir(diretorio))
#i=1


for pasta in pastas:
    
    nome_arq =  pasta + '\Documento Assinado.pdf'
    caminho_arquivo_pdf = os.path.join(diretorio, nome_arq)
    nome_cliente = extrair_nome_cliente(caminho_arquivo_pdf)
    nome_empre = extrair_nome_empre(caminho_arquivo_pdf)
    nome_cota = extrair_nome_cota(caminho_arquivo_pdf)
    
    caminho_antigo = os.path.join(diretorio, pasta)
    
    if nome_cliente and nome_empre and nome_cota:
        #i2=str(i)
        novo_nome_pasta = nome_cliente +'-'+  nome_empre +'-'+ nome_cota
        caminho_novo = os.path.join(diretorio, novo_nome_pasta)
        os.rename(caminho_antigo, caminho_novo)
        #i=i+1
   
