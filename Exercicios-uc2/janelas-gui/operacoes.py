# coding: utf-8

import csv


def cadastrar(isbn, autor, titulo, ano):
    with open('db.txt', 'a') as arquivo:
        arquivo.write('%s,%s,%s,%s\n' % (isbn, autor, titulo, ano))


def ler():
    with open('db.txt', 'r') as arquivo:
         return arquivo.readlines()


def alterar(titulo_antigo, isbn, autor, titulo, ano):
    linhas = ler()
    with open('db.txt', 'w') as arquivo:
        for linha in linhas:
            if linha.split(',')[2] == titulo_antigo:
                arquivo.write('%s,%s,%s,%s\n' % (isbn, autor, titulo, ano))
                continue
            arquivo.write('%s' % linha)


def buscar_livro_por_titulo(titulo):
    for linha in ler():
        if linha.split(',')[2] == titulo:
            return linha.split(',')


def excluir(titulo):
    linhas = ler()
    with open('db.txt', 'w') as arquivo:
        for linha in linhas:
            if linha.split(',')[2] == titulo:
                continue
            arquivo.write('%s' % linha)


def exportar_para_csv(nome_arquivo_saida):
    linhas = ler()

    with open('%s.csv' % (nome_arquivo_saida), 'w') as arquivo:
        writer = csv.writer(arquivo)

        for linha in linhas:
            writer.writerow(linha.strip().split(','))