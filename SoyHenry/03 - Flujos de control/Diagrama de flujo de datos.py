#Date 7/4/2023 6:30 AM
#Declaracion de variables 
a = 100
b = 2
#Estructura de control
#Si a es mayor que 0
if (a > 0): 
    #Bucle mientras sea mayor que 0
    while (a > 0):
            a = a - b
    #este if tiene que estar dentro del while para que use su output, si no, no funciona
    if(a == 0): 
        print ('a es divisible por b')
    else: 
        (print('b no es divisible por b'))


