# Quiz) 매주 1회 보고서 있음 

# -x 주차 주간보고- 
# 부서 : 
# 이름 : 
# 업무 요약 : 
# 1주차 50주차 보고서 파일 

# 조건 : 파일명은 '1주차.txt'~~~~

for i in range(1, 51):
    with open(str(i)+"주차.txt","w",encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고- \n".format(i))
        report_file.write("부서 :  \n")
        report_file.write("이름 :  \n")
        report_file.write("업무요약 :  \n")