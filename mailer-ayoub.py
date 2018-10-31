#tested no python3.7
#
#i dont send your email and password to some server or clint u  can see this on the script

import os
os.system('clear')
os.system('figlet uzumaki')
os.system('figlet ayoub')
print("mer7ba bik asidi")
from  smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
print("clicki 3la Enter")
im = raw_input("AyoubMouhssine>>")
im =  input(" Aji Fin ghadi blati dakhel lcode :")
if im == "0123" :
    os.system("clear")
    print("")
    print("")
    print(" Mer7ba bik ")
    print("\____________/")


print("Mer7ba w alf mer7ba")
print("")
print("")
print("                               ********************")
print("")
print("                               By      uzumaki       ")
print("")
print("                               *********************")
print("")

email = raw_input("enter your email Azbi : ")
passwd = raw_input("enter password of email Azbi : ")
sendto = raw_input("kteb l email li baghi tsifet lih: ")
subj = raw_input("enter subject Azbi: ")
mesg = raw_input("enter your message Azbi : ")
nummsg = int(raw_input("Kteb 1 : "))
from  smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = sendto
msg['Subject'] = subj

msg.attach(MIMEText(mesg, 'plain'))

try:
     server = SMTP('smtp.gmail.com', 587)
     server.starttls()
     server.login(email, passwd)
     text = msg.as_string()

except:
        print("w93 mochkil f dokhoul l compte")

num = 0

while nummsg > num :
    text = msg.as_string()
    try:
        server.sendmail(email, sendto, text)
        print("3la slamtek ra tsenda binaja7")
    except:
        print("sending message blocked or email send to not found")
        break
    num += 1

server.close()
