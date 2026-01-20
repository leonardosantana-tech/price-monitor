# LEIA ISSO: voce precisa definir as variáveis pelo Windows Power Shell para que o codigo funcione. É um método seguro.

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email_alert(old_price, new_price, product_url):
    sender = os.getenv("ALERT_EMAIL")
    password = os.getenv("ALERT_EMAIL_PASSWORD")
    receiver = os.getenv("ALERT_RECEIVER_EMAIL")

    print("DEBUG sender:", sender)
    print("DEBUG receiver:", receiver)
    print("DEBUG password existe?", bool(password))

    if not sender or not password or not receiver:
        print("❌ Variáveis de ambiente não configuradas")
        return

    subject = "📉 Alerta de queda de preço"
    body = f"""
O preço do produto caiu!

Preço anterior: R$ {old_price}
Novo preço: R$ {new_price}

Link do produto:
{product_url}
"""

    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        print("🔌 Conectando ao SMTP do gmail...")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        print("🔐 Fazendo login...")
        server.login(sender, password)
        print("📤 Enviando e-mail...")
        server.send_message(message)
        server.quit()
        print("✅ E-mail enviado com sucesso")

    except Exception as e:
        print("❌ Erro ao enviar e-mail:", e)
