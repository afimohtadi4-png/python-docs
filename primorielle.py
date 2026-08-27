def premier(x):
    test=True
    for i in range (2,x):
        if x%i==0:
            test=False
    return test
def prim(n):
    p=1
    for i in range (2,n+1):
        if premier(i)==True :
            p=p*i
    return p
#pp
n=int(input("donner n"))
print(prim(n))