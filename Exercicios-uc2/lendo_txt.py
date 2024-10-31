# Lendo arquivo texto

mensagem = """
      Olá, mundo!
    Eu sou o Python!
Eu estou na aula de Python!
"""

'''# Escrevendo arquivo texto
arquivo = open("Exercicios-uc2/arquivo.txt", "w", encoding="utf-8")
arquivo.write(mensagem)
arquivo.close()

# Lendo arquivo texto
arquivo = open("Exercicios-uc2/arquivo.txt", "r", encoding="utf-8")
print(arquivo.read())
arquivo.close()
'''
# Tratando exceções (erros na leitura)
try:
    with open("Exercicios-uc2/arquivo.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print("Arquivo não encontrado")
except IOError:
    print("Erro ao ler o arquivo")
