import smtplib
import ssl


# Define function with parameter message which will be added from main.py as argument
def send_message(message):
    host = "smtp.gmail.com"
    port = 465

    username = "testpythonplant@gmail.com"
    password = "anxwakymhwarrzyl"
    receiver = "testpythonplant@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
