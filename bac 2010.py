from numpy import array
t=array([int()]*11)
def saisie():
    global n
    n=int(input("n="))
    while not (4<=n<=10):
        n=int(input("redonner n"))
def remplir(n,t):
    t[0]=int(input("T[0]="))
    for i in range (1,n):
        t[i]=int(input("T["+str(i)+"]="))
        while t[i]<t[i-1]:
            t[i]=int(input("T["+str(i)+"]="))
def saisirr():
    global e
    e=int(input("e="))
def inserer(e,n,t):
    i=n-1
    while (i>=1) and (t[i]>e):
        t[i+1]=t[i]
        i=i-1
    t[i]=e
def afficher(n,t):
    for i in range (n+1):
        print(t[i])
#pp]
saisie()
remplir(n,t)
saisirr()
inserer(e,n,t)
afficher(n,t)