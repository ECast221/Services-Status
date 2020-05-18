"""

"""
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.conf import settings


class MailSender:
    """

    """

    def __init__(self, html, subject, text, to):
        """

        :param html:
        :param subject:
        :param text:
        :param to:
        """

        self.smtp_server = settings.SMTP_HOST
        self.port = settings.SMTP_PORT
        self.sender_email = settings.SMTP_USER
        self.password = settings.SMTP_PASS
        self.receiver_email = to

        self.message = MIMEMultipart("alternative")
        self.message["Subject"] = subject
        self.message["From"] = self.sender_email
        self.message["To"] = to

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        self.message.attach(part1)
        self.message.attach(part2)

    def send_mail(self):
        """

        :return:
        """
        # Create a secure SSL context
        context = ssl.create_default_context()

        # Try to log in to server and send email
        try:
            server = smtplib.SMTP(self.smtp_server, self.port)
            server.ehlo()  # Can be omitted
            server.starttls(context=context)  # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(self.sender_email, self.password)

            server.sendmail(self.sender_email, self.receiver_email, self.message.as_string())
            server.quit()

        except Exception as e:
            print(e)  # we should log this as an error
