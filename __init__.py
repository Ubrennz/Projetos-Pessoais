def aumentar(n, form=False):
    au = (10 / 100) * n + n

    if form:
        n1 = (f'{au:.2f}')            
        n2 = str(n1)
        n3 = n2.replace('.', ',')
        return n3
    else:
        return (f'{au:.2f}')  

def diminuir(n, form=False):
    d = (30 / 100) * n
    d2 = (d - n) * -1

    if form:
        n1 = (f'{d2:.2f}')            
        n2 = str(n1)
        n3 = n2.replace('.', ',')
        return n3
    else:
        return d2

def dobro(n, form=False):
    dobro = n * 2

    if form:
        n1 = (f'{dobro:.2f}')            
        n2 = str(n1)
        n3 = n2.replace('.', ',')
        return n3
    else:    
        return (f'{dobro:.2f}')

def metade(n, form=False):
    meta = (f'{n / 2:.2f}')

    if form:                   
        n2 = str(meta)
        n3 = n2.replace('.', ',')
        return n3
    else:    
        return meta
    