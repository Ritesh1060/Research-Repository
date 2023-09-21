#  stars on full screen
1 - The code starts by importing the turtle and random libraries, which are used for drawing graphics and generating random colors and positions for the stars, respectively.
2 - The random_color function selects a random color from a predefined list of colors.
3 - A Turtle screen is created with a black background using turtle.Screen(), and a Turtle object t is created for drawing.
4 - The speed of the turtle is set to the maximum speed (0) using t.speed(0) to make the drawing faster.
5 - The width of the lines drawn by the turtle is reduced to 1 using t.width(1) to create thinner stars.
6 - The screen dimensions (screen_width and screen_height) are obtained to ensure that stars are drawn within the visible screen area.
7 - A loop (for _ in range(500)) is used to draw 500 stars. You can adjust this number to change the density of stars.
8 - Inside the loop, the turtle's pen is lifted (t.penup()) to move to a new position without drawing. Random x and y coordinates within screen bounds are generated, and the turtle is moved to that position (t.goto(x, y)).
9 - The pen is lowered (t.pendown()) to start drawing, and a random color is assigned to the star using t.color(random_color()).
10 - Another loop is used to draw each star as a five-pointed star. The turtle moves forward by 10 units to draw a leg of the star (t.forward(10)) and then turns right by 144 degrees (t.right(144)) to create the next leg. This is repeated five times to complete the star.
11- Finally, the code keeps the Turtle graphics window open until you click inside it to close it.
references - https://www.tutorialspoint.com/turtle-programming-in-python
reference - https://www.youtube.com/watch?v=GoAl_Vh9U38
