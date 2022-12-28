import pymsteams


def msteamipexpireftg(host, ip, groupname):

    url_webhook = "https://thctechgroup.webhook.office.com/webhookb2/bb16601c-e361-4dd2-a765-d3e91813f61f@c721557d-32d7-4cbd-9aad-5ba096cd7683/IncomingWebhook/ef99037f9de046f58d328001a8659a8d/183db949-d3e9-4471-85a6-381466ccba6d"
    myTeamsMessage = pymsteams.connectorcard(url_webhook)
    myMessageSection = pymsteams.cardsection()

    myTeamsMessage.summary("fortigate")

    myTeamsMessage.color("#0000FF")
    # Activity Elements
    myMessageSection.activityTitle("Splunk Fortigate Action")

    myMessageSection.activityImage(
        "https://external-preview.redd.it/8QzkUXNHecjmGdlrSyhdTc4_WyjoueaC01TL5ku5o9s.jpg?auto=webp&s=1151421489c803cdb58d82443e932104bfe8f3dc"
    )

    myMessageSection.activitySubtitle("Remove IP Local")
    myMessageSection.text("Địa chỉ IP này đã được remove do quá thời gian block .")

    # myTeamsPotentialAction3.addAction("HttpPost","Xem kết quả", actionbutton2)

    ip_without_subnet = str(ip).split(" ")[0]
    subnet = str(ip).split(" ")[1]
    # Facts are key value pairs displayed in a list.
    myMessageSection.addFact(host, f"{groupname} - <b>{ip}</b>")
    # Section Text
    # Section Image

    # myTeamsMessage.addLinkButton("Start", actionbutton)

    # Add your section to the connector card object before sending

    myTeamsMessage.addSection(myMessageSection)

    myTeamsMessage.send()
    return myTeamsMessage.last_http_response.status_code
