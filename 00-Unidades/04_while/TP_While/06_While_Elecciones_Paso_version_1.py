import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Pablo
apellido: Rico
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        candidato_mas_votado = ("", 0, 0)
        candidato_menos_votado = ("", 0, 0)
        acumulador_edad = 0
        contador = 0
        total_votos = 0
        while True:
            nombre = prompt("Elecciones PASO", "Ingrese el nombre del candidato")
            if nombre == None:
                break
            while nombre.isdigit():
                nombre = prompt("ERROR", "El nombre no puede contener números, por favor reintroduzca el nombre")
            
            while True:
                edad = prompt("Elecciones PASO", "Ingrese la edad del candidato")
                if edad == None:
                    break
                elif edad.isnumeric():
                    if int(edad) < 25:
                        edad = prompt("ERROR", "Ingrese una edad mayor a 25:")
                        continue
                    break
                else:
                    edad = prompt("ERROR", "Ingrese un número entero para la edad del candidato:")
            edad = int(edad)
            
            while True:
                votos = prompt("Elecciones PASO", "Ingrese la cantidad de votos")
                if votos == None:
                    break
                elif votos.isnumeric():
                    if int(votos) < 0:
                        votos = prompt("ERROR", "Ingrese una cantidad válida de votos")
                        continue
                    break
                else:
                     votos = prompt("ERROR", "Ingrese una cantidad válida de votos")
            votos = int(votos)
            if contador == 0:
                candidato_mas_votado = (nombre, votos, edad)
                candidato_menos_votado = (nombre, votos, edad)
            else:
                if votos > candidato_mas_votado[1]:
                    candidato_mas_votado = (nombre, votos, edad)
                elif votos < candidato_menos_votado[1]:
                    candidato_menos_votado = (nombre, votos, edad)
            acumulador_edad += edad
            total_votos += votos
            contador += 1

        promedio_edad = acumulador_edad / contador
        mensaje = (
            f"A. El candidato más votado es: {candidato_mas_votado[0]}.\n"
            f"B. El candidato menos votado es: {candidato_menos_votado[0]} y su edad es {candidato_menos_votado[2]}.\n"
            f"C. El promedio de edad de los candidatos es: {promedio_edad}.\n"
            f"D. Total de votos emitidos: {total_votos}"
        )

        alert("ELECCIONES PASO", mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
