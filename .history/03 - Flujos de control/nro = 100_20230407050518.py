a = 10
b = 2
if (a > 0): 
    while True:
            a = a - b
            print(a)
            if a == 0:
                break  
            print(a)
    if(a == 0): 
        print ('Nro es divisible por b')
    else: 
        (print('Nro no es divisible por b'))


cadena = 'Python'
for letra in cadena: 
    if letra == 'P':
        continue
    print(letra)
    


c = 10
if(c > 0):
    while True:
        c = c - 1
        print(c)
        if c == 5:
            break
        print(c)
print('Fin del ciclo' + str(c))
