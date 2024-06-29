# Definición de la función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dado su base y altura.

    :param base: La base del triángulo (float)
    :param altura: La altura del triángulo (float)
    :return: El área del triángulo (float)
    """
    # Cálculo del área
    area = (base * altura) / 2
    return area


# Datos del triángulo
base = 4.0  # en cm
altura = 6.0  # en cm

# Cálculo del área
area_triangulo = calcular_area_triangulo(base, altura)

# Impresión del resultado
print(f"El área de un triángulo con base {base} cm y altura {altura} cm es {area_triangulo} cm²")