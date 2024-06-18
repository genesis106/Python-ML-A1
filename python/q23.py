def c_to_f(c):
    f = (c * 9/5) + 32
    return f

def f_to_c(f):
    c = (f - 32) * 5/9
    return c
def conversion():
    num=int(input("ENTER TEMPERATURE : "))
    select=int(input("ENTER 1 FOR C-TO-F OR 2 FOR F-TO-C CONVERSION: "))
    if(select==1):
        print(c_to_f(num))
        return
    else:
        print(f_to_c(num))
        return

conversion()
