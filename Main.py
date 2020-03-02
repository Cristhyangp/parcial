from Cadena import Cadena
from sys import argv
from Operaciones import Operator

script, conjunto, conjunto2= argv

cadena=Cadena(conjunto)
cadena2=Cadena(conjunto2)
op=Operator(conjunto,conjunto2)

cadena.validar(cadena.conjunto)
cadena2.validar(cadena2.conjunto)

op.op_conjuntos(conjunto,conjunto2)

