from time import sleep

def linhas(tam=50):
    print('-' * tam)


def titulos(txt):
    linhas()
    print(txt.center(50))
    linhas()


def menu(lista):
    titulos('MENU PRINCIPAL')
    for v in lista:
        print(v)
    linhas()


def leiaInt(txt):
    while True:
        try:
            n = input(txt)
            if n.isnumeric():
                num = int(n)
                return num
        except KeyboardInterrupt:
            print('O usuario preferiu forçar uma parada!')
            raise KeyboardInterrupt
        else:
            titulos('Por favor digite um numero inteiro valido.')


def verifica(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        print('Arquivo nao encontrado.')
        return False
    else:
        print(f'Arquivo {arq} encontrado')
        return True


def criararq(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print(f'Houve um problema ao criar o arquivo {arq}')
    else:
        print(f'Arquivo {arq} criado com sucesso!')


def lerarq(lista):
    try:
        a = open(lista, 'rt')
    except:
        print('Houve um problema...')
    else:
        for linha in a:
            nome, idade = linha.strip().split(',')
            print(f'{nome.ljust(40)}{idade} anos')
     

def adicionar(arq, n, id):
    try:
        a = open(arq, 'at')
    except:
        print('House um problema...')
    else:
        try:
            a.write(f'{n},{id}\n')
        except:
            print('Tivemos um problema.')
        finally:
            print(f'{n.capitalize()} cadastrado com sucesso')
            a.close()


# MAIN
arq = 'curso.txt'
if not verifica(arq):
    criararq(arq)
sistema_on = True
while sistema_on:
    try:
        menu(['1 - Ver cadastros', '2 - Novos cadastros', '3 - Finalizar o programa'])
        opc = leiaInt('Opçao >> ')
        if opc == 1:
            titulos('LISTA DE CADASTROS')
            lerarq(arq)
        elif opc == 2:
            titulos('NOVOS CADASTROS')
            n = input('Nome: ')
            id = leiaInt('Idade: ')
            adicionar(arq, n, id)
        elif opc == 3:
            titulos('FINALIZANDO, VOLTE SEMPRE')
            sistema_on = False
        elif opc not in range(0, 3):
            titulos('ERRO!!! OPÇAO INEXISTENTE')
            sleep(1)
    except KeyboardInterrupt:
        titulos('O USUARIO FORÇOU A PARADA')
        sleep(1)
        titulos('FINALIZANDO...')
        sleep(1)
        sistema_on = False