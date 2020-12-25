import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("\nOk!!! Vamos a registrarte en el sistema...")
        nombre = input("Cual es tu nombre: ")
        apellido = input("Cual es tu apellido: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellido, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")

        else: 
            print("No te has regsitrado los datos correctamente :(")

    def login(self):
        print("\nVale!! Identificate en el sistema...")

        try:
                
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:

                print(f"\nBienvenidos {login[1]}, te has registrado en el dia {login[5]}")
                self.proximasAcciones(login)

        except Exception:
            print("Login incorrecto. Intentalo más tarde ;)")    

    def proximasAcciones (self, usuario):
        print("""
        Acciones disponibles:
        -Crear notas (1)
        -Mostrar tus notas (2)
        -Eliminar nota (3)
        -Salir (4)
        """)

        accion = input("¿Que quieres hacer?: ")
        hazEl = notas.acciones.Acciones()

        if accion == "1":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "2":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "3":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "4":
            print("adios ;)")
            exit()

        else:
            print("La accion que escogistes, no esta disponible.")
            self.proximasAcciones(usuario)

        return None  