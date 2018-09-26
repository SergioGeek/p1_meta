
from os import listdir

import numpy


class Loader:


	#Constructor
	def __init__( self, rute = "" ):

		self.rute = rute

		self.size = 0

		self.excanges = []
		self.distances = []


	#Loading the data
	def load( self ):

		size_counter = 0

		for arch in listdir( self.rute ):
			
			if( arch[6] == "d" ):
				print("Nuevo archivoooooooooo")

				for idx, line in enumerate(open( self.rute + "/" + arch, "r" )):

					cleaned_line = line.split()

					if( len(cleaned_line) != 0 ):
				
						if( idx == 0 ):
						
							self.size = int( cleaned_line[0] )
							matrix = numpy.empty(( self.size, self.size ))

					
						else:
							print(len(cleaned_line))
							size_counter += len( cleaned_line )
						
						
						
						

				size_counter = 0


		#break
