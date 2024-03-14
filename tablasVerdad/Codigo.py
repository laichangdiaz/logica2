import ttg
import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from prettytable import PrettyTable


listVariables = set()  # conjunto que almacena variables (letras)
textoExpresion = "" #expresion generada por el usuario

#Muestra expresion generada por el usuario
def mostrar(letra):
    global listVariables
    global textoExpresion

    if letra in ["p", "q", "s", "r"]:
        #agrega elementos de la lista para saber si son variable empleadas
        listVariables.add(letra)  

    textoExpresion += letra + " "
    canvas.itemconfig(tagOrId=texto_conjuntos, text=f"{textoExpresion}")


#Borra el ultimo elemento de la lista
def borrar_elemento():
    global textoExpresion
    # separa la expresion y elimina el ultimo elemento
    words = textoExpresion.split()[:-1]
    textoExpresion = " ".join(words)
    canvas.itemconfig(tagOrId=texto_conjuntos, text=f"{textoExpresion}")


#limpia expresion y resultado (Borra todo)
def limpiar_expresion():
    global textoExpresion
    global listVariables
    listVariables.clear()
    textoExpresion = ""
    canvas.itemconfig(tagOrId=texto_conjuntos, text=f"{textoExpresion}")
    canvas.itemconfig(tagOrId=texto_Respuesta, text="")


#genera tabla de verdad y muestra el resultado
def tablaVerdad():
    global textoExpresion
    global listVariables

    if not listVariables:
        print("Por favor ingrese una variable.")
        return

    variables = list(listVariables)  #convierte el conjunto(set) en lista
    expression = f'{textoExpresion}'
    tabla = ttg.Truths(variables, [expression]) #, ints=False
    tipo =tabla.valuation()
    if tipo == "Tautology":
        tipo = "Tautologia"
    elif tipo == "Contingency":
        tipo="Continguencia"
    elif tipo =="Contradiction":
        tipo ="Contradicción"
    canvas.itemconfig(tagOrId=texto_Respuesta, text=f"{tabla} \n Tipo de proposición {tipo}")
   

window = tk.Tk()
window.geometry("1150x600")
window.title("Software: Tablas de Verdad")
window.configure(bg="white")
window.resizable(False, False)

canvas = tk.Canvas(window, width=1150, height=600, bd=0, highlightthickness=0)
canvas.place(x=0, y=0)
imgbackground = tk.PhotoImage(#fondo
     file="bg.png")
imageBG = canvas.create_image(
     572,
     300,
     image=imgbackground)
imgOperacion = tk.PhotoImage(#img expresion
     file="exp.png")
image_1 = canvas.create_image(
     335.0,
     368,
     image=imgOperacion
 )
texto_conjuntos = canvas.create_text(
    133.0, 360,
    anchor="nw",
    text="Inserte la expresión a realizar",
    fill="#792626",
    font=("Arial", 10)
)
imgRespuesta = tk.PhotoImage( #img respuesta
     file="resp.png")
image_2 = canvas.create_image(
     800,
     310,
     image=imgRespuesta
 )
texto_Respuesta = canvas.create_text(
    633.0, 135.0,
    anchor="nw",
    text="",
    fill="#792626",
    font=("Arial", 10)
)


#caracteristicas de botones ttk
style = ttk.Style()
style.configure("TButton", background="#FFD3CA")
#WIDGETS
#variables logicas 
ttk.Button(text="p", command=lambda: mostrar("p")).place(x=180, y=90,width=40,height=40)
ttk.Button(text="q", command=lambda: mostrar("q")).place(x=230, y=90,width=40,height=40)
ttk.Button(text="r", command=lambda: mostrar("r")).place(x=280, y=90,width=40,height=40)
ttk.Button(text="s", command=lambda: mostrar("s")).place(x=330, y=90,width=40,height=40)
#operadores logicos
tk.Label(text="Operadores Logicos",background="#FFD3CA",foreground="#792626", font=("Arial",11)).place(x=120,y=160)
ttk.Button(text='and', command=lambda: mostrar('and')).place(x=205, y=190,height=27,width=65)
ttk.Button(text='-', command=lambda: mostrar('-')).place(x=280, y=190,height=27,width=65)
ttk.Button(text='or', command=lambda: mostrar('or')).place(x=355, y=190,height=27,width=65)
ttk.Button(text='NOR', command=lambda: mostrar('nor')).place(x=205, y=225,height=27,width=65)
ttk.Button(text='XOR', command=lambda: mostrar('xor')).place(x=280, y=225,height=27,width=65)
ttk.Button(text='NAND', command=lambda: mostrar('nand')).place(x=355, y=225,height=27,width=65)
ttk.Button(text='Condicional  =>', command=lambda: mostrar('=>')).place(x=205, y=260,height=27,width=100) #→
ttk.Button(text='Bicondicional  =', command=lambda: mostrar('=')).place(x=316, y=260,height=27,width=103) #↔
ttk.Button(text='(', command=lambda: mostrar('(')).place(x=125, y=190,width=25,height=35)
ttk.Button(text=')', command=lambda: mostrar(')')).place(x=155, y=190,width=25,height=35)
#botones de apoyo
ttk.Button(text="Generar tabla", command=lambda: tablaVerdad()).place(x=240, y=400,height=35,width=100)
ttk.Button(text="Borrar", command=borrar_elemento).place(x=345, y=400,height=35,width=80)
ttk.Button(text="Limpiar", command=limpiar_expresion).place(x=430, y=400,height=35)
#label tipo leyenda
tk.Label(text="True = Verdad = V = 1   |  False = Falso = F = 0", font=("Arial",11),background="#FFD3CA",foreground="#792626").place(y=95,x=605)
tk.Label(text="Consideración:", font=("Arial",11),background="#FFD3CA",foreground="#792626").place(x=600,y=75)

window.mainloop()