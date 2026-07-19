import re

# abcd, book, desk
# ca?e 

p = re.compile("ca.e") 
# . (ca.e): 하나의 문자를 의미함 > care,cafe (o) | caffe(X)
# ^ (^de ): 해당 문자열로 시작: destination, desk(o)  : fade(x)
# $ (se$ ): 해당 문자열로 끝나는것 : case, base(o) : face(x)

def print_match(m):
    if m:
        print("m.group()", m.group())
        print("m.string()", m.string)
        print("m.start()", m.start())
        print("m.end()", m.end())
        print("m.span()", m.span())
    else:
        print("매칭되지 않음 ")

m = p.match("careless") #주어진 문자열의 처음부터 일치하는지 확인 
print_match(m)

m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인 
print_match(m)

lst = p.findall("careless")
print(lst)