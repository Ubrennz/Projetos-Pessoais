class Aluno:
    def __init__(self, loops):
        self.loops = loops


    def calcular_notas(self):      
        try:
            soma = 0
            count = 0

            for c in range(0, self.loops):
                notas = int(input(f'nota {c}ª: '))
                soma += notas
                count += 1

            print(f'Medía: {soma / count:.2f}')
        except:
            print('Erro ao tentar calcular a nota.')

def linha(count):
    linhas = '-' * count
    return linhas


def centralizar(posicao, texto):
    central = texto.center(posicao, ' ')
    return central


print(linha(56))
print(centralizar(56, 'Sistema de Notas'))
while True:
    try:
        print(linha(56))
        loop = int(input('Digite quantas notas vão ser calculadas ou 0 para sair: '))
        print(linha(56))
        
        if loop == 0:
            break

        aluno = Aluno(loop)
        aluno.calcular_notas()
    except ValueError:
        print('Digite um número inteiro!')
    
# fazer um arquivo para ter as notas dos alunos, as medias e puder editar as notas e a media
# e remover as notas e as medias dos alunos