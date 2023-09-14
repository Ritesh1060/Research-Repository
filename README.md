# Research-Repository
1. `import turtle`: This line imports the Turtle graphics library.
2. `turtle.color("yellow")`: Sets the pen color to yellow. This means that the turtle will draw using a yellow color.
3. `turtle.Screen().bgcolor("black")`: Sets the background color of the drawing screen to black.
4. `turtle.width(12)`: Sets the width of the turtle's pen to 12 units.
5. `for i in range(5):`: This line starts a for loop that will run five times. It's used to draw the star.
6. `turtle.forward(150)`: The turtle moves forward by 150 units. This is the length of each line segment that makes up the star's points.
7. `turtle.right(144)`: After moving forward, the turtle turns right by 144 degrees. This specific angle is used because it evenly divides 360 degrees into five parts
    (360 degrees / 5 = 72 degrees per point).
8. `turtle.done()`: This line marks the end of the drawing. After executing this line, the turtle graphics window will remain open, displaying the drawn star.
