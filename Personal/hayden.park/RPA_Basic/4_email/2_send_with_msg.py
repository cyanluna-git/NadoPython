import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다." # 제목
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = "hayden.park@edwardsvacuum.com" #받는 사람

# 여러 명에게 메일을 보낼 때
# msg["To"] = "nadocoding@gmail.com, nadocoding2@gamil.com"
to_list = ["nado1@gmail.com", "nado2@gmail.com"]
msg["To"] = ", ".join(to_list)


# # 참조처
# msg["Cc"] = "nadocoding@gmail.com"
# msg["Bcc"] = "nadocoding@gmail.com" # 비밀참조

msg.set_content("테스트 본문입니다.") # 본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)



