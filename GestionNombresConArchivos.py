def alta():
    nombres=open('nombres.txt','a',encoding='utf-8')
    nombre=''
    while(nombre!='FIN'):                                                                              
        nombre=input('ingrese_nombre/FIN_cuando_termines:')
        if(nombre!='FIN'and len(nombre)>0):
            nombres.write(nombre+'\n')
    nombres.close()

def lista():
    nombres=open('nombres.txt','r',encoding='utf-8')
    for linea in nombres:
        lectura=linea[:-1]
        print(lectura)
    nombres.close()

def comparar(nom, menor):
    if(nom<menor):
        menor=nom
    return(menor) 
    
def buscar_menor():
    nombres=open('nombres.txt','r',encoding='utf-8')
    x=0
    for linea in nombres:
        if(x==1):
            aux=linea[:-1]
            aux2=comparar(aux, aux2)
        if(x==0):
            aux2=linea[:-1]
            x=1   
    return(aux2)

def sacar_menor(men):
    nombres=open('nombres.txt','r',encoding='utf-8')
    temporal=open('temporal.txt','w',encoding='utf-8')
    for linea in nombres:
        aux=linea[:-1]
        if(aux!=men):
            temporal.write(aux+'\n')        
    temporal.close()
    nombres.close()

def pasar_lista():
    nombres=open('nombres.txt','w',encoding='utf-8')
    temporal=open('temporal.txt','r',encoding='utf-8')
    for linea in temporal:
        aux=linea[:-1]
        nombres.write(aux+'\n')
    nombres.close()
    temporal.close()

def ordenar_archivo():
    ordenado=open('ordenado.txt','w',encoding='utf-8')
    ordenado.close()
    nombres=open('nombres.txt','r',encoding='utf-8')
    for linea in nombres:
        if(linea!='\n'):
            menor=buscar_menor()
            ordenado=open('ordenado.txt','a',encoding='utf-8')
            ordenado.write(menor+'\n')
            ordenado.close()
            sacar_menor(menor)
            pasar_lista()
    nombres.close()
    nombres=open('nombres.txt','w',encoding='utf-8')
    ordenado=open('ordenado.txt','r',encoding='utf-8')
    for linea2 in ordenado:
        orden=linea2[:-1]
        nombres.write(orden+'\n')
    nombres.close()
    ordenado.close()
    
nombres=open('nombres.txt','a',encoding='utf-8')
nombres.close()
temporal=open('temporal.txt','a',encoding='utf-8')
temporal.close()
opc=''
while(opc!='0'):
    opc=input("ingrese opción_0)Salir/1)Alta_de_Nombres/2)Listado_de_Nombres/3)Ordenado_de_Archivo: ")
    if(opc=='0'):
        print("FIN")

    elif(opc=='1'):
        alta()
        
    elif(opc=='2'):
        lista()

    elif(opc=='3'):
        ordenar_archivo()
        print('ordenamiento completado.')

    else:
        print('opcion incorrecta ingrese devuelta')
