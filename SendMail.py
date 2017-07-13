# A helper function for sending emails
import datetime
import base64

def sendMail(Message):
	import smtplib
	fadd = 'omkarpathak.comp@mmcoe.edu.in'         # sender's email address
	tadd = 'omkarpathak.comp@mmcoe.edu.in'         # receiver's email address
	msg = Message                                  # Message to be sent!
	username = 'omkarpathak.comp@mmcoe.edu.in'     # Your username(email ID)
	with open('/home/omkarpathak/Documents/GITs/A-Simple-Note-Taking-Terminal-App/password.txt', 'rb') as password:
		encryptedData = password.read()
		password = base64.b64decode(encryptedData) # Your encrypted password for above email ID
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login(username, password.decode('utf-8'))
	server.sendmail(fadd,tadd,msg)
	server.close()

with open('/home/omkarpathak/Documents/GITs/A-Simple-Note-Taking-Terminal-App/Schedules.txt','r') as outFile:
    result = outFile.read().split('\n')
    for results in result:
        try:
            currentDateTime = results.split(' ')
            currentDate = currentDateTime[0].split('-')
            currentTime = currentDateTime[1].split(':')
            Message = currentDateTime[2:]
            date = datetime.date(int(currentDate[2]), int(currentDate[1]), int(currentDate[0])).strftime("%Y-%m-%d")
            time = datetime.time(int(currentTime[0]), int(currentTime[1])).strftime("%H:%M")
            res = date + ' ' + time
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
            # print(res, now)
            if res == now:
                message = ' '.join(Message)
                sendMail(message)
        except IndexError:
            pass
