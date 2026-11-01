from numpy import array
t=array([int()]*100)
def saisir():
    n=int(input("donnner la languer du tableau"))
    while not (1<=n<=100):
        n=int(input("redonnner la languer du tableau pour qu'elle soit entre 10 et 100"))
    return n
def remplir(t,n):
    for i in range (n):
        t[i]=int(input("T["+str(i)+"]="))
        while len(str(t[i]))!=4:
            t[i]=int(input("T["+str(i)+"]="))
def premier(x):
    i=2
    while (i<(x//2)+1) and (x%i!=0):
        i=i+1
    return i==(x//2)+1
def somme(nb,ch,a):
    if premier(a)==True:
        nb=nb+1
        ch=ch+str(a)+","
    return nb,ch
def former(x):
    nb=0
    ch=""
    nb,ch=somme(nb,ch,x//10)
    nb,ch=somme(nb,ch,x%100)
    nb,ch=somme(nb,ch,x%1000)
    nb,ch=somme(nb,ch,(x//10)%100)
    nb,ch=somme(nb,ch,x//1000)
    nb,ch=somme(nb,ch,x//100)
    nb,ch=somme(nb,ch,x)
    nb,ch=somme(nb,ch,x//10%10)
    nb,ch=somme(nb,ch,x//100%10)
    nb,ch=somme(nb,ch,x%10)
    if nb!=0:
        print(x,"possède"+str(nb)," nombres premiers qui sont"+ch[:len(ch)-1])
    else :
        print("Ce nombre ne contient pas des nombres premiers")
def afficher(t,n):
    for i in range(n):
        former(t[i])
#pp
n=saisir()
remplir(t,n)
afficher(t,n)