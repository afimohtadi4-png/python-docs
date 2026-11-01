def saisir():
    n=int(input("donner un entier:"))
    while n==0:
        n=int(input("redonner un autre entier supérieur à 0:"))
    return n
def produit(x):
    p=1
    while x!=0:
        if x%10!=0:
            p=p*(x%10)
        x=x//10
    return p
def cousin(x,y,t,r):
    if t==r:
        print(x,"et",y,"sont cousins")
    else:
        print(x,"et",y,"ne sont pas cousins")
#pp
a=saisir()
b=saisir()
cousin(a,b,produit(b),produit(a))