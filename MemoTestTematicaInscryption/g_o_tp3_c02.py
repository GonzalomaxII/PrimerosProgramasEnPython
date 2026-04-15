#Gonzalo Ortiz 1°3°csc
import random, time
from tkinter import PhotoImage
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial
    
def crear_matriz(fi, co):
    m=[None]*co
    for i in range(co):
        m[i]=[None]*fi
    return(m)

def generar_ind_image(m, fi, co):
    for columnas in range(co):
        for filas in range(fi):
            n=random.randint(1,16)
            while(num_matriz(n, m, co, fi)):
                n=random.randint(1,16)
            m[columnas][filas]=n
    return(m)

def num_matriz(n, m, co, fi):
    cont=int(0)
    for columnas in range(co):
        for filas in range(fi):
            if(m[columnas][filas]==n):
                for c in range(co):
                    for f in range(fi):
                        if(m[c][f]==n):
                            cont+=1
                if(cont>=2):
                    return(True)
    return(False)

def agregar_images():
    file_name='ins_card'
    file_ext='.png'
    i=int(0)
    for i in range(17):
        images.append(PhotoImage(file=file_name+str(i)+file_ext))
    return(images)

def cartas_botones(m, mb, co, fi, v_img):
    for i in range(co):
        for j in range(fi):
            mb[i][j]=Button(memo_test, image=v_img[m[i][j]], background='black', command=partial(click, m[i][j], i, j, images))
            mb[i][j].place(x=(i*100), y=(j*150), height=150, width=100)
    return(mb)

def click(m, i, j, v_img):
    if(cond[0]==1):
        cond[0]=2
        if(mat_bot[i][j]!=mat_bot[c[0]][f[0]]):
            usrJugada.set(usrJugada.get()+str(m))
            jugadaNueva=str(usrJugada.get())
            usrJugada.set(value="")
            mat_bot[i][j].configure(image=v_img[m], background='black')
            memo_test.update()
            print(":)", str(m))
            puntuacion[0]+=1
            if(comprobar_cartas(jugadaNueva, jugadaAnterior)):
                mat_bot[i][j]['state']='disabled'
                memo_test.update()
                mat_bot[c[0]][f[0]]['state']='disabled'
                memo_test.update()
                com_punt[0]+=2
                if(com_punt[0]==32):
                    puntuacion_final(puntuacion, com_punt)
            else:
                time.sleep(.5)
                mat_bot[i][j].configure(image=v_img[0], background='black')
                memo_test.update()
                mat_bot[c[0]][f[0]].configure(image=v_img[0], background='black')
                memo_test.update()
            cond[0]=1
    if(cond[0]==0):
        usrJugada.set(usrJugada.get()+str(m))
        jugadaAnterior[0]=str(usrJugada.get())
        usrJugada.set(value="")
        mat_bot[i][j].configure(image=v_img[m], background='black')
        memo_test.update()
        print(":)", str(m))
        c[0]=i
        f[0]=j
        puntuacion[0]+=1
        cond[0]=1
    else:
        cond[0]=0
def comprobar_cartas(jugadaNueva, jugadaAnterior):
    if(jugadaNueva==jugadaAnterior[0]):
        return(True)
    else:
        return(False)

def puntuacion_final(punt, com_punt):
    pun_fin=float(punt[0]/com_punt[0])
    promedio=int(100//pun_fin)
    print(promedio)
    messagebox.showinfo(title="<Puntaje final>", message="tu puntaje final es:"+str(promedio)+"/"+"100")
    
def iniciar_memo(mb, v_img):
    time.sleep(5)
    for i in range(co):
        for j in range(fi):
            time.sleep(0.02)
            mb[i][j].configure(image=v_img[0], background='black')
            memo_test.update()
    return(mb)
            
#programa principal:
memo_test=Tk()
memo_test.geometry('800x600')
memo_test.title('Memo_Test')
co=int(8)
fi=int(4)
usrJugada = StringVar(value="")
images=[]
images=agregar_images()
matriz=crear_matriz(fi, co)
cond=[0]
c=[0]
f=[0]
jugadaAnterior=[0]
puntuacion=[0]
com_punt=[0]
mat_bot=crear_matriz(fi, co)
generar_ind_image(matriz, fi, co)
print(matriz)
mat_bot=cartas_botones(matriz, mat_bot, co, fi, images)
memo_test.update()
mat_bot=iniciar_memo(mat_bot, images)


