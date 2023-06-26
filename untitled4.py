# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 08:53:10 2023

@author: gabriel.rodrigues
"""

import PyPDF2
from PIL import Image


def extrair_informacoes_imagem_pdf(caminho_pdf):
    # Abrir o arquivo PDF
    with open(caminho_pdf, 'rb') as arquivo_pdf:
        leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
        
        # Obter o número total de páginas do PDF
        num_paginas = len(leitor_pdf.pages)
        
        # Percorrer cada página do PDF
        for pagina_num in range(num_paginas):
            # Obter a página atual
            pagina = leitor_pdf.pages(pagina_num)
            
            # Obter a lista de objetos da página
            objetos_pagina = pagina['/Resources']['/XObject'].get_Object
            
            # Verificar se cada objeto é uma imagem
            for objeto_num, objeto in objetos_pagina.items():
                if objeto['/Subtype'] == '/Image':
                    # Extrair as informações da imagem
                    largura = objeto['/Width']
                    altura = objeto['/Height']
                    formato = objeto['/ColorSpace']
                    
                    # Exemplo de exibição das informações
                    print(f"Imagem {objeto_num}:")
                    print(f"Largura: {largura} pixels")
                    print(f"Altura: {altura} pixels")
                    print(f"Formato: {formato}")
                    print("---")
                    
                    # Para salvar a imagem em um arquivo, você pode usar o seguinte código:
                    # imagem = objeto._data
                    # with open(f"imagem{objeto_num}.png", 'wb') as arquivo_imagem:
                    #     arquivo_imagem.write(imagem)
                    
# Caminho para o arquivo PDF
caminho_pdf = 

# Chamar a função para extrair informações da imagem
extrair_informacoes_imagem_pdf(caminho_pdf)