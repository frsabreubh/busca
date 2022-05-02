import os.path        
import sys            
import csv

def valida_matriz(lista):

    if isinstance(lista, list):         
        for i in range(len(lista)):
            if isinstance(lista[i],list):
                if i == 0:
                    tam_item_zero = len(lista[i])
                else:
                    tam_lista_individual  = len(lista[i])
                    if tam_item_zero != tam_lista_individual:
                        raise Exception(f'Matriz com tamanho diferente. Ver item {i}')
    else:
        raise Exception(f'Deve-se informar uma matriz. Arquivo informado do tipo {type(lista)}')

def valida_conteudo(lista):
    for linha in range(len(lista)):
        for coluna in range(len(lista[linha])):             
            try:
                novo_num = int((lista[linha][coluna]))
                lista[linha][coluna] = novo_num
            except:
                print (f'Há elemento diferente de 0 e 1: {lista[linha][coluna]}')
            if lista[linha][coluna] != 0 and lista[linha][coluna] != 1:
                raise Exception(f'Há elementos diferente de 0 e 1: {lista[linha][coluna]}') 
        

with open(os.path.join(sys.path[0], 'matrix_dados.csv'), 'r') as arq:
    reader = csv.reader(arq)
    Matrix = list(reader)
    valida_matriz(Matrix)
    valida_conteudo(Matrix)
