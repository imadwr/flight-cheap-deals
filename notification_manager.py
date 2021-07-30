import smtplib


from_email = YOUR ORIGIN EMAIL ADDRESS
from_password = ORIGIN EMAIL PASSWORD
to_addrs = DESTINATION EMAIL ADDRESS


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
