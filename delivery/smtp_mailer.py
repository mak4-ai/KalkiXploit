import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email: str, sender_password: str, receiver_email: str, subject: str, message: str, smtp_server="smtp.gmail.com", port=587):
    """
    Send an email with the given subject and message from sender_email to receiver_email
    using the provided SMTP server and credentials.
    """
    try:
        # Create the message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Add body
        msg.attach(MIMEText(message, 'plain'))

        # Connect to the server
        context = ssl.create_default_context()
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)

        # Login
        server.login(sender_email, sender_password)

        # Send email
        server.sendmail(sender_email, receiver_email, msg.as_string())

        server.quit()
        print(f"Email sent successfully to {receiver_email}")

    except Exception as e:
        print(f" Failed to send email: {e}")
