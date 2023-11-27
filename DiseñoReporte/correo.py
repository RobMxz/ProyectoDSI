import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

# Configura los detalles de tu servidor de correo SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'robmxz1234@gmail.com'
smtp_password = 'uyaaqdtiuvewalmc'
name = "Roberto Paolo Palacios Chavez"
codigo = "21200069"
fecha_actual = datetime.date.today()
fecha_actual_str = fecha_actual.strftime("%Y-%m-%d")
Periodo = "2023-II"
Estado = "tudu bem"
P_prob = "No sé"
Recomendaciones = "No sé"
N1 = 19
N2 = 20
N3 = 14

# Crea el objeto MIMEMultipart para el correo
msg = MIMEMultipart()
msg['From'] = 'robmxz1234@gmail.com'
msg['To'] = 'neiter.aylas@unmsm.edu.pe'
msg['Subject'] = 'Test IMGS'
html = f"""
<!DOCTYPE html>
<html lang="es">
  <head>
    <title>Reporte de estudiante</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lexend+Deca:wght@400">
  </head>
  <body style="background-image: linear-gradient(to right, #ffe4fa84, #e4c7df84); background-repeat: repeat; font-family: 'Lexend Deca', sans-serif; margin-left: 20%; margin-right: 20%; margin-top: 5%; margin-bottom: 5%;">

    <h1 style="color: #b998b3; text-align: center;">Reporte de Rendimiento de Estudiante</h1>

    <div style="float: left;">
        <p class="items">Estudiante: {name}</p>
        <div id="nombreE"></div>

        <p class="items">Código de estudiante: {codigo}</p>
        <div id="codigoE"></div>

        <p class="items">Fecha de emisión: {fecha_actual_str}</p>
        <div id="fechaR"></div>

        <h2 style="color: #b998b3;">Resumen de notas</h2>

        <table width="500" border="1" style="font-family: Nixie-One; text-align: center; table-layout: fixed; border: 2px dashed #b998b3;">
          <tr style="color: #b998b3; font-weight: bold;">
            <td>Matemática</td>
            <td>Humanidades</td>
            <td>Ciencias</td>
          </tr>
          <tr>
            <td>{N1}<div id="mat"></div></td>
            <td>{N2}<div id="hum"></div></td>
            <td>{N3}<div id="ciencia"></div></td>
          </tr>
        </table>
    </div>

    <img src="https://is4-ssl.mzstatic.com/image/thumb/Purple49/v4/8c/2e/05/8c2e051b-a1f0-1600-dbd7-03707c029cd1/source/256x256bb.jpg" title="Gráfico de progreso" style="float: right; margin-left: 10px; margin-top: 10%; height: 15%; width: 24%; margin-right: 5%">

    <div style="clear: both;">
        <p class="items">Promedio final: {round(((N1+N2+N3)/3),2)}</p>
        <div id="promedio"></div>

        <p class="items">Periodo: {Periodo}</p>
        <div id="periodo"></div>

        <p id="acotacion" style="font-size: small; font-style: italic; color: #b998b3; margin-right: 50%;">
          * En la sección derecha puede visualizar un gráfico que resume el rendimiento en las tres (3) áreas consideradas.
        </p>

        <h2 style="color: #b998b3;">Análisis de rendimiento</h2>

        <p class="items">Estado de rendimiento: {Estado}</p>
        <div id="estado"></div>

        <p class="items">Posible problema identificado: {P_prob}</p>
        <div id="problema"></div>

        <p class="items">Recomendaciones: {Recomendaciones}</p>
        <div id="recomendacion"></div>
    </div>

  </body>
</html>
"""

# Adjunta el contenido HTML al correo
msg.attach(MIMEText(html, 'html'))
# Conéctate al servidor SMTP y envía el correo
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, msg['To'], msg.as_string())
    server.quit()
    print("Correo enviado con éxito")
except Exception as e:
    print("Error al enviar el correo:", str(e))
