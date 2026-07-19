from imap_tools import MailBox
from account import *

mailbox = MailBox("imap.gmail.com", 993)
mailbox.login(EMAIL_ADDRESS,EMAIL_PASSWORD, initial_folder="INBOX")

# limit : 최대메일 갯수
# reverse : True 일경우 최근 메일 부터 
for msg in mailbox.fetch(limit=1, reverse=True):
    print("제목", msg.subject)
    print("발신자", msg.from_)
    print("수신자", msg.to)
    print("참조자", msg.cc)
    print("비밀참조자", msg.Bcc)
    print("날짜", msg.date)
    print("본문", msg.text)
    print("HTML Message", msg.html)
    print("="*100)

    # 첨부 파일 
    for att in msg.attachments:
        print("첨부파일", att.filename)
        print("타입", att.content_type)
        print("크기", att.size)

        with open("download_" + att.filename, "wb") as f:
            f.write(att.payload)
            print("첨부 파일 {} 다운로드 종료".format(att.filename))

mailbox.logout()