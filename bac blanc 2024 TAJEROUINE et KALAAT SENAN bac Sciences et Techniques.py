from numpy import array
from random import randint
c=array([str]*10)
n=array([str]*10)
def saisie():
    global nc
    nc=int(input("nc="))
    while not (3<=nc<=10):
        nc=int(input("nc="))
def teste(x,nc,c):
    i=0
    while (i!=nc-1) and (c[i]!=x):
        i=i+1
    return i=nc
def verif(x,ch):
    test=True
    if not (("3"<=ch[0]<="4") or (ch[1].upper()=="M" and ch[2].upper()=="A") or (ch[1].upper()=="S" and ch[2].upper()=="C")or (ch[1].upper()=="T" and ch[2].upper()=="C") or ("1"<=ch[3]<="5")):
        test=False
    if (test==False) or (teste(x,nc,c)==False):
        test=False
    else:
        test=True
    return test
def remplir(nc,c):
    for i in range (nc):
        c[i]=input()
        while verif(c[i],i,c)==False:
            c[i]=input()
def remplirr(n,c):
    global nn
    nn=int(input("donner nn="))
    for i in range (nn):
        n[i]=c[i]+"*"+randint(1,9)