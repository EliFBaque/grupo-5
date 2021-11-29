#clase para crear y modificar ojetos usuarios

class usuario:
    def __init__(self, **kwarg):
        self.nombre = kwarg.get('nombre')
        self.apellido = kwarg.get('apellido')
        if kwarg.get('perfil'):
            self.perfil = kwarg.get('perfil')
    
    def compra(self, usuario, id):
        usuario.carro = id

    def set_perfil(self, perfil, usuario):
        usuario.perfil = perfil
       

    def __str__(self):
        return str(self.__dict__)
        #return f"Nombre: {self.__dict__['nombre']}, Apellido: {self.__dict__['apellido']}, perfil: {self.__dict__['perfil']}, Carro_ID: {self.__dict__['carro']}"

#clase carritos de compras con metodos para agregar productos
class carro(usuario):
    def __init__(self, id, usuario,):
        self.id=id
        self.productos=[]
        super().compra(usuario,id)

    def add(self, *args):
        for arg in args:
            self.productos.append(arg)
    
    def __str__(self):
        return str(self.__dict__)
        #return f"Carro: {self.id}. Productos: {self.productos}"


#Clase para crear perfiles y permisos
class perfil(usuario):
    def __init__(self, **kwarg):
        self.perfil=kwarg.get('perfil')
        self.permisos=[]
        if kwarg.get('usuario'):
            usuario.perfil=kwarg.get('perfil')
    
    def asignar_usuario(self, usuario):
        usuario.set_perfil(self.perfil, usuario)

    def add_permiso(self, *args):
        for arg in args:
             self.permisos.append(args)
    
    def __str__(self):
        return f"{self.perfil} : {self.permisos}"
    
#Crear usuario
usr1=usuario(nombre="Lucas", apellido="Rohatsch")

#crear perfil admin
admin=perfil(perfil="Administrador")

#asignar permisos al perfil
admin.add_permiso("listar_clientes", "listar_carritos", "detalle_productos")

#Asigna perfil al usuario
admin.asignar_usuario(usr1)

#crea carrito de compras para el usuario
carro1=carro("AR01",usr1)

#Agregar productos al carro
carro1.add("Lechuga", "jugo")
carro1.add("tomate")

#Crear perfil de reportero
report=perfil(perfil="Reportero")

#Establecer permisos del perfil
report.add_permiso("listar_clientes", "listar_carritos")

#Crear un usuario reportero
usr2=usuario(nombre="Juan", apellido="Perez", perfil=report.perfil)


print(usr1)
print(carro1)
print(usr2)
