
lista = [1, 10]
arquivo = open('teste.txt', 'r')

try:
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    x = a
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por zero')
except IndexError:
    print('Erro ao acessar um índice inválido da lista')
#
# BaseException ou Exception devem vir por último!!! É uma árvore!
#
except BaseException as ax:
    print('Erro desconhecido. Erro: {}'.format(ax))
else:
    print('Executa quando não há exceção.')
finally:
    print('Sempre executa.')
    arquivo.close()


