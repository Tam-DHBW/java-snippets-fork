import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    from_email = "your_email@example.com"
    password = "your_password"  # Use environment variables or secure storage in real applications

    # Create a text/plain message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # Connect to the SMTP server
    with smtplib.SMTP_SSL('smtp.example.com', 465) as server:
        server.login(from_email, password)
        server.send_message(msg)
        print("Email sent successfully.")

# Example usage
send_email("Test Subject", "This is the body of the email.", "recipient@example.com")
