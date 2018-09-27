
from os import listdir

import numpy


class Loader:


	#Constructor
	def __init__( self, rute = "" ):

		self.rute = rute

		self.size = 0

		self.exchanges = []
		self.distances = []


	#Loading the data
	def load( self ):

		size_counter = 0
		

		for arch in listdir( self.rute ):

			

			#Diferencio si es un archivo .dat o un .sln dentro de la carpeta			
			if( arch[4] == "1" and arch[6] == "d" ):

				row_pos = 0 #Posición de inserción de la fila
				col_pos = 0 #Posición de inserción de la columna

				print( arch )
				change_mtx_type = False

				#Recorro línea a línea el fichero abierto
				for idx, line in enumerate(open( self.rute + "/" + arch, "r" )):


					#Limpio la línea de espacios en blanco quedándome con los datos
					cleaned_line = line.split()
					
					#Verificamos que la línea tenga datos
					if( len(cleaned_line) != 0 ):

						#Si estamos en la primera línea (primera iteración) nos quedamos con el tamaño y creamos la matriz
						if( idx == 0 ):
						
							self.size = int( cleaned_line[0] )
							matrix = numpy.empty(( self.size, self.size ))
				
						else:
							
							if( col_pos == self.size ):
	
								if ( row_pos < self.size ):
									
									row_pos += 1
									col_pos = 0
									

	
								else:
									print( "Termino de matriz--------------------------")
									if ( change_mtx_type == False ):

										self.exchanges.append( matrix )
										change_mtx_type = True
										row_pos += 0

									else:
										
										self.distances.append( matrix)
									
									matrix = numpy.empty(( self.size, self.size ))

							else:
								
								for dinx in cleaned_line:
								
									matrix[row_pos][col_pos] = dinx
									col_pos += 1
							

