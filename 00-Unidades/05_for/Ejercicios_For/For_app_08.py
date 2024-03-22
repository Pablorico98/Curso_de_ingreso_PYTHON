import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Mostrar cada número primo entre 1 y el número ingresado, e informar la cantidad de números primos encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        # Se solicita al usuario que ingrese un número
        numero = int(prompt(None, "Ingresa un numero"))
        # Se inicializa el contador de números primos encontrados
        cantidad_primos= 0

        # Se itera sobre todos los números desde 2 hasta el número ingresado
        for i in range(2, numero + 1):
            es_primo = True  # Se asume que el número es primo inicialmente

            # Se itera sobre todos los números desde 2 hasta i-1
            for j in range(2, i):
                # Si i es divisible por algún número en ese rango, entonces no es primo
                if i % j == 0:
                    es_primo = False  # Se marca el número como no primo
                    break  # Se sale del bucle, ya que no es necesario continuar la verificación

            # Si al final del bucle interno, es_primo sigue siendo True, significa que i es primo
            if es_primo:
                cantidad_primos += 1  # Se incrementa el contador de números primos
                print(f"\t{i}")  # Se imprime el número primo encontrado

        # Al finalizar el bucle, se muestra la cantidad total de números primos encontrados
        print(f"Del 1 al {numero} hay {cantidad_primos} primos.")
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
