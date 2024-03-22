import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Simulacro Turno Noche

Un famoso casino de mar del plata,  requiere una app para controlar el egreso de dinero durante una jornada. Para ello se ingresa por cada ganador:

Nombre

Importe ganado (mayor o igual $1000)

Género (“Femenino”, “Masculino”, “Otro”)

Juego (Ruleta, Poker, Tragamonedas)

Necesitamos saber:

Nombre y género de la persona que más ganó.

Promedio de dinero ganado en Ruleta.

Porcentaje de personas que jugaron en el Tragamonedas.

Cuál es el juego menos elegido por los ganadores.

El nombre del jugador que ganó más dinero jugando Poker

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):

        continuar=True
        contador_ganadores=0
        acumulador_ruleta=0
        contador_ruleta=0
        contador_tragamonedas=0
        contador_poker=0
    #Proceso
        while continuar:
            nombre=prompt("Casino","Ingrese su nombre")
            while nombre == None:
                    nombre=prompt("Casino","Reingrese su nombre")
            importe_ganado= prompt("Casino", "Ingrese el importe ganado")
            while importe_ganado == None or not(importe_ganado.isdigit()) or int(importe_ganado) <1000:
                importe_ganado=prompt("Casino", "Reingrese el importe ganado")
            genero=prompt("Casino","Ingrese su genero")
            while genero != "Femenino" and genero!= "Masculino" and genero!= "Otro":
                genero=prompt("Casino","Reingrese su genero")
            juego=prompt("Casino","Ingrese el juego")
            while juego !="Ruleta" and juego!="Poker" and juego!="Tragamonedas":
                juego=prompt("Casino","Reingrese el juego")

            contador_ganadores+=1

            #Promedio de dinero ganado en Ruleta.
            match (juego):
                case "Ruleta":
                    acumulador_ruleta+=importe_ganado
                    contador_ruleta+=1
                #Porcentaje de personas que jugaron en el Tragamonedas.
                case "Tragamonedas":
                     contador_tragamonedas+=1
                case "Poker":
                     contador_poker+=1
                     if contador_poker==1 or mayor_importe_poker<importe_ganado:
                        mayor_importe_poker= importe_ganado
                        mayor_ganador_poker= nombre

        
             #Nombre y género de la persona que más ganó.
             
            if contador_ganadores==1 or mayor_importe<importe_ganado:
                mayor_importe= importe_ganado
                mayor_ganador= nombre
                mayor_ganador_genero= genero
                persona_mas_gano=f"El jugador que mas gano es {mayor_ganador} y su genero es {mayor_ganador_genero}"

            contador_ganadores+=1
            continuar=question("Casino","Desea seguir ingresando")

        
         #Promedio de dinero ganado en Ruleta.
        if contador_ruleta ==0:
            mensaje_ruleta= "No se ingresaron jugadores de ruleta, no puedo calcular el promedio"
        else:
           promedio_ruleta=acumulador_ruleta/contador_ruleta
           mensaje_ruleta= f"El promedio de lo ganado en la ruleta es de {promedio_ruleta}"
        #Porcentaje de personas que jugaron en el Tragamonedas.
        if contador_tragamonedas==0:
            mensaje_tragamonedas="No se ingresaron jugadores de tragamonesas, su porcentaje es 0%"
        else:
            porcentaje_tragamonedas=(contador_tragamonedas*100)/contador_ganadores
            mensaje_tragamonedas=F"El porcentaje de jugadores de tragamonedas es de {porcentaje_tragamonedas}%"

        #Cuál es el juego menos elegido por los ganadores.
        if contador_tragamonedas < contador_ruleta and contador_tragamonedas<contador_poker:
            juego_menos_ingresado="El juego menos ingresado es tragamonedas"
        elif contador_ruleta < contador_poker:
            juego_menos_ingresado="El juego menos ingresado es ruleta"
        else:
            juego_menos_ingresado="El juego menos ingresado es poker"
        #El nombre del jugador que ganó más dinero jugando Poker
        if contador_poker==0:
            mensaje_poker="No se ingresaron jugadores de poquer, no hay un mayor ganador"
        else:
            mensaje_poker=F"El jugador que mas gano jugando el poker es{mayor_ganador_poker}"
       
    
        #Salidas
# Nombre y género de la persona que más ganó.

# Promedio de dinero ganado en Ruleta.

# Porcentaje de personas que jugaron en el Tragamonedas.

# Cuál es el juego menos elegido por los ganadores.

# El nombre del jugador que ganó más dinero jugando Poker
        mensaje=(f"{persona_mas_gano}\n{mensaje_ruleta}\n{mensaje_tragamonedas}\n{juego_menos_ingresado}\n{mensaje_poker} ")


        alert("Casino",mensaje)
        
                    

           
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()