import os
import zipfile

diretorio_raiz = r'W:\ARQUIVOS-GNA\PUBLICA\Pub. Coordenação SALA\CONTRAKTOR\Vigente_\arquivozip\0023'

# Itera sobre todos os arquivos no diretório raiz
for arquivo in os.listdir(diretorio_raiz):
    caminho_arquivo = os.path.join(diretorio_raiz, arquivo)
    
    # Verifica se o arquivo é um arquivo ZIP
    if arquivo.lower().endswith('.zip'):
        # Cria o caminho para a pasta de destino usando o nome do arquivo ZIP
        pasta_destino = os.path.splitext(arquivo)[0]
        caminho_destino = os.path.join(diretorio_raiz, pasta_destino)
        
        # Extrai o conteúdo do arquivo ZIP para a pasta de destino
        with zipfile.ZipFile(caminho_arquivo, 'r') as zip_ref:
            zip_ref.extractall(caminho_destino)