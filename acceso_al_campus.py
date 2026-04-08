# Credenciales fijas
usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
max_intentos = 3
acceso = False

# LOGIN
while intentos < max_intentos:
    print(f"Intento {intentos + 1}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso = True
        break
    else:
        print("Error: datos invalidos.")
        intentos += 1

# Si falla 3 veces
if not acceso:
    print("Cuenta bloqueada.")

# MENÚ
while acceso:
    print("\n1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
    opcion = input("Opción: ")

    # Validar q sea número
    if not opcion.isdigit():
        print("Error: ingrese un número válido.")
        continue

    opcion = int(opcion)

    # Validar opcion
    if opcion < 1 or opcion > 4:
        print("Error: opción invalida.")
        continue

    # Opciones
    if opcion == 1:
        print("Inscripto")

    elif opcion == 2:
        nueva_clave = input("Nueva clave: ")

        # Validar la longitud
        if len(nueva_clave) < 6:
            print("Error: mínimo 6 caracteres.")
            continue

        confirmacion = input("Confirmar clave: ")

        if nueva_clave != confirmacion:
            print("Error: las claves no coinciden.")
        else:
            clave_correcta = nueva_clave
            print("Clave actualizada correctamente.")

    elif opcion == 3:
        print("Segui intentando, vas muy bien")

    elif opcion == 4:
        print("Saliendo del sistema...")
        break