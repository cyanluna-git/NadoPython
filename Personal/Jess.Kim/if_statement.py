taxi = 3000
my_money = 5000
if my_money >= taxi:
    print("Catch a taxi")

else:
    print("Walk, No taxi")



treehit = 0
tree_hp = 8

while treehit < 10:
    treehit = treehit + 1
    print("나무를 찍었습니다.")
    if treehit == 10:
        print("스태미나가 다했습니다.")
    else:
        print ("나무를 %d번 찍었습니다." % treehit)
    tree_hp = tree_hp - 1
    if tree_hp == 0:
        print("나무가 쓰러졌습니다.")
        break
    




