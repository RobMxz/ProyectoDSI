import smtplib
import sys
import joblib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import sklearn
from sklearn.model_selection import train_test_split
# Configura los detalles de tu servidor de correo SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'robmxz1234@gmail.com'
smtp_password = 'uyaaqdtiuvewalmc'

modelo = joblib.load('modelo2.pkl')
X_prediccion= ["15","0","1","1","3","0","0","1","3","0","0"]

prediccion = modelo.predict([X_prediccion])
name = sys.argv[1]
codigo = sys.argv[2]
fecha_actual = datetime.now()
fecha_actual_str = fecha_actual.strftime("%Y-%m-%d")
Periodo = "2023-II"
Estado = ""
P_prob = "No sé"
Recomendaciones = "No sé"
N1 = float(sys.argv[3])
N2 = float(sys.argv[4])
N3 = float(sys.argv[5])


if(round(((N1+N2+N3)/3),2)>14):
    Estado = "Buen promedio"
elif (round(((N1+N2+N3)/3),2)>=10.5):
    Estado = "Promedio regular"
else:
    Estado = "Mal promedio"
    
fecha_nacimiento = sys.argv[6]
    
def calcular_edad(fecha_nacimiento):
    # Convertir las fechas de cadena a objetos datetime
    fecha_nacimiento =  datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
    fecha_actual = datetime.strptime(fecha_actual_str, '%Y-%m-%d')

    # Calcular la diferencia en años
    edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

    return edad

edad = calcular_edad(fecha_nacimiento)
tmp_est = int(sys.argv[7])
failures = int(sys.argv[8])
interes = sys.argv[9]
higher = 0

if (interes != ""):
    higher = 1
# Crea el objeto MIMEMultipart para el correo
msg = MIMEMultipart()
msg['From'] = 'robmxz1234@gmail.com'
msg['To'] = 'carolina.seminario@unmsm.edu.pe'
msg['Subject'] = 'Talvez correo final 2'
html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <title>Reporte de estudiante</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lexend+Deca:wght@400">
    <style>
        /* Agrega aquí el enlace CSS copiado de Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Lexend+Deca&display=swap');
    </style>
</head>
<body style="background-image: linear-gradient(to right, #ffe4fa84, #e4c7df84); background-repeat: repeat; font-family: Lexend-Deca, sans-serif; margin-left: 20%; margin-right: 20%; margin-top: 5%; margin-bottom: 5%; color:#442836; font-weight: bold;">

    <h1 style="color: #9a547c; text-align: center;">Reporte de Rendimiento de Estudiante</h1>

    <div style="display: flex; flex-direction: row;">

        <div style="flex: 1;">

            <p class="items">Estudiante: {name}</p>
            <div id="nombreE"></div>

            <p class="items">Código de estudiante: {codigo}</p>
            <div id="codigoE"></div>

            <p class="items">Fecha de emisión: {fecha_actual_str}</p>
            <div id="fechaR"></div>

            <h2 style="color: #9a547c;">Resumen de notas</h2>

            <table width="500" border="1" style="font-family: Lexend-Deca; text-align: center; table-layout: fixed; border: 2px dashed #7c2951;">
                <tr style="color: #9a547c; font-weight: bold;">
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

            <p class="items">Promedio final: {round(((N1+N2+N3)/3),2)}</p>
            <div id="promedio"></div>

            <p class="items">Periodo: {Periodo}</p>
            <div id="periodo"></div>

            <p id="acotacion" style="font-size: small; font-style: italic; color: #b998b3; margin-right: 50%;">
                * En la sección derecha puede visualizar un gráfico que resume el rendimiento en las tres (3) áreas consideradas.
            </p>

            <h2 style="color: #9a547c;">Análisis de rendimiento</h2>

            <p class="items">Estado de rendimiento: {Estado}</p>
            <div id="estado"></div>

            <p class="items">Posible problema identificado: {prediccion}</p>
            <div id="problema"></div>

            <p class="items">Recomendaciones: {Recomendaciones}</p>
            <div id="recomendacion"></div>
        </div>

        <!-- Imagen a la derecha -->
        <div style="margin-left: 20px;">
            <img src="https://is4-ssl.mzstatic.com/image/thumb/Purple49/v4/8c/2e/05/8c2e051b-a1f0-1600-dbd7-03707c029cd1/source/256x256bb.jpg" alt="Gráfico de progreso" style="width: 70%; height: auto; margin-top: 35%; margin-right:120px">
        </div>
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
