# Download the helper library from https://www.twilio.com/docs/python/install
import os

import smtplib
from twilio.rest import Client

# Loads env variables from the .env file
from dotenv import load_dotenv
load_dotenv()

_HOST = "smtp.gmail.com"

# https://kb.sandisk.com/app/answers/detail/a_id/17056/~/list-of-mobile-carrier-gateway-addresses
# https://www.gmass.co/blog/send-text-from-gmail/
_CARRIER = {
    "verizon": "vtext.com",
    "tmobile": "tmomail.net",
    "sprint": "messaging.sprintpcs.com",
    "at&t": "txt.att.net",
    "boost": "smsmyboostmobile.com",
    "cricket": "sms.cricketwireless.net",
    "uscellular": "email.uscc.net",
}

class SmtpLib():

    def __init__(self, 
            login_email: str=os.environ['EMAIL_ADDRESS'],
            # Create email application password (different from regular email password)
            # https://support.google.com/accounts/answer/185833?visit_id=638740700522860919-3941533513&p=InvalidSecondFactor&rd=1
            login_password: str=os.environ['EMAIL_APPLICATION_PASSWORD']
            ):
        self._login_email = login_email
        self._login_password = login_password

    def __enter__(self):
        # make a smtp connection and return it
        print('Creating SMTP connection')
        self._server = smtplib.SMTP(_HOST, 587)
        self._server.ehlo()
        self._server.starttls()
        self._server.login(self._login_email, self._login_password)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # make sure the smtp gets closed
        print('Closing SMTP connection')
        self._server.quit()

    def send_message(self,
            message: str,
            recipient: str,
            phone_carrier: str=None):
        # recipient will look something like '1234567890@vtext.com'
        if phone_carrier:
            recipient = f'{to_num}@{_CARRIERS[carrier]}'
        
        print(f'Sending message to {recipient}')
        self._server.sendmail(self._login_email, recipient, message)

if __name__ == "__main__":
    # First way of emailing or texting using Sftp Library.
    # It's free!
    with SmtpLib() as smtp_server:
        recipient=os.environ['TEST_EMAIL_RECIPIENT']
        smtp_server.send_message("some_message", recipient)