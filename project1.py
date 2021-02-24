
import turtle #importing the turtle library to use its attributes to make this project

my_turtle = turtle.Turtle() # a variable that contains the turtle function
my_turtle.speed(0)  #fastens the building process
my_turtle.shape("turtle") #gives the pointer the shape of anything you choose, in this case, a turtle
turtle.bgcolor("black") #gives a background color to the output window


def square(length, angle):
    colors = ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]

    for i in range(4): # for loop loop used to give our output a color
            for j in colors: 
                my_turtle.color(j)
                my_turtle.forward(length)
                my_turtle.right(angle)
                my_turtle.right(11)
            


for i in range (100): #for loop wherein function is called and output is drawn
    square(100,90)
    
