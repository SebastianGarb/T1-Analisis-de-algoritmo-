class PuestodeTrabajo:
    def __init__(self, codigo : int = 0, descripcion = "", areaSolicitante = "", plazasRequeridas : int = 0, sueldo : float = 0.0):
        self.codigo = codigo
        self.descripcion = descripcion
        self.areaSolicitante = areaSolicitante
        self.plazasRequeridas = plazasRequeridas
        self.sueldo = sueldo
    def __str__(self):
        return f"\nPuesto: {self.areaSolicitante} \n Codigo: {self.codigo} \n Descripcion: {self.descripcion} \n Sueldo: {self.sueldo} \n Meses de experiencia requeridos: {self.plazasRequeridas}\n"
    
    def __repr__(self):
        return f"\nPuesto: {self.areaSolicitante} \n Codigo: {self.codigo} \n Descripcion: {self.descripcion} \n Sueldo: {self.sueldo} \n Meses de experiencia requeridos: {self.plazasRequeridas}\n"
def buscaPuesto(lista, cod) -> bool:
        for c in lista:
            if c.codigo == cod.codigo or c.descripcion == cod.descripcion or c.areaSolicitante == cod.areaSolicitante:
                return True
        return False
def ordSeleccion(lista):
    n = len(lista)
    for puesto in range(n-1):
        posMayor = puesto
        for ver in range(puesto + 1, n):
            if lista[ver].codigo > lista[posMayor].codigo:
                posMayor = ver
        lista[puesto], lista[posMayor] = lista[posMayor], lista[puesto]


lista = []

while True:
    opc = int(input("1-Agregar puesto \n2-Listar puestos \n3-Borrar puesto \n4-Buscar sueldo \n5-Puesto a contratar \n9-Salir\n"))
    if opc == 1:
        codigo = int(input("Ingrese codigo:"))
        areaSolicitante = input("Ingrese el area que se solicita:")
        if(len(areaSolicitante) >= 3):
            
            descripcion = input("Ingrese la descripcion del puesto:")
            sueldo = float(input("Ingrese sueldo:"))
            plazasRequeridas = int(input("Ingrese las plazas requeridas del puestro:"))

            nuevo = PuestodeTrabajo(codigo,descripcion, areaSolicitante, plazasRequeridas, sueldo)
        
            if not buscaPuesto(lista, nuevo):
                print(nuevo)
                lista.append(PuestodeTrabajo(codigo,descripcion,areaSolicitante, plazasRequeridas, sueldo))
                print(len(lista))
        else: print("el area solicitante debe tener por lo menos 3 letras")

        
    elif opc == 2:
        print(lista)
    elif opc == 3:
        ordSeleccion(lista)
        elicod = int(input("ingrese puesto a eliminar\n"))
        
        for idx, q in enumerate(lista):
            if q.codigo == elicod:
                del lista[idx]
    elif opc == 4:
        ordSeleccion(lista)
        elicod = int(input("ingrese el codigo para buscar el sueldo\n"))

        for idx, q in enumerate(lista):
            if q.codigo == elicod:
                print(f"El sueldo del puesto es {q.sueldo}") 
            else : print("no se encontro el puesto")
    elif opc == 5:
        ordSeleccion(lista)
    elif opc == 9:
        break



