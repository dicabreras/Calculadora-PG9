import tkinter as tk
from tkinter import ttk 
def init_window():
    global window
    global entrada1
    global entrada2
    global combo_operadores
    global label_resultado
    global label_entrada1
    global label_entrada2
    global label_operador
    global boton
    global boton2
    global boton4
    global boton5
    global boton6

    window = tk.Tk() #crear la pantalla
    window.title('Ich weiß alles')
    window.geometry('500x400')

    label = tk.Label(window, text = 'Tu Calculadora', font = ('Arial bold', 15))
    label.grid(column = 0, row = 0)

    entrada1 = tk.Entry(window, width = 12)
    entrada2 = tk.Entry(window, width = 12)

    entrada1.grid(column = 1, row = 1)
    entrada2.grid(column = 1, row = 2)

    label_entrada1 = tk.Label(window, text = 'Ingrese primer número:', font = ('Arial bold', 10))
    label_entrada1.grid(column = 0, row = 1)

    label_entrada2 = tk.Label(window, text = 'Ingrese segundo número:', font = ('Arial bold', 10))
    label_entrada2.grid(column = 0, row = 2)

    #crear una etiqueta para el seleccionador (combobox)
    label_operador = tk.Label(window, text = 'escoja un operador', font = ('Arial bold', 10))
    label_operador.grid(column = 0, row = 3)
    #crear un seleccioador (combobox)
    combo_operadores = ttk.Combobox(window)
    #Aisgnar los valores del seleccionados a traves de un atributo values
    combo_operadores['values'] = ['+', '-', '*', '/', 'pow']
    #Asignar por defecto una opcion seleccionada: 0 es el indice de los valores
    combo_operadores.current(0)#set te selected item
    #ubicar el seleccionador
    combo_operadores.grid(column=1, row=3)

    #Agregar etiqueta para mostrar el resultado de la operación en pantalla
    label_resultado = tk.Label(window, text='Resultado: ', font=('Aril bold', 15))
    label_resultado.grid(column = 0, row = 5)

    boton = tk.Button(window, 
                command = lambda: click_calcular(
                       label_resultado,
                       entrada1.get(),
                       entrada2.get(),
                       combo_operadores.get()),
                       text = 'Calcular',
                       bg = 'purple',
                       fg = 'white')
    boton.grid(column = 1, row = 4) # boton para calcular el resultado de la operación que indica el usuario     

    boton2 = tk.Button(window, 
               command = lambda : otro_cuadro(),
               text = 'Otro número',
               bg = 'red',
               fg = 'black')
    boton2.grid(column =1, row = 5)    # boton para hacer aparecer otro cuadro  y otro boton en las opciones de la culculadora

    boton4 = tk.Button(window, 
                command = lambda : otro_cuadro2(label), 
                text = 'Cambiar estilo',
                bg = 'firebrick1',
                fg = 'blue')   
    boton4.grid(column = 2, row = 5)  # boton para cambiar el estilo de la letra de la calculadora
    boton5 =tk.Button(window,
                command = lambda : aleman(label),
                text = 'Deutsch',
                bg = 'black',
                fg = 'red')
    boton5.grid(column = 2, row  =6)  # boton para cambiar el idioma a aleman de la calculadora (solo funciona cuando se ha calculado 
                                           # previamente el resultado y se ha dado en la opción de "otro cuadro")           
    boton6 = tk.Button(window,
                command = lambda: reiniciar(init_window),
                text = 'Reiniciar',
                bg = 'green',
                fg = 'white')
    boton6.grid(column=0, row = 10)  # boton para reiniciar la aplicacion, de manera que se vuelve a abrir en una nueva ventana y se destuye principal        
    window.mainloop()
                               

def calculadora(num1, num2, operador):
    
    if operador=='+':
         resultado = num1 + num2
    elif operador=='-':
         resultado = num1-num2
    elif operador == '*':
         resultado = num1*num2
    elif operador == '/':
         resultado = round(num1/num2, 2)   
    else:
         resultado = num1**num2 
    return resultado

def logaritmo(label_resultado, num1, num2, num3, operador): # Funcion que calcula el lagoritmo del resultado 
     import math                                              #que se obtuvo despues de calcular las dos primeras entradas de la calculadora
     import cmath
     valor1 = float(num1)
     valor2 = float(num2)
     cont = int(num3)
     res1 = calculadora(valor1, valor2, operador)
     res2 = math.log(res1, cont)
     res = round(res2, 5)
     label_resultado.configure(text = 'Resultado: ' + str(res))

def otro_cuadro():                                            #Funcion que muestra otro casilla de entrada en la calculadora
     global boton3
     entrada3 = tk.Entry(window, width = 12)
     entrada3.grid(column = 1, row = 6)

     boton3 = tk.Button(window, 
                command = lambda: logaritmo(
                       label_resultado,
                       entrada1.get(),
                       entrada2.get(),
                       entrada3.get(),
                       combo_operadores.get()),
                       text = 'Logaritmo en base # de Resultado',
                       bg = 'yellow',
                       fg = 'black') 
     boton3.grid(column = 1, row= 7)                  

def otro_cuadro2(label):                               # Funcion que cambia el estilo de letra de la calculadora
     label.configure(font = ('Courier', 12))
     label_resultado.configure(font = ('Courier', 10))
     label_entrada1.configure(font = ('Courier', 10))
     label_entrada2.configure(font = ('Courier', 10))
     label_operador.configure(font = ('Courier', 10))
def aleman(label):                                    # Funcion que cambia el idioma de esapañol a alemán de la calculadora
     label.configure(text= 'Dein Taschenrechner')  
     label_resultado.configure(text = 'Das Ergebnis: ' + str(res))
     label_entrada1.configure(text = 'Eingeben Sie die erste Zahl')
     label_entrada2.configure(text = 'Eingeben Sie die zweite Zahl')
     label_operador.configure(text = 'Wählen Sie einigen Operator')   
     boton.configure(text= 'Berechnen')
     boton6.configure(text = 'Neustart') 
     boton2.configure(text = 'Andere Zahl')
     boton3.configure(text = 'Der Logartihmus im Base # des Ergebnis ')
     boton4.configure(text = 'Ändern der Stil')        

def click_calcular(label_resultado, num1, num2, operador):
    global res
    #conversion de valores
    valor1 = float(num1)
    valor2 = float(num2)      
    #calculo dados los valores y el operador
    res = calculadora(valor1, valor2, operador)

    #Actualizacion del texto en la etiqueta
    label_resultado.configure(text = 'Resultado: ' + str(res))   

def reiniciar(init_window):   # Función que destruye la ventana principal y vuelve a correr el prorama. "opción de riniciar"
     window.destroy()
     init_window()       
    
def main():
    init_window()
 
main()    

