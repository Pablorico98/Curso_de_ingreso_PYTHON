import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Enunciado 1 : De 5  personas que ingresan al hospital se deben tomar y validar los siguientes datos.

nombre , 
temperatura, entre 35 y 42 
sexo( f, m , nb ) 
 edad(mayor a 0)
pedir datos por prompt y mostrar por print
Punto A-informar cual fue el sexo mas ingresado
Punto B-el porcentaje de personas con fiebre y el porcentaje sin fiebre

Punto C - por el número de DNI del alumno
DNI terminados en  0 o 1

1)informar la cantidad de personas de sexo  femenino
2) la edad promedio de  personas de sexo  masculino
3) el nombre de la persona la persona de sexo  nb con más temperatura(si la hay)


DNI terminados en  2 o 3

1) informar la cantidad de personas de sexo  masculino
2) la edad promedio de  personas de sexo  nb
3) el nombre de la persona de sexo  femenino  con la temperatura mas baja(si la hay)


DNI terminados en  4 o 5

1)informar la cantidad de personas de sexo  nb
2) la edad promedio de  personas de sexo  femenino
3) el nombre de la persona  la persona de sexo  masculino con la temperatura mas baja(si la hay)


DNI terminados en  6 o 7

1)informar la cantidad de personas mayores de edad (desde los 18 años)
2)la edad promedio en total de todas las personas mayores de edad (18 años)
3) el nombre de la persona  la persona de sexo  masculino con la temperatura mas baja(si la hay)


DNI terminados en  8 o 9

1))informar la cantidad de personas menores de edad (menos de 18 años)
2)la temperatura promedio en total de todas las personas menores de edad
3) el nombre de la persona de sexo  femenino  con la temperatura mas baja(si la hay)


Todos los alumnos: 
B-informar cual fue el sexo mas ingresado 
C-el porcentaje de personas con fiebre y el porcentaje sin fiebre

'''
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Registrar", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        #Inicializo las variables
        contador_f=0
        contador_m=0    
        contador_nb=0
        contador_fiebre=0
        acumulador_nb=0
        total_usarios=0
        
        #proceso
        while total_usarios <5:
            
            nombre=prompt("UTN","Ingrese el nombre del paciente: ")
            while nombre==None or not(nombre.isalpha()):
              nombre=prompt("UTN","reingrese el nombre del paciente: ")  
            
            temperatura=prompt("UTN","Ingrese la tempreratura del paciente: ")
            while temperatura== None or not(temperatura.isdigit()) or int(temperatura) < 35 or int(temperatura) > 42:
                temperatura=prompt("UTN","Reingrese la tempreratura del paciente: ")
            temperatura=int(temperatura)

            sexo=prompt("UTN","Ingrese el sexo")
            while sexo==None or  not(sexo.isalpha()) or (sexo!="f" and sexo!="m" and sexo!="nb"):
                sexo=prompt("UTN","Reingrese el sexo")

            edad=prompt("UTN","Ingrese la edad del paciente: ")
            while edad== None or not(edad.isdigit()) or int(edad) < 0:
                edad=prompt("UTN","Reingrese la edad del paciente: ")
            edad=int(edad)
            #Punto A-informar cual fue el sexo mas ingresado
            match (sexo):
                case "f":
                    contador_f+=1
                    #3) el nombre de la persona de sexo  femenino  con la temperatura mas baja(si la hay)
                    if contador_f==1 or temperatura_baja_f<temperatura: 
                        temperatura_baja_f=temperatura
                        nombre_temperatura_baja_f=nombre

                case "m":
                    contador_m+=1
                case "nb":
                    contador_nb+=1
                    # 2) la edad promedio de  personas de sexo  nb
                    acumulador_nb+=edad
            #Punto B-el porcentaje de personas con fiebre y el porcentaje sin fiebre
            if temperatura > 37.5:
                contador_fiebre+=1
            
            total_usarios=contador_nb+contador_f+contador_m
            

        #Punto A-informar cual fue el sexo mas ingresado
        
        if contador_f >contador_m and contador_f>contador_nb:
            sexo_mas_ingresado="El sexo mas ingresado es f"
        elif contador_m > contador_nb:
            sexo_mas_ingresado="El sexo mas ingresado es m"
        else:
            sexo_mas_ingresado="El sexo mas ingresado es nb"
        
        #Punto B-el porcentaje de personas con fiebre y el porcentaje sin fiebre
        
        procentaje_con_fiebre=(contador_fiebre*100)/total_usarios
        procentaje_sin_fiebre=100-procentaje_con_fiebre

        # 2) la edad promedio de  personas de sexo  nb
        promedio_edad_nb=(acumulador_nb/contador_nb)


        #Salidas
        #Punto A-informar cual fue el sexo mas ingresado
        #Punto B-el porcentaje de personas con fiebre y el porcentaje sin fiebre
        # 1) informar la cantidad de personas de sexo  masculino
        # 2) la edad promedio de  personas de sexo  nb
        # 3) el nombre de la persona de sexo  femenino  con la temperatura mas baja(si la hay)
        if contador_f==0:
            nombre_temperatura_baja_f="No se ingresaron pacientes de genero femenino"
        mensaje = (f"{sexo_mas_ingresado}\n"
           f"El porcentaje de ingresos con fiebre es {procentaje_con_fiebre}%\n"
           f"El porcentaje de ingresos sin fiebre es {procentaje_sin_fiebre}%\n"
           f"La cantidad de ingresos masculinos es de {contador_m}\n"
           f"El promedio de edad de los ingresis nb es de {promedio_edad_nb}\n"
           f"La mujer con la temperatura mas baja es: {nombre_temperatura_baja_f}")



        alert("UTN",mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()