
#Lendo arquivo
# path = "C:/Users/davix/Desktop/Arquivos/Profissional/Estudos/Análise de dados/Base de dados/excert..txt"
# with open(path, "r") as f:
#     content = f.read()
#     print(content)

#Lendo apenas linhas não vazias:
path = "C:/Users/davix/Desktop/Arquivos/Profissional/Estudos/Análise de dados/Base de dados/excert..txt"
with open(path, "r") as f:
    for i, line in enumerate(f):            #Adicionando número de linha a linha
        if line.strip():                    #filtrando as linhas vazias
            print(f"Line {i}: ", line.strip())
