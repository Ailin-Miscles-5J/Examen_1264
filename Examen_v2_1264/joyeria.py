class joyeria_1264:
    print("")

def Empleados_1264(self):
    print("")
empleados_1264 = {
    "Nombre" : "Ailin",
    "Edad" : 25,
    "Direccion" : "calle cualquiera 123",
    "Id_empleado" : 1234,
    "Telefono" : 6561087676,
    "Correo" : "ailinruv@gmail.com",
    "Sexo" : "Femenino"
}
print("  Empleados")
for a, b in empleados_1264.items():
    print(a, b)

def Productos_1264(self):
    print("")
productos_1264 = {
    "Nombre" : "Anillo",
    "Id_Producto" : 2535,
    "Precio Venta" : "$25",
    "Stock" : 200,
    "Especificaciones" : "Color rosa gold",
    "Medidas" : "2cm",
    "Precio Compra" : "$10"
}
print("\n Productos")
for c, d in productos_1264.items():
    print(c, d)

def Distribuidores_1264(self):
    print("")
distribuidores_1264 = {
    "Nombre" : "Renata",
    "Telefono" : 6561958205,
    "Correo" : "renataron@gmil.com",
    "Ciudad" : "Juarez",
    "Id_Distribuidor" : 3444,
    "Edad" : 40,
    "Costos" : "$300"
}
print("\n Disribudores")
for e, f in distribuidores_1264.items():
    print(e, f)

def Sucursal_1264(self):
    print("")
sucursal_1264 = {
    "Direccion" : "Av. Las torres 345",
    "Telefono" : 6567105295,
    "Correo" : "sucursaltorres@gail.com",
    "Horario" : "10 am - 6 pm",
    "Id_Sucursal" : 21619,
    "Contidad de Empleados" : 100,
    "Ciudad" : "Juarez"
}
print("\n Sucursal")
for g, h in sucursal_1264.items():
    print(g, h)

obj_1264 = joyeria_1264()


obj_1264.Sucursal_1264()
obj_1264.Distribuidores_1264()
obj_1264.Productos_1264()
obj_1264.Empleados_1264()