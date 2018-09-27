
from modules.loader import Loader



if __name__ == "__main__":


	prueba = Loader( "/home/anonymous/Desktop/datos" )

	prueba.load()


	print( prueba.exchanges[0] )
