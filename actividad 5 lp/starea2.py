def calcular_promedio(notas):
    # Dividir las notas por materia y convertirlas a números
    notas_por_materia = [int(nota.split(":")[1]) for nota in notas.split(",")]

    # Calcular el promedio
    promedio = sum(notas_por_materia) / len(notas_por_materia)

    return promedio

def main():
    # Abrir el archivo de entrada
    with open("notas_estudiantes.txt", "r") as archivo_entrada:
        lineas = archivo_entrada.readlines()

    # Abrir el archivo de salida
    with open("promedio_estudiantes.txt", "w") as archivo_salida:
        # Procesar cada línea del archivo de entrada
        for linea in lineas:
            # Dividir la línea en nombre y notas por materia
            nombre, notas = linea.strip().split(", ", 1)

            # Calcular el promedio
            promedio = calcular_promedio(notas)

            # Escribir el resultado en el archivo de salida
            archivo_salida.write(f"{nombre}, Promedio: {promedio:.2f}\n")

if __name__ == "__main__":
    main()
