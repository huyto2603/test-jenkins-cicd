import pymsteams
url="https://thctechgroup.webhook.office.com/webhookb2/bb16601c-e361-4dd2-a765-d3e91813f61f@c721557d-32d7-4cbd-9aad-5ba096cd7683/IncomingWebhook/ef99037f9de046f58d328001a8659a8d/183db949-d3e9-4471-85a6-381466ccba6d"
# You must create the connectorcard object with the Microsoft Webhook URL
myTeamsMessage = pymsteams.connectorcard(url)

# Add text to the message.
myTeamsMessage.text("hello")

# send the message.
myTeamsMessage.send()
