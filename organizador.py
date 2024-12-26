def salvar_tarefa(tarefa):
    try:
        with open('tarefas.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{tarefa} - pendente \n')            
    except:
        print('Erro ao tentar salvar a tarefa')
    else:
        print('Tarefa salva com sucesso!')


def ver_tarefas():
    try:
        with open('tarefas.txt', 'r', encoding='utf-8') as arquivo:
            leitor = arquivo.readlines()

            for linha in leitor:
                print(linha)
    except FileNotFoundError:
        print('Arquivo não encontrado!')


def tarefa_concluida():
    try:        
        with open('tarefas.txt', 'r', encoding='utf-8') as arquivo:           
            lista = list(arquivo.readlines())      

        for p, linha in enumerate(lista):
            print(f'{p} - {linha}') 
       
        marcador = int(input(f'\nqual você deseja marcar? Digite entre 0 e {len(lista) - 1}: '))
        lista_atualizada = []

        if marcador >= 0 and marcador < len(lista):
            for p, linha in enumerate(lista):
                if p == marcador:
                    tarefas_at = linha.replace('pendente', 'concluído')
                    lista_atualizada.append(tarefas_at)
                else:
                    lista_atualizada.append(linha)
            
            with open('tarefas.txt', 'w', encoding='utf-8') as arquivo:          
                arquivo.writelines(lista_atualizada)
                print('Tarefa atualizada com sucesso!')  
        else:
            print(f'{marcador} não estar entre 0 e {len(lista) - 1}')           
    except FileNotFoundError:
        print('Arquivo não encontrado.')
    except ValueError:
        print('Digite apenas números inteiros.')


def remover_nota():
    try:
        with open('tarefas.txt', 'r', encoding='utf-8') as arquivo:           
            lista = list(arquivo.readlines())
            for p, linha in enumerate(lista):
                print(f'{p} - {linha}')

        numero = int(input(f'\ndigite o número da tarefa que você deseja remover, Digite entre 0 e {len(lista) - 1}: '))
        
        if numero >= 0 and numero < len(lista):
            tarefas_atualizadas = [linha for p, linha in enumerate(lista) if p != numero]

            with open('tarefas.txt', 'w', encoding='utf-8') as arquivo:
                arquivo.writelines(tarefas_atualizadas)
                print('Tarefa removida com sucesso!')
        else:
            print(f'{numero} não estar entre 0 e {len(lista) - 1} ') 
    except FileNotFoundError:
        print('Arquivo não encontrado.')
    except ValueError:
        print('Digite apenas números inteiros.')
              

while True:
    try:
        opcao = int(input('''
        [0] para sair
        [1] para salvar uma tarefa
        [2] para ver as tarefas
        [3] para marcar como concluída uma tarefa
        [4] para remover uma tarefa
        Digite a opção aqui: '''))

        if opcao == 0:
            break
        elif opcao == 1:
            afazer = input('Digite aqui: ')
            salvar_tarefa(afazer)
        elif opcao == 2:
            ver_tarefas()
        elif opcao == 3:
            tarefa_concluida()
        elif opcao == 4:
            remover_tarefa()
    except ValueError:
         print('Digite apenas números inteiros.')
