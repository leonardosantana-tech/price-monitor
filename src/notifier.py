# Envia e-mail
# Recebe os dados prontos
# LEIA ISSO: voce precisa definir as variáveis pelo Windows Power Shell para que o codigo funcione. É um método seguro.

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


def send_email_alert(old_price, new_price, product_url):
    sender_email = os.getenv("ALERT_EMAIL")
    sender_password = os.getenv("ALERT_EMAIL_PASSWORD")
    receiver_email = os.getenv("ALERT_RECEIVER_EMAIL")

    if not sender_email or not sender_password or not receiver_email:
        print("⚠️ Variáveis de ambiente de e-mail não configuradas")
        return

    subject = "📉 Alerta de Preço – Produto na Amazon"
    body = f"""
O preço do produto caiu!

Preço anterior: R$ {old_price}
Novo preço: R$ {new_price}

Link do produto:
{product_url}
"""

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()

        print("📧 E-mail de alerta enviado com sucesso")

    except Exception as e:
        print("Erro ao enviar e-mail:", e)
