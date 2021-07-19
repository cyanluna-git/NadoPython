
#from os import stat_result
from tkinter import*

#import 뒤에 *를 꼭 붙여주세요... 저거 안해서 못한 거였어...
root = Tk()

root.title ('Filp the switch')
#root.iconbitmap ('C:\Users\USER\Documents\GitHub\NadoPython\Personal\Jess.Kim\Toggle_on.jpg')
root.geometry("500x300")

my_label = Label(root, text="Switch On", fg="green", font=("Helvetica", 32))
my_label.pack(pady=20)

#창까지는 띄웠는데 아래 내용에 오류가 있음
'''

on = PhotoImage(file="C:\Users\USER\Documents\GitHub\NadoPython\Personal\Jess.Kim\Toggle_on.jpg")
off = PhotoImage(file="C:\Users\USER\Documents\GitHub\NadoPython\Personal\Jess.Kim\Toggle_off.jpg")

on_button = Button(root, image=on)
on_button.pack(pady=50)
'''

root.mainloop()
