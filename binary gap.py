import re
g=int(input("enter a number:"))
print(bin(g))
def solution(n):
    d=re.findall("0+1",n)
    print(d)
    for i in range(0,len(d)):
        print(d[i].count("0"))
solution(bin(g))

