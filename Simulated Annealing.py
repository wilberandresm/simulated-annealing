import template as t
import numpy as np
from math import exp
import random as r
import networkx as nx
import matplotlib.pyplot as plt

def ObjetiveFunction(pos,matriz):
    z = 0
    for i in range(len(pos)-1):
        z += matriz[pos[i]][pos[i+1]]#sumatoria de dintancia anterior con la siguiente
    return z

def DisruptMatrix(x):
    x1 = r.randint(1,len(x)-2)
    x2 = r.randint(1,len(x)-2)
    while(x2==x1):
        x2 = r.randint(1,len(x)-2)
    aux = x[x1]
    x[x1] = x[x2]
    x[x2] = aux
    return x

if __name__ == "__main__":
    coor = t.distancesFromCoords()#obtención de las distancias para establecer coordenadas
    x = [] #posicion
    pos = r.randint(0,len(coor)-1)
    x.append(pos)#posición random inicial
    for i in range(len(coor)):
        if(i!=pos):
            x.append(i)
    x.append(pos)
    T = 1000 #se asigna un valor T aleatorio
    alpha = 0.98 #alpha cualquiera 
    ite=0
    while(T>0.1): #cuando sea menor 0.1 significa que el algoritmo finalizó
        ite+=1
        z = ObjetiveFunction(x,coor) #distancia
        new_x = DisruptMatrix(x[:]) #nueva posicion
        new_z = ObjetiveFunction(new_x,coor)
        if(new_z<z):
            x = new_x
            T *= alpha

        else:
            n = r.random()# generacion de numero random aleatorio 
            p = exp((-(new_z - z)/T))
            if(n < p):
                x = new_x
                T *= alpha
        print("La temperatura es: ", T, "iteracion: ", ite)
        print("\n")

    print("Route:",x)
    print("Final distance:",new_z)

    
