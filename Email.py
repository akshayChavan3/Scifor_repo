import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email, smtp_server, smtp_port, smtp_username, smtp_password):
    # Create the email message
    message = MIMEMultipart()
    message['From'] = smtp_username
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Log in to the SMTP server (if authentication is required)
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(smtp_username, to_email, message.as_string())

# Example usage
subject = "Hello from Python Email Sender"
body = "This is a test email sent from a Python script."
to_email = "recipient@example.com"
smtp_server = "smtp.example.com"
smtp_port = 587  # Use 465 for SSL, 587 for TLS, or 25 for non-secure
smtp_username = "your_username"
smtp_password = "your_password"

send_email(subject, body, to_email, smtp_server, smtp_port, smtp_username, smtp_password)
