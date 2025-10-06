class ReflexAgent2Room:
	def __init__(self):
		# Reflex agent initialization
		# Reflex agents act solely based on the current percept and do not store internal state
		pass

	def __str__(self):
		# Provides a string representation of the reflex agent
		return "Reflex Agent"

	def selectAction(self, percept):
		"""
		YOUR CODE GOES HERE
		"""

		# print(f"Selecting action based on percept: {percept}")  # Debugging output
		# Si estoy en la habitacion izquierda y esta sucia, limpio
		if percept["agent_location"] == "L" and percept["dirty"]:
			action = "clean"
		# Si estoy en la habitacion izquierda y esta limpia, me muevo a la derecha
		elif percept["agent_location"] == "L" and not percept["dirty"]:
			action = "moveR"
		# Si estoy en la habitacion derecha y esta sucia, limpio
		elif percept["agent_location"] == "R" and percept["dirty"]:
			action = "clean"
		# Si estoy en la habitacion derecha y esta limpia, me muevo a la izquierda
		elif percept["agent_location"] == "R" and not percept["dirty"]:
			action = "moveL"
		return action  # Return the chosen action
		# pass -- No es por tirar hate, pero no hace falta y me rallo demasiado la cabeza con el pass por que se quedaba bugeado

		pass

	def execAction(self, action, environment):
		# Executes the chosen action by modifying the environment's state
		environment.setEnvironment(action)

	def perceiveAndAct(self, environment):
		# This method manages the process of perception and action execution
		# 1. Get the current percept from the environment
		percept = environment.getPerceptFromEnvironment()
		print(f"Perceived: {percept}")  # Output the percept for clarity

		# 2. Select an action based on the percept
		action = self.selectAction(percept)
		print(f"Action selected: {action}")  # Output the selected action

		# 3. Execute the selected action and update the environment's state
		self.execAction(action, environment)
		print(
			f"New Environment state: {environment}"
		)  # Output the updated environment state


class MemoryAgentNRooms:
	def __init__(self):
		# Initialize the memory to store the agent's last two actions
		self.memory = []  # Memory is initially empty

	def __str__(self):
		# Provides a string representation of the memory-based agent
		return "Memory-based Agent"

	def selectAction(self, percept):
		"""
		YOUR CODE GOES HERE
		"""
		memoria = self.memory

		# Si está sucio y (estoy en pared o estoy yendo a la izquierda) → limpiar
		if percept["dirty"] and (percept["wall"] or (len(memoria) > 0 and memoria[-1] == "moveL")):
			action = "clean"

		# Si estoy en pared derecha y no está sucio → mover a la izquierda
		elif percept["wall"] and len(memoria) > 0 and memoria[-1] == "moveR":
			action = "moveL"

		# Si estoy en pared izquierda y no está sucio → mover a la derecha
		elif percept["wall"] and (len(memoria) == 0 or memoria[-1] == "moveL"):
			action = "moveR"

		# Si no estoy en pared
		else:
			if len(memoria) > 0 and memoria[-1] == "moveL":
				action = "moveL"
			else:
				action = "moveR"

		return action
		pass

	def execAction(self, action, environment):
		# Executes the chosen action in the environment and updates the agent's memory

		# Update the environment's state based on the action
		environment.setEnvironment(action)

		# Add the action to the agent's memory (store up to the last two actions)
		self.memory.append(action)
		if len(self.memory) > 2:
			self.memory.pop(0)  # Keep only the last two actions in memory

	def perceiveAndAct(self, environment):
		# This method handles the perception and action execution process

		# 1. Get the current percept from the environment
		percept = environment.getPerceptFromEnvironment()
		print(f"Perceived: {percept}")  # Output the percept for clarity

		# 2. Select an action based on the percept and the agent's memory
		action = self.selectAction(percept)
		print(f"Action selected: {action}")  # Output the selected action

		# 3. Execute the selected action and update the environment
		self.execAction(action, environment)
		print(
			f"New Environment state: {environment}"
		)  # Output the updated environment state


class MemoryAgentNXNRooms:
	def __init__(self):
		# Initialize a memory-based agent that stores its last two actions.
		self.memory = []  # Memory starts empty

	def __str__(self):
		# Provide a string representation of the memory-based agent.
		return "Memory-based Agent"

	def selectAction(self, percept):
		"""
		YOUR CODE GOES HERE
		"""
		walls = percept['walls']
		memoria = self.memory
		
		# Si la memoria no tiene 2 acciones, inicializar con acciones por defecto
		if len(memoria) < 2:
			# Prioridad: limpiar si está sucio
			if percept['dirty']:
				return "clean"
			# Movimiento inicial: intentar derecha, si no izquierda, si no arriba si no abajo
			if 'R' not in walls:
				return "moveR"
			elif 'L' not in walls:
				return "moveL"
			elif 'D' not in walls:
				return "moveD"
			else:
				return "moveU"
		
		# PRIORIDAD 1: Limpiar si está sucio
		if percept['dirty']:
			return "clean"
		
		# PRIORIDAD 2: Después de limpiar, continuar en la misma dirección
		if memoria[-1] == "clean":
			# Inferir dirección basada en la acción anterior a limpiar
			if len(memoria) >= 2:
				accion_anterior = memoria[-2]
			else:
				accion_anterior = "moveR"  # Por defecto
			
			if accion_anterior == "moveR" and 'R' not in walls:
				return "moveR"
			elif accion_anterior == "moveL" and 'L' not in walls:
				return "moveL"
			elif accion_anterior == "moveU" and 'U' not in walls:
				return "moveU"
			elif accion_anterior == "moveD" and 'D' not in walls:
				return "moveD"
		
		# PRIORIDAD 3: Después de bajar, cambiar dirección horizontal
		if memoria[-1] == "moveD":
			# Alternar dirección basada en el historial
			if len(memoria) >= 2:
				accion_anterior = memoria[-2]
				if accion_anterior == "moveR":
					if 'L' not in walls:
						return "moveL"  # Cambiar a izquierda
				elif accion_anterior == "moveL":
					if 'R' not in walls:
						return "moveR"  # Cambiar a derecha
			
			# Por defecto, intentar derecha o izquierda
			if 'R' not in walls:
				return "moveR"
			elif 'L' not in walls:
				return "moveL"
		
		# PRIORIDAD 4: Movimiento continuo en dirección horizontal
		if memoria[-1] == "moveR" and 'R' not in walls:
			return "moveR"
		elif memoria[-1] == "moveL" and 'L' not in walls:
			return "moveL"
		elif memoria[-1] == "moveU" and 'U' not in walls:
			return "moveU"
		elif memoria[-1] == "moveD" and 'D' not in walls:
			return "moveD"
		
		# PRIORIDAD 5: Si no podemos movernos horizontalmente, bajar
		if (memoria[-1] == "moveR" or memoria[-1] == "moveL") and 'D' not in walls:
			return "moveD"
		
		# PRIORIDAD 6: Si no podemos bajar, intentar subir
		if 'U' not in walls:
			return "moveU"
		
		# PRIORIDAD 7: Si todo falla, cambiar dirección horizontal
		if memoria[-1] == "moveR" and 'L' not in walls:
			return "moveL"
		elif memoria[-1] == "moveL" and 'R' not in walls:
			return "moveR"
		
		# ÚLTIMO RECURSO: Movimiento aleatorio seguro
		if 'R' not in walls:
			return "moveR"
		elif 'L' not in walls:
			return "moveL"
		elif 'D' not in walls:
			return "moveD"
		elif 'U' not in walls:
			return "moveU"
		else:
			return "clean"  # No hay movimiento posible
		pass

	def execAction(self, action, environment):
		# Executes the agent's action and updates the environment accordingly.
		environment.setEnvironment(
			action
		)  # Update the environment based on the chosen action

		# Add the action to the agent's memory, maintaining only the last two actions.
		self.memory.append(action)
		if len(self.memory) > 2:
			self.memory.pop(0)  # Limit memory to the last two actions

	def perceiveAndAct(self, environment):
		# Handle the process of perception and action execution.

		# 1. Get the current percept from the environment.
		percept = environment.getPerceptFromEnvironment()
		print(f"Perceived: {percept}")  # Output the percept for clarity

		# 2. Select an action based on the percept and the agent's memory.
		action = self.selectAction(percept)
		print(f"Action selected: {action}")  # Output the selected action

		# 3. Execute the selected action and update the environment.
		self.execAction(action, environment)
		print(
			f"New Environment state: {environment}"
		)  # Output the updated environment state
