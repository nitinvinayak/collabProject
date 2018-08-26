import datetime
def option(start,numDig):
    for i in range(start,numDig):
        guess=guess+x[start]
        if (check()==True):
            print(guess)
            break
        elif(numDig<15):
            numDig+=1
            option(start,numDig)
        elif(numDig==15):
            numDig=0
            start+=1
        else:
            print("password greater than 15 digits")
        
    
def check():
    return(passw==guess)
        
if __name__=="__main__":
    start=0
    guess=""
    current=datetime.datetime.now()
    x=[]
    for k in range(15):
        for t in range(65,91):
            x.append(chr(t));
        for l in range(97,123):
            x.append(chr(l));
        for i in range(10):
            x.append(str(i))

    passw=str(input("Enter Password:"))
    #print(x)
    leng=passw.__len__()
    print(leng)
    decode=[]
    option(start,15)
    '''for i in range(15):
        a=option(i,opt);
        if(a[:a.__len__()]==passw[:passw.__len__()]):
            decode.append(a)
            break
            '''
    end=datetime.datetime.now()
    net=end-current
    print(net)
    print(decode)
    
