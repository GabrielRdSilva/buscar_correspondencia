import os

# Diretório onde as pastas estão localizadas
diretorio = R'C:\Users\gabriel.rodrigues\Desktop\teste'

# Lista todas as pastas no diretório
pastas = [nome for nome in os.listdir(diretorio) if os.path.isdir(os.path.join(diretorio, nome))]

# Função de classificação personalizada
def elemento_no_meio(pasta):
    # Extrai o elemento desejado do nome da pasta
    partes = pasta.split('-')  # Supondo que o elemento está separado por '_'
    parte1 = partes[-2]
    parte21 = parte1.split(' ')
    i = str(parte21)
    return i  # Retorna o elemento no meio

# Ordena a lista de pastas usando a função de classificação personalizada
pastas_ordenadas = sorted(pastas, key=elemento_no_meio)

# Realize as operações necessárias para reorganizar as pastas de acordo com a ordem determinada
for pasta in enumerate(pastas_ordenadas):
    caminho_antigo = os.path.join(diretorio, pasta)
    i2 = str(pasta)
    pasta1 = i + i2
    caminho_novo = os.path.join(diretorio, pasta1)  # Adiciona um número de ordem no início do nome
    os.rename(caminho_antigo, caminho_novo)