import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "gerald.park@edwardsvacuum.com"
msg.set_content("다운로드 하세요")

with open("file.png","rb") as f:
    msg.add_attachment(f.read(), maintype="image", subtype="png", filename=f.name)

with open("test.pdf","rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=f.name)

with open("sample.xlsx","rb") as f:
    msg.add_attachment(f.read(), maintype="appication", subtype="octet-stream", filename=f.name)

with smtplib.SMTP("smtp.gmail.com",587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
