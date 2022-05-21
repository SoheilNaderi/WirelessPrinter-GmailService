import easyimap
import os
import time

def Receiveemail():
    chk=open('log.txt','r');lastid=chk.read();chk.close()   
    lcont={} ; listname="" ; listfile=("png","jpg","pdf","jpeg")
    imapper = easyimap.connect('imap.gmail.com','gmail','password')
    mail_id=imapper.listids(limit=100)
    if str(mail_id[0])!=lastid :
        mail = imapper.mail(mail_id[0])
        lcont.update({"from": mail.from_addr})
        lcont.update({"to": mail.to})
        lcont.update({"cc":mail.cc})
        lcont.update({"subject":mail.title})
        lcont.update({"body":mail.body})
        lcont.update({"attach":mail.attachments})
        for attachment in mail.attachments:
            filetype=attachment[0][attachment[0].find('.')+1:]
            for i in listfile:
                if filetype==i:                
                    listname+=" "+attachment[0]
                    f = open(attachment[0], "wb")
                    f.write(attachment[1])
                    f.close()
        reg=open('log.txt','w');reg.write(str(mail_id[0]));reg.close()
    return lcont,listname

print("=================================\nCheck...",end="    ")
while True:
    lcont,listname=Receiveemail()
    if lcont and listname:
        print("OMG! you have an item *_*")
        print(lcont["from"],listname)
        os.system("lp -o sides=two-sided-long-edge "+listname)
        print("Finish!\n=================================")
    else:
        print("\nCheck...",end="    ")
    time.sleep(30)