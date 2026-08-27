from numpy import array
t1=array([int()]*30)
t2=array([int()]*30)
t3=array([int()]*30)
def saisie():
    n=int(input("n="))
    while not(5<=n<=30):
        n=int-(input("n="))
    return n
def remplir(n,t):
    for i in range (n):
        t[i]=int(input("T["+str(i)+"]="))
def afficher (n,t):
    for i in range (n):
        print(t[i], end="|")
n1=saisie()
