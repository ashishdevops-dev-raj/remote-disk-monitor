import os
import sys
from twilio.rest import Client

ACCOUNT_SID = os.environ.get("TWILIO_SID")
AUTH_TOKEN = os.environ.get("TWILIO_TOKEN")
FROM = os.environ.get("TWILIO_FROM")
TO = os.environ.get("ALERT_PHONE")

message = sys.argv[1] if len(sys.argv) > 1 else "No message provided"

try:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(body=message, from_=FROM, to=TO)
    print(f"Sent SMS to {TO}: {message}")
except Exception as e:
    print(f"Failed to send SMS: {e}")
