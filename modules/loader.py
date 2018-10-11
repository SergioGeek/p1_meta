
from os import listdir

import numpy

class Loader:


	#Constructor
	def __init__( self, rute = "" ):

		self.rute = rute
		self.size = 0
		
		#Atributos para los ficheros de datos
		self.dfile_exchange = {} #Diccionario que por nombre de archivo guarda su solución
		self.dfile_distance = {} #Diccionario que por nombre de archivo guarda su solución
		self.sfile_solution = {} #Diccionario que por nombre de archivo guarda su solución
		self.sfile_cost = {} #Diccionario que por nombre de archivo guarda


	#Lectura de datos
	def load( self ):

		#Leemos todos los datos de la ruta que se pasa
		for arch in listdir( self.rute ):
			
			if( arch[6] == "d" ): #Para saber si es un .dat

				row_pos = 0 #Posición de inserción de la fila
				col_pos = 0 #Posición de inserción de la columna
				change_mtx_type = False #Variable para cambiar la matriz (intercambio -> distancias)


				dfile = open( self.rute + "/" + arch, "r" ) #Se habre el fichero

				data = dfile.read().split() #Se eliminan todos los espacios del fichero

				#Sacamos de la lista la primera posición y la guardamos en el tamaño de la matriz que crearemos
				self.size = int(data.pop(0))
				#Matriz en la que se almacenarán los datos y se guardará en diccionario correspodiente
				matrix = numpy.empty( (self.size, self.size), int )

				for itm in data: #Se recorren todos los valore

					matrix[row_pos][col_pos] = int(itm) #Se inserta el valor
					col_pos += 1

					if( col_pos == self.size ): #Si la columna es igual que el tamaño de la matriz, 
								    # hemos rellenado la línea y  cambiamos a otra
						col_pos = 0
						row_pos += 1

						if ( row_pos == self.size ): #Si la línea es igula que el tamaño de la matriz,
									     # hemos rellenado una matriz y la cambiamos

							if( change_mtx_type == False): #Si la matriz no se ha cambiado...
								
								self.dfile_exchange[arch[0:5]] = matrix #Metemos la matriz de intercambios en su 														#estructura,
								matrix = numpy.empty( (self.size, self.size), int ) # limpiamos la matriz
								row_pos = 0
								change_mtx_type = True
								

							else:
					
								self.dfile_distance[arch[0:5]] = matrix #Metemos la matriz de distancias en 														#su estructura

			
			if( arch[6] == "s" ): #Para saber si es un .sln

				sfile = open( self.rute + "/" + arch, "r" ) #Se habre el fichero

				sln = sfile.read().split() #Se eliminan todos los espacios del fichero

				sln.pop(0) #Saco el tamaño que no interesa

				self.sfile_cost[arch[0:5]] = sln.pop(0)

				self.sfile_solution[arch[0:5]] = sln


				

				
