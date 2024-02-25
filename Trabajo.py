import tkinter as tk
import tkinter.ttk as ttk
import random
from tkinter import messagebox

class preposicion: #clase que crea objeto basado en las preposiciones
    letra = str()
    def __init__(self, letra= str(), lista=None):
        if lista is None:
            lista = []
        self.conjunto = set(lista) #actualiza
        self.letra = letra
        
    @property
    def Letra(self):
        return self.letra

    @Letra.setter
    def Letra(self, letra):
        self.letra = letra

class ventana(ttk.Frame): #clase que contiene informacion de la ventana 
    def __init__(self, master):
        super().__init__(master)
        self.master =master
        self.pack()

#variables relacionadas a la clase preposiciones
texto_expresion = "" #texto generado para actualizar la expresion
conjunto_lista =[] 

def mostrar_enVentana(letra,le):
    global texto_expresion
    global conjunto_lista
    
    objecto = preposicion(letra,[le])
    conjunto_lista.append(objecto)
    texto_expresion += letra + " "
    #ubica y actualiza el texto que genero canvas
    canvas.itemconfig(tagOrId=texto_conjuntos, text=f"{texto_expresion}")


def mostrar_operaciones(letra): #muestra elementos de la operacion
    global texto_expresion
    
    texto_expresion += letra + " "
    canvas.itemconfig(tagOrId=texto_conjuntos, text=f"{texto_expresion}")


def quitar_elemento(): #quita un elemento de la expresion
    global texto_expresion
    
    operadores = ["p","q","r","s","^","v","→","-","↔","(",")"]
    elemento = ["p","q","r","s"]
    
    for operador in reversed(texto_expresion):
        if operador in operadores:
            texto_expresion = texto_expresion.replace(operador, "", 1)
            try:
                texto_expresion = texto_expresion.replace(" ", "", 1)
            except:
                pass
            if operador in elemento:
                conjunto_lista.pop() #quita elemento
            break
    #actualiza expresion
    canvas.itemconfig(tagOrId=texto_conjuntos, text=f"{texto_expresion}")


def mostrar_resultados(texto, lista_conjuntos):
    
    operadores = {"^","v","-","→","↔"}

    conjunto_actual = set()
    operacion_actual = '^'  # Operación predeterminada
    conjunto_temporal = []
    
    contador = 0

    for char in texto:
        if char.isalpha() and char not in operadores:  # Si es una letra, la consideramos como un conjunto
            conjunto_temporal.append(lista_conjuntos[contador].conjunto) 
            contador += 1
        elif char in operadores:  # Si es un operador, cambiamos la operación actual
            operacion_actual = char
        elif char == '(':  # Si es un paréntesis de apertura, reiniciamos el conjunto temporal
            conjunto_temporal = []
        elif char == ')':  # Si es un paréntesis de cierre, realizamos la operación y actualizamos el conjunto actual
            conjunto_actual = realizar_operacion(conjunto_temporal, operacion_actual)
            conjunto_temporal.append(list(conjunto_actual))

    #resultado_ordenado = sorted(conjunto_actual)
    canvas.itemconfig(tagOrId=texto_Respuesta, text=f"{conjunto_actual}")
    contador = 0


def realizar_operacion(lista_de_conjuntos, operacion_actual):  
    try:
        conjunto_retornar = []
        
        uno = "".join(str(item) for item in lista_de_conjuntos[-2])
        dos = "".join(str(item) for item in lista_de_conjuntos[-1])

        if(operacion_actual == "^"): #conjucion
            conjunto_retornar = f"{uno} y {dos}"
        elif(operacion_actual == "v"):#disyuccion
            conjunto_retornar = f"{uno} o {dos}"
        #ACOMODAR
        elif(operacion_actual == "-"):#negacion (-p^-q)
            conjunto_retornar = f"No es cierto que {uno} y tampoco es cierto que {dos}"
            
        elif(operacion_actual == "→"): #condicional
            conjunto_retornar = f"{uno} si {dos}" 
        elif(operacion_actual == "↔"): #bicondicional
            conjunto_retornar = f"{uno} si y solo si {dos}"

        return conjunto_retornar
    except ValueError:
        messagebox(text="Datos ingresados invalidos")
        

def limpiar(): #elimina expresion
    global texto_expresion
    global conjunto_lista

    canvas.itemconfig(tagOrId=texto_conjuntos, text="Inserte la expresión a realizar")
    canvas.itemconfig(tagOrId=texto_Respuesta,text="Traducción en lenguaje natural")

    texto_expresion = ""
    conjunto_lista=[]
    
   
def aleatorio():
    #limpia y esconde formato de inrgeso de datos por teclado
    a_entry.delete('0', 'end')
    a_entry.place_forget(); boton_a.place_forget()
    b_entry.delete('0', 'end')
    b_entry.place_forget(); boton_b.place_forget()
    c_entry.delete('0', 'end')
    c_entry.place_forget(); boton_c.place_forget()
    d_entry.delete('0', 'end')
    d_entry.place_forget(); boton_d.place_forget()

    #lista de preposiciones aleatorias tema: clima
    listaAleatoria =[
        "el día esta soleado",
        "el día esta nublado",
        "el día esta lluvioso",
        "la primavera se acerca",
        "el invierno es frío",
        "el verano se acerca",
        "en otoño las hojas caen",
        "el día esta lindo",
        "el clima me gusta",
        ]
    #subconjuntos emplean valores del conjunt u para ser rellenados
    a_label.config(text=random.choice(listaAleatoria))
    a_label.place(x=270,y=180,width=200)
    boton_a_aleatorio.config(command=lambda: mostrar_enVentana("p", a_label.cget("text")))
    boton_a_aleatorio.place(x=477,y=180)

    b_label.config(text= random.choice(listaAleatoria))
    b_label.place(x=270,y=220,width=200)
    boton_b_aleatorio.config(command=lambda: mostrar_enVentana("q", b_label.cget("text")))
    boton_b_aleatorio.place(x=477,y=220)

    c_label.config(text=random.choice(listaAleatoria))
    c_label.place(x=658,y=180,width=200)
    boton_c_aleatorio.config(command=lambda: mostrar_enVentana("r", c_label.cget("text")))
    boton_c_aleatorio.place(x=865,y=180)

    d_label.config(text=random.choice(listaAleatoria))
    d_label.place(x=658,y=220,width=200)
    boton_d_aleatorio.config(command=lambda: mostrar_enVentana("s", d_label.cget("text")))
    boton_d_aleatorio.place(x=865,y=220)

    boton_aleatorio.place_forget()
    boton_teclado.place(width=200,height=30,x=760,y=109.8)
    

def teclado(): 
    #esconde formato de ingreso aleatorio 
    a_label.place_forget(); boton_a_aleatorio.place_forget()
    b_label.place_forget(); boton_b_aleatorio.place_forget()
    c_label.place_forget(); boton_c_aleatorio.place_forget()
    d_label.place_forget(); boton_d_aleatorio.place_forget()

    #muestra formato de ingreso de datos a traves del teclado
    a_entry.place(x=270,y=180,width=200); boton_a.place(x=477,y=180)
    b_entry.place(x=270,y=220,width=200);boton_b.place(x=477,y=220)
    c_entry.place(x=658,y=180,width=200); boton_c.place(x=865,y=180)
    d_entry.place(x=658,y=220,width=200);boton_d.place(x=865,y=220)

    boton_teclado.place_forget()
    boton_aleatorio.place(width=200,height=30,x=760,y=109.8)
    

#Ventana generada
window = tk.Tk()
window.geometry("1200x645")
window.title("Software de logica proposicional")
window.configure(bg = "white")    
window.resizable(False, False)

canvas =tk.Canvas(window,
    width = 1200,height=645,
    bd = 0,
    highlightthickness = 0)
canvas.place(x=0,y=0) #REVISAR 
imgbackground = tk.PhotoImage(#fondo
     file="backgroundLogica.png")
imageBG = canvas.create_image(
     600,
     321,
     image=imgbackground)
imgOperacion = tk.PhotoImage(#img expresion
     file="operacion.png")
image_1 = canvas.create_image(
     553.0,
     368,
     image=imgOperacion
 )
texto_conjuntos = canvas.create_text( #texto expresion
    365.0,360,
    anchor="nw",
    text="Inserte la expresión a realizar",
    fill="white",
    font=("Arial", 10))

imgRespuesta = tk.PhotoImage( #img respuesta
     file="respuesta.png")
image_2 = canvas.create_image(
     530,
     453,
     image=imgRespuesta
 )
texto_Respuesta = canvas.create_text( #texto respuesta
    305.0,445,
    anchor="nw",
    text="Traducción en lenguaje natural",
    fill="white",
    font=("Arial", 10))

#caracteristicas de botones ttk
style = ttk.Style()
style.configure("TButton", background="#410666",foreground="#30094E")
style.configure("TEntry", background ="#410666")

#labels de los entrys
ttk.Label(window,text="p:",background="#551375",foreground="white",font=("arial",11,"bold")).place(x=250,y=180)
ttk.Label(window,text="q:",background="#50136D",foreground="white",font=("arial",11,"bold")).place(x=250,y=220)
ttk.Label(window,text="r:",foreground="white",background="#450977",font=("arial",11,"bold")).place(x=638,y=180)
ttk.Label(window,text="s:",background="#450977",foreground="white",font=("arial",11,"bold")).place(x=638,y=220)

#witgets teclado
a1 = tk.StringVar()
a_entry = ttk.Entry(window,textvariable=a1,)
a_entry.place(x=270,y=180,width=200)
boton_a =ttk.Button(window,text="Insertar",
                    command=lambda: mostrar_enVentana("p", a1.get()))
boton_a.place(x=477,y=180)

b1 =tk.StringVar()
b_entry = ttk.Entry(window,textvariable=b1)
b_entry.place(x=270,y=220,width=200)
boton_b =ttk.Button(window,text="Insertar",
                    command=lambda: mostrar_enVentana("q", b1.get()))
boton_b.place(x=477,y=220)

c1 =tk.StringVar()
c_entry = ttk.Entry(window,textvariable=c1)
c_entry.place(x=658,y=180,width=200)
boton_c =ttk.Button(window,text="Insertar",
                    command=lambda: mostrar_enVentana("r", c1.get()))
boton_c.place(x=865,y=180)

d1 =tk.StringVar()
d_entry = ttk.Entry(window,textvariable=d1)
d_entry.place(x=658,y=220,width=200)
boton_d =ttk.Button(window,text="Insertar",
                    command=lambda: mostrar_enVentana("s", d1.get()))
boton_d.place(x=865,y=220)

#witgets random
a_label= tk.Label(window, background="#30094E", fg="white",highlightbackground="white")
a_label.place_forget()
boton_a_aleatorio = ttk.Button(window,text="Insertar")
boton_a_aleatorio.place_forget()

b_label= tk.Label(window, background="#30094E", fg="white")
b_label.place_forget()
boton_b_aleatorio = ttk.Button(window,text="Insertar")
boton_b_aleatorio.place_forget()

c_label= tk.Label(window, background="#30094E", fg="white")
c_label.place_forget()
boton_c_aleatorio = ttk.Button(window,text="Insertar")
boton_c_aleatorio.place_forget()

d_label= tk.Label(window, background="#30094E", fg="white")
d_label.place_forget()
boton_d_aleatorio = ttk.Button(window,text="Insertar")
boton_d_aleatorio.place_forget()

#boton para generar conjuntos a traves del teclado
boton_teclado =  ttk.Button(window,text="Generar preposiciones propias",command=teclado)
boton_teclado.place_forget()

#boton para generar conjuntos a traves de random
boton_aleatorio =  ttk.Button(window,text="Generar preposiciones aleatorias",command=aleatorio)
boton_aleatorio.place(width=200,height=30,x=760,y=109.8)

#botoneÑ operadores logicos
#conjucion
boton_conjucion= ttk.Button(window, text="^",command=lambda: mostrar_operaciones("^")
                            ).place(width=40,height=27,x=450,y=280)
#diyuccion
boton_Diyuccion= ttk.Button(window, text="v",command=lambda: mostrar_operaciones("v")
                         ).place(width=40,height=27,x=510,y=280)
#negacion
boton_negacion= ttk.Button(window, text="-",command=lambda: mostrar_operaciones("-")
                             ).place(width=40,height=27,x=570,y=280)
#condicional
boton_condiconal= ttk.Button(window, text="→",command=lambda: mostrar_operaciones("→")
                              ).place(width=40,height=27,x=630,y=280)
#Bicondicional
boton_bicondiconal= ttk.Button(window, text="↔",command=lambda: mostrar_operaciones("↔")
                             ).place(width=40,height=27,x=690,y=280)
#parentesis que abren y cierran expresion
boton_1 =ttk.Button(window, text="(",command=lambda: mostrar_operaciones("(")
                   ).place(width=20,x=300,y=353)
boton_2 =ttk.Button(window, text=")",command=lambda: mostrar_operaciones(")")
                    ).place(width=20,x=325,y=353)
#boton que calcula expresion
boton_calcular =ttk.Button(window, text="Calcular",
                           command=lambda: mostrar_resultados(canvas.itemcget(texto_conjuntos, 'text'), conjunto_lista)
                           ).place(width=65,x=830,y=354)
#borra un elemento 
boton_borrar =ttk.Button(window, text="Borrar",command=lambda: quitar_elemento()
                           ).place(width=65,x=760,y=354)
#boton que limpia expresion para hacer una nueva
boton_nuevaOperacion = ttk.Button(window,text="Nueva Operación",command=lambda:limpiar()).place(width=117,x=790,y=440)
#invoca clase para que aparezca la ventana
w =ventana(window)
w.mainloop()