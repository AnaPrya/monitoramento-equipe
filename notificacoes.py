import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Função para enviar o e-mail
def send_email(to_emails, subject, body):
    from_email = "prya3201@gmail.com"  # Substitua com seu e-mail do Outlook
    password = "3435abacaxi"  # Substitua com sua senha ou senha de app

    # Configurações do servidor SMTP (Outlook)
    smtp_server = "smtp-mail.outlook.com"
    smtp_port = 587

    # Configuração do servidor SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email, password)

    # Criar a mensagem
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Enviar o e-mail
    server.sendmail(from_email, to_emails, msg.as_string())
    server.quit()


    # Print de confirmação
    print(f"E-mail enviado para: {', '.join(to_emails)}")

# Função que será chamada para agendar o envio
def send_notification():
    to_emails = ["abartolo@regiacapital.com.br", "bbernardo@regiacapital.com.br", "canjos@regiacapital.com.br", "svaladares@regiacapital.com.br", "glopes@regiacapital.com.br", "lbrandao@regiacapital.com.br"]
    subject = "Atualização de Tarefas"
    body = "Olá, hoje é dia de atualizar suas tarefas! Faça isso acessando o link: http://localhost:8501"
    send_email(to_emails, subject, body)

# Função para verificar se o dia atual é útil (segunda a sexta-feira)
def is_weekday():
    today = datetime.today().weekday()
    return today < 5  # 0 é segunda-feira, 4 é sexta-feira (dias úteis)

# Função para agendar o envio a cada 2 dias úteis
def schedule_task():
    count = 0  # Contador para rastrear o número de dias úteis
    while count < 2:  # Enquanto o contador for menor que 2, espera um dia
        if is_weekday():  # Verifica se o dia é útil
            schedule.every(1).day.do(send_notification)  # Agenda o envio para o dia
            count += 1  # Incrementa o contador de dias úteis
        time.sleep(60 * 60 * 24)  # Espera 24 horas (um dia)
    
# Agendar a tarefa
schedule_task()

while True:
    schedule.run_pending()
    time.sleep(60 * 60)  # Espera uma hora para verificar novamente