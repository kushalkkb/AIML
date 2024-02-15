from twilio.rest import Client

# Twilio credentials (replace with your own values)
account_sid = "AC70a3774ff54266b51cc821b181a221cd"
auth_token = "e678eed019766099a6eee8bf704fb439"
twilio_phone_number = "+12054028394"
recipient_phone_number = "+918792038996"  # Replace with the recipient's phone number

# Create a Twilio client
client = Client(account_sid, auth_token)

# Message content
message_body = "Hello, !"

# Send the message
message = client.messages.create(
    body=message_body,
    from_=twilio_phone_number,
    to=recipient_phone_number
)

# Print the SID (Message ID) to confirm the message was sent successfully
print(f"Message sent successfully. SID: {message.sid}")
