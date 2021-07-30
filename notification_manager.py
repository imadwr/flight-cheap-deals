import smtplib
import os

from_email = os.getenv("email")
from_password = os.getenv("password")
to_addrs = os.getenv("to_email")


class NotificationManager:

    def send_email(self, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=from_email, password=from_password)
            connection.sendmail(
                from_addr=from_email,
                to_addrs=to_addrs,
                msg=f"Subject: Low price Flight\n\n{message}"
            )

        # Prints if successfully sent.
        print(message)
