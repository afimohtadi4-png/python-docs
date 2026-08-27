def saisir():
    global x
    x=int(input("x="))
    while x%1000==0:
        x=int(input("x="))
def somdivs(x):
    u=x%10
    n=str(x)
    s=0
    for i in range (1,len(n)):
        if x%i==0:
            s=s+1
    return s
def verif(x,s):
    test=True
    while test==True:
        if s<x%10:
            test=False
m=saisir()
def verifier(x):
    for i in range (len(str(x))):
        test2=True
        a=str(x)
        ch=a[i]
        s1=somdivs(int(ch))
        while test2==True:
            if verif(int(ch),s1)==False :
                test2==False
    return test2
if verifier(m):
    print(str(m)+"est decimal parfait")
else:
    print(str(m)+"n'est pas decimal parfait")
        
    