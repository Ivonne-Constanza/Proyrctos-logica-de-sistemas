def menu_principal():
    # Presenta el menú principal con las opciones de conversión disponibles.
    print("Seleccione el tipo de conversión:")
    print("1. Longitud entre Millas y Kilómetros")
    print("2. Volumen entre Metros Cúbicos (m3) y Pies Cúbicos (ft3)")
    print("3. Longitud entre Pies, Metros y Yardas")
    print("4. Salir")
    return input("Ingrese el número de su elección: ")  # Devuelve la elección del usuario.

def menu_longitud_millas_kilometros():
    # Presenta el submenú para la conversión entre millas y kilómetros.
    print("Seleccione la conversión de longitud:")
    print("1. Millas a Kilómetros")
    print("2. Kilómetros a Millas")
    return input("Ingrese el número de su elección: ")  # Devuelve la elección del usuario.

def menu_volumen():
    # Presenta el submenú para la conversión entre metros cúbicos y pies cúbicos.
    print("Seleccione la conversión de volumen:")
    print("1. Metros cúbicos (m3) a Pies cúbicos (ft3)")
    print("2. Pies cúbicos (ft3) a Metros cúbicos (m3)")
    return input("Ingrese el número de su elección: ")  # Devuelve la elección del usuario.

def menu_longitud_pies_metros_yardas():
    # Presenta el submenú para la conversión entre pies, metros y yardas.
    print("Seleccione la conversión de longitud:")
    print("1. Pies a Metros")
    print("2. Metros a Pies")
    print("3. Pies a Yardas")
    print("4. Yardas a Pies")
    print("5. Metros a Yardas")
    print("6. Yardas a Metros")
    return input("Ingrese el número de su elección: ")  # Devuelve la elección del usuario.

# Funciones de conversión para cada tipo de medida.
def millas_a_kilometros(millas):
    return millas * 1.60934

def kilometros_a_millas(kilometros):
    return kilometros / 1.60934

def metros_cubicos_a_pies_cubicos(m3):
    return m3 * 35.3147

def pies_cubicos_a_metros_cubicos(ft3):
    return ft3 / 35.3147

def pies_a_metros(pies):
    return pies * 0.3048

def metros_a_pies(metros):
    return metros / 0.3048

def pies_a_yardas(pies):
    return pies / 3

def yardas_a_pies(yardas):
    return yardas * 3

def metros_a_yardas(metros):
    return metros * 1.09361

def yardas_a_metros(yardas):
    return yardas / 1.09361

def main():
    while True:  # Bucle principal que mantiene el programa en ejecución hasta que el usuario decida salir.
        opcion_principal = menu_principal()  # Muestra el menú principal y obtiene la elección del usuario.
        
        if opcion_principal == "1":
            opcion_longitud = menu_longitud_millas_kilometros()  # Muestra el submenú para millas y kilómetros.
            if opcion_longitud == "1":
                millas = float(input("Ingrese la cantidad en Millas: "))
                print(f"{millas} Millas son {millas_a_kilometros(millas)} Kilómetros.")
            elif opcion_longitud == "2":
                kilometros = float(input("Ingrese la cantidad en Kilómetros: "))
                print(f"{kilometros} Kilómetros son {kilometros_a_millas(kilometros)} Millas.")
            else:
                print("Opción no válida.")
        
        elif opcion_principal == "2":
            opcion_volumen = menu_volumen()  # Muestra el submenú para metros cúbicos y pies cúbicos.
            if opcion_volumen == "1":
                m3 = float(input("Ingrese la cantidad en Metros cúbicos (m3): "))
                print(f"{m3} Metros cúbicos son {metros_cubicos_a_pies_cubicos(m3)} Pies cúbicos.")
            elif opcion_volumen == "2":
                ft3 = float(input("Ingrese la cantidad en Pies cúbicos (ft3): "))
                print(f"{ft3} Pies cúbicos son {pies_cubicos_a_metros_cubicos(ft3)} Metros cúbicos.")
            else:
                print("Opción no válida.")
        
        elif opcion_principal == "3":
            opcion_longitud_py_m_y = menu_longitud_pies_metros_yardas()  # Muestra el submenú para pies, metros y yardas.
            if opcion_longitud_py_m_y == "1":
                pies = float(input("Ingrese la cantidad en Pies: "))
                print(f"{pies} Pies son {pies_a_metros(pies)} Metros.")
            elif opcion_longitud_py_m_y == "2":
                metros = float(input("Ingrese la cantidad en Metros: "))
                print(f"{metros} Metros son {metros_a_pies(metros)} Pies.")
            elif opcion_longitud_py_m_y == "3":
                pies = float(input("Ingrese la cantidad en Pies: "))
                print(f"{pies} Pies son {pies_a_yardas(pies)} Yardas.")
            elif opcion_longitud_py_m_y == "4":
                yardas = float(input("Ingrese la cantidad en Yardas: "))
                print(f"{yardas} Yardas son {yardas_a_pies(yardas)} Pies.")
            elif opcion_longitud_py_m_y == "5":
                metros = float(input("Ingrese la cantidad en Metros: "))
                print(f"{metros} Metros son {metros_a_yardas(metros)} Yardas.")
            elif opcion_longitud_py_m_y == "6":
                yardas = float(input("Ingrese la cantidad en Yardas: "))
                print(f"{yardas} Yardas son {yardas_a_metros(yardas)} Metros.")
            else:
                print("Opción no válida.")
        
        elif opcion_principal == "4":
            # Opción para salir del programa.
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")  # Maneja una entrada no válida en el menú principal.
            
if __name__ == "__main__":
    main()  # Ejecuta la función principal al iniciar el programa.
