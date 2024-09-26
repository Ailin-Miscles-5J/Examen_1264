class Distribuidores1264:
    nombre_1264 = ""
    Telefono_1264 = 0
    Correo_1264 = ""
    Ciudad_1264 = ""
    ID_dist_1264 = 0
    edad_1264 = 0
    costos_1264 = 0




print ("  Listas")
nombres_1264=["Renata","Alex","Dieguito","Alexis","Ailin","Katy","Kelly"]
nom_1264=len(nombres_1264)
print("Elementos que contiene la lista nombres:" , nombres_1264)
for ailin in nombres_1264:
    print(ailin)

print (" \n  Tuplas")
telefonos_1264=(656381852,6561056397,6562057502,6561057295,6561057295,6561057365,6561057294)
print(telefonos_1264)
for ailin in telefonos_1264:
    print (ailin)


def diccionario_1264(self):
    correo_1264= {
        "1:": "ailinruvalcaba@gmail.com",
        "2:": "renata@gmail.com",
        "3": "alexis@gmail.com",
        "4": "alex@gmail.com",
        "5": "katy@gmail.com",
        "6": "kelly@gmail.com",
        "7": "dieguito@gmail.com"
    }
    print(correo_1264)
    for lin,ai in correo_1264:
            print (lin,ai)

print(" \n  Funciones")
def correc_1264(mensa):
    print(f"{mensa}")
def incorrec_1264(mensa):
    print(f"{mensa}")

correc_1264("Se guardaron correctamente los datos para distribuidor")
incorrec_1264("No se guardarn correctamente los datos")

obj = Distribuidores1264()

obj.nombre_1264 = "Ailin"
obj.Telefono_1264 = 6561086483
obj.Correo_1264 = "Ailin@gmail.com"
obj.Ciudad_1264 = "Juarez"
obj.ID_dist_1264 = 12345
obj.edad_1264 = 20
obj.costos_1264 = 300