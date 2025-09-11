class AFD:
	def __init__(self, estados, alfabeto, transiciones, estado_inicial, estados_finales):
		self.estados = estados
		self.alfabeto = alfabeto
		self.transiciones = transiciones # Diccionario de diccionarios: {estado: {letra: siguiente_estado}} OJO: hay que incluir todos los simbolos del diccionario y sus transiciones(si no no funciona xd)
		self.estado_inicial = estado_inicial
		self.estados_finales = estados_finales

	def check_cadena(self, cadena_lower): # Funcion para checkear que la cadena solo este compuesta de simbolos que este en el alfabeto
		# No necesito convertir la cadena lower porque ya se la paso en minusculas
		for i in cadena_lower:
			if i not in self.alfabeto:
				return False
		return True

	def procesar_cadena(self, cadena):
		cadena_lower = cadena.lower()  # Convertir la cadena a minúsculas por si alguna de las letras de ajo estuviese en mayuscula
		cadena_ok = self.check_cadena(cadena_lower)
		if not cadena_ok:
			print(f"La cadena '{cadena}' contiene símbolos no válidos.")
			return False
			# Si la cadena contiene simbolos no validos, devolvemos False y no procesamos la cadena

			# Considero que es mas importante que la cadena sea valida a que la cadena a buscar este dentro de 
			# Por ejemplo, si la cadena a buscar es 'ajo' y el texto es 'ajoaj0', aunque la cadena 'ajo' esta en el texto, 
			# la cadena no es valida porque contiene un simbolo no valido (el 0), salta un error y automaticamente es False y no la analiza.
		estado_actual = self.estado_inicial
		for simbolo in cadena_lower:
			if estado_actual in self.transiciones and simbolo in self.transiciones[estado_actual]:
				estado_actual = self.transiciones[estado_actual][simbolo]
			else:
				return False # Símbolo no válido o transición inexistente
			if estado_actual == 'fin':
				return True
		return estado_actual in self.estados_finales

# Un AFD que acepta cadenas que conjetngan -ajo- 
estados = {'q0', 'q1', 'q2', 'fin'}
alfabeto = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '}

# Transiciones: {estado_actual: {símbolo_entrada: siguiente_estado}}
transiciones = {
	'q0': {'a': 'q1', 'b': 'q0', 'c': 'q0', 'd': 'q0', 'e': 'q0', 'f': 'q0', 'g': 'q0', 'h': 'q0', 'i': 'q0', 'j': 'q1', 'k': 'q0', 'l': 'q0', 'm': 'q0', 'n': 'q0', 'o': 'q0', 'p': 'q0', 'q': 'q0', 'r': 'q0', 's': 'q0', 't': 'q0', 'u': 'q0', 'v': 'q0', 'w': 'q0', 'x': 'q0', 'y': 'q0', 'z': 'q0', ' ': 'q0'},
	'q1': {'j': 'q2', 'a': 'q1', 'b': 'q0', 'c': 'q0', 'd': 'q0', 'e': 'q0', 'f': 'q0', 'g': 'q0', 'h': 'q0', 'i': 'q0', 'k': 'q0', 'l': 'q0', 'm': 'q0', 'n': 'q0', 'o': 'q2', 'p': 'q0', 'q': 'q0', 'r': 'q0', 's': 'q0', 't': 'q0', 'u': 'q0', 'v': 'q0', 'w': 'q0', 'x': 'q0', 'y': 'q0', 'z': 'q0', ' ': 'q0'},
	'q2': {'o': 'fin', 'a': 'q0', 'b': 'q0', 'c': 'q0', 'd': 'q0', 'e': 'q0', 'f': 'q0', 'g': 'q0', 'h': 'q0', 'i': 'q0', 'j': 'q0', 'k': 'q0', 'l': 'q0', 'm': 'q0', 'n': 'q0', 'p': 'q0', 'q': 'q0', 'r': 'q0', 's': 'q0', 't': 'q0', 'u': 'q0', 'v': 'q0', 'w': 'q0', 'x': 'q0', 'y': 'q0', 'z': 'q0', ' ': 'q0'},
	'fin': {'a': 'q1', 'b': 'q0', 'c': 'q0', 'd': 'q0', 'e': 'q0', 'f': 'q0', 'g': 'q0', 'h': 'q0', 'i': 'q0', 'j': 'q1', 'k': 'q0', 'l': 'q0', 'm': 'q0', 'n': 'q0', 'o': 'q0', 'p': 'q0', 'q': 'q0', 'r': 'q0', 's': 'q0', 't': 'q0', 'u': 'q0', 'v': 'q0', 'w': 'q0', 'x': 'q0', 'y': 'q0', 'z': 'q0', ' ': 'q0'},
}
estado_inicial = 'q0'
estados_finales = {'fin'}

# Crear el autómata
mi_afd = AFD(estados, alfabeto, transiciones, estado_inicial, estados_finales)

# Probar con algunas cadenas
# print(f"Cadena 'estar': {mi_afd.procesar_cadena('estar')}") # Debería ser False 
# print(f"Cadena 'majo': {mi_afd.procesar_cadena('majo')}") # Debería ser True
# print(f"Cadena 'maja': {mi_afd.procesar_cadena('maja')}") # Debería ser False

# Probemos ahora con una cadena de entrada por terminal
cadena = str(input("Introduce una cadena para verificar si es aceptada por el AFD: "))
# mi_afd.procesar_cadena(cadena)
print(f"Cadena '{cadena}': {mi_afd.procesar_cadena(cadena)}")