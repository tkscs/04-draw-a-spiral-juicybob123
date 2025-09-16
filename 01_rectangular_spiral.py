import turtle

"""
Make a rectangular spiral (see the README.md for an example)
"""


### YOUR CODE STARTS HERE
x = 1
for loop in range(20):
    turtle.forward(180 / x)
    turtle.right(90)
    turtle.forward(180 / x)
    turtle.right(90)


    x = x + 0.3


### YOUR CODE ENDS HERE

turtle.exitonclick()