import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Pablo
apellido:Rico
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        acumulador_negativos = 0
        acumulador_positivos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0

        while True:
            numero_ingresado = prompt("Solicitar numero","Ingrese un numero")

            if numero_ingresado != None:
                
            
                numero_ingresado = float(numero_ingresado)

                

                if numero_ingresado < 0:
                    acumulador_negativos += numero_ingresado
                    contador_negativos += 1
                elif numero_ingresado > 0:
                    acumulador_positivos += numero_ingresado
                    contador_positivos += 1
                else :
                    contador_ceros += 1
            else:
                break
        if contador_positivos > contador_negativos:
            diferencia = contador_positivos - contador_negativos
        else:
            diferencia = contador_negativos - contador_positivos
        mensaje = (
    f"A. La suma acumulada de los negativos es {acumulador_negativos}\n" +
    f"B. La suma acumulada de los positivos es {acumulador_positivos}\n" +
    f"C. Cantidad de números positivos ingresados es {contador_positivos}\n" +
    f"D. Cantidad de números negativos ingresados es {contador_negativos}\n" +
    f"E. Cantidad de ceros es {contador_ceros}\n" +
    f"F. Diferencia entre la cantidad de los números positivos ingresados y los negativos es {diferencia}")
        

        
        alert("UTN",mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
