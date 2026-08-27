from numpy import array
n=int(input("donner n"))
while n>15:
    n=int(input("donner n"))
def alpha(ch):
    test=True
    for i in range (len(ch)):
        if not("A"<=ch[i].upper()<="Z"):
            test=False
    return test
T=array([str]*n)
def remplir(n,T):
    for i in range (n):
        T[i]=input("T["+str(i)+"]=")
        while T[i]=="" and alpha(T[i])==False:
            T[i]=input("T["+str(i)+"]=")
def maxi(n,T):
    global m
    m=len(T[0])
    for i in range (n):
        if len(T[i])>m:
            m=len(T[i])
    for i in range (n):
        if len(T[i])==m:
            print(T[i])
    print("la taille maximale est"+str(m))
remplir(n,T)
maxi(n,T)
    
    
    
    
    
    
    