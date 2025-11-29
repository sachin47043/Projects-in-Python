from twilio.reset import Client
ACCOUNT_SID = "AC2ccca2aadb42f41d41ded47d74c53aad"
AUTH_TOKEN = "892e678e275c121cc50e2f3f85fc6949"
TWILIO_NUM = "+18312312172"
RECEIVER_NUM = "+918102092566"
Client = Client(ACCOUNT_SID, AUTH_TOKEN)
messages = Client.messages.create(
    body = "hello i am python",
    from_ = TWILIO_NUM,
to=RECEIVER_NUM)