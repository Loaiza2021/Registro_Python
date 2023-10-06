import os
import re
import smtplib
import pywhatkit as kit

# Validar nombre
def validar_nombre(nombre):
    return bool(re.match("^[A-Za-zÁ-ÿ ]+$", nombre))

# Validar apellido  
def validar_apellido(apellido):
    return bool(re.match("^[A-Za-zÁ-ÿ ]+$", apellido))

# Validar correo
def validar_correo(correo):
    return bool(re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", correo))

# Validar teléfono
def validar_telefono(telefono):
  return bool(re.match("^\+[0-9]{10,}$", telefono))


# Registro de usuario
def registro():
    print("Ingrese los siguientes datos:")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    correo = input("Correo: ")
    telefono = input("Telefono: ")

    if validar_nombre(nombre) and validar_apellido(apellido) and validar_correo(correo) and validar_telefono(telefono):
        print(f"Los datos son válidos: {nombre}, {apellido}, {correo}, {telefono}")

        # Guardar los datos en un archivo
        with open("usuarios.txt", "a") as f:
            f.write(f"Nombre: {nombre}\n")
            f.write(f"Apellido: {apellido}\n")
            f.write(f"Correo: {correo}\n")
            f.write(f"Telefono: {telefono}\n")
            f.write("-" * 30 + "\n")
            # Cerrar el archivo
            f.close()



        # Enviar mensaje a WhatsApp
        mensaje_whatsapp = f"Bienvenido, {nombre} {apellido}! Gracias por registrarte."
        kit.sendwhatmsg_instantly("+584165261974", mensaje_whatsapp)

        # Enviar correo electrónico
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login("adrianloaiza816@gmail.com","contraseña")

        mensaje_correo = f"Subject: Bienvenido\n\n{mensaje_whatsapp}"
        servidor.sendmail({correo}, mensaje_correo)
        servidor.quit()

        print("Registro exitoso. Se ha enviado un mensaje")

    else:
        print(f"Los datos son inválidos: {nombre}, {apellido}, {correo}, {telefono}")

# Consulta de usuarios
def consultar_usuarios():
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r") as f:
            usuarios = f.read()
            print("Contenido del archivo")
            print(usuarios)
    else:
        print("No hay usuarios registrados")

# Menú Principal
while True:
    print("\nMenu:")
    print("1. Registrar usuarios")
    print("2. Consultar usuarios")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registro()
    elif opcion == "2":
        consultar_usuarios()
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Intente de nuevo")
