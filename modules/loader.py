
from os import listdir

import numpy

class Loader:


	#Constructor
	def __init__( self, rute = "" ):

		self.rute = rute

		self.excanges = []
		self.distances = []


	#Loading the data
	def load( self ):


		for arch in listdir( self.rute ):
			
			if( arch[6] == "d" ):


				pfile = open( self.rute + "/" + arch, "r" )


			
