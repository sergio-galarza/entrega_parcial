
pacientes = []

def cargar():
    #se encarga de cargar a los nuevos pacientes a la lsita de pacientes
    n = input("¿cuantos pacientes desea ingresar? :")
    while not n.isdigit():#valida que sea un entero
        n = input("Error. ingrese un numero valido: ")
    n = int(n)
        
    for i in range(n):#ingresa al bucle segun la iteraciones que idica el usuario y recopila los datos
        numero_historia = input("ingrese el numero de historia clinica: ")
        while not numero_historia.isdigit():
            numero_historia = input("Error. ingrese un numero valido: ")
        numero_historia = int(numero_historia)
        nombre = input("ingrese el nombre del paciente: ")
        edad = input("ingrese la edad del paciente: ")
        while not edad.isdigit():
            edad = input("Error. ingrese un numero valido: ")
        edad = int(edad)
        diagnostico = input("ingrese el diagnostico del paciente: ")
        dias_internacion = input("ingrese la cantidad de dias que estuvo internado: ")
        while not dias_internacion.isdigit():
            dias_internacion = input("Error. ingrese un numero valido: ")
        dias_internacion = int(dias_internacion)
        
            
    return pacientes.append([numero_historia,nombre,edad,diagnostico,dias_internacion])# agrega los datos cargados en forma de lista

def mostrar_pacientes():
    if not pacientes:
        print("no se puede realizar esta operacion porque la lista esta vacia") #valida que la lista contenga elementos para realizar la accion
        return
    else:
        for i in range(len(pacientes)):#recorre el tamaño de la lista e imprime en cada iteracion los elementos de la misma
            print(pacientes[i])
    

def buscar():
    if not pacientes:#valida que la lista contenga elementos para realizar la accion
        print("no se puede realizar esta operacion porque la lista esta vacia")
        return
    
    buscar_paciente = input("ingrese el nombre del paciente: ")
    for i in pacientes: # recorre la lista utlizando de comparativa al nombre ingresado. si coincide imprime los datos del pacientes 
        if buscar_paciente == i:
            buscar_paciente = i
        print(f"""
Paciente encontrado:
Número de historia clínica: {i[0]}
Nombre: {i[1]}
Edad: {i[2]}
Diagnóstico: {i[3]}
Días de internación: {i[4]}""")

def paciente_max():
    if not pacientes:#valida que la lista contenga elementos para realizar la accion
        print("no se puede realizar esta operacion porque la lista esta vacia")
        return
    paciente_max = pacientes [0] #toma como inicio al primer paciente de la lista
    dias_max = pacientes[0][4]#toma como inicio al los dias de internacion del primer paciente
    for i in pacientes:  #recorre la lista y compara los dias de internacion de los diferentes elementos de la lista. al finalizar establece el maximo segun la comparativa
        if dias_max < i[4]:
            dias_max = i[4]
    print(f"el paciente {paciente_max[1]} es el paciente con mas dias de internacion con {dias_max} dias")# imprime el resultado
def paciente_min(): #realiza la misma tarea que la funcion anterior pero estableciendo los dias minimos de internacion
    if not pacientes:
        print("no se puede realizar esta operacion porque la lista esta vacia")
        return
    paciente_min = pacientes [0]
    dias_min = pacientes[0][4]
    for i in pacientes:  
        if dias_min > i[4]:
            dias_min = i[4]
    print(f"el paciente {paciente_min[1]} es el paciente con mas dias de internacion con {dias_min} dias")
    
def ordenar (pacientes):
    if len(pacientes) < 1: #valida que la lista contenga elementos
        return []
    
    izquierda = []
    derecha = []
    pivote = pacientes[0] #establece como pivote al primer paciente de la lista
    
    for i in range(1, len(pacientes)):#recorre la lista y conpara con el pivote establecido
        if pacientes[i][1] < pivote[1]:
            izquierda.append(pacientes[i])# si es menor que el pivote lo agrega a la lista izquierda
        else:
            derecha.append(pacientes[i])#si es mayor que el pivote lo agrega a la lista derecha
            
    return izquierda,pivote,derecha #retorna los valores guardados

def quicksort (pacientes):
    if len(pacientes) < 2:# valida que ya no quedan mas elementos a comparar
        return pacientes
    
    izquierda,pivote,derecha = ordenar(pacientes)#llama a la funcion para inicar el bucle
    
    return quicksort(izquierda)+ [pivote]+quicksort(derecha) #retorna y concatena las listas izquierdad y derecha, dejando al pivote en su posicion verdadera

def mas_cinco():
    if not pacientes:#valida que la lista contenga elementos para realizar la accion
        print("no se puede realizar esta operacion porque la lista esta vacia")
        return
    paciente_nombre = pacientes[0][1] #establecemos como inicio a comparar los valores del primer paciente
    paciente_dias = pacientes[0][4] #establecemos como inicio a comparar los valores del primer paciente
    lista = []
    for i in pacientes:
        if i[4] > 5: #si al recorrer el bucle encuentra en la posicion 4 de la lista a un paciente con mas de 5 dias de internacion.lo agrega a la lista vacia definida
            lista.append([i[1],i[4]])
        
    if len(lista) > 0: #si encuentra elementos en la lista los imprimne
        print(f"""
los pacientes que estuvieron mas de 5 dias son:
{lista}
""")
    else:# si no encuentra pacientes imprime el siguiente mensaje 
        print("no hay pacientes con mas de 5 dias de internacion")
        
def promedio():
    if not pacientes:#valida que la lista contenga elementos para realizar la accion
        print("no se puede realizar esta operacion porque la lista esta vacia")
        return
    
    inicio = 0
    
    for i in pacientes: #recorre la lista pacientes
        inicio += i[4]#cuando llegue a la posicion 4 de cada paciente la suma a la variable inicio
    
    promedio = inicio / len(pacientes) #realiza el promedio teneniendo en cuenta la cantidad de iteraciones sumadas dividio la cantidad de elementos dentro de la lista pascientes
    print(f"el promedio de internacion de los pacientes registrados es: {promedio}")

inicio = ""
while inicio == "":
    accion = int(input("""
---------------------------------------------------------
opciones:
1.cargar pacientes
2.mostrar todos los pacientes
3.buscar pacientes
4.paciente con mas dias de internacion
5.paciente con menos dias de internacion
6.ordenar pacientes por historia clinica
7.cantidad de pacientes con mas de 5 dias de internacion
8.promedio de dias de internacion de los pacientes
9. salir del sistema
---------------------------------------------------------
indique el numero: 
"""))
    
    if accion == 1:
        cargar()
    elif accion == 2:
        mostrar_pacientes()
    elif accion == 3:
        buscar()
    elif accion == 4:
        paciente_max()
    elif accion == 5:
        paciente_min()
    elif accion == 6:
        if not pacientes:
            print("no se puede realizar esta operacion porque la lista esta vacia")#valida que la lista contenga elementos para realizar la accion
        else:
            print(quicksort(pacientes))
    elif accion == 7:
        mas_cinco()
    elif accion == 8:
        promedio()
    elif accion == 9:
        print("hasta la proxima")
        break