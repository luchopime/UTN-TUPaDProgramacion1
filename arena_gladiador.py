# =========================
# 1. NOMBRE DEL JUGADOR
# =========================
print("--- BIENVENIDO A LA ARENA ---")

nombre = input("ingresa el nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

# =========================
# 2. VARIABLES INICIALES
# =========================
vida_jugador = 100
vida_enemigo = 100
pociones = 3
daño_jugador = 15
daño_enemigo = 12
turno_jugador = True  

print("=== INICIO DEL COMBATE ===")

# =========================
# 3. CICLO DE COMBATE
# =========================
while vida_jugador > 0 and vida_enemigo > 0:

    print("\n=== NUEVO TURNO ===")
    print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

    # =========================
    # TURNO DEL JUGADOR
    # =========================
    print("\nElige accion:")
    print("1. Ataque Pesado")
    print("2. Rafaga Veloz")
    print("3. Curar")

    opcion = input("Opcion: ")

    while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
        print("Error: Ingrese un numero valido.")
        opcion = input("Opcion: ")

    opcion = int(opcion)

    # -------------------------
    # ATAQUE PESADO
    # -------------------------
    if opcion == 1:
        daño_final = daño_jugador

        if vida_enemigo < 20:
            daño_final = daño_jugador * 1.5  # float
            print("Golpe critico!")

        vida_enemigo -= daño_final
        print(f"Atacaste al enemigo por {daño_final} de danio!")

    # -------------------------
    # RAFAGA VELOZ
    # -------------------------
    elif opcion == 2:
        print(">> Inicias una rafaga de golpes!")

        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    # -------------------------
    # CURAR
    # -------------------------
    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print("Te curaste 30 puntos de vida!")
        else:
            print("No quedan pociones!")

    # =========================
    # TURNO DEL ENEMIGO
    # =========================
    if vida_enemigo > 0:
        vida_jugador -= daño_enemigo
        print(f">> El enemigo contraataca por {daño_enemigo} puntos!")

# =========================
# 4. RESULTADO FINAL
# =========================
if vida_jugador > 0:
    print(f"VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caido en combate.")