#MODULOS-----------------------------------
import sys
import math #para el mcd



##FUNCIONES---------------------------------

#Leer el texto base de un archivo y generar la Fuente de información con frecuencias absolutas.
def fuente_informacion_freq_absolutas(nombre_archivo):
    
    fuente_informacion = {} #diccionario que sera mi fuente (alfabeto + frecuencias)
    
    
    
    with open(nombre_archivo, 'r', encoding='utf8') as f: #open abre el archivo; r en modo lectura; f el descriptor de fichero; importante decirle que es utf8 el fichero que sino no carga las ñ ni ´´

        linea = f.readline() #leo primera linea del archivo


        while linea: #mientras que siga habiendo líneas
            #Cojo caracter a caracter de la línea
            for caracter in linea:
                #print(caracter)


                    #Miro si es el caracter de fin de línea en cuyo caso lo agregaré como un doble espacio separado, dos espacios simples vaya, no un nuevo símbolo que sea "  "
                if caracter == "\n":    
                        
                    caracter = " " #convierto el \n en un espacio
                    for i in range(0,2): #0 incluido, 2 excluido --> 2 iteraciones
                        if " " in fuente_informacion: #si ya he añadido antes un espacio
                            fuente_informacion[" "] = fuente_informacion[" "] + 1 #si ya estaba el simbolo solo le sumo una ocurrencia 
                        else:
                            fuente_informacion[" "] = 1 #si es la primera ocurrencia, añado al diccionario el espacio (" ") con una ocurrencia
                   
                else: #si no es el de fin de linea es otro pero que tampoco esta en el alfabeto actualmente

                    #miro si el caracter esta ya en el alfabeto
                    if caracter in fuente_informacion:


                        fuente_informacion[caracter] = fuente_informacion[caracter]+1  #si está le sumo uno a su nº de ocurencias
                    
                    else:
                        
                        fuente_informacion[caracter] = 1  #simplemente le pongo una ocurrencia (al ponerle 1 ocurrencia se añaden la clave y el valor, es decir el caracter y el 1)



            #sigo leyendo la siguiente
            linea = f.readline()
        



      

    #TENIENDO YA EL ALFABETO Y LAS FRECUENCIAS ABS EN EL DICCIONARIO DE NOMBRE fuente_informacion {caracter : freq} las devuelvo
    return fuente_informacion

def leerAlfabetoTalCual(nombre_archivo):
    alfabeto = []
    
    
    
    with open(nombre_archivo, 'r', encoding='utf8') as f: #open abre el archivo; r en modo lectura; f el descriptor de fichero; importante decirle que es utf8 el fichero que sino no carga las ñ ni ´´

        linea = f.readline() #leo primera linea del archivo


        while linea: #mientras que siga habiendo líneas
            #Cojo caracter a caracter de la línea
            for caracter in linea:
                alfabeto.append(caracter)
        
            linea = f.readline()

     

    #TENIENDO YA EL ALFABETO lo devuelvo
    return alfabeto

def procesarFuenteInformacion(fuenteInformacion):
    
    alfabeto = []
    
    for i in fuenteInformacion.keys():
        alfabeto.append(i)

    return alfabeto

def leerMsjCifrado(ruta):

    msjEnClaro = []
    aux = "" #cadena auxiliar para leer por caracteres y sustituir el \n
    

    with open(ruta, 'r', encoding='utf8') as f: #open abre el archivo; r en modo lectura; f el descriptor de fichero; importante decirle que es utf8 el fichero que sino no carga las ñ ni ´´

            linea = f.readline() #leo primera linea del archivo


            while linea: #mientras que siga habiendo líneas
                aux  = ""
                for caracter in linea:
                    if(caracter == "\n"):
                        aux = aux + "  "
                    else:
                        aux = aux + caracter

                msjEnClaro.append(aux)
                
                #sigo leyendo la siguiente
                linea = f.readline()

    return msjEnClaro

def codifNcaEstandar(modulo):

    cne = []

    #el modulo es la longitud del alfabeto. La codificación numérica estándar empezaría en el 0 e iría hasta el 6
    for i in range(modulo):
        cne.append(i)

    return cne

def codifNcaOtra(modulo):

    cno = []
    for i in range(incluido, exluido): #range(start, stop, step)
        cno = i

    return cno

def codNumericaDeMsjCifrado(msjCifrado, alfyCodNca):
    listaCN = []
  

    for linea in msjCifrado:
        num = ""
        for caracter in linea:
            for letra, numero in alfyCodNca.items():
                if caracter == letra:
                    listaCN.append(numero)

        

    return listaCN

def desCifradoSustMonoalf(listaCN, a, b, modulo, alfyCodNca):

    msjNumericoCifrado =[]
    saltoLinea = ""
    caracterDesCifrado = ""
    lineaActual = ""

    i = 1
#Primera clave necesaria
    nuevaClave = actualizarClaveCifrado(a, b, i, modulo)
    claveDescifrado = calculoClaveDescifrado(nuevaClave)

    for numero in listaCN: #cada numero del msj cifrado (tipicamente solo tiene 1 linea)
       

        caracterDesCifrado = str((claveDescifrado[0]*int(numero)+claveDescifrado[1])%modulo)
        letra = codLetraDeMsjNumericoDesCifrado(caracterDesCifrado, alfyCodNca)
        if letra == " ": #si es un espacio
            saltoLinea = saltoLinea + letra
        else:
            saltoLinea = "" #sino contara los 2 espacios aunque tengan cosas entre medias

        if saltoLinea == "  ":
            i = i+1
            nuevaClave = actualizarClaveCifrado(a, b, i, modulo)
            claveDescifrado = calculoClaveDescifrado(nuevaClave)
            saltoLinea = ""
                   
        lineaActual = lineaActual + letra
    msjNumericoCifrado.append(lineaActual)
        
        
        
        
        
            
    return msjNumericoCifrado

def actualizarClaveCifrado(a, b, i, modulo):

    nuevaClave = []
    a = (a**i)%modulo
    print("A --->", a)
    b = (i*b)%modulo
    print("B --->", b)

    nuevaClave.append(a)
    nuevaClave.append(b)

    return nuevaClave

def codLetraDeMsjNumericoDesCifrado(caracterDesCifrado, alfyCodNca):
    
    let = ""
    num = int(caracterDesCifrado)

    for letra, numero in alfyCodNca.items():
        if int(num) == numero:
          print(letra)
          let = letra

    return let

def verificarSiInversible(a, b, modulo):
    #Si el número es primo con el módulo, tiene inverso en el módulo -> mcd()=1
    inversible = False
    mcda = math.gcd(a, modulo)
    mcdb = math.gcd(b, modulo)

    if mcda == 1 & mcdb == 1:
        testigo = True
    
    return testigo

def calculoClaveDescifrado(nuevaClave):
    
    claveDescifrado = []

    #en base a la clave de cifrado tengo que aplicarle (a^-1,-a^-1*b)
    a = nuevaClave[0]
    b = nuevaClave[1]

    #como sé que tienen inverso porque la clave de cifrado inicial lo tiene, lo calculo
    aInv = pow(a, -1, modulo) #pow(value, -1, modulus)

    b = (((-1)*aInv)*b)%modulo
    print("NUEVAS A Y B", aInv, b)

    claveDescifrado.append(aInv) #a^-1 
    claveDescifrado.append(b)

    return claveDescifrado




##PROGRAMA------------------------
print("Bienvenid@ a la Práctica 5: Simulacion de un Sistema criptográfico de clave privada SUSTITUCION MONOALFABETICA")

    #1. Cargar Alfabeto 

#ENTRADA TAL CUAL DEL ARCHIVO
#alfabeto = leerAlfabetoTalCual('/Users/mario/Desktop/Segundo Cuatrimestre/Seguridad Informática/Prácticas/Practica_5_SI/Resolucion/Descifrar/Alfabeto.txt')
#print("Tal cual del archivo -> ", alfabeto)
#modulo = len(alfabeto)
#print("Tamaño = ", modulo)

#ENTRADA PROCESADA LOS \N como 2 espacios (OJO SI EL ALFABETO DADO NO CONTIENE EL ESPACIO QUE LO METE COMO SIMBOLO)
fuenteInformacion = fuente_informacion_freq_absolutas('/Users/mario/Desktop/Segundo Cuatrimestre/Seguridad Informática/Prácticas/Practica_5_SI/Resolucion/Descifrar/Alfabeto.txt')
alfabeto = procesarFuenteInformacion(fuenteInformacion) #de la fuente de informacion nos quedamos solo con el alfabeto en una lista
print("Alfabeto = ", alfabeto)
print("Tamaño = ", len(alfabeto))
modulo = len(alfabeto)



#ENTRADA MANUAL
#alfabeto = []
#alfabeto = ['P','R','A','C','T','I','C','A','T','R','E','S']
#print(alfabeto)
#modulo = len(alfabeto)
#print("Tamaño = ", modulo)



    # LEER MENSAJE A DECODIFICAR (Mensaje Cifrado)

msjCifrado = leerMsjCifrado('/Users/mario/Desktop/Segundo Cuatrimestre/Seguridad Informática/Prácticas/Practica_5_SI/Resolucion/Descifrar/MsjCifrado.txt')
print("Mensaje en Claro", msjCifrado)


    # CÁLCULO DE LA CODIFICACIÓN NUMÉRICA

codifNcaEstandar = codifNcaEstandar(modulo)
print("Cod. Num. Std", codifNcaEstandar)

#codifNcaOtra = codifNcaOtra(modulo)
#print("Cod. Num. Otra", codifNcaOtra)

#codifNcaManual =[0,1,2,3,4,5,6]
#print("Cod. Manual", codifNcaManual)

#Junto el alfabeto y la codificacion numerica en una misma estructura diccionario
alfyCodNca = {alfabeto[i]: codifNcaEstandar[i] for i in range(len(alfabeto))}

print(alfyCodNca)


    # DESCIFRADO POR SUSTITUCIÓN MONOALFABÉTICA

print("Introduzca la clave DE CIFRADO inicial (a,b)")
a = input()
b = input()

a = int(a)
b = int(b)

inversible = verificarSiInversible(a, b, modulo)
if inversible == False:
    print("ERROR La clave de cifrado no es inversible en Z módulo", modulo)
    exit()

listaCN = codNumericaDeMsjCifrado(msjCifrado, alfyCodNca)

#ahora tengo la listaCN con el mensaje en claro pero en codificacion numerica
#tengo que aplicar linea a linea (posicion a posicion de lista) el cifrado y la clave

msjNumericoDesCifrado = desCifradoSustMonoalf(listaCN, a, b, modulo, alfyCodNca)
print("DESCIFRADO", msjNumericoDesCifrado)

msjFinal = ""

for linea in msjNumericoDesCifrado:
    msjFinal = msjFinal+linea

msjFinal = msjFinal.replace("  ", "\n")

print("\n**********************************************************************")
print("MENSAJE DESCIFRADO:")
print(msjFinal, end = '')
print("|Barra que marca el fin msj")
print("**********************************************************************")

print("\nFIN DEL PROGRAMA")
       







##APENDICES:

    #pintar todos los valores del diccionario
#for i in fuente_freq_abs.values():
#        print(i)

    #pintar todas las claves del diccionario
#for i in fuente_freq_abs.keys():
#        print(i)

    #manejar clave y valor a la vez en un diccionario para ir por las posiciones
#for clave, valor in fuente_de_informacion.items():  
#        fuente_de_informacion[clave] = Fraction(valor, total_frecuencias)


    #fraccion es numerador/denominador
#fraccion = Fraction(1, 2) #--> 1/2
#print(fraccion)


    #logaritmo en base 2 de 100
#math.log(100,2)



#utf8stdout = open(1, 'w', encoding='utf-8', closefd=False) # fd 1 is stdout
#cadena = "ó"
#print(cadena)
#for i in fuente_freq_abs.keys():
    #print(i, file=utf8stdout)
