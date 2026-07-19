# 신청 메일 양식 

import smtplib
from random import *
from account import *
from email.message import EmailMessage

nicknames = ["유재석","박명수","정형돈","조세호","노홍철"]

with smtplib.STMP("smtp.gmail.com",587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for nickname  in nicknames:
        msg = EmailMessage()
        msg["Subject"] = "파이썬 특강 신청합니다"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = "gerald.park@edwardsvacuum.com"

        # content = nickname + "/" + str(randint(1000,9999))
        content = "/".join([nickname, str(randint(1000,9999))])
        msg.set_content(content)
        smtp.send_message(msg)
        print(nickname + "님이 나도코딩 계정으로 메일 발송 완료")

