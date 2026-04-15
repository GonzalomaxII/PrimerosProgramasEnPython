#Gonzalo Ortiz 1°3° CSC
from tkinter import PhotoImage
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial
import tkinter as tk
from tkinter.ttk import Treeview

def verificar_gmail(ema):
    t=int(0)
    if(len(ema)>0):
        for i in range(len(ema)):
            if(t==2):
                if(ema[i]=='.'):
                    t=1
            if(ema[i]=='@'):
                if(i>0 and i<len(ema)-1):
                    if(ema[i+1]!='.' and ema[-1]!='.'):
                        t=2
                    else:
                        messagebox.showinfo(title='ERROR', message="La dirección de correo electrónico no es válida (punto adyacente al '@' o al final).")
                        return(False)
                else:
                    messagebox.showinfo(title='ERROR', message="La dirección de correo electrónico no es válida (falta un carácter antes o después del '@').")
                    return(False)
    if(t==2):
        messagebox.showinfo(title='ERROR', message="La dirección de correo electrónico falta ('.').")
        return(False)
    if(t==1):
        return(True)

def pasar_modificaciones_alu(v_aux, datos, lista):
    alumnos=open('alumnos.dat','r',encoding='utf-8')
    temporal=open('temporal.txt','w',encoding='utf-8')
    aux=''
    x=int(0)
    cond=False
    for linea in alumnos:
        aux=linea[:-1]
        if(cond):
            x+=1
            if(x==6):
                cond=False
                for elemento in datos:
                    temporal.write(elemento.get()+'\n')     
        else:
            if(aux==lista):
                temporal.write(aux+'\n')
                cond=True
            else:
                temporal.write(aux+'\n')       
    temporal.close()
    alumnos.close()
    v_aux.destroy()
    alumnos=open('alumnos.dat','w',encoding='utf-8')
    temporal=open('temporal.txt','r',encoding='utf-8')
    aux=''
    for linea2 in temporal:
        aux=linea2[:-1]
        alumnos.write(aux+'\n')
    alumnos.close()
    temporal.close()
    
def verificar_alu(dni, ape, nom, ema, cur, div, v_aux, cond, lista):
    x=int(0)
    datos=[dni, ape, nom, ema, cur, div]
    dato_g=datos[3].get()
    verificar_gmail(dato_g)
    #---------------
    if(verificar_gmail(dato_g)):
        for dato in datos:
            if(len(dato.get())>0):
                x+=1
    if(x==6):
        if(not cond):
            alumnos=open('alumnos.dat','a',encoding='utf-8')
            id_alumnos=open('id_alumnos.txt','r',encoding='utf-8')
            linea=id_alumnos.readline()[:-1]
            id_alumnos.close()
            alumnos.write(linea+'\n')
            #-------------------------------------
            id_alu=int(linea[1:])
            id_alu+=1
            print(id_alu)
            id_alu='a'+str(id_alu)
            id_alumnos=open('id_alumnos.txt','w',encoding='utf-8')
            id_alumnos.write(id_alu+'\n')
            id_alumnos.close()    
            for dato2 in datos:
                alumnos.write(dato2.get()+'\n')
            alumnos.close()
            v_aux.destroy()
        else:
            pasar_modificaciones_alu(v_aux, datos, lista[0])
            
    else:
        messagebox.showinfo(title='ERROR', message="Faltan datos/correo electrónico incorrecto")
  
def alt_alu(datos):
    v_aux=Toplevel(boletin)
    if not datos:
        cond=False
        v_aux.title('Alta de alumnos')
    else:
        cond=True
        v_aux.title('Modificación de alumnos')
    v_aux.geometry('300x400')
    v_aux.transient(boletin)
    #------------------------------
    ent_dni=Entry(v_aux, width=50)
    ent_ape=Entry(v_aux, width=50)
    ent_nom=Entry(v_aux, width=50)
    ent_ema=Entry(v_aux, width=50)
    ent_dni.place(x=75, y=50, height=25, width=150)
    ent_ape.place(x=75, y=100, height=25, width=200)
    ent_nom.place(x=75, y=150, height=25, width=200)
    ent_ema.place(x=75, y=200, height=25, width=200)
    #------------------------------
    combo_cur = tk.StringVar()
    combo1 = ttk.Combobox(v_aux, textvariable=combo_cur, state='readonly')
    combo1['values'] = ('1' , '2', '3', '4', '5')
    if(cond):
        combo1.set(datos[5])
    combo1.place(x=75, y=250, height=25, width=100)
    combo_div = tk.StringVar()
    combo2 = ttk.Combobox(v_aux, textvariable=combo_div, state='readonly')
    combo2['values'] = ('1' , '2', '3', '4', '5')
    if(cond):
        combo2.set(datos[6])
    combo2.place(x=75, y=300, height=25, width=100)
    if(cond):
        cont_id=Label(v_aux, text=datos[0])
        ent_dni.insert(0, datos[1])
        ent_ape.insert(0, datos[2])
        ent_nom.insert(0, datos[3])
        ent_ema.insert(0, datos[4])
    else:
        id_alumnos=open('id_alumnos.txt','r',encoding='utf-8')
        id_alu=id_alumnos.readline()[:-1]
        id_alumnos.close()
        cont_id=Label(v_aux, text=id_alu)
    cont_id.place(x=55, y=0, height=25, width=100)
    #------------------------------
    lab_id=Label(v_aux, text="id_alum:")
    lab_dni=Label(v_aux, text="DNI:")
    lab_ape=Label(v_aux, text="Apellido:")
    lab_nom=Label(v_aux, text="Nombre:")
    lab_ema=Label(v_aux, text="Email:")
    lab_cur=Label(v_aux, text="Curso:")
    lab_div=Label(v_aux, text="División:")
    lab_id.place(x=0, y=0, height=25, width=75)
    lab_dni.place(x=0, y=50, height=25, width=75)
    lab_ape.place(x=0, y=100, height=25, width=75)
    lab_nom.place(x=0, y=150, height=25, width=75)
    lab_ema.place(x=0, y=200, height=25, width=75)
    lab_cur.place(x=0, y=250, height=25, width=75)
    lab_div.place(x=0, y=300, height=25, width=75)
    #----------
    btn_ver=Button(v_aux, text='Agregar', command=partial(verificar_alu, ent_dni, ent_ape, ent_nom, ent_ema, combo_cur, combo_div, v_aux, cond, datos))
    btn_ver.place(x=0, y=350, height=25, width=300)


def buscar_alu(combo_alumnos, v_aux):
    elegido=combo_alumnos.get()
    alumnos=open('alumnos.dat','r',encoding='utf-8')
    aux=''
    lista=[]
    x=int(0)
    cond=False
    for linea in alumnos:
        aux=linea[:-1]
        if(cond):
            lista.append(aux)
            x+=1
            if(x==6):
                cond=False
                print(lista)
                alt_alu(lista)       
        else:
            if(aux==elegido):
                cond=True
                lista.append(aux)
    alumnos.close()
    v_aux.destroy()
    
def mod_alu():   
    x=int(0)
    alumnos=open('alumnos.dat','r',encoding='utf-8')
    pasar_datos=True
    datos=[]
    primer_linea=alumnos.readline()
    if(primer_linea==''):
        messagebox.showinfo(title='ERROR', message="No hay alumnos ingresados.")
        pasar_datos=False
    else:
        datos.append(primer_linea[:-1])
        while(primer_linea!=''):
            primer_linea=alumnos.readline() 
            x+=1
            if(x==7):
                x=0
                datos.append(primer_linea[:-1])
    alumnos.close()
    if(pasar_datos):
        v_aux=Toplevel(boletin)
        v_aux.title('modificación de alumnos')
        v_aux.geometry('300x200')
        v_aux.transient(boletin)
        lab_lista=Label(v_aux, text="Lista de alumnos para modificar")
        lab_lista.place(x=0, y=0, height=25, width=300)
        combo_alumnos = tk.StringVar()
        combo = ttk.Combobox(v_aux, textvariable=combo_alumnos)
        combo['values'] = datos[:-1]#esto esta puesto porque el if(x==7): para sacar el espacio que añade la ultima iteración del while
        combo.place(x=100, y=50, height=25, width=100)
        btn_ver=Button(v_aux, text='Modificar', command=partial(buscar_alu, combo_alumnos, v_aux))
        btn_ver.place(x=100, y=100, height=25, width=100)
        
def eliminar_alu(combo_alumnos, v_aux):
    elegido=combo_alumnos.get()
    alumnos=open('alumnos.dat','r',encoding='utf-8')
    temporal=open('temporal.txt','w',encoding='utf-8')
    x=int(0)
    aux=''
    cond=True
    for linea in alumnos:
        aux=linea[:-1]
        if(cond):
            if(aux!=elegido):
                temporal.write(aux+'\n')
            else:
                cond=False
        else:
            x+=1
            if(x==6):
                cond=True
    temporal.close()
    alumnos.close()
    alumnos=open('alumnos.dat','w',encoding='utf-8')
    temporal=open('temporal.txt','r',encoding='utf-8')
    aux=''
    for linea2 in temporal:
        aux=linea2[:-1]
        alumnos.write(aux+'\n')
    alumnos.close()
    temporal.close()
    #borrar sus datos de notas
    #------------------------------
    notas=open('notas.dat','r',encoding='utf-8')
    temporal=open('temporal.txt','w',encoding='utf-8')
    x=int(0)
    lista=[]
    for linea3 in notas:
        aux=linea3[:-1]
        lista.append(aux)
        x+=1
        if(x==7):
            x=0
            if(lista[1]!=elegido):
                i=int(0)
                for i in range(len(lista)):
                    temporal.write(lista[i]+'\n')
                lista.clear()
            else:
                lista.clear()
    notas.close()
    temporal.close()
    notas=open('notas.dat','w',encoding='utf-8')
    temporal=open('temporal.txt','r',encoding='utf-8')
    for linea4 in temporal:
        aux=linea4[:-1]
        notas.write(aux+'\n')
    notas.close()
    temporal.close()
    v_aux.destroy()
def baj_alu():
    x=int(0)
    alumnos=open('alumnos.dat','r',encoding='utf-8')
    pasar_datos=True
    datos=[]
    primer_linea=alumnos.readline()
    if(primer_linea==''):
        messagebox.showinfo(title='ERROR', message="No hay alumnos ingresados.")
        pasar_datos=False
    else:
        datos.append(primer_linea[:-1])
        while(primer_linea!=''):
            primer_linea=alumnos.readline() #esto pasa todos los datos del alumno la idea es que solo pase el id para identificarlo
            x+=1
            if(x==7):
                x=0
                datos.append(primer_linea[:-1])       
    alumnos.close()
    if(pasar_datos):
        v_aux=Toplevel(boletin)
        v_aux.title('Baja de alumnos')
        v_aux.geometry('400x200')
        v_aux.transient(boletin)
        lab_lista=Label(v_aux, text="Lista de alumnos para bajas")
        lab_lista.place(x=0, y=0, height=25, width=400)
        combo_alumnos = tk.StringVar()
        combo = ttk.Combobox(v_aux, textvariable=combo_alumnos)
        combo['values'] = datos[:-1]
        combo.place(x=150, y=50, height=25, width=100)
        btn_ver=Button(v_aux, text='Eliminar', command=partial(eliminar_alu, combo_alumnos, v_aux))
        btn_ver.place(x=150, y=100, height=25, width=100)

def list_alu():
    x=int(0)
    alumnos=open('alumnos.dat','r',encoding='utf-8')
    pasar_datos=True
    primer_linea=alumnos.readline()
    if(primer_linea==''):
        messagebox.showinfo(title='ERROR', message="No hay alumnos ingresados.")
        pasar_datos=False
    else:
        while(primer_linea!=''):
            primer_linea=alumnos.readline() 
            x+=1
            if(x==7):
                x=0
    alumnos.close()
    if(pasar_datos):
        v_list = tk.Tk()
        v_list.title("Lista de alumnos")
        vec_head=("ID_Alu", "DNI", "Apellido", "Nombre", "Email", "Curso", "División")
        trv_frame=Frame(v_list)
        trv_frame.pack(pady=10)
        trv_scroll=Scrollbar(trv_frame)
        trv_scroll.pack(side=RIGHT, fill=Y)
        trv_alumnos = Treeview(trv_frame, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", yscrollcommand=trv_scroll.set, selectmode="extended")
        trv_scroll.config(command=trv_alumnos.yview)
        j=int(1)
        for i in vec_head:
            trv_alumnos.heading(j, text=i)
            j+=1
            
        #-----------------
        alumnos=open('alumnos.dat','r',encoding='utf-8')
        aux=''
        lista=[]
        x=int(0)
        cond=False
        for linea in alumnos:
            aux=linea[:-1]
            lista.append(aux)
            x+=1
            if(x==7):
                trv_alumnos.insert("", "end", values=(lista))
                lista.clear()
                x=0
        alumnos.close()
        trv_alumnos.pack()
        trv_alumnos.focus_set()
        v_list.mainloop()
    
def combobox_alum(event):
    elegido=event.widget.get()
    lista=[]
    print("Combobox de Alumnos - Elemento seleccionado:", elegido)
    if(elegido=='alum_Altas'):
        alt_alu(lista)
    elif(elegido=='alum_Bajas'):
        baj_alu()
    elif(elegido=='alum_Modificar'):
        mod_alu()
    else:
        list_alu()
#acaba alumnos
#--------------------------------------------------------------------------------------------------------------------
#empieza materias
def pasar_modificaciones_mat(v_aux, datos, lista):
    materias=open('materias.dat','r',encoding='utf-8')
    temporal=open('temporal.txt','w',encoding='utf-8')
    aux=''
    x=int(0)
    cond=False
    for linea in materias:
        aux=linea[:-1]
        if(cond):
            x+=1
            if(x==2):
                cond=False
                for elemento in datos:
                    temporal.write(elemento.get()+'\n')     
        else:
            if(aux==lista):
                temporal.write(aux+'\n')
                cond=True
            else:
                temporal.write(aux+'\n')       
    temporal.close()
    materias.close()
    v_aux.destroy()
    materias=open('materias.dat','w',encoding='utf-8')
    temporal=open('temporal.txt','r',encoding='utf-8')
    aux=''
    for linea2 in temporal:
        aux=linea2[:-1]
        materias.write(aux+'\n')
    materias.close()
    temporal.close()
    
def verificar_mat(mat, cur, v_aux, cond, lista):
    x=int(0)
    datos=[mat, cur]
    #---------------
    for dato in datos:
        if(len(dato.get())>0):
            x+=1
    if(x==2):
        if(not cond):
            materias=open('materias.dat','a',encoding='utf-8')
            id_materias=open('id_materias.txt','r',encoding='utf-8')
            linea=id_materias.readline()[:-1]
            id_materias.close()
            materias.write(linea+'\n')
            #-------------------------------------
            id_mat=int(linea[1:])
            id_mat+=1
            print(id_mat)
            id_mat='m'+str(id_mat)
            id_materias=open('id_materias.txt','w',encoding='utf-8')
            id_materias.write(id_mat+'\n')
            id_materias.close()    
            for dato2 in datos:
                materias.write(dato2.get()+'\n')
            materias.close()
            v_aux.destroy()
        else:
            pasar_modificaciones_mat(v_aux, datos, lista[0])   
    else:
        messagebox.showinfo(title='ERROR', message="Faltan datos.")
        
def alt_mat(lista):
    v_aux=Toplevel(boletin)
    if not lista:
        cond=False
        v_aux.title('Alta de Materias')
    else:
        cond=True
        v_aux.title('Modificación de Materias')
    v_aux.geometry('200x200')
    v_aux.transient(boletin)
    #------------------------------
    ent_mat=Entry(v_aux, width=50)
    ent_mat.place(x=100, y=50, height=50, width=100)
    #------------------------------
    combo_cur = tk.StringVar()
    combo1 = ttk.Combobox(v_aux, textvariable=combo_cur, state='readonly')
    combo1['values'] = ('1' , '2', '3', '4', '5')
    if(cond):
        combo1.set(lista[2])
        cont_id=Label(v_aux, text=lista[0])
        ent_mat.insert(0, lista[1])
    else:
        id_materias=open('id_materias.txt','r',encoding='utf-8')
        id_mat=id_materias.readline()[:-1]
        id_materias.close()
        cont_id=Label(v_aux, text=id_mat)
    combo1.place(x=100, y=100, height=50, width=50)
    cont_id.place(x=100, y=0, height=50, width=100)
    #------------------------------
    lab_id=Label(v_aux, text="id_mat:")
    lab_mat=Label(v_aux, text="Materias:")
    lab_cur=Label(v_aux, text="Curso:")
    lab_id.place(x=0, y=0, height=50, width=100)
    lab_mat.place(x=0, y=50, height=50, width=100)
    lab_cur.place(x=0, y=100, height=50, width=100)
    #----------
    btn_ver=Button(v_aux, text='agregar', command=partial(verificar_mat, ent_mat, combo_cur, v_aux, cond, lista))
    btn_ver.place(x=0, y=150, height=50, width=200)
    
def eliminar_mat(combo_materias, v_aux):
    elegido=combo_materias.get()
    materias=open('materias.dat','r',encoding='utf-8')
    temporal=open('temporal.txt','w',encoding='utf-8')
    aux=''
    x=int(0)
    cond=True
    for linea in materias:
        aux=linea[:-1]
        if(cond):
            if(aux!=elegido):
                temporal.write(aux+'\n')
            else:
                cond=False
        else:
            x+=1
            if(x==2):
                cond=True
    temporal.close()
    materias.close()
    materias=open('materias.dat','w',encoding='utf-8')
    temporal=open('temporal.txt','r',encoding='utf-8')
    aux=''
    for linea2 in temporal:
        aux=linea2[:-1]
        materias.write(aux+'\n')
    materias.close()
    temporal.close()
    v_aux.destroy()
    #borrar las notas de la materia
    #---------------------------------------------------
    notas=open('notas.dat','r',encoding='utf-8')
    temporal=open('temporal.txt','w',encoding='utf-8')
    x=int(0)
    lista=[]
    for linea3 in notas:
        aux=linea3[:-1]
        lista.append(aux)
        x+=1
        if(x==7):
            x=0
            if(lista[2]!=elegido):
                i=int(0)
                for i in range(len(lista)):
                    temporal.write(lista[i]+'\n')
                lista.clear()
            else:
                lista.clear()
    notas.close()
    temporal.close()
    notas=open('notas.dat','w',encoding='utf-8')
    temporal=open('temporal.txt','r',encoding='utf-8')
    for linea4 in temporal:
        aux=linea4[:-1]
        notas.write(aux+'\n')
    notas.close()
    temporal.close()
    v_aux.destroy()
    
def baj_mat():
    x=int(0)
    materias=open('materias.dat','r',encoding='utf-8')
    pasar_datos=True
    datos=[]
    primer_linea=materias.readline()
    if(primer_linea==''):
        messagebox.showinfo(title='ERROR', message="No hay materias ingresadas.")
        pasar_datos=False
    else:
        datos.append(primer_linea[:-1])
        while(primer_linea!=''):
            primer_linea=materias.readline() #esto pasa todos los datos del alumno la idea es que solo pase el id para identificarlo
            x+=1
            if(x==3):
                x=0
                datos.append(primer_linea[:-1])       
    materias.close()
    if(pasar_datos):
        v_aux=Toplevel(boletin)
        v_aux.title('Baja de Materias')
        v_aux.geometry('400x200')
        v_aux.transient(boletin)
        lab_lista=Label(v_aux, text="Lista de alumnos para bajas")
        lab_lista.place(x=0, y=0, height=25, width=400)
        combo_materias = tk.StringVar()
        combo = ttk.Combobox(v_aux, textvariable=combo_materias)
        combo['values'] = datos[:-1]
        combo.place(x=150, y=50, height=25, width=100)
        btn_ver=Button(v_aux, text='Eliminar', command=partial(eliminar_mat, combo_materias, v_aux))
        btn_ver.place(x=150, y=100, height=25, width=100)
        
def buscar_mat(combo_materias, v_aux):
    elegido=combo_materias.get()
    materias=open('materias.dat','r',encoding='utf-8')
    aux=''
    lista=[]
    x=int(0)
    cond=False
    for linea in materias:
        aux=linea[:-1]
        if(cond):
            lista.append(aux)
            x+=1
            if(x==2):
                cond=False
                print(lista)
                alt_mat(lista)       
        else:
            if(aux==elegido):
                cond=True
                lista.append(aux)
    materias.close()
    v_aux.destroy()

def mod_mat():
    x=int(0)
    materias=open('materias.dat','r',encoding='utf-8')
    pasar_datos=True
    datos=[]
    primer_linea=materias.readline()
    if(primer_linea==''):
        messagebox.showinfo(title='ERROR', message="No hay materias ingresadas.")
        pasar_datos=False
    else:
        datos.append(primer_linea[:-1])
        while(primer_linea!=''):
            primer_linea=materias.readline() #esto pasa todos los datos del alumno la idea es que solo pase el id para identificarlo
            x+=1
            if(x==3):
                x=0
                datos.append(primer_linea[:-1])       
    materias.close()
    if(pasar_datos):
        v_aux=Toplevel(boletin)
        v_aux.title('modificación de materias')
        v_aux.geometry('300x200')
        v_aux.transient(boletin)
        lab_lista=Label(v_aux, text="Lista de materias para modificar")
        lab_lista.place(x=0, y=0, height=25, width=300)
        combo_materias = tk.StringVar()
        combo = ttk.Combobox(v_aux, textvariable=combo_materias)
        combo['values'] = datos[:-1]
        combo.place(x=100, y=50, height=25, width=100)
        btn_ver=Button(v_aux, text='Modificar', command=partial(buscar_mat, combo_materias, v_aux))
        btn_ver.place(x=100, y=100, height=25, width=100)

def list_mat():
    x=int(0)
    materias=open('materias.dat','r',encoding='utf-8')
    pasar_datos=True
    primer_linea=materias.readline()
    if(primer_linea==''):
        messagebox.showinfo(title='ERROR', message="No hay materias ingresadas.")
        pasar_datos=False
    else:
        while(primer_linea!=''):
            primer_linea=materias.readline() 
            x+=1
            if(x==3):
                x=0
    materias.close()
    if(pasar_datos):
        v_list = tk.Tk()
        v_list.title("Lista de materias")
        vec_head=("ID_mat", "Materia", "Curso")
        trv_frame= Frame(v_list)
        trv_frame.pack(pady=10)
        trv_scroll=Scrollbar(trv_frame)
        trv_scroll.pack(side=RIGHT, fill=Y)
        trv_materias = Treeview(trv_frame, columns=(1, 2, 3), show="headings", yscrollcommand=trv_scroll.set, selectmode="extended")
        trv_scroll.config(command=trv_materias.yview)
        j=int(1)
        for i in vec_head:
            trv_materias.heading(j, text=i)
            j+=1
        #-----------------
        materias=open('materias.dat','r',encoding='utf-8')
        aux=''
        lista=[]
        x=int(0)
        cond=False
        for linea in materias:
            aux=linea[:-1]
            lista.append(aux)
            x+=1
            if(x==3):
                trv_materias.insert("", "end", values=(lista))
                lista.clear()
                x=0
        materias.close()
        trv_materias.pack()
        trv_materias.focus_set()
        v_list.mainloop()
        
def combobox_mate(event):
    elegido=event.widget.get()
    lista=[]
    print("Combobox de Materias - Elemento seleccionado:", elegido)
    if(elegido=='mate_Altas'):
        alt_mat(lista)
    elif(elegido=='mate_Bajas'):
        baj_mat()
    elif(elegido=='mate_Modificar'):
        mod_mat()
    else:
        list_mat()
        
#acaba materias
#--------------------------------------------------------------------------------------------------------------------
#empieza notas
def pasar_modificaciones_not(v_aux, datos, lista):
    notas=open('notas.dat','r',encoding='utf-8')
    temporal=open('temporal.txt','w',encoding='utf-8')
    aux=''
    x=int(0)
    cond=False
    for linea in notas:
        aux=linea[:-1]
        if(cond):
            x+=1
            if(x==6):
                cond=False
                for elemento in datos:
                    temporal.write(elemento.get()+'\n')     
        else:
            if(aux==lista):
                temporal.write(aux+'\n')
                cond=True
            else:
                temporal.write(aux+'\n')       
    temporal.close()
    notas.close()
    v_aux.destroy()
    notas=open('notas.dat','w',encoding='utf-8')
    temporal=open('temporal.txt','r',encoding='utf-8')
    aux=''
    for linea2 in temporal:
        aux=linea2[:-1]
        notas.write(aux+'\n')
    notas.close()
    temporal.close()
    
def verificar_not(not1, not2, not3, not4, alu, mat, v_aux, cond, lista):
    x=int(0)
    datos=[alu, mat, not1, not2, not3, not4]
    for dato in datos:
        if(len(dato.get())>0):
            x+=1
    if(x==6):
        if(not cond):
            notas=open('notas.dat','a',encoding='utf-8')
            id_notas=open('id_notas.txt','r',encoding='utf-8')
            linea=id_notas.readline()[:-1]
            id_notas.close()
            notas.write(linea+'\n')
            #-------------------------------------
            id_not=int(linea[1:])
            id_not+=1
            print(id_not)
            id_not='n'+str(id_not)
            id_notas=open('id_notas.txt','w',encoding='utf-8')
            id_notas.write(id_not+'\n')
            id_notas.close()    
            for dato2 in datos:
                notas.write(dato2.get()+'\n')
            notas.close()
            v_aux.destroy()
        else:
            pasar_modificaciones_not(v_aux, datos, lista[0])
            
    else:
        messagebox.showinfo(title='ERROR', message="Faltan datos.")
        
def alt_not(lista):
    x=int(0)
    alumnos=open('alumnos.dat','r',encoding='utf-8')
    list_alu=[]
    primer_linea=alumnos.readline()
    if(primer_linea==''):
        id_alumnos=open('id_alumnos.txt','r',encoding='utf-8')
        primer_linea=id_alumnos.readline()[:-1]
        list_alu.append(primer_linea)
        id_alumnos.close()
    else:
        list_alu.append(primer_linea[:-1])
        while(primer_linea!=''):
            primer_linea=alumnos.readline() #esto pasa todos los datos del alumno la idea es que solo pase el id para identificarlo
            x+=1
            if(x==7):
                x=0
                list_alu.append(primer_linea[:-1])
        list_alu=list_alu[:-1]
    alumnos.close()
    #--------------------------------------------------
    x=int(0)
    materias=open('materias.dat','r',encoding='utf-8')
    list_mat=[]
    primer_linea=materias.readline()
    if(primer_linea==''):
        id_materias=open('id_materias.txt','r',encoding='utf-8')
        primer_linea=id_materias.readline()[:-1]
        list_mat.append(primer_linea)
        id_materias.close()
    else:
        list_mat.append(primer_linea[:-1])
        while(primer_linea!=''):
            primer_linea=materias.readline() #esto pasa todos los datos del alumno la idea es que solo pase el id para identificarlo
            x+=1
            if(x==3):
                x=0
                list_mat.append(primer_linea[:-1])
        list_mat=list_mat[:-1]
    materias.close()
    #--------------------------------------------------
    v_aux=Toplevel(boletin)
    if not lista:
        cond=False
        v_aux.title('Alta de Notas')
    else:
        cond=True
        v_aux.title('Modificación de Notas')
    v_aux.geometry('200x400')
    lab_id_not=Label(v_aux, text="id_notas")
    lab_id_not.place(x=0, y=0, height=25, width=100)
    lab_id_alu=Label(v_aux, text="id_alumnos")
    lab_id_alu.place(x=0, y=50, height=25, width=100)
    lab_id_mat=Label(v_aux, text="id_materias")
    lab_id_mat.place(x=0, y=100, height=25, width=100)
    lab_not1=Label(v_aux, text="nota1")
    lab_not1.place(x=0, y=150, height=25, width=100)
    lab_not2=Label(v_aux, text="nota2")
    lab_not2.place(x=0, y=200, height=25, width=100)
    lab_not3=Label(v_aux, text="nota3")
    lab_not3.place(x=0, y=250, height=25, width=100)
    lab_not4=Label(v_aux, text="nota4")
    lab_not4.place(x=0, y=300, height=25, width=100)
    #--------------
    ent_not1=Entry(v_aux, width=50)
    ent_not2=Entry(v_aux, width=50)
    ent_not3=Entry(v_aux, width=50)
    ent_not4=Entry(v_aux, width=50)
    ent_not1.place(x=100, y=150, height=25, width=100)
    ent_not2.place(x=100, y=200, height=25, width=100)
    ent_not3.place(x=100, y=250, height=25, width=100)
    ent_not4.place(x=100, y=300, height=25, width=100)
    #--------------
    if(cond):
        cont_id=Label(v_aux, text=lista[0])
        ent_not1.insert(0, lista[3])
        ent_not2.insert(0, lista[4])
        ent_not3.insert(0, lista[5])
        ent_not4.insert(0, lista[6])
    else:
        id_notas=open('id_notas.txt','r',encoding='utf-8')
        id_not=id_notas.readline()[:-1]
        id_notas.close()
        cont_id=Label(v_aux, text=id_not)
    cont_id.place(x=100, y=0, height=25, width=100)
    #-----------------------------
    combo_alumnos = tk.StringVar()
    combo1 = ttk.Combobox(v_aux, textvariable=combo_alumnos, state='readonly')
    combo1['values'] = list_alu
    if(cond):
        combo1.set(lista[1])
    combo1.place(x=100, y=50, height=25, width=100)
    
    combo_materias = tk.StringVar()
    combo2 = ttk.Combobox(v_aux, textvariable=combo_materias, state='readonly')
    combo2['values'] = list_mat
    if(cond):
        combo2.set(lista[2])
    combo2.place(x=100, y=100, height=25, width=100)
    #------------------------------------------------------
    btn_ver=Button(v_aux, text='Agregar', command=partial(verificar_not, ent_not1, ent_not2, ent_not3, ent_not4, combo_alumnos, combo_materias, v_aux, cond, lista))
    btn_ver.place(x=0, y=350, height=50, width=200)
    v_aux.mainloop()

def eliminar_not(combo_notas, v_aux):
    elegido=combo_notas.get()
    notas=open('notas.dat','r',encoding='utf-8')
    temporal=open('temporal.txt','w',encoding='utf-8')
    x=int(0)
    aux=''
    cond=True
    for linea in notas:
        aux=linea[:-1]
        if(cond):
            if(aux!=elegido):
                temporal.write(aux+'\n')
            else:
                cond=False
        else:
            x+=1
            if(x==6):
                cond=True
    temporal.close()
    notas.close()
    notas=open('notas.dat','w',encoding='utf-8')
    temporal=open('temporal.txt','r',encoding='utf-8')
    aux=''
    for linea2 in temporal:
        aux=linea2[:-1]
        notas.write(aux+'\n')
    notas.close()
    temporal.close()
    v_aux.destroy()
def baj_not():
    x=int(0)
    notas=open('notas.dat','r',encoding='utf-8')
    pasar_datos=True
    datos=[]
    primer_linea=notas.readline()
    if(primer_linea==''):
        messagebox.showinfo(title='ERROR', message="No hay notas ingresadas.")
        pasar_datos=False
    else:
        datos.append(primer_linea[:-1])
        while(primer_linea!=''):
            primer_linea=notas.readline() #esto pasa todos los datos del alumno la idea es que solo pase el id para identificarlo
            x+=1
            if(x==7):
                x=0
                datos.append(primer_linea[:-1])       
    notas.close()
    if(pasar_datos):
        v_aux=Toplevel(boletin)
        v_aux.title('Baja de notas')
        v_aux.geometry('400x200')
        v_aux.transient(boletin)
        lab_lista=Label(v_aux, text="Lista de notas para bajas")
        lab_lista.place(x=0, y=0, height=25, width=400)
        combo_notas = tk.StringVar()
        combo = ttk.Combobox(v_aux, textvariable=combo_notas)
        combo['values'] = datos[:-1]
        combo.place(x=150, y=50, height=25, width=100)
        btn_ver=Button(v_aux, text='Eliminar', command=partial(eliminar_not, combo_notas, v_aux))
        btn_ver.place(x=150, y=100, height=25, width=100)


def buscar_not(combo_notas, v_aux):
    elegido=combo_notas.get()
    v_aux.destroy()
    notas=open('notas.dat','r',encoding='utf-8')
    aux=''
    lista=[]
    x=int(0)
    cond=False
    for linea in notas:
        aux=linea[:-1]
        if(cond):
            lista.append(aux)
            x+=1
            if(x==6):
                cond=False
                print(lista)
                alt_not(lista)       
        else:
            if(aux==elegido):
                cond=True
                lista.append(aux)
    notas.close()
def mod_not():
    x=int(0)
    notas=open('notas.dat','r',encoding='utf-8')
    pasar_datos=True
    datos=[]
    primer_linea=notas.readline()
    if(primer_linea==''):
        messagebox.showinfo(title='ERROR', message="No hay alumnos ingresados.")
        pasar_datos=False
    else:
        datos.append(primer_linea[:-1])
        while(primer_linea!=''):
            primer_linea=notas.readline() 
            x+=1
            if(x==7):
                x=0
                datos.append(primer_linea[:-1])
    notas.close()
    if(pasar_datos):
        v_aux=Toplevel(boletin)
        v_aux.title('Modificación de notas')
        v_aux.geometry('300x200')
        v_aux.transient(boletin)
        lab_lista=Label(v_aux, text="Lista de notas para modificar")
        lab_lista.place(x=0, y=0, height=25, width=300)
        combo_notas = tk.StringVar()
        combo = ttk.Combobox(v_aux, textvariable=combo_notas)
        combo['values'] = datos[:-1]
        combo.place(x=100, y=50, height=25, width=100)
        btn_ver=Button(v_aux, text='Modificar', command=partial(buscar_not, combo_notas, v_aux))
        btn_ver.place(x=100, y=100, height=25, width=100)

def list_not():
    x=int(0)
    notas=open('notas.dat','r',encoding='utf-8')
    pasar_datos=True
    primer_linea=notas.readline()
    if(primer_linea==''):
        messagebox.showinfo(title='ERROR', message="No hay notas ingresadas.")
        pasar_datos=False
    else:
        while(primer_linea!=''):
            primer_linea=notas.readline() 
            x+=1
            if(x==7):
                x=0
    notas.close()
    if(pasar_datos):
        v_list = tk.Tk()
        v_list.title("Lista de notas")
        vec_head=("ID_Not", "ID_Alu", "ID_Mat", "Nota1", "Nota2", "Nota3", "nota4")
        trv_frame=Frame(v_list)
        trv_frame.pack()
        trv_scroll=Scrollbar(trv_frame)
        trv_scroll.pack(side=RIGHT, fill=Y)
        trv_notas = Treeview(trv_frame, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", yscrollcommand=trv_scroll.set, selectmode="extended")
        trv_scroll.config(command=trv_notas.yview)
        j=int(1)
        for i in vec_head:
            trv_notas.heading(j, text=i)
            j+=1
        #-----------------
        notas=open('notas.dat','r',encoding='utf-8')
        aux=''
        lista=[]
        x=int(0)
        cond=False
        for linea in notas:
            aux=linea[:-1]
            lista.append(aux)
            x+=1
            if(x==7):
                trv_notas.insert("", "end", values=(lista))
                lista.clear()
                x=0
        notas.close()
        trv_notas.focus_set()
        trv_notas.pack()
        v_list.mainloop()

def combobox_notas(event):#acordarse que cuando se elimina un alumno tambien se eliminan sus notas y lo mismo al revez
    elegido=event.widget.get()
    lista=[]
    print("Combobox de Notas - Elemento seleccionado:", elegido)
    if(elegido=='notas_Altas'):
        alt_not(lista)
    elif(elegido=='notas_Bajas'):
        baj_not()
    elif(elegido=='notas_Modificar'):
        mod_not()
    else:
        list_not()

def list_selecc(event, trv_alumnos):
    selected_items = trv_alumnos.selection()
    for item in selected_items:
        datos = trv_alumnos.item(item)['values']
    elegido = datos[0]
    print(elegido)
    #-------------------------fijarse que existe en notas
    notas=open('notas.dat','r',encoding='utf-8')
    pasar_datos=False
    for elem in notas:
        aux=elem[:-1]
        if(aux==elegido):
            pasar_datos=True
    notas.close()
    #----------------------------------------------------
    if(pasar_datos):
        v_list = tk.Tk()
        v_list.title("Lista de notas")
        vec_head=("ID_Not", "ID_Alu", "ID_Mat", "Nota1", "Nota2", "Nota3", "nota4")
        trv_frame=Frame(v_list)
        trv_frame.pack()
        trv_scroll=Scrollbar(trv_frame)
        trv_scroll.pack(side=RIGHT, fill=Y)
        trv_notas = Treeview(trv_frame, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", yscrollcommand=trv_scroll.set, selectmode="extended")
        trv_scroll.config(command=trv_notas.yview)
        j=int(1)
        for i in vec_head:
            trv_notas.heading(j, text=i)
            j+=1
    #-------------------buscar cuantas notas ingresadas tiene tal alumno
        notas=open('notas.dat','r',encoding='utf-8')
        ant=''
        aux=''
        vec_not=[]
        x=int(0)
        for linea in notas:
            aux=linea[:-1]
            x+=1
            if(x==2):
                if(aux==elegido):
                    vec_not.append(ant)
            ant=linea[:-1]
            if(x==7):
                x=0
        notas.close()
        print(vec_not)#tiene todos las id_notas de ese id_alu
    #------------------
        x=int(0)
        pos=int(0)
        aux=''
        lista=[]
        cond=True
        for pos in range(len(vec_not)):
            print("valor de iteración:", vec_not[pos])
            notas=open('notas.dat','r',encoding='utf-8')
            linea2=int(0)
            for linea2 in notas:
                aux=linea2[:-1]
                if(cond):
                    if(aux==vec_not[pos]):
                        print(aux)
                        lista.append(aux)
                        cond=False
                    else:
                        lista.clear()
                        x+=1
                        if(x==7):
                            x=0
                            lista.clear()
                else:
                    lista.append(aux)
                    x+=1
                    print(x)
                    if(x==6):
                        print(lista)
                        trv_notas.insert("", "end", values=(lista))
                        x=0
                        cond=True
                        lista.clear()
            notas.close()
        trv_notas.focus_set()
        trv_notas.pack()
        v_list.mainloop()
    else:
        messagebox.showinfo(title='ERROR', message="todavia no han sido ingresadas las notas de ese alumno")

    
def lista_alumnos(lista_id, v_aux):
    v_list = Toplevel(v_aux)
    v_list.title("Lista de alumnos")
    v_list.transient(v_aux)
    vec_head=("ID_Alu", "DNI", "Apellido", "Nombre", "Email", "Curso", "División")
    trv_frame=Frame(v_list)
    trv_frame.pack(pady=10)
    trv_scroll=Scrollbar(trv_frame)
    trv_scroll.pack(side=RIGHT, fill=Y)
    trv_alumnos = Treeview(trv_frame, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", yscrollcommand=trv_scroll.set, selectmode="extended")
    trv_scroll.config(command=trv_alumnos.yview)
    j=int(1)
    for i in vec_head:
        trv_alumnos.heading(j, text=i)
        j+=1     
    #-----------------
    alumnos=open('alumnos.dat','r',encoding='utf-8')
    aux=''
    lista=[]
    x=int(0)
    pos=int(0)
    for linea in alumnos:
        aux=linea[:-1]
        lista.append(aux)
        x+=1
        if(x==7):
            if(lista[0]==lista_id[pos]):
                trv_alumnos.insert("", "end", values=(lista))
                pos+=1
                x=0
                lista.clear()
            else:
                x=0
                lista.clear()
    alumnos.close()
    trv_alumnos.pack()
    trv_alumnos.bind("<<TreeviewSelect>>", lambda event: list_selecc(event, trv_alumnos))
    trv_alumnos.focus_set()
    v_list.mainloop() 
def verificar_curso(cur, div, v_aux): #durante el for guardas los 7 datos diferentes de cada alumno si el curso y la división coinciden se guarda el id del alumno en una lista aparte
    x=int(0)
    lista=[]
    lista_id=[]
    datos=[cur, div]
    for dato in datos:
        if(len(dato.get())>0):
            x+=1
    if(x==2):
        x=int(0)
        aux=''
        alumnos=open('alumnos.dat','r',encoding='utf-8')
        for linea in alumnos:
            aux=linea[:-1]
            lista.append(aux)
            x+=1
            if(x==7):
                x=0
                if(cur.get()==lista[5] and div.get()==lista[6]):
                    lista_id.append(lista[0])
                lista.clear()
        alumnos.close()
        if(len(lista_id)>0):
            print(lista_id)
            lista_alumnos(lista_id, v_aux)
        else:
            messagebox.showinfo(title='ERROR', message="No han sido ingresados alumnos con esos datos todavia.")    
    else:
        messagebox.showinfo(title='ERROR', message="Faltan datos.")
        #lista.clear()
       
def listados_boletines():
    v_aux=Toplevel(boletin)
    v_aux.title('Listados de Boletines')
    v_aux.geometry('300x200')
    v_aux.transient(boletin)
    lab_lista=Label(v_aux, text="ingrese curso y división")
    lab_lista.place(x=0, y=0, height=25, width=300)
    lab_cur=Label(v_aux, text="Curso")
    lab_cur.place(x=100, y=25, height=25, width=100)
    lab_div=Label(v_aux, text="División")
    lab_div.place(x=100, y=75, height=25, width=100)
    combo_cur = tk.StringVar()
    combo1 = ttk.Combobox(v_aux, textvariable=combo_cur, state='readonly')
    combo1['values'] = ('1' , '2', '3', '4', '5')
    combo1.place(x=100, y=50, height=25, width=100)
    combo_div = tk.StringVar()
    combo2 = ttk.Combobox(v_aux, textvariable=combo_div, state='readonly')
    combo2['values'] = ('1' , '2', '3', '4', '5')
    combo2.place(x=100, y=100, height=25, width=100)
    btn_ver=Button(v_aux, text='confirmar', command=partial(verificar_curso, combo_cur, combo_div, v_aux))
    btn_ver.place(x=100, y=150, height=50, width=100)
#Programa principal-------------------------------------------
boletin=Tk()
boletin.geometry('500x280')
boletin.title('Boletines')
#------------------------------------------
fondo=PhotoImage(file='fondo_tp6.png')
lab_fondo=Label(image=fondo)
lab_fondo.pack(fill="both", expand=True)
lab_alu=Label(boletin, text="Alumno")
lab_alu.place(x=0, y=0, height=25, width=100)
lab_mat=Label(boletin, text="Materia")
lab_mat.place(x=100, y=0, height=25, width=100)
lab_not=Label(boletin, text="Notas")
lab_not.place(x=200, y=0, height=25, width=100)
lab_bol=Label(boletin, text="Boletines")
lab_bol.place(x=300, y=0, height=25, width=100)
v_asig=['alum_', 'mate_', 'notas_']
combos=[]
#-----------------
id_alumnos=open('id_alumnos.txt','a',encoding='utf-8')
id_alumnos.close()
id_materias=open('id_materias.txt','a',encoding='utf-8')
id_materias.close()
id_notas=open('id_notas.txt','a',encoding='utf-8')
id_notas.close()
alumnos=open('alumnos.dat','a',encoding='utf-8')
alumnos.close()
materias=open('materias.dat','a',encoding='utf-8')
materias.close()
notas=open('notas.dat','a',encoding='utf-8')
notas.close()
#-----------------
id_alumnos=open('id_alumnos.txt','r',encoding='utf-8')
primer_linea=id_alumnos.readline()[:-1]
id_alumnos.close()
if(primer_linea==''):
    id_alu='a1000'
    id_alumnos=open('id_alumnos.txt','w',encoding='utf-8')
    id_alumnos.write(id_alu+'\n')
    id_alumnos.close()
#-----------------
id_materias=open('id_materias.txt','r',encoding='utf-8')
primer_linea=id_materias.readline()[:-1]
id_materias.close()
if(primer_linea==''):
    id_mat='m1000'
    id_materias=open('id_materias.txt','w',encoding='utf-8')
    id_materias.write(id_mat+'\n')
    id_materias.close()
#-----------------
id_notas=open('id_notas.txt','r',encoding='utf-8')
primer_linea=id_notas.readline()[:-1]
id_notas.close()
if(primer_linea==''):
    id_not='n1000'
    id_notas=open('id_notas.txt','w',encoding='utf-8')
    id_notas.write(id_not+'\n')
    id_notas.close()
for i in range(3):
    combo_var = tk.StringVar()
    combo = ttk.Combobox(boletin, textvariable=combo_var, state='readonly')
    combo['values'] = (str(v_asig[i]+'Altas'),str(v_asig[i])+'Bajas', str(v_asig[i])+'Modificar', str(v_asig[i]+'Listados'))
    if(i==0):
        combo.bind("<<ComboboxSelected>>", combobox_alum)
    elif(i==1):
        combo.bind("<<ComboboxSelected>>", combobox_mate)
    else:
        combo.bind("<<ComboboxSelected>>", combobox_notas)
    combo.place(x=(i * 100), y=25, height=25, width=100)
    combos.append(combo)    
btn_ver=Button(boletin, text='Listados', command=partial(listados_boletines))
btn_ver.place(x=300, y=25, height=25, width=100)
boletin.mainloop()
