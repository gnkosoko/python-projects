#Name:
#Date:

#Initialize
import turtle
t = turtle.Turtle()

#Functions

#Draws an admission ticket with a label and customer information inside. This function uses a turtle to draw a ticket with the name of the customer and the price paid for the ticket.
#(string: name) represents the customers name that appears inside the ticket
#(integer: price) represents the price the customer paid that appears inside the ticket
#(string: dayofweek) represents the day of the week that the ticket was purchased
#(integer: y_location) y_location represents the vertical loction of the ticket
def draw_ticket(name, price, dayofweek, y_location):
    t.goto(-50, y_location)
    t.write("Ticket", font=("Arial", 15), align="right")
    t.pendown()
    for i in range(2):
        t.forward(500)
        t.left(90)
        t.forward(250)
        t.left(90)
    t.penup()
    t.goto(50, y_location +215)
    t.write("Admit One", font=("Arial", 15), align="right")
    t.goto(440, y_location +215)
    t.write(dayofweek, font=("Arial", 15), align="right")
    t.goto(225, y_location +135)
    t.write(name, font=("Arial", 15), align="right")
    t.goto(225, y_location +15)
    t.write(price, font=("Arial", 15), align="right")

#Main
#1. Indroduce the user to your ticketr generator
print("Welcome to ticket generator!")
#2. Collect pertinent information
#Name
name = input("Enter name: ") #String (Good!)
age = int(input("Enter age: ")) #Integer (Good!)
#Day of the week
day = input("Enter day: ")
#Coupon Code
coupon = input("Enter coupon code")


#3. Algorithm for setting the price
def set_price(): #Algroithim for setting the price
    #Globaliziing variables:
    global name
    global age
    global day
    global coupon
    global price
    #setting the price
    if age <= 3:
        price = 0 #Price for babies
    elif age >=4 and age <= 17:
        if day == "friday" and coupon == "FREEFRIDAY":
            price = 0
        elif day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday":
            price = 50 #Price fro students on monday
        elif day == "saturday":
            price = 100
        elif day == "sunday" and coupon == "SUNDAY10":
            price = 90
    elif age >= 18:
        price = 100

#4. Genrate the ticket
price = 100
set_price()
draw_ticket(name, price, day, 0)
