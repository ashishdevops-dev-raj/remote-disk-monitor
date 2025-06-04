import os
import sys
from twilio.rest import Client

# Load from environment or secrets
ACCOUNT_SID = os.environ["TWILIO_SID"]
AUTH_TOKEN = os.environ["TWILIO_TOKEN"]
FROM = os.environ["TWILIO_FROM"]
TO = os.environ["ALERT_PHONE"]

client = Client(ACCOUNT_SID, AUTH_TOKEN)
message = sys.argv[1]

client.messages.create(
    body=message,
    from_=FROM,
    to=TO
)
