import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
# Configura los detalles de tu servidor de correo SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'robmxz1234@gmail.com'
smtp_password = 'uyaaqdtiuvewalmc'

# Crea el objeto MIMEMultipart para el correo
msg = MIMEMultipart()
msg['From'] = 'robmxz1234@gmail.com'
msg['To'] = 'carolina.seminario@unmsm.edu.pe'
msg['Subject'] = 'Test'

# Crea el contenido HTML
html = """
<!DOCTYPE html>
<html>
  <head>
    <title>Reporte de rendimiento</title>
    <style>
      body {
          background-color: #bd85d5;
      }

      h1 {
          color: #9685d5
      }
      *{
          font-family: Roboto;
      }
    </style>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  </head>

  <body>
    <h1>Reporte de rendimiento</h1>

    <div>
      <p>Estudiante: <span>[nombre y apellido]</span> </p> 
      <p>Código: <span>[codigo]</span></p>
      <p>Fecha de emisión: <span>[fecha]</span></p>
    </div>

    <h2>Resumen de notas</h2>
    
    <div>
      <table class="Notas_por_area">
        <thead>
          <tr>
            <th>Matematicas</th>
            <th>Humanidades</th>
            <th>Ciencias</th>
            <th>Promedio final</th>
          </tr>        </tr>
        </thead>
            <td>[nota mat]</td>
            <td>[nota hum]</td>       
            <td>[nota cien]</td>  
            <td>[nota fin]</td>  
          </tr>
        </tbody>
      </table>
      <p>* En la sección derecha puede visualizar el seguimiento de notas</p>
    </div>
    </table>

    <img src="ruta.png">

    <div>
      <p>Estado de rendimiento: <span>[alto/medio/bajo]</span> </p> 
      <h2>Posible problema que afectan su rendimiento</h2>
      <p>[posible problema]</p>
      <h2>Recomendaciones</h2>
      <p>[se programa o no cita con el psicopedagogo]</p>
    </div>
  </body>
</html>

"""

# Adjunta el contenido HTML al correo
msg.attach(MIMEText(html, 'html'))
csv_filename = 'student_data.csv'
attachment = open(csv_filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % csv_filename)
msg.attach(part)
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