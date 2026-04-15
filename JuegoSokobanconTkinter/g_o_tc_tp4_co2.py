#Gonzalo Ortiz 1°3°CSC

#https://www.askpython.com/python-modules/tkinter/bind-in-tkinter

import time
from tkinter import PhotoImage
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial

def crear_matriz():
    m=[None]*10
    for i in range(10):
        m[i]=[None]*10
    return(m)

def agregar_images():
    file_name='maze_'
    file_ext='.png'
    i=int(0)
    for i in range(6):
        images.append(PhotoImage(file=file_name+str(i)+file_ext))
    return(images)

def cartas_botones(m, mb, v_img):
    for i in range(10):
        for j in range(10):
            if(m[0][i][j]==5):
                pos_jug[0]=i
                pos_jug[1]=j
                print(pos_jug)
            elif(m[0][i][j]==4):
                cant_dest[0]+=1
            mb[i][j]=ttk.Label(maze, image=v_img[m[0][i][j]], background='black')
            mb[i][j].place(x=(i*64), y=(j*64), height=64, width=64)
    print('cantidad de destinos:',cant_dest[0])
    return(mb)

def obtener_pos(event):
    tecla=event.keysym
    cond=[None, None] #para determinar el sentido del movimiento
    if(tecla=='Left'):
        cond[1]=-1
    elif(tecla=='Up'):
        cond[0]=-1
    elif(tecla== 'Down'):
        cond[0]=+1
    elif(tecla=='Right'):
        cond[1]=+1
    mover_personaje(cond, matriz, mat_bot, images, pos_jug)
    
def mover_personaje(cond, m, mb, v_img, p_j):
    co=p_j[0]
    fi=p_j[1]        
    if(cond[0]==-1 or cond[0]==1 and fi>0):
        nuevo_fi=fi+cond[0]
        if(matriz[0][co][nuevo_fi]!=1 and matriz[0][co][nuevo_fi]!=2):
            aux=nuevo_fi+cond[0]
            if(matriz[0][co][nuevo_fi]==3):
                if(matriz[0][co][aux]==0 or matriz[0][co][aux]==4):
                    if(matriz[1][co][aux]==4):
                        mb[co][aux].configure(image=v_img[2])
                        m[0][co][aux]=2
                        cant_dest[0]-=1
                        print(cant_dest)
                    else:
                        mb[co][aux].configure(image=v_img[3])
                        m[0][co][aux]=3
                    mb[co][nuevo_fi].configure(image=v_img[5])
                    m[0][co][nuevo_fi]=5
                    mb[co][fi].configure(image=v_img[0])
                    m[0][co][fi]=0
                    maze.update()
                    p_j[1]=nuevo_fi        
            elif(matriz[1][co][fi]==4):
                mb[co][nuevo_fi].configure(image=v_img[5])
                m[0][co][nuevo_fi]=5
                mb[co][fi].configure(image=v_img[4])
                m[0][co][fi]=4
                maze.update()
                p_j[1]=nuevo_fi   
            else:
                mb[co][nuevo_fi].configure(image=v_img[5])
                m[0][co][nuevo_fi]=5
                mb[co][fi].configure(image=v_img[0])
                m[0][co][fi]=0
                maze.update()
                p_j[1]=nuevo_fi
                 
    if(cond[1]== -1 or cond[1] == 1 and co>0):
        nuevo_co=co+cond[1]
        if(matriz[0][nuevo_co][fi]!=1 and matriz[0][nuevo_co][fi]!=2):
            aux=nuevo_co+cond[1]
            if(matriz[0][nuevo_co][fi]==3):
                if(matriz[0][aux][fi]==0 or matriz[0][aux][fi]==4):
                    if(matriz[1][aux][fi]==4):
                        mb[aux][fi].configure(image=v_img[2])
                        m[0][aux][fi]=2
                        cant_dest[0]-=1
                        print(cant_dest)
                    else:
                        mb[aux][fi].configure(image=v_img[3])
                        m[0][aux][fi]=3
                    mb[nuevo_co][fi].configure(image=v_img[5])
                    m[0][nuevo_co][fi]=5
                    mb[co][fi].configure(image=v_img[0])
                    m[0][co][fi]=0
                    maze.update()
                    p_j[0] = nuevo_co       
            elif(matriz[1][co][fi]==4):
                mb[nuevo_co][fi].configure(image=v_img[5])
                m[0][nuevo_co][fi]=5
                mb[co][fi].configure(image=v_img[4])
                m[0][co][fi]=0
                maze.update()
                p_j[0]=nuevo_co
            else:
                mb[nuevo_co][fi].configure(image=v_img[5])
                m[0][nuevo_co][fi]=5
                mb[co][fi].configure(image=v_img[0])
                m[0][co][fi]=0
                maze.update()
                p_j[0]=nuevo_co
    if(cant_dest[0]==0):
        messagebox.showinfo(title='Ganaste', message='has entregado todas las cajas a su destino')
        maze.destroy()
#programa principal----------------------------

maze=Tk()
maze.geometry('700x700')
maze.title('Maze')
matriz=[[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 4, 0, 0, 0, 0, 2, 0, 4, 1],
         [1, 2, 2, 1, 3, 0, 0, 3, 0, 1],
         [1, 4, 0, 1, 0, 1, 1, 3, 0, 1],
         [1, 0, 0, 0, 4, 1, 4, 0, 2, 1],
         [1, 0, 3, 1, 0, 3, 0, 3, 0, 1],
         [1, 0, 0, 5, 0, 1, 0, 0, 4, 1],
         [1, 0, 3, 1, 0, 0, 0, 2, 1, 1],
         [1, 4, 3, 0, 0, 0, 0, 0, 4, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                          [1, 4, 0, 0, 0, 0, 2, 0, 4, 1],
                                          [1, 2, 2, 1, 3, 0, 0, 3, 0, 1],
                                          [1, 4, 0, 1, 0, 1, 1, 3, 0, 1],
                                          [1, 0, 0, 0, 4, 1, 4, 0, 2, 1],
                                          [1, 0, 3, 1, 0, 3, 0, 3, 0, 1],
                                          [1, 0, 0, 5, 0, 1, 0, 0, 4, 1],
                                          [1, 0, 3, 1, 0, 0, 0, 2, 1, 1],
                                          [1, 4, 3, 0, 0, 0, 0, 0, 4, 1],
                                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]]
mat_bot=crear_matriz()      
images=[]
images=agregar_images()
pos_jug=[None, None]
cant_dest=[0]
mat_bot=cartas_botones(matriz, mat_bot, images)
maze.bind('<Key>', obtener_pos)

