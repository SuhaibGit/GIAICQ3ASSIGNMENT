def doubleit():
    userinput:int=int(input("Enter Number to double it:"))
    if userinput >= 0:
        while userinput < 100:   
            print(userinput ,"doubled", userinput*2)
            userinput=userinput*2
    else:
        print("Invalid input")
doubleit()