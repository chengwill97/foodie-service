# Download the helper library from https://www.twilio.com/docs/python/install
import os
from dotenv import load_dotenv

import smtplib
from twilio.rest import Client

# Loads env variables from the .env file
load_dotenv()


# Defines a class template Twilio which we can use to create objects later.
class Twilio():

    # First thing that runs when the class is created.
    def __init__(self,
            from_num: str=os.environ['FROM_NUMBER'],
            to_num: str=os.environ['TO_NUMBER']):
        print('Created a Twilio class!')

        self.from_num = from_num
        self.to_num = to_num

        print('Setting up Twilio authentication from environment.')
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.client = Client(self.account_sid, self.auth_token)

    def text_client(self, text_message: str="Join Earth's mightiest heroes. Like Kevin Bacon."):
        print(f'Sending text message from {self.from_num} to {self.to_num}.')
        message = client.messages.create(
            body=text_message,
            from_=self.from_num,
            to=self.to_num,
        ) 
        print(message.body)


class SmtpLib():
 
    _CARRIERS = {
        "att": "@mms.att.net",
        "tmobile": "@tmomail.net",
        "verizon": "@vtext.com",
        "sprint": "@messaging.sprintpcs.com"
    }

    def __init__(self, 
            email: str=os.environ['EMAIL_ADDRESS'],
            # Create email application password (different from regular email password)
            # https://support.google.com/accounts/answer/185833?visit_id=638740700522860919-3941533513&p=InvalidSecondFactor&rd=1
            password: str=os.environ['EMAIL_APPLICATION_PASSWORD']
            ):
        self._email = email
        self._password = password

    def __enter__(self):
        # make a smtp connection and return it
        print('Creating SMTP connection')
        self._server = smtplib.SMTP("smtp.gmail.com", 587)
        self._server.starttls()
        self._server.login(self._email, self._password)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # make sure the smtp gets closed
        print('Closing SMTP connection')
        self._server.quit()

    def send_message(self,
            message: str="testing",
            to_num: str=os.environ['TO_NUMBER'],
            carrier: str="verizon"):
        # recipient will look something like '1234567890@vtext.com'
        recipient = f'{to_num}{SmtpLib._CARRIERS[carrier]}'
        
        print(f'Sending message to {recipient}')
        self._server.sendmail(self._email, recipient, message)

if __name__ == "__main__":
    # First way of texting using Sftp Library.
    # It's free!
    with SmtpLib() as smtp_server:
        smtp_server.send_message(message="some_message", carrier="verizon")

    # Second way of texting using Twilio
    # test_client = Twilio()
    # test_client.text_client()