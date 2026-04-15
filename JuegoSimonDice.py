#Gonzalo Ortiz 1°3°
import random
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial

def click(index):
    usrJugada.set(usrJugada.get()+str(index))
    print(":)", str(index))

def crear_botones(c):
    vb=[]
    for i in range(c):
        vb.append(Button(simon, text="", activebackground=vec_coloreado[i], command=partial(click, i)))
        vb[i].place(x=(i*100), y=50, height=100, width=100)
    return(vb)
    
def maquina():
    d=int(0)
    maq_jugadas.append(int(random.randint(0,3)))
    print(maq_jugadas)
    for j in maq_jugadas:
        if(j>3):
            d=1
        elif(j>6):
            d=2
        elif(j>9):
            d=3
    for i in maq_jugadas:
        vec_botones[i].configure(text=vec_coloreado[i], background=vec_coloreado[i])
        time.sleep(dificultad[d])
        simon.update()
        vec_botones[i].configure(text="", background=vec_coloreado[4])
        time.sleep(dificultad[d])
        simon.update()

def pasarM(MJ):
    strMJ=""
    for i in MJ:
        strMJ+=str(i)
    return strMJ

def jugada_correcta():
    i=int(0)
    for i in range(4):
        vec_botones[i].configure(text=vec_coloreado[i], background=vec_coloreado[i])
        time.sleep(0.1)
        simon.update()
    for j in range(4):
        vec_botones[j].configure(text="", background=vec_coloreado[4])
        time.sleep(0.1)
        simon.update()
    
def comprobar():
    jugadaMaquina=pasarM(maq_jugadas)
    jugadaJugador=str(usrJugada.get())
    print(jugadaMaquina, " - ", jugadaJugador)

    if(jugadaMaquina!=jugadaJugador):
        messagebox.showerror("PERDISTE", "GAME OVER")
        maq_jugadas.clear()
        usrJugada.set(value="")
        score[0]=0
        lbl_txt.configure(text=str(score[0]))
        simon.update
    else:
        jugada_correcta()
        usrJugada.set(value="")
        score[0]+=1
        lbl_txt.configure(text=str(score[0]))
        simon.update()
           
#Ṕrograma principal
simon=Tk()
score=[0]
vec_coloreado=['yellow', 'blue', 'red', 'green', 'lightgrey']
simon.geometry('400x225')
simon.title('Simon DICE')
maq_jugadas=[]
dificultad=[0.30, 0.20, 0.10, 0.05]
vec_botones=crear_botones(4)
usrJugada = StringVar(value="")
lbl_Jugadas = ttk.Label(simon, textvariable = usrJugada, background="orange")
lbl_Jugadas.place(x=0, y=20, height=40, width=400)
lbl_txt = Label(text=str(score), borderwidth=1, relief='solid', height=40)
lbl_txt.place(x=150, y=185, height=40, width=100)
btn_comenzar=Button(text='comenzar',command=maquina)
btn_comenzar.pack(anchor=N, fill=X, expand=True)
btn_comprobar=Button(text='comprobar',command=comprobar)
btn_comprobar.place(x=0, y=150, height=40, width=400)



simon.mainloop()
