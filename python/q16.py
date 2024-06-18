def frequency(str):
    frequency={}
    temp=[]
    for i in str:
        if i not in temp:
            frequency[i]=str.count(i)
    return frequency
dict1=frequency("The mantis stalks the cicada, unaware of the oriole behind")
for i in dict1:
    print(i,":",dict1[i])
