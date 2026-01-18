# PLANTILLAS

from email.mime.multipart import MIMEMultipart
from email.mime.text      import MIMEText
from email.mime.image     import MIMEImage
from pathlib              import Path
from string               import Template # Nos permite trabajar con las plantillas
import smtplib

# Escribiendo una plantilla de HTML
plantilla_HTML = Path("paquetes-nativos/plantilla.html").read_text("utf-8") 
template = Template(plantilla_HTML)
body_plantilla = template.substitute(
    ###
    # Tenemos dos opciones:
    # 1) Pasarlo como si fuera un diccionario
    # 2) Pasarlo como argumento nombrado
    # ###

    # Lo paso como diccionario
    #{ "usuario": "Miguel" }

    # Lo paso como argumento nombrado
    usuario = "Miguel"
)





imagen = Path("paquetes-nativos/copa-fifa.png")
mime_image = MIMEImage(imagen.read_bytes())

email_usuario = "soymigueprogramador@gmail.com"

mensaje = MIMEMultipart()

mensaje["from"] = "Migue-dev"
mensaje["yo"] = email_usuario
mensaje["subject"] = "Prueba"

cuerpo_del_mensaje = MIMEText(
    # Lleva dos argumentos
    body_plantilla, # El cuerpo del mensaje con la plantilla
    "html",         # Le indicamos que ahora es un HTML
)

mensaje.attach(cuerpo_del_mensaje)
mensaje.attach(mime_image)

with smtplib.SMTP(
    host="smtp.google.com",
    port="587",
) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(
        "soymigueprogramador@gmail.com",
        "password"
    )
    smtp.send_message(mensaje)
    print("Mensaje enviado!!")
