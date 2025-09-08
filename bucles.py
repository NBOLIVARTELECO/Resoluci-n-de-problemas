#ciclo for
'''
for a in (0,1,2,3,4):
    dato = int(input("Escriba un numero para ser sumado con a: "))
    print("la suma del numero ingresado con a es:", dato + a) 


'''
x = int(input("Ingrese el numero de veces que se ejecuta el ciclo"))
a=1
b=1
c=2

while(x < 10):
    x = x + 1
    if (x==5):
        # result  = a*x**2 + b*x + c 
        result = a*(x**2) + (b*x) + c 
        print(f"El resultado de la funcion cuadratica es : {x}, {result}")

# Tarea para el miercoles 10 septiembre, realizar una encuesta a sus compañeros,
# si la persona es mayor de 18 añños, proporcion un consejo de economia
# si la persona es mayor de 20, de un consejo de amor
