
from os import listdir

import numpy

class Loader:


	#Constructor
	def __init__( self, rute = "" ):

		self.rute = rute
		self.size = 0

		self.exchanges = []
		self.distances = []


	#Lectura de datos
	def load( self ):


		for arch in listdir( self.rute ):
			
			if( arch[4] == "1" and arch[6] == "d" ):


				row_pos = 0 #Posición de inserción de la fila
				col_pos = 0 #Posición de inserción de la columna
				change_mtx_type = False


				dfile = open( self.rute + "/" + arch, "r" )

				data = dfile.read().split()

				#Sacamos de la lista la primera posición y la guardamos en el tamaño de la matriz que crearemos
				self.size = int(data.pop(0))

				matrix = numpy.empty( (self.size, self.size), int )

				for itm in data:

					matrix[row_pos][col_pos] = int(itm)
					col_pos += 1

					if( col_pos == self.size ):

						col_pos = 0
						row_pos += 1

						if ( row_pos == self.size ):

							if( change_mtx_type == False):
								
								self.exchanges.append( matrix )
								matrix = numpy.empty( (self.size, self.size), int )
								row_pos = 0
								change_mtx_type = True
								

							else:
					
								self.distances.append( matrix )

								

				


			
