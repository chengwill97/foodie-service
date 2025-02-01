# Download the helper library from https://www.twilio.com/docs/python/install
import os
import sys
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = sys.argv[1]
auth_token = sys.argv[2]
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    from_="+18447873896",
    to="+12678797686",
)

print(message.body)
