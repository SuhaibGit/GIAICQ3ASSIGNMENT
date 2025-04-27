
#adding two numbers
def Add_to_num():
    print("This function add 2 number")
    num1:str=input("Enter first Number: ")
    num1:int=int(num1)
    num2:str=input("Enter Second Number: ")
    num2:int=int(num2)
    res:int=num1+num2
    print("The total is: "+str(res))


# aggreemenyt bot
def Fav_Anim():
    print("This function is to ask favourite animal")
    user:str=input("What's your favourite animal? ")
    print("My favorite animal is also "+user+ ".")


#temp converter
def temp_conv():
    print("This function is for temp convertor")
    Farh:str=input("Enter Temperatue in Fahrenheit: ")
    Farh:float=float(Farh)
    celsius:float=(Farh-32)* 5.0/9.0
    print("Temperature: "+str(Farh)+" = "+str(celsius)+"C")


#Age Riddle
def AgeRid():
    anton:int=21
    beth:int=6+anton
    chen:int=20+beth
    derw:int=chen+anton
    ethan:int=chen
    print("Anton is "+str(anton))
    print("Beth is "+str(beth))
    print("Chen is "+str(chen))
    print("Drew is "+str(derw))
    print("Ethan is "+str(ethan))


#triangle peri
def triangle():
    side1: float = float(input("What is the length of side 1? "))
    side2: float = float(input("What is the length of side 2? "))
    side3: float = float(input("What is the length of side 3? "))
    print("The perimeter of the triangle is " + str(side1 + side2 + side3))


#Square of a number
def Square():
    value:float=float(input("Enter the Number you wanted to square: "))
    print("The square of a given number will be: "+str(value**2))
Square()

