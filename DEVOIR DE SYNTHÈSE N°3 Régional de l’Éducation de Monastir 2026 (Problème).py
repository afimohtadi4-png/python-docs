from random import randint
from numpy import array
t=array([str]*100)
v=array([str]*100)
def saisir():
    global n
    n=int(input("donner n"))
    while not (n<=100):
        n=int(input("redonner n pour qu'elle soit inférieure à 100"))
def remplir(t,n):
    for i in range (n):
        t[i]=str(input("donner T["+str(i)+"]"))
        while not ((len(t[i])==8) and (t[i].isdecimal()==True)):
            print(len(ch))
            t[i]=str(input("redonner T["+str(i)+"] pour qu'elle soit valide"))            
def eligible(ch):
    m=0
    for i in range (1,len(ch)):
        j=0
        while (j<=i-1) and (ch[j]!=ch[i]):
            j=j+1
        if j!=i:
            m=m+1
    return m<=1
def former(v,t,n):
    global q
    q=0
    for i in range (n):
        if eligible(t[i])==True:
            ch=t[i]
            v[q]=ch
            q=q+1
def afficher(v,q):
    ch="les numéros gagnants sont:"
    k=int(input("donner le nombre de gagnants"))
    if q==0:
        print("Aucun abonné n'admet un numéro éligible")
    else:
        for i in range(k):
            p=randint(0,q-1)
            while ch.find(v[p])!=-1 :
                p=randint(0,q-1)
            ch=ch+v[p]+" "
        print(ch[:len(ch)-1])

#pp
saisir()
remplir(t,n)
former(v,t,n)
afficher(v,q)