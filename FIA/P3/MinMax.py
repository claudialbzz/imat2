def juego_division(n):
    """
    Juego simple: empezando en n, turnos de MAX y MIN
    Movimientos: n-1 o n//2
    Gana quien deje el 0 al oponente
    """
    
    def evaluar(estado, turno_max):
        # Si estado == 0, el jugador anterior ganó
        if estado == 0:
            return 1 if not turno_max else -1  # Si era turno de MIN y hay 0, MAX ganó
        
        if turno_max:
            mejor = -2
            # Probar ambas jugadas
            if estado-1 >= 0:
                valor = evaluar(estado-1, False)
                if valor > mejor:
                    mejor = valor
            if estado//2 >= 0:
                valor = evaluar(estado//2, False)
                if valor > mejor:
                    mejor = valor
            return mejor
        else:
            mejor = 2
            if estado-1 >= 0:
                valor = evaluar(estado-1, True)
                if valor < mejor:
                    mejor = valor
            if estado//2 >= 0:
                valor = evaluar(estado//2, True)
                if valor < mejor:
                    mejor = valor
            return mejor
    
    resultado = evaluar(n, True)
    return "Gana MAX" if resultado == 1 else "Gana MIN"

# Probar con algunos valores
for num in [3, 6, 7, 10]:
    print(f"n={num}: {juego_division(num)}")