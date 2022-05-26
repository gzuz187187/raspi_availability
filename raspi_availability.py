from bs4 import BeautifulSoup
import requests
import time
import pywhatkit as pwk
import os

url1_2gb = "https://buyzero.de/products/raspberry-pi-4b?src=raspberrypi&variant=28034031812710"
url2_1gb = "https://electronics.semaf.at/Raspberry-Pi-4-15GHz-ARM-Cortex-A72-1GB-LPDDR4-RAM?src=raspberrypi"
url3_1gb = "https://www.berrybase.at/detail/index/sArticle/9348?src=raspberrypi"
url4_1gb = "https://www.pi-shop.ch/raspberry-pi-4-model-b-1gb?src=raspberrypi"
url5_2gb = "https://electronics.semaf.at/Raspberry-Pi-4-15GHz-ARM-Cortex-A72-2GB-LPDDR4-RAM?src=raspberrypi"
url6_2gb = "https://www.pi-shop.ch/raspberry-pi-4-model-b-2gb?src=raspberrypi"
url7_4gb = "https://www.pi-shop.ch/raspberry-pi-4-model-b-4gb?src=raspberrypi"
url8_8gb = "https://electronics.semaf.at/Raspberry-Pi-4-B-4x-15GHz-CPU-8GB-DDR4-RAM-BLE5-WLAN?src=raspberrypi"
url9_8gb = "https://buyzero.de/products/raspberry-pi-4-model-b-8gb?src=raspberrypi"
message = ""

def get_soup(url, find_all_text, msg_on_website):
    temp_message = ""
    raw = requests.get(url)
    temp_soup = BeautifulSoup(raw.text, "html.parser")
    result = temp_soup.findAll(class_=find_all_text)

    if msg_on_website.upper() in str(result).upper():
        temp_message += f"{url.split('/')[2]}: Nicht vorhanden\n\n"
    else:
        temp_message += f"{url.split('/')[2]}: Vorhanden ({url})\n\n"
    
    return temp_message

# 1st url
msg = get_soup(url1_2gb, "product-form__inventory inventory", "ausverkauft")
message += "(2gb/4gb) " + msg

# 2nd url
msg = get_soup(url2_1gb, "signal_image label red-600 status-0", "nicht auf lager")
message += "(1gb) " + msg

# 3rd url
msg = get_soup(url3_1gb, "alert--content", "Dieser Artikel steht derzeit nicht zur Verfügung!")
message += "(1gb) " + msg

# 4th url
msg = get_soup(url4_1gb, "availability", "Zur Zeit nicht an Lager")
message += "(1gb) " + msg

# 5th url
msg = get_soup(url5_2gb,"signal_image label red-600 status-0", "Nicht auf Lager")
message += "(2gb) " + msg

# 6th url
msg = get_soup(url6_2gb, "availability", "Zur Zeit nicht an Lager")
message += "(2gb) " + msg

# 7th url
msg = get_soup(url7_4gb, "availability", "Zur Zeit nicht an Lager")
message += "(4gb) " + msg

# 8th url
msg = get_soup(url8_8gb,"signal_image label red-600 status-0", "Nicht auf Lager")
message += "(8gb) " + msg

# 9th url
msg = get_soup(url9_8gb, "product-form__inventory inventory", "ausverkauft")
message += "(8gb) " + msg

print(message)

time.sleep(30)

try:
     pwk.sendwhatmsg("+436605348510", message, 00, 3)
 
     print("Message Sent!")
except: 
     print("Error in sending the message")

time.sleep(120)
os.system("TASKKILL /F /IM firefox.exe")