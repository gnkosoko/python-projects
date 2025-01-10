#Mad Libs
#Gabriel Kosoko
#Date

#Function
def madlibs():
    print("Welcome to Madlibs, a simulation that brings your ideas to life")
    print("Please enter your choices")
    adjective1 = input("Please enter an adjective:")
    noun1 = input("Please enter a noun:")
    location = input("Please enter a location:")
    verb1 = input("Please enter a verb:")
    emotion = input("Please enter a emotion:")
    verb2 = input("Please enter another verb:")
    location = input("Please enter another location:")
    print("Thank you, generating your story now...")
    print("One afternoon, a "  + "\033[1m" + adjective1 +"\033[0m"+ " " + "\033[1m" +  noun1 +"\033[0m"+ " went to the " + "\033[1m" + location +"\033[0m"+ ". At the " + "\033[1m" +location + "\033[0m"+" the " + "\033[1m"+ noun1 + "\033[0m"+" wanted to go " +"\033[1m"+  verb1 +"\033[0m"+ ". A lot of other people showed up to the " +"\033[1m"+ location +"\033[0m"+" and told the " +"\033[1m"+ noun1 +"\033[0m"+ " that that was not allowed. The " +"\033[1m"+ noun1+ "\033[0m"+" then felt " +"\033[1m"+ emotion +"\033[0m"+ " and told all of the people there to " +"\033[1m"+ verb2 +"\033[0m"+". The " +"\033[1m"+ noun1 +"\033[0m"+ " then wanted to leave and finally went to a " +"\033[1m"+ noun3 + "\033[0m")

#Main
madlibs()
