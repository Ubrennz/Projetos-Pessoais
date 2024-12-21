from utilidades_dev import moeda

try:
    num = input('Digite um valor: ').replace(',', '.').strip()
    num2 = int(num)
    moeda.resumo(num2, 50, 30)
except ValueError:
    print(f'{num} não é um número!')