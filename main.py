
from modules.loader import Loader



if __name__ == "__main__":


	prueba = Loader( "/home/anonymous/Desktop/datos" )

	prueba.load()
	
	for idx, df in enumerate( prueba.dfile_names ):

		print( "Nombre del fichero: " )
		print( prueba.dfile_names[idx] )
		print("Mostramos los intercambios" )
		print( prueba.exchanges[idx] )
		print("Mostramos las distancias" )
		print( prueba.distances[idx] )
