# 제목 : 파이썬 특강 신청합니다.
# 본문 : 닉네임/전화번호 뒤 4자리 (Random)
# (예)   나도코딩/1234

from imap_tools import MailBox
from account import *

applicant_list = [] # 지원자 리스트


with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    index = 1 # 순번 저장
    for msg in mailbox.fetch('(SENTSINCE 17-Oct-2021)'): # 2021년 10월 17일 이후로 온 메일 조회
        if "파이썬 특강 신청합니다." in msg.subject:
            nickname, phone = msg.text.split("/")
            print("순번 : {0} 닉네임 : {1} 전화번호 : {2}".format(index, nickname, phone))
            applicant_list.append((msg, index, nickname, phone))
            index += 1

for applicant in applicant_list:
    print(applicant)
