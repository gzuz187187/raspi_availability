import pywhatkit as pwk
 
# using Exception Handling to avoid unexpected errors
try:
     # sending message in Whatsapp in India so using Indian dial code (+91)
     pwk.sendwhatmsg("+436605348510", "Komm in die Gruppe, was hast du zu verlieren", 22, 51)
 
     print("Message Sent!") #Prints success message in console
 
     # error message
except: 
     print("Error in sending the message")