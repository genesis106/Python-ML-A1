def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    if(n1>n2):
        return n1-n2
    else:
        return n2-n1
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    if(n1>n2):
        return n1/n2
    else:
        return n2/n1

def main():
    a=input("ENTER A SIGN (*+/-) : ")
    n1=int(input("ENTER NUMBER1 : "))
    n2=int(input("ENTER NUMBER2 : "))
    if(a=="*"):
        print(multiply(n1,n2))
        return
    elif(a=="+"):
        print(add(n1,n2))
    elif(a=="-"):
        print(subtract(n1,n2))
    else:
        print(divide(n1,n2))
main()
