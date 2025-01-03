class Aluno:
    def __init__(self, nome, nota1, nota2, nota3):        
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3


    def calcular_notas(self):      
        import csv
        try:
            media = (self.nota1 + self.nota2) / 3   
            lista = []            
            lista.append(self.nome)
            lista.append(self.nota1)
            lista.append(self.nota2)
            lista.append(self.nota3)             
            lista.append(f'{media:.2f}')
            print(lista)

            with open('notas_alunos.csv', 'a', encoding='utf-8', newline='') as arquivo_csv:
                notas_aluno = csv.writer(arquivo_csv)
                notas_aluno.writerow(lista)

            print(f'Medía: {media:.2f}')
        except Exception as erro:
            print(erro)


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
        nome_aluno = input('Digite o nome do aluno ou digite 0 para sair: ')
        print(linha(56))

        if nome_aluno == '0':
            break
        elif isinstance(nome_aluno, str):
            if nome_aluno.isdigit():            
                print(f'{nome_aluno} não é um nome valido!')
            else:
                nota1 = int(input('Digite a primeira nota: '))
                print(linha(56))
                nota2 = int(input('Digite a segunda nota: '))
                print(linha(56))
                nota3 = int(input('Digite a terceira nota: '))
                print(linha(56))
                aluno = Aluno(nome_aluno, nota1, nota2, nota3)
                aluno.calcular_notas()
                aluno.ver_notas()                    
    except ValueError:
        print('Digite um número inteiro!')