class ColaImpresion:
    def __init__(self,capacidadMax):
        self.capacidadMax=capacidadMax
        self.lista=[]

    def agregar_documento(self,nombre,paginas,urgente):
        if len(self.lista) < self.capacidadMax:
            nuevo_perfil = {
                "nombre": nombre,
                "paginas": paginas,
                "urgente": urgente
            }
            if urgente == True:
                self.lista.insert(0, nuevo_perfil) #a inicio
        
            else:
                self.lista.append(nuevo_perfil) #a final
        else: 
            print("Error por memoria llena")
        
    def imprimir_documento(self):
        if len(self.lista)>0:
            doc_actual = self.lista.pop(0)
            print(f" Imprimiendo documento: {doc_actual['nombre']}") #solo extraer el dato "nombre" de la variable
            return doc_actual
        else:
            print("no hay perfil agregado (esta vacío)")
            
mi_cola = ColaImpresion(3)
mi_cola.agregar_documento("cristian","19",True)
mi_cola.imprimir_documento()