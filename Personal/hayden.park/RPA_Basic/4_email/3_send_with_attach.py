import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다." # 제목
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = "hyungmin08@gmail.com" #받는 사람
msg.set_content("다운로드 하세요")

# msg.add_attachment()

with open("file_menu.png", "rb") as f:
    msg.add_attachment(f.read(), maintype="image", subtype="png", filename=f.name) # 구글에서 MIME 검색하여 파일타입 참조

with open("테스트.pdf", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=f.name)

with open("테스트.xlsx", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=f.name)

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
