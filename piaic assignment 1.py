#piaic 1st assignment
##Q24
sum=0
for i in range(1,11):
    sum+=i
print(sum)
##Q25
sum_of_digits=0
number=1215
for i in str(number):
    sum_of_digits+=int(i)
print(sum_of_digits)
##Q26
lumber=2
a=bin(lumber)
print(a)
b=oct(lumber)
print(b)
c=hex(lumber)
print(c)

##Q27
##Q30
her="mobility"
newlist=[]
for i in her:
    newlist.append(i)
print(newlist)
print(newlist.count("i"))


#GCD
def gcd(a,d):
    if a!=0 and d!=0:
        r=a%d
        q=a//d
        if r==0:
            print("the answer is:",r)
        else:
            d_1=r
            a_1=d
            r_1=a_1%d_1
            q_1=a_1//d_1
            if r_1==0:
                print("The ans is",d_1)
            else:
                d_2=r_1
                a_2=d_1
                r_2=a_2%d_2
                q=a_2//d_2
                if r_2==0:
                 print("the result is:",d_2)
                else:
                    print("next time")
    else:
        print("TRY AGAIN")
#a=int(input("Enter value of dividend:"))
#d=int(input("Enter value of divisor:"))
#gcd(a,d)
# Function to return gcd of a and b
def gcd(a, b):
	if a == 0 :
		return b
	else:
	    return gcd(b%a, a)

a = 91
b = 287
#print("gcd(", a , "," , b, ") = ", gcd(a, b))

n=int(input("enter rows"))
for i in range(0,n+1):
    if i<5:
      for j in range(0,i+1):
        print("*",end="")
    else:
        for j in range(0,(n+1)-i):
         print("*",end="")
    print()


n=int(input("enter rows"))
for i in range(1,n+2):
    if i<=5:
      for j in range(1,i+1):
        print(j,end="")
    else:
        for j in range(1,(n+3)-i):
         print(j,end="")
    print()


n=int(input("Enter no. of rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()

n=int(input("no. of rows"))
for i in range(0,n+1):
    if i<5:
        for j in range(0,i+1):
            print("/",end="")
    else:
        for j in range(0,(n+1)-i):
            print("/",end="")
    print()


#table
def table(n,r):
    for i in range(1,r+1):
        c=n*i
        print(n, "*", i, "=", c)
n=int(input("enter no of which table u want"))
r=int(input("entr the range till u want"))
table(n,r)

#table
def table(n):
    for i in range(1,r+1):
        return n*i
n=int(input("enter no."))
for i in range(1,10):
    print(n,"*",i,"=",table(n))




























