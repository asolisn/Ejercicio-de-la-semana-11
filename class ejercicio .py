class Ejercicio:
    def __init__(self):
        pass
    
    def parImpar(self,numero):
        if numero % 2 == 0:
            print("{} es Par".format(numero))
        else:
            
ejer = ejercicios()
#num = int(input("Ingrese un numero"))
lista = [2,3,1,5,6,8,10]
for num in lista:
    ejer.parImpar(num)