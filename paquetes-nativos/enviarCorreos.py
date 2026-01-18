# Enviando correos

# Estructura en codigo para enviar correos electronicos

# Importando modulos necesarios
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage # Para envia una imagen
from pathlib import Path
import smtplib # Libreria del SMTP de google

# Enviamos un archivo adjunto
imagen = Path("paquetes-nativos/copa-fifa.png") # Ruta de la imagen
mime_image = MIMEImage(imagen.read_bytes()) # Llamamos a la variable que guarda la imagen

email_usuario = "soymigueprogramador@gmail.com"

# Creando el mensaje
mensaje = MIMEMultipart()

# Propiedades del paquete
mensaje["from"] = "Migue-dev" # Quien manda el correo
mensaje["yo"] = email_usuario # A donde se manda el correo
mensaje["subject"] = "Prueba" # El asunto del mensaje

cuerpo_del_mensaje = MIMEText(
    # Recibe dos argumentos
    "Mensaje", # El cuerpo del mensaje
    # La forma del correo, si este HTML o texto plano (Por default manda un texto plano)

)
mensaje.attach(cuerpo_del_mensaje) # Llamamos al cuerpo del mensaje
mensaje.attach(mime_image)         # Llamamos a la imagen

# Cerrando la coneccion al servidor
with smtplib.SMTP(
    # Recibe dos parametros:
    host="smtp.google.com", # Le indicamos donde esta el servidor
    port="587",             # Le indicamos el puerto por donde accedemos al servidor

) as smtp:
    # Llamados necesario para enviar el correo
    smtp.ehlo() # Nos identifica con el servidor y identifica el dominio que usamos.
    smtp.starttls() # Encripta el mensaje que estamos enviando

    # Iniciamos sesion en el servidor de google
    smtp.login(
        # Recibe dos parametros:
        "soymigueprogramador@gmail.com", # Email del usuario
        "password"                       # La clave del usuario
    )
    smtp.send_message(mensaje) # Le indicamos el mensaje que vamos a enviar
    print("Mensaje enviado!!")
