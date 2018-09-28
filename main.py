
from modules.loader import Loader



if __name__ == "__main__":


	prueba = Loader( "/home/anonymous/Desktop/datos" )

	prueba.load()

	print("Mostramos los intercambios" )
	print( prueba.exchanges[0] )
	print("Mostramos las distancias" )
	print( prueba.distances[0] )
