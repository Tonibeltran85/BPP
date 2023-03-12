import pandas as pd
import numpy as np


Enero = []
Febrero = []
Marzo = []
Abril = []
Mayo = []
Junio = []
Julio = []
Agosto = []
Septiembre = []
Octubre = []
Noviembre = []
Diciembre = []

def meses(num):
    if num == 0:
        return "Enero"
    elif num == 1:
        return "Febrero"
    elif num == 2:
        return "Marzo"
    elif num == 3:
        return "Abril"
    elif num == 4:
        return "Mayo"
    elif num == 5:
        return "Junio"
    elif num == 6:
        return "Julio"
    elif num == 7:
        return "Agosto"
    elif num == 8:
        return "Septiembre"
    elif num == 9:
        return "Octubre"
    elif num == 10:
        return "Noviembre"
    elif num == 11:
        return "Diciembre"
    else:
        return ""
    
#verificacion de fichero
try:
    with open("finanzas2020[1].csv","r") as f:       
        for line in f:
            value = line.strip().split()
            if(len(value) == 12):
                Enero.append(value[0])
                Febrero.append(value[1])
                Marzo.append(value[2])
                Abril.append(value[3])
                Mayo.append(value[4])
                Junio.append(value[5])
                Julio.append(value[6])
                Agosto.append(value[7])
                Septiembre.append(value[8])
                Octubre.append(value[9])
                Noviembre.append(value[10])
                Diciembre.append(value[11])
            else:
                print("No contiene 12 columnas")         
except IOError:
    print("No encuentro el fichero o no puedo leerlo")
else:
    print("He leido el fichero")

def Entero(value):
    try:
        return int(value)
    except ValueError:
        return False
    
def comillas(value):
    try:
        if(value == 'bug' or value== 'ups'):
            return False
        else:
            valor = eval(value)
            return valor
    except ValueError:
        return False 
     
def ingresos(mes):
    listSum=0
    length = len(mes)
    for i in range(length):
        if i==0:
            print("El valor del mes: ", mes[i])
        else:    
            try:               
                if (comillas(mes[i])):
                    if(Entero(mes[i])):
                        listSum += int(mes[i])               
                    else:
                        mes[i]=0  
            except IOError:
                print("Error")               
    print("Es: ", listSum)
    return listSum

IngresosTotal = []
IngresosTotal.append(ingresos(Enero))
IngresosTotal.append(ingresos(Febrero))
IngresosTotal.append(ingresos(Marzo))
IngresosTotal.append(ingresos(Abril))
IngresosTotal.append(ingresos(Mayo))
IngresosTotal.append(ingresos(Junio))
IngresosTotal.append(ingresos(Julio))
IngresosTotal.append(ingresos(Agosto))
IngresosTotal.append(ingresos(Septiembre))
IngresosTotal.append(ingresos(Octubre))
IngresosTotal.append(ingresos(Noviembre))
IngresosTotal.append(ingresos(Diciembre))


print("El mes con menos ingresos es: ", meses(IngresosTotal.index(min(IngresosTotal))), "con el valor de: ",min(IngresosTotal))
print("El mes con mas ingresos es: ", meses(IngresosTotal.index(max(IngresosTotal))), "con el valor de: ",max(IngresosTotal))

Gastos = 0
IngresosTotales = 0
for i in IngresosTotal:
    if i < 0:
        Gastos = i + Gastos
        i+=i
    else:
        IngresosTotales = i + IngresosTotales
    
print("Los ingresos han sido de: ", IngresosTotales)

print("Los gastos han sido de: ", Gastos)

print("La media anual de Gastos ha sido: ", Gastos/12)

