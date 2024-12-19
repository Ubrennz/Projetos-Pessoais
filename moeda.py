import moeda

while True:
    num2 = input('Digite um valor R$').replace(',', '.').strip()
    num = float(num2)

    if num == 0:
        break
    
    print(f"R${num:.2f} com um aumento de 10% é R${moeda.aumentar(num, form=True)}")
    print(f"R${num:.2f} com uma diminuição de 10% é R${moeda.diminuir(num, form=True)}")
    print(f"R${num:.2f} dobrado é R${moeda.dobro(num, form=True)}")
    print(f"A metade de R${num:.2f} é R${moeda.metade(num, form=True)}")