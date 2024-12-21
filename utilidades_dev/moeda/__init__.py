def ponto(numero):
    n1 = (f'{numero:.2f}')            
    n2 = str(n1)
    n3 = n2.replace('.', ',')
    return n3

def aumentar(n, form=False):
    aumen = (10 / 100) * n + n

    if form:
        n2 = ponto(aumen)
        return n2
    else:
        return (f'{aumen:.2f}')  

def diminuir(n, form=False):
    desconto = (30 / 100) * n
    desconto2 = (desconto - n) * -1

    if form:
        d3 = ponto(desconto2)
        return d3
    else:
        return desconto2

def dobro(n, form=False):
    dobro = n * 2

    if form:
        dob = ponto(dobro)
        return dob
    else:    
        return (f'{dobro:.2f}')

def metade(n, form=False):
    meta = n / 2

    if form:                   
        metad = ponto(meta)
        return metad
    else:    
        return (f'{meta:.2f}')

def resumo(n, aumento, reducao):
    aumen = (aumento / 100) * n + n    
    desconto = (reducao / 100) * n
    desconto2 = (desconto - n) * -1 
    dobro = n * 2
    metade = n / 2

    print('-' * 35)
    print(f'Valor analisado:        {n}')
    print(f'{aumento}% de aumento:      {ponto(aumen)}')
    print(f'{reducao}% de redução:        {ponto(desconto2)}')
    print(f'O dobro de {n}:        {ponto(dobro)}')
    print(f'A metade de {n}:        {ponto(metade)}')
    print('-' * 35)
    
