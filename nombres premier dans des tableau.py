from numpy import array
T1=array([int()]*20)
T2=array([int()]*20)
def saisie():
    n=int(input("n="))
    while not (0<=n<=30):
        n=int(input("redonner n"))
    return n
def remplir(n,T):
    for i in range(n):
        T[i]=int(input("donner T["+str(i)+"]="))
def prem(x):
    d=2
    test=True
    while test==True and d<=x//2:
        if x%d==0:
            test=False
        else:
            d=d+1
    return test
#pp
n1=saisie()
n2=saisie()
remplir(n1,T1)
remplir(n2,T2)
s1=""
s2=""
for i in range (n1):
    print (T1[i],end="/")
print()
for i in range (n2):
    print (T2[i], end="/")
for i in range (n1):
    if prem(T1[i])==True:
        s1=s1+str(T1[i])
for i in range (n2):
    if prem(T2[i])==True:
        s2=s2+str(T2[i])
print("les nombres premiers de T1 sont"+s1)
print("les nombres premiers de T2 sont"+s2)       