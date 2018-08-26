x1=[]
for i in range(10):
    x1.append(str(i))
#x1=[''.join(x1)]
c=[]
for i in range(10):
    c.append(str(i))
#digit=input("Enter digits for password")
#for k in range(digit):
c=[i+j for i in x1 for j in x1]
c=[i+j for i in c for j in x1]
c=[i+j for i in c for j in x1]
c=[i+j for i in c for j in x1]
print(c)
