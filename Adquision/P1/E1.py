class AFD:
    def __init__(self, estados, alfabeto, transiciones, estado_inicial, estados_finales):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transiciones = transiciones # Diccionario de diccionarios: {estado: {letra: siguiente_estado}} OJO: hay que incluir todos los simbolos del diccionario y sus transiciones(si no no funciona xd)
        self.estado_inicial = estado_inicial
        self.estados_finales = estados_finales

    def procesar_cadena(self, cadena):
        estado_actual = self.estado_inicial
        for simbolo in cadena:
            if estado_actual in self.transiciones and simbolo in self.transiciones[estado_actual]:
                estado_actual = self.transiciones[estado_actual][simbolo]
            else:
                return False # Símbolo no válido o transición inexistente

        return estado_actual in self.estados_finales

# Un AFD que acepta cadenas que conjetngan -ajo- 
estados = {'q0', 'q1', 'q2'}
alfabeto = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '}

# Transiciones: {estado_actual: {símbolo_entrada: siguiente_estado}}
transiciones = {
    'q0': {'a': 'q1', 'b': 'q0', 'c': 'q0', 'd': 'q0', 'e': 'q0', 'f': 'q0', 'g': 'q0', 'h': 'q0', 'i': 'q0', 'j': 'q1', 'k': 'q0', 'l': 'q0', 'm': 'q0', 'n': 'q0', 'o': 'q0', 'p': 'q0', 'q': 'q0', 'r': 'q0', 's': 'q0', 't': 'q0', 'u': 'q0', 'v': 'q0', 'w': 'q0', 'x': 'q0', 'y': 'q0', 'z': 'q0', ' ': 'q0'},
    'q1': {'j': 'q1', 'a': 'q1', 'b': 'q0', 'c': 'q0', 'd': 'q0', 'e': 'q0', 'f': 'q0', 'g': 'q0', 'h': 'q0', 'i': 'q0', 'k': 'q0', 'l': 'q0', 'm': 'q0', 'n': 'q0', 'o': 'q2', 'p': 'q0', 'q': 'q0', 'r': 'q0', 's': 'q0', 't': 'q0', 'u': 'q0', 'v': 'q0', 'w': 'q0', 'x': 'q0', 'y': 'q0', 'z': 'q0', ' ': 'q0'},
    'q2': {'o': 'q2', 'a': 'q1', 'b': 'q0', 'c': 'q0', 'd': 'q0', 'e': 'q0', 'f': 'q0', 'g': 'q0', 'h': 'q0', 'i': 'q0', 'j': 'q1', 'k': 'q0', 'l': 'q0', 'm': 'q0', 'n': 'q0', 'p': 'q0', 'q': 'q0', 'r': 'q0', 's': 'q0', 't': 'q0', 'u': 'q0', 'v': 'q0', 'w': 'q0', 'x': 'q0', 'y': 'q0', 'z': 'q0', ' ': 'q0'},
}
estado_inicial = 'q0'
estados_finales = {'q2'}

# Crear el autómata
mi_afd = AFD(estados, alfabeto, transiciones, estado_inicial, estados_finales)

# Probar con algunas cadenas
# print(f"Cadena 'bba': {mi_afd.procesar_cadena('estar')}") # Debería ser False 
# print(f"Cadena 'baba': {mi_afd.procesar_cadena('majo')}") # Debería ser True
# print(f"Cadena 'abb': {mi_afd.procesar_cadena('maja')}") # Debería ser False

# Probemos ahora con una cadena de entrada por terminal
cadena = str(input("Introduce una cadena para verificar si es aceptada por el AFD: "))
print(f"Cadena '{cadena}': {mi_afd.procesar_cadena(cadena)}")