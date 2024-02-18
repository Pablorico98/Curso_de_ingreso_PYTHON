import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Pablo
apellido: Rico
---
Ejercicio: while_06
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
    #antes del while
        #declarar e inicializar el contador
        contador=0
        #declarar el acumulador
        acumulador=0
        while contador < 5:
    #durante e inicializar el while
         #pedir un numero (esto se repite 5 veces)
            numero=prompt("Datos","Ingrese un numero")
            numero=float(numero)
         #acumulo el numero en el acumulador
            acumulador+=numero
         #incrementar la variable de control
            contador+=1
    #despues el while
        #calculo el promedio 
        promedio=acumulador/contador #podria poner "/5" Si itero esta linea de codigo voy a hacer que la cuenta se itere 5 veces porque estara dentro del while
        #muestro el acumulador 
        self.txt_suma_acumulada.delete(0,"end")
        self.txt_suma_acumulada.insert(0,acumulador)
        #muestro el promedio
        self.txt_promedio.delete(0,"end")
        self.txt_promedio.insert(0,promedio)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
