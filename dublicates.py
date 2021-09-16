a=[1,2,3,4,2,2,2,5,5,5,5,4]
b=[]
def dublic(a):
    for i in a:
        if a.count(i)>1:
            b.append(i)
    print(list(set(b)))
dublic(a)
