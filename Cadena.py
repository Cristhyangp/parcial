from sys import argv
'''print("Hola Señor : "+nombre)
print(len(nombre))
print(nombre.find('{'))
print(nombre.rfind('}')) '''
#falta validación de las comas y ya 


class Cadena:
    
    
    def __init__(self,conjunto):
        self.conjunto = conjunto
    
   
    def validar(self,conjunto):

        if conjunto.count(',,')==0 and conjunto.find(',')!=3 and conjunto.rfind(',')!=len(conjunto)-2 and conjunto.find('=')==1 and conjunto.find('{')==2 and conjunto.rfind('}')==len(conjunto)-1 and conjunto.count('}')==1 and conjunto.count('{')==1:
        
            #respuesta=sum(1 for c in conjunto if c.isdigit())
            #print(respuesta)
            print("sintaxis correcta")
            print()
        else:
            print("error")


        

    def validarVacio(self,conjunto):

        if len(conjunto) is 0:
            print("error")
        else:
            print("No está vacío")

