import turtle
import random

# Function to generate a random color
def random_color():
    colors = ["red", "green", "blue", "orange", "purple", "pink", "cyan", "magenta", "yellow"]
    return random.choice(colors)

# Create a Turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a Turtle object
t = turtle.Turtle()
t.speed(0)  # Set the turtle speed to maximum
t.width(1)  # Decrease the width of the stars

# Get screen dimensions
screen_width = screen.window_width()
screen_height = screen.window_height()

# Loop to draw lots of stars across the entire screen
for _ in range(500):  # Adjust the number of stars as needed
    t.penup()
    x = random.randint(-screen_width // 2, screen_width // 2)
    y = random.randint(-screen_height // 2, screen_height // 2)
    t.goto(x, y)
    t.pendown()
    t.color(random_color())
    
    for _ in range(5):
        t.forward(10)  # Adjust the star size as needed
        t.right(144)

# Close the Turtle graphics window on click
screen
