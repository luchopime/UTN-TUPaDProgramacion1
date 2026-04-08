# Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0  # para la regla anti-spam

# Nombre del agente
agente = input("Ingrese nombre del agente: ")
while not agente.isalpha():
    print("Error: solo letras.")
    agente = input("Ingrese nombre del agente: ")

# Juego principal
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    # Regla de bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("Sistema bloqueado por alarma. DERROTA.")
        break

    print("\n--- ESTADO ---")
    print(f"Energia: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    print(f"Alarma: {'ON' if alarma else 'OFF'}")

    print("\n1) Forzar cerradura")
    print("2) Hackear panel")
    print("3) Descansar")

    opcion = input("Opcion: ")

    if not opcion.isdigit():
        print("Error: ingrese un numero valido.")
        continue

    opcion = int(opcion)

    if opcion < 1 or opcion > 3:
        print("Error: opcion fuera de rango.")
        continue

    # =========================
    # 1. FORZAR CERRADURA
    # =========================
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        # Regla anti-spam
        if racha_forzar == 3:
            alarma = True
            print("La cerradura se trabo. Alarma activada.")
            continue

        # Riesgo de alarma si energia < 40
        if energia < 40 and not alarma:
            num = input("Riesgo de alarma! Elija numero (1-3): ")

            while not num.isdigit() or int(num) < 1 or int(num) > 3:
                print("Error: numero invalido.")
                num = input("Elija numero (1-3): ")

            if num == "3":
                alarma = True
                print("Alarma activada.")

        # Si no hay alarma, abre cerradura
        if not alarma:
            cerraduras_abiertas += 1
            print("Cerradura abierta.")

    # =========================
    # 2. HACKEAR PANEL
    # =========================
    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        racha_forzar = 0  # corta la racha

        for i in range(4):
            print(f"Hackeo paso {i+1}/4...")
            codigo_parcial += "A"

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Codigo suficiente. Cerradura abierta.")

    # =========================
    # 3. DESCANSAR
    # =========================
    elif opcion == 3:
        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1
        racha_forzar = 0  # corta la racha

        if alarma:
            energia -= 10
            print("Descansar con alarma activa consume energia extra.")

# =========================
# RESULTADO FINAL
# =========================
if cerraduras_abiertas == 3:
    print("VICTORIA! Abriste la boveda.")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA. Te quedaste sin recursos.")