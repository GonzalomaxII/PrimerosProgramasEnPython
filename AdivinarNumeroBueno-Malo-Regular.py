#Gonzalo Ortiz 1°3°
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def click_num():
 n=int(0)
 for i in range(4):
     n=str(random.randint(0,9))
     while(num_esta(num_gen,n)):
         n=str(random.randint(0,9))
     num_gen.append(n)
 intentos.append(0)
 print(num_gen)
 btn_gen_num['state'] = 'disabled'
 return(num_gen, intentos)
     
def num_esta(num,n):
 cr7=int(0)
 while(cr7<len(num)):
     if(str(n)==num[cr7]):
         return(True)
     cr7+=1
 return(False)

def verificar_jugada():
    if(len(ent_num.get())!=4):
        messagebox.showinfo(title="ERROR",message="Ingresa un numero hasta 4 digitos")
        ent_num.delete(0,END)
        ent_num.focus_set()
        return
    adivinar_num(num_gen)
    b=int(0)
    m=int(0)
    r=int(0)
    for i in range(4):
        j=int(0)
        while(num_gen[i]!=ent_num.get()[j] and j<3):
            j+=1
        if(num_gen[i]==ent_num.get()[j]):
            if(i == j):
                b+=1
            else:
                r+=1
        else:
            m+=1
    txt.insert(END,str(b)+'b'+str(m)+'m'+str(r)+'r\n')
    ent_num.delete(0,END)
    ent_num.focus_set()
    
def adivinar_num(num_gen):
    c=int(0)
    for i in range(len(num_gen)):
        if(num_gen[i]==ent_num.get()[i]):
                   c+=1
    if(c==4):
        messagebox.showinfo(title="Ganaste",message="lograste acertar el numero"+str(num_gen))
        intentos[0]=0
        num_gen=[]
        btn_gen_num['state'] = 'normal'

    if(c!=4):
        if(intentos[0]==10):
            messagebox.showinfo(title="Perdiste",message="no lograste acertar el numero"+str(num_gen))
            intentos[0]=0
            num_gen=[]
            btn_gen_num['state'] = 'normal'
        
        else:
            intentos[0]+=1
            print('sumo un intento')
            
    
    return(intentos, num_gen)
             
#programa principal
num_gen=[]
intentos=[]
ventana=Tk()
ventana.geometry('600x400')
ventana.title('buenos-malos-regulares')
btn_gen_num=Button(text='generar num',command=click_num)
ent_num=Entry(width=40)
btn_jugar=Button(text='JUGAR',command=verificar_jugada)
btn_gen_num.pack(side=TOP,fill=X)
ent_num.pack(anchor=N,side=LEFT,fill=X)
btn_jugar.pack(anchor=N,side=RIGHT,fill=X)
txt=Text()
txt.pack()

ventana.mainloop()


