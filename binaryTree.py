

class Nodo:
	def __init__(self, nombre=None,cedula=None,izq=None,der=None):
		self.nombre= nombre
		self.cedula=cedula
		self.izq= izq
		self.der= der

	def __str__(self):
		return self.nombre+": " + self.cedula

class BinaryTree:
	def __init__(self):
		self.raiz = None

	def agregar(self,elemento): #elemento es de tipo nodo
		if self.raiz== None:
			self.raiz = elemento #se hace una unica vez, para identificar la raiz

		else:
			aux= self.raiz #aux siempre empieza por la raiz
			padre = None #es la referencia para saber cual es el nodo padre, antes de entrar a
			#explorar con aux, gracias a padre es que podemos asignar hijos al nodo
			while aux != None:#si el elemento no tiene una referencia a izq o der significa que es null y ahi terminaria 
				padre = aux
				#aux es el que va explorando por derecha e izq, pero puede encontrar un ref a null
				if int(elemento.cedula) >= int(aux.cedula):
					aux = aux.der #el aux.der puede estar en null o tener datos
				else:
					aux = aux.izq

			#en este punto se fija que elemento a izq/der va a tener el nodo
			#ya sea a izq o der, ya no va a estar en null, eso ayuda a saber que el nodo tiene hijos
			if int(elemento.cedula) >= int(padre.cedula):
				padre.der = elemento #se el asigna al nodo padre un hijo por derecha
			else:
				padre.izq = elemento

	#raiz, izq, der	
	def preorden(self, elemento):
		if elemento != None:
			print(elemento) #lo 1ero que recibe es la raiz, entonces se imprime
			self.preorden(elemento.izq)#llamado recursivo enviando el hijo de la izq
			self.preorden(elemento.der)#cuando se exploro toda la parte izq, se imprimen todos los de derecha

	#izq, der, raiz
	def posorden(self, elemento):
		if elemento != None:
			self.posorden(elemento.izq)
			self.posorden(elemento.der)
			print (elemento)#luego que explora e imprime izq  y derecha,por ultimo 
			#imprime la raiz

	# izq, raiz, der
	def inorden(self, elemento):
		if elemento != None:
			self.inorden(elemento.izq)
			print (elemento)
			self.inorden(elemento.der)

	def getRaiz(self):
		return self.raiz 

if __name__ == "__main__":
	tree = BinaryTree()
	while (True):
		print("--Menu--\n"+
			"1.Agregar\n"+
			"2.preorden\n"+
			"3.postorden\n"+
			"4.inorden\n")
		num = input("ingrese la op: ")
		if num == 1:
			nombre = raw_input("ingrese nom: ")
			cedula = raw_input("ingrese la ced: ")
			nodo = Nodo(nombre,cedula)
			tree.agregar(nodo)
		elif num ==2:
			print "imprimiendo en preorden"
			tree.preorden(tree.getRaiz())
		elif num ==3:
			print "imprimiendo en posorden"
			tree.posorden(tree.getRaiz())
		elif num ==4:
			print "imprimiendo en inorden"
			tree.inorden(tree.getRaiz())


