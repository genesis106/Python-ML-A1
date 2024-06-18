def noOfDigits(n):
    if n == 0:
        return 1  
    if n < 0:
        n = -n  
    if n < 10:
        return 1
    return 1 + noOfDigits(n // 10)

print(noOfDigits(6789))  
print(noOfDigits(0))     
print(noOfDigits(-1234)) 
