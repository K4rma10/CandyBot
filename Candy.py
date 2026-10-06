import time
import pyautogui
import pygetwindow as gw
import keyboard


# ============================================================
# CONFIGURACIÓN
# ============================================================

# Tiempo que tarda entre acciones
ESPERA = 0.15

# Tecla para iniciar la prueba
TECLA_INICIO = "f6"

# Tecla de emergencia
TECLA_STOP = "f8"

bot_activo = False


# ============================================================
# BUSCAR ROBLOX
# ============================================================

def buscar_roblox():
    """
    Busca una ventana cuyo título contenga 'Roblox'.
    """

    ventanas = gw.getWindowsWithTitle("Roblox")

    if not ventanas:
        print("❌ No se encontró Roblox.")
        return None

    ventana = ventanas[0]

    print("✅ Roblox encontrado.")
    print(f"   Título: {ventana.title}")
    print(f"   Posición: {ventana.left}, {ventana.top}")
    print(f"   Tamaño: {ventana.width}x{ventana.height}")

    return ventana


# ============================================================
# ACTIVAR ROBLOX
# ============================================================

def activar_roblox():

    ventana = buscar_roblox()

    if ventana is None:
        return False

    try:
        if ventana.isMinimized:
            ventana.restore()

        ventana.activate()

        time.sleep(0.5)

        return True

    except Exception as e:
        print("❌ No se pudo activar Roblox.")
        print(e)
        return False


# ============================================================
# TECLADO
# ============================================================

def tecla(tecla_nombre, duracion=0.1):

    if not bot_activo:
        return

    print(f"⌨️ Tecla: {tecla_nombre}")

    pyautogui.keyDown(tecla_nombre)

    time.sleep(duracion)

    pyautogui.keyUp(tecla_nombre)

    time.sleep(ESPERA)


# ============================================================
# CLICK
# ============================================================

def click():

    if not bot_activo:
        return

    print("🖱️ Click")

    pyautogui.click()

    time.sleep(ESPERA)


# ============================================================
# MOVIMIENTO
# ============================================================

def mover_w(segundos=1):

    tecla("w", segundos)


def mover_a(segundos=1):

    tecla("a", segundos)


def mover_s(segundos=1):

    tecla("s", segundos)


def mover_d(segundos=1):

    tecla("d", segundos)


# ============================================================
# ACCIONES DE GPO
# ============================================================

def interactuar():

    print("🟢 Interactuando con E")

    tecla("e")


def seleccionar_arma():

    print("⚔️ Seleccionando arma [2]")

    tecla("2")


def seleccionar_canasta():

    print("🍬 Seleccionando canasta [4]")

    tecla("4")


def atacar():

    print("⚔️ Ataque")

    click()


# ============================================================
# CAPTURA DE PANTALLA
# ============================================================

def capturar_pantalla():

    imagen = pyautogui.screenshot()

    imagen.save("pantalla_gpo.png")

    print("📸 Captura guardada como pantalla_gpo.png")


# ============================================================
# PRUEBA DE CONTROLES
# ============================================================

def prueba_controles():

    global bot_activo

    if not activar_roblox():
        return

    print()
    print("====================================")
    print("       PRUEBA DE CONTROLES GPO")
    print("====================================")
    print()

    print("W")
    mover_w(1)

    print("S")
    mover_s(1)

    print("A")
    mover_a(1)

    print("D")
    mover_d(1)

    print("E")
    interactuar()

    print("2")
    seleccionar_arma()

    print("CLICK")
    atacar()

    print("4")
    seleccionar_canasta()

    print()
    print("✅ Prueba terminada.")


# ============================================================
# INICIAR BOT
# ============================================================

def iniciar():

    global bot_activo

    if bot_activo:
        print("⚠️ El bot ya está activo.")
        return

    bot_activo = True

    print()
    print("🟢 BOT ACTIVADO")
    print()


# ============================================================
# DETENER BOT
# ============================================================

def detener():

    global bot_activo

    bot_activo = False

    # Soltar todas las teclas importantes
    for tecla_nombre in ["w", "a", "s", "d", "e", "2", "4"]:

        try:
            pyautogui.keyUp(tecla_nombre)
        except:
            pass

    print()
    print("🛑 BOT DETENIDO")
    print()


# ============================================================
# HOTKEYS
# ============================================================

keyboard.add_hotkey("f6", iniciar)
keyboard.add_hotkey("f8", detener)


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

print("============================================")
print("        BOT DE PRUEBA - GRAND PIECE")
print("============================================")
print()
print("F6  → activar bot")
print("F8  → detener inmediatamente")
print()
print("Buscando Roblox...")

ventana = buscar_roblox()

if ventana:

    print()
    print("Roblox está abierto.")
    print("Pulsa F6 para activar el bot.")
    print("Pulsa F8 para detenerlo.")
    print()

else:

    print()
    print("⚠️ Abre Roblox antes de continuar.")
    print()


# Mantener el programa funcionando

try:

    while True:

        if bot_activo:

            prueba_controles()

            detener()

        time.sleep(0.1)


except KeyboardInterrupt:

    detener()

    print("Programa cerrado.")