def check(str1, sub):
    if(str1.endswith(sub) or str1.startswith(sub)):
        return True
    else:
        return False
print(check("hi betty", "hi"))
print(check("mango is tasty", "tasty"))
