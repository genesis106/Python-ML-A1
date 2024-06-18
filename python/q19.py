def removePunctuation(str):
    new=""
    for i in str:
        if i in ",.?!:;'-[]_{}&()/":
            continue
        new+=i
    return new
print(removePunctuation("The weather was unexpectedly hot today; I forgot my umbrella, and now I'm soaked!"))

            
