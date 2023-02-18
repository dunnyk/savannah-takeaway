import africastalking
import os
from django.conf import settings

def send_sms(phone_number):
    username = "sandbox"

    africastalking.initialize(username, settings.AT_API_KEY)
    sms = africastalking.SMS

    # set the message and recipient details
    message = "Thanks customer, your order is successful TESTING OUT"
    recipients = [phone_number]
    sender = '56776'

    # send the sms message
    try:
        response = sms.send(message, recipients, sender)
    except Exception as e:
        print(f"Found an error while sending SMS: {e}")
