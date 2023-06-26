
import PyPDF2


def extrair_texto_primeira_pagina(caminho_pdf):
    with open(caminho_pdf, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        primeira_pagina = pdf_reader.pages[0]
        texto = primeira_pagina.extract_text()
        return texto



caminho_arquivo_pdf = R'W:\ARQUIVOS-GNA\PUBLICA\Pub. Coordenação SALA\CONTRAKTOR\Vigente_\arquivozip\0005\2021_827 - contrato_Assinado\Documento Assinado.pdf'
texto_extraido = extrair_texto_primeira_pagina(caminho_arquivo_pdf)


print(texto_extraido)



   if nome_cliente:
       print("Nome do cliente encontrado:", nome_cliente)
   else:
       print("Nome do cliente não encontrado.")
   if nome_empre:
       print("Nome do cliente encontrado:", nome_empre)
   else:
       print("Nome do cliente não encontrado.")   
   if nome_cota:
       print("Nome do cliente encontrado:", nome_cota)
   else:
       print("Nome do cliente não encontrado.")  
   if nome_bloco:
       print("Nome do cliente encontrado:", nome_bloco)
   else:
       print("Nome do cliente não encontrado.")  