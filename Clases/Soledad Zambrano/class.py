from random import randint

#con init clases de numeros complejos
class Complejo:
     def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
        self.i="i"
     def getimaginary(self,r,i):
        return str(r)+ "+" + str(i)+"i"

     def suma(self,x,y):
         return str(x+self.real)+str(y+self.imaginary)+self.i
     
     def resta(self,x,y):
         return str(x-self.real)+str(y-self.imaginary)+self.i

     def multiplicacion(self,x,y):
         return str(x*self.real)+str(y*self.imaginary)+self.i

     def division(self,x,y):
         return str(x/self.real)+str(y/self.imaginary)+self.i
         
    


#clase con init
# complejo=Complejo(3,4)
# print(complejo.getimaginary(9,3))
# print(complejo.suma(3,6))
# print(complejo.resta(3,6))
# print(complejo.multiplicacion(3,6))
# print(complejo.division(3,6))


#clase sin init de numero complejo
# class Complejo:
    
#      def getimaginary(self,r,i):
#         return str(r)+ "+" + str(i)+"i"
#      def suma(self,x,y):
#          real=int(x[0:1])+ int(y[0:1])
#          imaginary=int(x[2:])+int(y[2:])
#          complejo=str(real)+"+"+str(imaginary)+self.i
#          return (complejo)

# complejo=Complejo()
# print(complejo.getimaginary(9,3))
# numero1=input("ingrese un numero complejo para sumar")
# numero2=input("ingrese el segundo valor")
# print(complejo.suma(numero1,numero2))
#idem para el resto de operaciones, pedir valores

#ejercicio 2 clase vector de 3 dimensiones

class Vector:

    def suma(self,v1,v2):
        x= int(v1[0:1])+int(v2[0:1])
        y= int(v1[2:3])+int(v2[2:3])
        z= int(v1[4:])+int(v2[4:])
        return str(x)+","+str(y)+","+str(z)
    def resta(self,v1,v2):
        x= int(v1[0:1])-int(v2[0:1])
        y= int(v1[2:3])-int(v2[2:3])
        z= int(v1[4:])-int(v2[4:])
        return str(x)+","+str(y)+","+str(z)
    def multiplicacion(self,v1,num):
        x= int(v1[0:1])*int(num)
        y= int(v1[2:3])*int(num)
        z= int(v1[4:])*int(num)
        return str(x)+","+str(y)+","+str(z)
    def dividir(self,v1,num):
        x= int(v1[0:1])/int(num)
        y= int(v1[2:3])/int(num)
        z= int(v1[4:])/int(num)
        return str(x)+","+str(y)+","+str(z)

# vector=Vector()
# vec1=input("ingrese un vector ejemplo a,b,c")
# vec2=input("ingree otro vector")
# num=input("ingrese un numero para multiplicar y/o dividir")
# print(vector.suma(vec1,vec2))
# print(vector.resta(vec1,vec2))
# print(vector.multiplicacion(vec1,num))
# print(vector.dividir(vec1,num))

#ejercicio3 clases matrices

class Matriz:

    def __init__(self, dim):
        # self.m=[[a,b,c],[d,e,f],[g,h,i]]
        matriz=[]
        for fila in range(dim): # para fila desde 0 hasta dim-1
            nuevaC = []
            for columna in range(dim): 
                nuevaC.append(randint(1,10))
            matriz.append(nuevaC)
        
        # matriz: [[7,4], [4,9]]
        self.m = matriz

    def representacion(self):
        for fila in self.m:
            print(fila)

    def sumaMatriz(self,m1):
        matriz=[]
        dim = len(self.m)
        if dim != len(m1.m):
            if(len(self.m[0]) != len(m1.m[0])):
                return('Las dimensiones de sus matrices no son iguales')
        for i in range(dim):
            nuevaC = []
            for j in range(len(self.m[0])):
                nuevaC.append(self.m[i][j]+m1.m[i][j])
            matriz.append(nuevaC)
        return matriz
    def restaMatriz(self,m1):
        matriz=[]
        dim = len(self.m)
        if dim != len(m1.m):
            if(len(self.m[0]) != len(m1.m[0])):
                return('Las dimensiones de sus matrices no son iguales')
        for i in range(dim):
            nuevaC = []
            for j in range(len(self.m[0])):
                nuevaC.append(self.m[i][j]-m1.m[i][j])
            matriz.append(nuevaC)
        return matriz

    # def multiplicacion(self,vec):



    

dimension = int(input('Ingrese dimensión de la matriz cuadrada: '))
dimensionSegunda = int(input('Ingrese dimensión de la matriz cuadrada: '))

matriz=Matriz(dimension)
matrizSegunda=Matriz(dimensionSegunda)
# print(matriz)
matriz.representacion()
print('\n *********** \n')
matrizSegunda.representacion()
print('\n *********** \n')
#para que la representacion sea igual a las matrices
suma = matriz.sumaMatriz(matrizSegunda)
for fila in suma:
    print(fila)


        






    