import turtle
from scipy.constants import golden as phi

"""
In a golden spiral, for every 90 degrees, the arm length of the spiral grows
by a factor of phi (which is approximately 1.618)

So if the spiral has so far turned 90 degrees i times, then the current arm
length will be:

initial_arm_length * (phi**i)
"""
turtle.speed(19999)
x = 0.1
### YOUR CODE STARTS HERE
for loop in range (1000):
    turtle.forward(x)
    turtle.right(90)
    x = x * phi


### YOUR CODE ENDS HERE

turtle.exitonclick()