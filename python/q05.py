def writeToFile():
    f = open("demofile.txt", "w")
    str=input("Enter what you want to write in file : ")
    f.write(str)
    f.close()
    
