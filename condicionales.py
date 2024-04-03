"""
A una reunión asistirán personas de diferentes países y géneros. Diseñe una
aplicación que calcule:
a) Cuantas personas son extranjeras, es decir que no pertenecen a Ecuador.
b) Cuantas personas son de Argentina.
c) Cuantas personas son mujeres argentinas.
d) Cuantas personas son varones argentinos.
e) Ingresar información hasta que se digite el valor cero "O" cuando se solicite el país
del participante
"""
"""
# Inicializar variables
extranjeros = 0
argentina = 0
mujeres_argentinas = 0
varones_argentinos = 0

# Ingresar información hasta que se digite el valor cero "O" cuando se solicite el país del participante
while True:
    pais = input("Ingrese el país de origen de la persona (O para salir): ").lower()
    if pais == "o":
        break
    genero = input("Ingrese el género de la persona (M o F): ").lower()
    if pais != "ecuador":
        extranjeros += 1
    if pais == "argentina":
        argentina += 1
        if genero == "f":
            mujeres_argentinas += 1
        else:
            varones_argentinos += 1
            
# Mostrar los resultados
print(f"Personas extranjeras: {extranjeros}")
print(f"Personas de Argentina: {argentina}")
print(f"Mujeres argentinas: {mujeres_argentinas}")
print(f"Varones argentinos: {varones_argentinos}")

# Fin del programa


"""

# otra opcion usando funciones y diccionarios

"""
"def ingresarPais():
  unPais = input("Ingrese Su pais completo / (O): para terminar").lower()  
  return unPais

def ingresarSexo():
  unSexo = input("Ingrese F si sos mujer / M: si sos hombre ")  
  return unSexo
def getEstadisticas():
  dicEstadisticas = {} # clave el pais y valor un diccionario con claves F y M cuyos       #valores son la cantidad de mujeres y hombres respectivamente para ese pais
  unPais = ''
  while( unPais != 'O' ):
    pais = ingresarPais()
    sexo = ingresarSexo()
    if (pais not in dicEstadisitcas.keys()): 
      dicEstadisticas[pais] = {}
      dicEstadisticas[pais][F] = 0 
      dicEstadisticas[pais][M] = 0 
      dicEstadisticas[pais][sexo] += 1
    else: 
      dicEstadisticas[pais][sexo] += 1

def main(): 
  getEstadisticas()  
main()

"""


"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
Si el divisor es cero el programa debe mostrar un error.

"""
"""
# inicializar variables
dividendo = 0
divisor = 0
resultado = 0

# Ingresar los números
dividendo = float(input("Ingrese el dividendo: "))
divisor = float(input("Ingrese el divisor: "))
if divisor == 0:
    print("Error: No se puede dividir entre cero")
else:
    resultado = dividendo / divisor
    print(f"El resultado de la división es: {resultado}")
    

#hacer lo mismo pero con una funcion

def division(dividendo, divisor):
    if divisor == 0:
        return "Error: No se puede dividir entre cero"
    else:
        return dividendo / divisor
      
dividendo = float(input("Ingrese el dividendo: "))
divisor = float(input("Ingrese el divisor: "))
print(division(dividendo, divisor))


"""

# hacerlo con funcion pero la funcion sin parametros
"""
def division():
    dividendo = float(input("Ingrese el dividendo: "))
    divisor = float(input("Ingrese el divisor: "))
    if divisor == 0:
        return "Error: No se puede dividir entre cero"
    else:
        return dividendo / divisor
      
      
resultado = division()
      
print(f"El resultado de la división es: {resultado} ")

"""


"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña 
introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""
"""
contraseña = "contraseña"
contraseña_usuario = input("Introduce la contraseña: ")
if contraseña == contraseña_usuario.lower():
    print("La contraseña coincide")
else:
    print("La contraseña no coincide")
    
 """   
    
# hacerlo con funcion sin parametros 
"""
def verificar_contraseña():
  contraseña = "abraham".lower()
  try:
    contraseña_usuario = input("Introduce la contraseña: ")
    if contraseña == contraseña_usuario.lower():
      return "La contraseña coincide"
    else:
      return "La contraseña no coincide"
  except Exception as contra_error:
    print(f"Ha ocurrido un error: {contra_error}")

print(verificar_contraseña())

 """
# esta es un ejemplo de condicionales incluyentes, evlaua todos los if y segun edad muestra varias respuestas.
"""
 #Ejercicio Edad y cine:
 #crear una funcion que pregunte edad del usuario y muestre que categorias de peliculas puede ver
 #peliculas para todas las edades (1 a 100) mayores de 12 o mayores de 18.
 
def edad_cine():
    
        edad = int(input("Ingrese su edad: "))
        if (edad <= 0 or edad >= 101):
            print("error: debe ingresar un número entre 1 y 100")
            return "error"
        if edad >= 1 and edad <= 100:  
              print("Usted puede ver películas infantiles")
        if edad >= 12:
              print("Puede ver películas para mayores de 12 años")
        if edad >= 18:
               print( "Puede ver películas para mayores de 18 años" )  
          

edad_cine()


"""
# correcion del ejecicio anterior, haciendo el codigo excluyente, es decir que si cumple una condicion no se evalua la siguiente

 #Ejercicio Edad y cine:
 #crear una funcion que pregunte edad del usuario y muestre que categorias de peliculas puede ver
 #peliculas para todas las edades (1 a 100) mayores de 12 o mayores de 18.
"""
def edad_cine():
  
    edad = int(input("Ingrese su edad: "))
    if edad <= 0 or edad >= 101:
        print("Error, Debe ingresar un número entre 1 y 100")
        return "Error"
    elif edad >= 18:
        print("Puede ver películas para mayores de 18 años")
    elif edad >= 12:
        print("Puede ver películas para mayores de 12 años")
    else:
        print("Usted puede ver películas infantiles")
        
        
        
edad_cine()
 """    
 
 
"""
 
def edad_cine():
  
    edad = int(input("Ingrese su edad: "))
    if edad <= 0 or edad >= 101:
        print("Error, Debe ingresar un número entre 1 y 100")
        return "Error"
    elif edad >= 60:
        print("Puede ver películas para mayores de 60 años")
    elif edad >= 18:
        print("Puede ver películas para mayores de 18 años")
    elif edad >= 12:
        print("Puede ver películas para mayores de 12 años")
    else:
        print("Usted puede ver películas infantiles")
        
edad_cine()

"""

#en estecodigo, si la edad ingreada es 65 se mostrara el mensaje "Puede ver películas para mayores de 60 años" y no se evaluaran las otras condiciones
#recuerdenvque las condiciones se verifican en el orden en que estan escritas,
#por lo que debe poner las condiciones mas restrictivas primero y las menos restrictivas al final,
#de esta manera si una condicion se cumple no se evaluaran las siguientes
#por eso se pone la edad mas grande primero y la mas pequeña al final


#promedio de numeros
"""
Crear una funcion que genere 3 numeros aleatorios y clacule su promedio ,
muestre su resultado, el resultado entero y retorne el promedio (float)
"""
import random

def promedio(): #definicion de la funcion
    
    #usar seed para que los numeros aleatorios sean los mismos
    random.seed(4)  
    
    # genera un numero aleatorio entre 50 y 100, y lo asigna a la variable num1, num2 y num3.
    #round() redondea el numero a 3 decimales
    num1 = round(random.uniform(50, 100),3) 
    num2 = round(random.uniform(50, 100),3)
    num3 = round(random.uniform(50, 100),3)  
     #calcula el promedio
    promedio = (num1 + num2 + num3) / 3  
     #muestra el promedio flotante y el promedio entero en el segundo print con la funcion int()
    print(f"El promedio de {num1}, {num2} y {num3} es: {round(promedio, 2)}") # redondea el promedio a 2 decimales
    print(f"El promedio entero es: {int(promedio)}")   
    return promedio    #retorna , escupe el promedio.

promedio()  #llamada a la funcion


