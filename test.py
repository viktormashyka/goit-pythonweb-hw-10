import smtplib

smtp_server = "smtp.meta.ua"
sender_email = "v.mashyka@meta.ua"
password = "Vi1ktor2"

# Try different ports and settings
ports = [465, 587, 25]
use_ssl = [True, False]

for port in ports:
    for ssl in use_ssl:
        server = None
        try:
            if ssl:
                server = smtplib.SMTP_SSL(smtp_server, port, timeout=10)
            else:
                server = smtplib.SMTP(smtp_server, port, timeout=10)
                server.starttls()
            server.login(sender_email, password)
            print(f"Successfully connected to the SMTP server on port {port} with SSL={ssl}")
        except Exception as e:
            print(f"Error on port {port} with SSL={ssl}: {e}")
        finally:
            if server:
                server.quit()