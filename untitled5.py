from tika import parser



    raw = parser.from_file()
    texto = raw['content']
    
    padrao_nome_cliente = r"Nome:(.*?)\n" 
    match = re.search(padrao_nome_cliente, texto)
    
    if match:
         nome_cliente = match.group(1)
         return nome_cliente
    else:
         return None

nomear_arquivo()

diretorio = R'C:\Users\gabriel.rodrigues\Desktop\teste 2'
pastas = os.listdir(diretorio)
for pasta in pastas:
    nomear_arquivo(pastas)
    
    
    
print(nomear_arquivo)