from Cadena import Cadena


class Operator(Cadena):


    def __init__(self,conjunto,conjunto2):
        Cadena.__init__ (self,conjunto)
        self.conjunto2=conjunto2



    def op_conjuntos(self,conjunto1,conjunto2):

        
        p=conjunto1.replace('{','').replace('}','').replace('=','').replace(',',' ')
        y=conjunto2.replace('{','').replace('}','').replace('=','').replace(',',' ')
        #print(p)
        #print(y)
        x=p[1:len(p)]
        a=y[1:len(y)]
        #print(x)
        #print(a)

        lista1=x.split()
        lista2=a.split()

        #print(lista1)
        #print(lista2)
        papa = set(lista1)
        arroz= set(lista2)
        #print(papa)
        #print(arroz)

        #Subconjunto 
        print("***Subconjunto**")
        print(papa.issubset(arroz))
        print("==============================")
        print ("Es A un subconjunto propio de B")
        print (papa.issubset(arroz) and papa != arroz)
        #igualdad
        print("***Igualdad**")
        print (papa == arroz)
        print("==============================")
        # Union de conjuntos
        print("***Union de conjuntos****")
        print (papa.union(arroz)) 
        print("==============================")
        print("***Interseccion de conjuntos***")
        # Intersección de conjuntos
        print (papa.intersection(arroz))
        print("==============================")
        # Diferencia entre conjuntos
        print("***Diferencia de conjuntos***")
        print (papa - arroz)
        print (arroz - papa)
        print("==============================")
        #Cardinalidad de un conjunto con len().
        print("**Cardinalidad de Conjuntos**")
        print(len(papa))
        #Invierte la cadena.
        print("**Invertir Cadena**")
        revertA = lista1[::-1]
        revertB = lista2[::-1]
        print("**Conjunto A**")
        print (revertA)
        print("**Conjunto B**")
        print (revertB)

        #concatenacion
        print("==================================")
        print(" concatenacion ")
        lista3=[]
        
        if(y.find("Ø")!=-1):
            print("Ø")      
        else:        
            for i in papa:
                for e in arroz:
                    lista3.append(i+e)
            print(lista3)

         










