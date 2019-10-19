import smtplib
import numpy as np
#import ultrasonic_relay as u

d = np.random.randint(low=12, high=300, size=20)


EMAIL_ADDRESS = "ubermenschsystem@gmail.com"
EMAIL_PASSWORD = "ubermensch1234"

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = "Greetings from Ubermensch! Here are your home stats"
    body = "Here are the readings:\n{}\n".format(d)

    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail(EMAIL_ADDRESS, "srivastava41099@gmail.com", msg)
