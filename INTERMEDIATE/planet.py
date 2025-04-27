mercury=0.376
venus=0.889
mars=0.378
jupiter=2.36
saturn=1.081
uranus=0.815
neptune=1.14
def weightCal():
    weight=int(input("Enter a weight on Earth: "))
    planet=input("Enter a planet: ")
    if planet == "Mars":
        weight=weight*mars
        weightUpdated=round(weight,2)
        print("The equivalent weight on Mars:",weightUpdated)
    elif planet == "Saturn":
        weight=weight*saturn
        weightUpdated=round(weight,2)
        print("The equivalent weight on Saturn:",weightUpdated)
    elif planet == "Jupiter":
        weight=weight*jupiter
        weightUpdated=round(weight,2)
        print("The equivalent weight on Jupiter:",weightUpdated)
    elif planet == "Uranus":
        weight=weight*uranus
        weightUpdated=round(weight,2)
        print("The equivalent weight on Uranus:",weightUpdated)
    elif planet == "Mercury":
        weight=weight*mercury
        weightUpdated=round(weight,2)
        print("The equivalent weight on Mercury:",weightUpdated)
    elif planet == "Neptune":
        weight=weight*neptune
        weightUpdated=round(weight,2)
        print("The equivalent weight on Neptune:",weightUpdated)
    elif planet == "Venus":
        weight=weight*venus
        weightUpdated=round(weight,2)
        print("The equivalent weight on Venus:",weightUpdated)
weightCal()


