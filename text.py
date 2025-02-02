# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv

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

if __name__ == "__main__":
    test_client = Twilio()
    test_client.text_client()