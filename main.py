from usuarios import acciones

print("""
Acciones disponibles:
    - registro (1)
    - login (2)
""")

hazEl = acciones.Acciones()
accion = input("¿Que quieres hacer?: ")

if accion == "1":
    hazEl.registro()

elif accion == "2":
    hazEl.login()
