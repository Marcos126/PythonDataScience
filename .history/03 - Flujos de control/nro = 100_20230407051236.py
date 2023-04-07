
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
print('Fin del ciclo ' + str(c))
