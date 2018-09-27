
from os import listdir

import numpy

class Loader:


	#Constructor
	def __init__( self, rute = "" ):

		self.rute = rute

		self.exchanges = []
		self.distances = []


	#Lectura de datos
	def load( self ):


		for arch in listdir( self.rute ):
			
			if( arch[6] == "d" ):


				pfile = open( self.rute + "/" + arch, "r" )


			
