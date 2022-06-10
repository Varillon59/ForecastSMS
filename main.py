from ipaddress import IPv4Address
import time
import requests


from ssl import HAS_TLSv1
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService

ip = IPv4Address("192.168.1.20")
session = AirmoreSession(ip)
service = MessagingService(session)





response = requests.get("http://api.weatherapi.com/v1/current.json?key=1911adca0ab14800bc980847221006&q=Montreuil-sur-Mer&aqi=no")
temp = response.json()["current"]["temp_c"]
condition = response.json()['current']['condition']['text']
g = 0

while g == 0:
    messages = service.fetch_message_history()
    message = messages[0]
    chat = service.fetch_chat_history(message, 0, 2)
    sender_number = message.phone

    for i in range(len(chat)):
        if chat[i].content == "Température":
            service.send_message(sender_number,temp)
            print("envoi température")
        elif chat[i].content == "Condition":
            service.send_message(sender_number,condition)
            print("envoi condition")
        else:
            print("echec")
    









    time.sleep(10)