import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:  
apellido:  
---
TP: While_validaciones_rising_btl
---
Enunciado:
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.txt_tipo = customtkinter.CTkEntry(master=self)
        self.txt_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        apellido = prompt("UTN", "Ingrese su apellido")    
        while apellido==None or apellido == " " or not apellido.isalpha():
            apellido = prompt("ERROR", "Apellido invalido. Reingrese su apellido")
                        
        edad= prompt("UTN", "Ingrese su edad")
        while edad == None or edad == " " or not edad.isdigit() or (int(edad) <18 or int(edad) > 90):
            edad=prompt("Error", "Ingreso una letra no una edad, reingrese su edad")
           
                    
        tipo=prompt("UTN","Ingrese su estado civil")
        while  tipo == None or tipo == " " or not (tipo == "Soltero" or tipo == "Soltera" or tipo == "Casado" or tipo == "Casada" or tipo == "Viudo" or tipo == "Viuda" or tipo == "Divorciado" or tipo == "Divorciada"):
            tipo=prompt("Error", "Reengrese un estadio civil correcto, revise si la incial es mayuscula")
            
        legajo= prompt("UTN", "Ingrese su numero de legajo")
        while legajo == None or legajo == " " or not legajo.isdigit() or (int(legajo) <1000 or int(legajo) > 10000):
           
            legajo=prompt("Error", "Ingrese un legajo de 4 dígitos.")               
           
        
        self.txt_apellido.delete(0,"end")
        self.txt_apellido.insert(0,apellido)
        self.txt_edad.delete(0,"end")
        self.txt_edad.insert(0,edad)
        self.txt_tipo.delete(0,"end")
        self.txt_tipo.insert(0,tipo)
        self.txt_legajo.delete(0,"end")
        self.txt_legajo.insert(0,legajo)
       

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
