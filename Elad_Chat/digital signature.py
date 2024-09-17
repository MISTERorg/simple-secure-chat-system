def arrange(x,y):
    if x>y:
        a=x
        x=y
        y=a
    return [x,y]


#division algorithm
def DivisionAlgorithm(x,y):
    [x,y]=arrange(x,y)
    i=0
    q=0

    while q>=0:
        i=i+1
        q=y-(x*i)
    i=i-1
    r=y-(x*i)
    return [i,r]



#euclidean algorithm
def euclidean(x,y):
    [x,y]=arrange(x,y)
    while x>0:
        [i,r]=DivisionAlgorithm(x,y)
        y=x
        x=r
    return y
    


#euclidean inverse algorithm
#this function assumes thier GCD is zero else it will work but give fack answers
def euclideanInv(x,y):
    [x,y]=arrange(x,y)
    t1=0
    t2=1
    s1=1
    s2=0

    while x>1:
        [i,r]=DivisionAlgorithm(x,y)
        T=t1-(t2*i)
        S=s1-(s2*i)
        y=x
        x=r
        t1=t2
        s1=s2
        t2=T
        s2=S
    return [S,T]

    


def bigValues(i,e,n):
    
    if e%2==0:
        h=2
        g=(i**2)%n
        while h<e:
            g=g*((i**2)%n)
            g=g%n
            h=h+2
    else:
        h=3
        g=(i**3)%n
        while h<e:
            g=g*((i**2)%n)
            g=g%n
            h=h+2
    return g

         
def bighash(he,e,n):
    h=1
    g=he%n
    while h<e:
        g=g*(he%n)
        g=g%n
        h=h+1

    return g
 


def RSAencription(e,n,m,he):
    c=[]
    for i in m:
        c.append(bigValues(i,e,n))
    c.append(bighash(he,e,n))
    return c


    


def RSAdecription(d,n,c):
    T=[]
    j=c.pop()
    for i in c:
        T.append(bigValues(i,d,n))
    T.append(bighash(j,d,n))
    return T
    


print("this is for RSA , enter two large prime p and q")
p=int(input("enter a value p: "))
q=int(input("enter a value q: "))
text=input("enter your text to encrypt : ")
print("the string is "+text)

he=hash(text)
print(he)

m=[]
for i in text:
    m.append(ord(i))
print(m)

n=p*q
print("n is "+str(n))

Qn=(p-1)*(q-1)
print(" Q(n) is "+str(Qn))

print("choose a value e such that 1<e<"+str(Qn)+" and Gcd(e,Q("+str(n)+"))=1")
e=int(input("enter e from the above condition"))

while euclidean(e,Qn)>1 and e>=Qn :
    e=input("wrong value please enter a value e such that e>1<"+str(Qn)+" and Gcd(e,Q("+str(n)+"))=1")


print(" e is "+str(e))

[l,E]= euclideanInv(e,Qn)
d=E%Qn
print(" d is "+str(d))

c= RSAencription(e,n,m,he)
print("the encrypted value is ",str(c))

dm= RSAdecription(d,n,c)
print("the decrypted value is "+str(dm))
he=dm.pop()
print(he)
print("the new decrypted value is "+str(dm))
de=[]
for i in dm:
    de.append(chr(i))
hd=hash(''.join(de))
if he==hd%n:
    print("the message has not been altered")
    print("the decrypted value is "+str(de))
else:
    print("the message has been altered can\'t print fake messages")