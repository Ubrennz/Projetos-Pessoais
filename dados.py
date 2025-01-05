import csv
from time import sleep

def criar(nome):
    try:
        with open('dados_salvos.csv', 'r', encoding='utf-8', newline='') as arquivo_csv:
            ler_csv = csv.reader(arquivo_csv)
            leitor = list(ler_csv)
            user_id = len(leitor)

        lista_nome = [user_id, nome]
        with open('dados_salvos.csv', 'a', encoding='utf-8', newline='') as arquivo_csv:
            criar_csv = csv.writer(arquivo_csv)
            criar_csv.writerow(lista_nome)
    except FileNotFoundError:
        print('O arquivo dados_salvos.csv não foi encontrado.')
    else:
        print(f'Usuário {nome} criado com sucesso!')


def ver():
    try:
        with open('dados_salvos.csv', 'r', encoding='utf-8', newline='') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            arquivo = dict(leitor)

            for k, v in arquivo.items():
                if k == 'ID' and v == 'Nome':
                    print('ID - Nome')
                else:
                    print(f'{k} - {v}')
    except FileNotFoundError:
        print('Não foi possivel encontrar o arquivo dados_salvos.csv.')


def editar():
    try:        
        with open('dados_salvos.csv', 'r', encoding='utf-8', newline='') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            lista = list(leitor)
                        
        user_antigo = int(input('Digite o ID do usuário que você deseja editar: '))        

        if user_antigo <= 0 or user_antigo > len(lista):
            print('Não existe um usuário com esse ID.')
        else:
            user_novo = input('Digite o nome do novo usuário: ')

            for posicao, valor in enumerate(lista):
                if user_antigo == posicao:
                    valor[1] = user_novo
            
            with open('dados_salvos.csv', 'w', encoding='utf-8', newline='') as arquivo_csv:
                escritor = csv.writer(arquivo_csv)

                for linha in lista:
                    escritor.writerow(linha)       
    except ValueError:
        print('Digite um valor inteiro.')
    except FileNotFoundError:
        print('O Arquivo dados_salvos.csv não foi encontrado.')
    else:
        print('Arquivo editado com sucesso!')


def remover():
    try:       
        n = int(input('Digite o ID que você deseja remover: '))

        with open('dados_salvos.csv', 'r', encoding='utf-8', newline='') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            lista = [valor for p, valor in enumerate(leitor) if p != n]

        if n <= 0 or n > len(lista):
            print('Não existe um usuário com esse ID.')
        else:
            with open('dados_salvos.csv', 'w', encoding='utf-8', newline='') as arquivo_csv:
                escritor = csv.writer(arquivo_csv)

                for linha in lista:
                    escritor.writerow(linha)       
    except ValueError:
        print('Digite um valor inteiro.')
    except FileNotFoundError:
        print('O Arquivo dados_salvos.csv não foi encontrado.')
    else:
        print('Usuário removido com sucesso!')


while True:
    try:
        opcao = int(input('''
        [0] para sair
        [1] para criar um usuário
        [2] para ver os usuários
        [3] para editar um usuário
        [4] para remover um usuário
        digite a opção aqui: '''))

        if opcao == 0:
            print('Saindo...')
            sleep(2)
            print('Volte sempre :)')
            break
        elif opcao == 1:
            nome = input('Digite o nome do usuário: ')
            criar(nome)
        elif opcao == 2:
            ver()
        elif opcao == 3:
            editar()
        elif opcao == 4:
            remover()
        else:
            print('Número invalido!')
    except ValueError:
        print('Digite um número inteiro!')