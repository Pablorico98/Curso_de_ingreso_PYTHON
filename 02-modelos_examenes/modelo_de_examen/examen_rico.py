import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Rico    Pablo Ignacio DNI 41399313 Division "i"


De 20 contenedores que llegan al puerto de Rosario, se deben pedir y validar los siguientes datos
Marca (no validar)
Categoría (peligroso, comestible, indumentaria)
Peso ( entre 100 y 800)
Tipo de material ( aluminio, hierro , madera)
Costo en $ (mayor a 0)
Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue tipo de material más usado ( aluminio, hierro , madera)
Informe B- El porcentaje de contenedores de Categoría peligroso
Informe C- La marca y tipo del contenedor más pesado
Informe D- La marca del contenedor de comestible con menor costo
Informe E- El promedio de costo de todos los contenedores de HIerro

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        #ingresos
        contador_contenedores=0
        contador_aluminio=0
        contador_hierro=0
        contador_madera=0
        contador_peligroso=0
        contador_comestibles=0
        acumulador_costo_contenedor_hierro=0
        #proceso
        while contador_contenedores <5:

            #validaciones 
            marca=prompt("UTN","Ingrese la marca de contenedor")
            categoria=prompt("UTN","Ingrese la categoria del contenedor ")
            while categoria==None or (categoria!="peligroso" and categoria!="comestible" and categoria!= "indumentaria"):
                categoria=prompt("UTN", "Reingrese categoria del contenedor")
            peso=prompt("UTN","Ingrese el peso del contenedor")
            while peso==None or not(peso.isdigit()) or float(peso) <100 or float(peso)>800:
                peso=prompt("UTN","Reingrese el peso del contenedor")
            peso=float(peso)
            material=prompt("UTN", "Ingrese el material del contenedor")
            while material==None or (material !="aluminio" and material !="hierro" and material != "madera"):
                material=prompt("UTN", "Reingrese el material del contenedor")
            costo=prompt("UTN","ingrese el costo del contenedor")
            while costo==None or not(costo.isdigit()) or float(costo) <0:
                costo=prompt("UTN","Reingrese el costo del contenedor")
            costo=float(costo)

            #Informe A- Cuál fue tipo de material más usado ( aluminio, hierro , madera)
            match(material):
                case "aluminio":
                    contador_aluminio+=1
                case "hierro":
                    contador_hierro+=1
                    #Informe E- El promedio de costo de todos los contenedores de HIerro
                    acumulador_costo_contenedor_hierro+=costo
                case "madera":
                    contador_madera+=1

            #Informe B- El porcentaje de contenedores de Categoría peligroso
                    
            match(categoria):
                case "peligroso":
                    contador_peligroso+=1
            #Informe D- La marca del contenedor de comestible con menor costo
                case"comestible":
                    contador_comestibles+=1
                    if contador_comestibles==1 or contenedor_comestibles_menor_costo > costo:
                        contenedor_comestibles_menor_costo=costo
                        marca_contenedor_comestibles_menor_costo=marca

            #Informe C- La marca y tipo del contenedor más pesado
                    
            if contador_contenedores ==0 or contenedor_mas_pesado < peso:
                contenedor_mas_pesado=peso
                marca_contenedor_mas_pesado=marca
                material_contenedor_mas_pesado=material             
            
            contador_contenedores+=1

        #Informe A- Cuál fue tipo de material más usado ( aluminio, hierro , madera)
            
        if contador_aluminio > contador_hierro and contador_aluminio>contador_madera:
            material_mas_usado="El material mas usado es aluminio \n"
        elif contador_hierro > contador_madera:
            material_mas_usado="El material mas usado es hierro \n"
        else:
            material_mas_usado="El material mas usado es madera \n"

        mensaje=material_mas_usado
        
        #Informe B- El porcentaje de contenedores de Categoría peligroso

        if contador_peligroso > 1:
            porcentaje_contador_peligroso=(contador_peligroso*100)/20
        else:
            porcentaje_contador_peligroso=0
            
        mensaje_porcentaje_contador_peligroso= f"El porcentaje de los contenedores de categoria peligroso es de {porcentaje_contador_peligroso}%\n"
        mensaje+=mensaje_porcentaje_contador_peligroso

        #Informe C- La marca y tipo del contenedor más pesado

        mensaje_marca_tipo_contenedor_mas_pesado=f"La marca del contenedor mas pesado es {marca_contenedor_mas_pesado} y su tipo es {material_contenedor_mas_pesado}\n"
        mensaje+=mensaje_marca_tipo_contenedor_mas_pesado
        
        #Informe D- La marca del contenedor de comestible con menor costo

        if contador_comestibles>0:
            mensaje_marca_contenedor_menor_costo=f"La marca del contenedor de comestibles de menor costo es {marca_contenedor_comestibles_menor_costo}\n"
        else:
            mensaje_marca_contenedor_menor_costo="No hay contenedores de comestibles, no se puede calcular cual es el contenedor de combustibles de menor costo\n"
        mensaje+=mensaje_marca_contenedor_menor_costo

        #Informe E- El promedio de costo de todos los contenedores de HIerro

        if acumulador_costo_contenedor_hierro > 0:
            promedio_costo_contenedor_hierro=acumulador_costo_contenedor_hierro/contador_hierro
            mensaje_promedio_costo_contenedor_hierro=F"El promedio del costo de todos los contenedores de hierro es {promedio_costo_contenedor_hierro}"
        else:
            mensaje_promedio_costo_contenedor_hierro="No hay contenedores de hierro, no se puede calcular el promedio del costo de los mismos"

        mensaje+=mensaje_promedio_costo_contenedor_hierro




        #salidas

        alert("UTN",mensaje)


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()