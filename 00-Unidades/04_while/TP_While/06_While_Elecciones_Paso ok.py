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

        
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        contador_candidatos=0
        acumulador_votos=0
        acumulador_edad=0
        continuar=question("Votacion","¿Desea ingresar candidatos?")
        
        while continuar:
            nombre=prompt("Nombre", "Ingrese el nombre del candidato")
            while nombre==None or not nombre.isalpha():
                nombre = prompt("ERROR", "Nombre invalido. Reingrese el nombre del candidato")
            
            edad=prompt("Edad", "Ingrese la edad del candidato")
            while edad==None or not(edad.isdigit()) or int(edad)<25:
                edad=prompt("Edad", "Reingrese la edad del candidato")
            edad=int(edad)

            votos=prompt("Votos","Ingrese la cantidad de votos del candidato")
            while votos== None or not(votos.isdigit()) or int(votos) <0:
                votos=prompt("Votos","Reingrese la cantidad de votos del candidato")
            votos=int(votos)
            if contador_candidatos == 0 or votos > mayor_votado:
                mayor_votado=votos
                candidato_mas_votado=nombre
            if contador_candidatos == 0 or votos < menor_votado:
                menor_votado=votos
                candidato_menos_votado=nombre
            acumulador_edad+=edad
            acumulador_votos+=votos
            contador_candidatos+=1
                        
            continuar = question("Votacion","¿Desea continuar ingresando candidatos?")
            
        if contador_candidatos > 0:
            promedio_edad=acumulador_edad/contador_candidatos
            mensaje = (
                f"Candidato mas votado: {candidato_mas_votado}.\n"
                f"Candidato menos votado: {candidato_menos_votado} con {menor_votado} votos.\n"
                f"El promedio de la edad de los candidatos es: {promedio_edad}.\n"
                f"Total de votos : {acumulador_votos}"
            )
        else:
            mensaje="no se ingresaron candidatos"

        alert("Votacion",mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
