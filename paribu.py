import requests
import time

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 OPR/68.0.3618.63'}

liste = []

# telegram mesaj gönderme
def telegram_bot_sendtext(bot_message):
    bot_token = '5606823959:AAFSrYDqxT45c0eHEtiilltuyt6Vxe-hXHU'
    bot_chatID = '-880267023'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

f = open("linkler.txt", "r")
while True:
    for x in f:
        r = requests.get(x.replace("\n",""),headers=headers)
        if r.status_code == 200 and x not in liste:
            liste.append(x.replace("\n",""))
            telegram_bot_sendtext(x.split("/")[-1].replace("\n","") + " Bulundu.")
            print("Bulundu")
