class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        pass
    def mostrar_informacion(self):
        print("Codigo:", self.codigo)
        print("Nombre:", self.nombre)
        print("Precio:", self.precio)
        print("Cantidad:", self.cantidad)

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
    def aumentar_existencias(self,cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
Producto1 = Producto(98, "The legend of zelda", 100000, 47)
Producto2 = Producto(99, "Half life", 20000, 50)
Producto3 = Producto(100, "GTA VI", 300000, 30)
Producto4 = Producto(101, "FIFA 24", 70000, 20)


Producto1.actualizar_precio(120000)
Producto2.aumentar_existencias(10)
Producto3.actualizar_precio(10000)
Producto3.aumentar_existencias(9)
Producto1.mostrar_informacion()
Producto2.mostrar_informacion()
Producto3.mostrar_informacion()
Producto4.mostrar_informacion()
