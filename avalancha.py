# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:30:35 2020

@author: Telma
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib . animation as animation

def crear_tablero(n):
    nr=n+2
    t=np . repeat (0, nr*nr) . reshape(nr,nr)
    for i in range(nr):
        t[0,i]=-1
        t[i,0]=-1
        t[i,nr-1]=-1
        t[nr-1,i]=-1
    return t
def es_borde(tablero , coord):
    return tablero[coord]==-1
def tirar_copo(tablero , coord):
    if es_borde(tablero,coord)==False:
        tablero[coord]+=1
def vecinos_de(tablero , coord):
    lista_vecinos=[]
    if not es_borde(tablero , coord):
        vecino1=(coord[0]+1 , coord[1])
        if not es_borde(tablero , vecino1):
            lista_vecinos.append(vecino1)
        vecino2=(coord[0] , coord[1]+1)
        if not es_borde(tablero , vecino2):
            lista_vecinos.append(vecino2)
        vecino3=(coord[0]-1 , coord[1])
        if not es_borde(tablero , vecino3):
            lista_vecinos.append(vecino3)
        vecino4=(coord[0] , coord[1]-1)
        if not es_borde(tablero , vecino4):
            lista_vecinos.append(vecino4)
    return lista_vecinos
def desbordar_pos(tablero , coord):
    if tablero[coord]>=4:
        tablero[coord]-=4
        vecinos=vecinos_de(tablero , coord)
        for i in range(len(vecinos)):
            tablero[vecinos[i]]+=1
def desbordar_arenero(tablero):
    cantidad_filas = tablero . shape [0]
    cantidad_columnas = tablero . shape [1]
    for i in range (1 , cantidad_filas - 1) :
        for j in range (1 , cantidad_columnas - 1) :
            desbordar_pos(tablero , (i,j))
def hay_que_desbordar(tablero):
    cantidad_filas = tablero . shape [0]
    cantidad_columnas = tablero . shape [1]
    for i in range (1 , cantidad_filas - 1) :
        for j in range (1 , cantidad_columnas - 1) :
            if tablero[(i,j)]>=4:
                return tablero[(i,j)]>=4
    return False
def estabilizar(tablero):
    while hay_que_desbordar(tablero):
        desbordar_arenero(tablero)
def paso(tablero):
    x=int(t.shape[0]/2)
    y=int(t.shape[0]/2)
    tirar_copo(tablero , (x,y))
    estabilizar(tablero)
n =5
cant_iteraciones = 100
t = crear_tablero ( n )
ims = []
fig = plt . figure ()
for i in range ( cant_iteraciones ) :
    paso ( t )
    im = plt . imshow (t , animated = True )
    ims . append ([ im ])
ani = animation . ArtistAnimation ( fig , ims , interval =50 , blit = True ,
repeat_delay =400)
print (" Listo para guardar animacion ")
ani . save ("dynamic_images .gif")
plt . show ()
def aleatorio(n):
    asd=random.randint(1,n)
    return asd
def generar_tablero_aleatorio(n , cant_granitos):
    t=crear_tablero(n)
    for i in range(cant_granitos):
        coor1=aleatorio(n)
        coor2=aleatorio(n)
        tirar_copo(t , (coor1 , coor2))
    return(t)
x=generar_tablero_aleatorio(5,10)
print(x)


    
    

    

       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        





