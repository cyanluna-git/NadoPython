import smtplib
from account import *
with smtplib.SMTP("smtp.gmail.com",587) as smtp:
    smtp.ehlo() # 연결이 잘 수행 되는지 확인
    smtp.starttls() # 모든내용이 암호화 
    ### 여기까지는 기본 
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = "test mail"
    body = "main body"

    msg = f"Subjext: {subject}\n{body}"

    #발신자,수신자, 메시지
    smtp.sendmail(EMAIL_ADDRESS, "gerald.park@edwardsvacuum.com", msg) 