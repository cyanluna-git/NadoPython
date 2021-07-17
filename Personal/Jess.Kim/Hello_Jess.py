print('trial 2')


#from os import stat_result
from tkinter import*

State = 0


#import 뒤에 *를 꼭 붙여주세요... 저거 안해서 못한 거였어...
root = Tk()

root.title ('Filp the switch')
#root.iconbitmap ('C:\Users\USER\Documents\GitHub\NadoPython\Personal\Jess.Kim\on.png')
root.geometry("500x300")

my_label = Label(root, text="Switch On", fg="green", font=("Helvetica", 32))
my_label.pack(pady=20)

Button (PhotoImage(file="on.png"))

'''
#이미지 불러오기가 안되는 듯 합니다.
#해결방안 찾아보기 1안 ==> https://www.youtube.com/watch?v=6Sf-P507nwg

#해결방안 `1안 적용` ... 실패

def Test (event):
    global state 
    if state == 1:
    my_label.config(image=on)
    State = 0

    else:
    my_label.config(image=off)
    State = 1



on = PhotoImage(file="Toggle_on.jpg")
off = PhotoImage(file="Toggle_off.jpg")


on_button = Button(root, image=on)
on_button.pack(pady=50)
'''

root.mainloop()



print('Hello Pyton. This is Jess')
