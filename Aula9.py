import shutil

def escrever_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)
    arquivo.close()

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy2(nome_arquivo, 'Dados.txt')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'Data.txt')

if __name__ == '__main__':
    copia_arquivo('notas.txt')
    # escrever_arquivo('Primeira linha\n')
    # atualizar_arquivo('Segunda linha\n')
    # ler_arquivo('teste.txt')
    # aluno = 'Rafael,10,10,5,5\n'
    # atualizar_arquivo('notas.txt', aluno)
    # aluno = 'Felipe,7,8,5,6\n'
    # atualizar_arquivo('notas.txt', aluno)
    # aluno = 'Cesar,8,9,5,6\n'
    # atualizar_arquivo('notas.txt', aluno)
    # media_notas('notas.txt')
