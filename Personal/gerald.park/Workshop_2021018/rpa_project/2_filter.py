from imap_tools import MailBox
from account import *

applicant_list = []

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS,EMAIL_PASSWORD, intial_folder="INBOX") as f:
    index = 1 
    for msg in mailbox.fetch('SENTSINCE 07-NOV-2021'):
        if "파이썬 특강 신청합니다." in msg.subject:
            nickname, phone = msg.text.strip().split("/")
            print("순번 : {} 닉네임 : {} 전화번호 : {}".format(index, nickname,phone))
            applicant_list.append((msg, index,nickname,phone))
            index += 1

for applicant in applicant_list:
    print(applicant)