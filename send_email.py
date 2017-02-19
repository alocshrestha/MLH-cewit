import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

def sendmail():
    from_addr = ''
    to_addr = ''
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = "Baby Alert!"

    body = 'Your baby is crying..'

    msg.attach(MIMEText(body, 'plain'))
    filename = "baby.jpg"
    attachment = open("baby.jpg", "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, "")
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()



