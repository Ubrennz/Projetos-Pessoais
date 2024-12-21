from utilidades_dev import moeda

try:
    while True:
        num = input('Digite um valor R$').replace(',', '.').strip()
        num2 = float(num)

        if num2 == 0:
            break
        
        print(f"R${num2:.2f} com um aumento de 10% é R${moeda.aumentar(num2, form=True)}")
        print(f"R${num2:.2f} com uma diminuição de 10% é R${moeda.diminuir(num2, form=True)}")
        print(f"R${num2:.2f} dobrado é R${moeda.dobro(num2, form=True)}")
        print(f"A metade de R${num2:.2f} é R${moeda.metade(num2, form=True)}")
        
except ValueError:
    print(f'{num} não é um número!')