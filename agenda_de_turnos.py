# Turnos inicializados vacios
lunes1 = lunes2 = lunes3 = lunes4 = ""
martes1 = martes2 = martes3 = ""

# Nombre operador
operador = input("Ingrese nombre del operador: ")
while not operador.isalpha():
    print("Error: solo letras.")
    operador = input("Ingrese nombre del operador: ")

# Menu principal
while True:
    print("\n1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del dia")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")

    opcion = input("Opcion: ")

    if not opcion.isdigit():
        print("Error: ingrese un numero valido.")
        continue

    opcion = int(opcion)

    if opcion < 1 or opcion > 5:
        print("Error: opcion fuera de rango.")
        continue

    # =========================
    # 1. RESERVAR TURNO
    # =========================
    if opcion == 1:
        dia = input("Dia (1=Lunes, 2=Martes): ")

        if not dia.isdigit() or int(dia) not in [1, 2]:
            print("Error: dia invalido.")
            continue

        nombre = input("Nombre del paciente: ")

        if not nombre.isalpha():
            print("Error: solo letras.")
            continue

        # LUNES
        if dia == "1":
            if nombre in (lunes1, lunes2, lunes3, lunes4):
                print("Error: paciente ya tiene turno ese dia.")
            elif lunes1 == "":
                lunes1 = nombre
            elif lunes2 == "":
                lunes2 = nombre
            elif lunes3 == "":
                lunes3 = nombre
            elif lunes4 == "":
                lunes4 = nombre
            else:
                print("No hay turnos disponibles.")

        # MARTES
        elif dia == "2":
            if nombre in (martes1, martes2, martes3):
                print("Error: paciente ya tiene turno ese dia.")
            elif martes1 == "":
                martes1 = nombre
            elif martes2 == "":
                martes2 = nombre
            elif martes3 == "":
                martes3 = nombre
            else:
                print("No hay turnos disponibles.")

    # =========================
    # 2. CANCELAR TURNO
    # =========================
    elif opcion == 2:
        dia = input("Dia (1=Lunes, 2=Martes): ")

        if not dia.isdigit() or int(dia) not in [1, 2]:
            print("Error: dia invalido.")
            continue

        nombre = input("Nombre del paciente: ")

        if not nombre.isalpha():
            print("Error: solo letras.")
            continue

        encontrado = False

        if dia == "1":
            if lunes1 == nombre:
                lunes1 = ""
                encontrado = True
            elif lunes2 == nombre:
                lunes2 = ""
                encontrado = True
            elif lunes3 == nombre:
                lunes3 = ""
                encontrado = True
            elif lunes4 == nombre:
                lunes4 = ""
                encontrado = True

        elif dia == "2":
            if martes1 == nombre:
                martes1 = ""
                encontrado = True
            elif martes2 == nombre:
                martes2 = ""
                encontrado = True
            elif martes3 == nombre:
                martes3 = ""
                encontrado = True

        if encontrado:
            print("Turno cancelado.")
        else:
            print("No se encontro el turno.")

    # =========================
    # 3. VER AGENDA
    # =========================
    elif opcion == 3:
        dia = input("Dia (1=Lunes, 2=Martes): ")

        if not dia.isdigit() or int(dia) not in [1, 2]:
            print("Error: dia invalido.")
            continue

        if dia == "1":
            print("Lunes:")
            print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")

        elif dia == "2":
            print("Martes:")
            print("Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("Turno 3:", martes3 if martes3 != "" else "(libre)")

    # =========================
    # 4. RESUMEN GENERAL
    # =========================
    elif opcion == 4:
        ocupados_lunes = sum([
            lunes1 != "", lunes2 != "", lunes3 != "", lunes4 != ""
        ])
        ocupados_martes = sum([
            martes1 != "", martes2 != "", martes3 != ""
        ])

        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes

        print("\nResumen:")
        print(f"Lunes: {ocupados_lunes} ocupados, {disponibles_lunes} libres")
        print(f"Martes: {ocupados_martes} ocupados, {disponibles_martes} libres")

        if ocupados_lunes > ocupados_martes:
            print("Dia con mas turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Dia con mas turnos: Martes")
        else:
            print("Ambos dias tienen la misma cantidad de turnos.")

    # =========================
    # 5. SALIR
    # =========================
    elif opcion == 5:
        print("Sistema cerrado.")
        break