

import operator



def greedy( self, x_matrix, d_matrix ):

	
	sol = []

	x_aux = {} #Almacenamiento de los sumatorios del flujo de intercambio de piezas
	d_aux = {} #Alamacenamiento de las distancias de unidad

	x_counter = 0
	d_counter = 0
	

	#Recorro las matrices línea a línea, y realizo su sumatorio para guardarlo en su estructura
	for idx, x_row, d_row in enumerate( x_matrix ), d_matrix:

		for x_item, d_item in x_row, d_row:

			x_counter += x_item
			d_counter += d_item

		x_aux[idx] = x_counter
		d_aux[idx] = d_counter

		x_counter = 0
		y_counter = 0


	exchanges = sorted( x_aux.items(), key = operator.itemgetter(1) )

	exchages.reverse()

	distances = sorted( d_aux.items(), key = operator.itemgetter(1) )

	
	for e, d in exchages, distances:

		sol.insert( e.first, d.fisrt )


	return sol



	
