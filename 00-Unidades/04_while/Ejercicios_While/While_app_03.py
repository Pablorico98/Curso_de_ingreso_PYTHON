import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Pablo
apellido: Rico
---
Ejercicio: while_03
---
Enunciado:
Al presionar el botón ‘Pedir clave’, solicitar al usuario que ingrese una contraseña mediante prompt. 
Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no coincidir, 
volver a solicitarla hasta que coincidan.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_pedir_clave = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_pedir_clave_on_click)
        self.btn_pedir_clave.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_pedir_clave_on_click(self):
        #visto en clase
        clave=prompt("UTN", "Ingrese su clave")
        while clave != "utn750":
            clave=prompt("Error", "Reingrese su clave")
        alert("UTN","Contraseña correcta")
        
        #usa nas recursos lo de abajo 

        #clave=prompt("UTN", "Ingrese su clave")
        #while not (clave == "utn750"):
        #   clave=prompt("Error", "Reingrese su clave")
        #alert("UTN","Contraseña correcta")



        #como lo hice yo
       # while True:
        #    contraseña = prompt("UTN","Ingrese su clave")
         #   if contraseña =="utn750":
          #      alert("UTn","Contraseña correcta")
           #     break
            #else:
             #   alert("UTn","Contraseña incorrecta")
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()