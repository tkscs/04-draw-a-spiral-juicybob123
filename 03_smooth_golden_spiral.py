import turtle
from scipy.constants import golden as phi

"""
If the spiral has so far turned degrees_turned_so_far degrees, then the current
arm length will be:

initial_arm_length * (phi**(degrees_turned_so_far / 90))

The aloe polyphylla plant grows in a pattern with five golden spirals
eminating from the same center. Make a function that draws a single golden
spiral, and use that to draw a shape like the aloe polyphylla.

You may find these functions useful:

turtle.up()

turtle.down()

turtle.setposition(x, y)

turtle.setheading(degrees)

The turtle starts at position(0, 0) with heading 0 degrees.
"""
y = 1

x =   3
turtle.speed(100-0)
### YOUR CODE STARTS HERE
for loop in range(1000):
    turtle.forward(x)
    turtle.right(3 *(phi**(y / 90)))
    if y == 1000000000:
            x = x * phi
    # for loop in range(90):
    #     turtle.forward(0.01)
    #     turtle.right(1)

    y = y - 1


### YOUR CODE ENDS HERE

turtle.exitonclick()