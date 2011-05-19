from wrapper_turtle import *

# lets move somewhere lower in the screen
penup()
# point down
right(90)
# go down
forward(100)
# point right
left(90)
# position ourselves
backward(200)
#now we are ready to draw
pendown()

# lets draw something simple, like a house
# floor
forward(100)
# right wall
left(90)
forward(100)

# roof
# up
left(30)
forward(100)
# down
left(120)
forward(100)

# left wall
left(30)
forward(100)

# let's fix that roof
backward(100)
left(90)
forward(100)
# we are done, let's admire our art
done()
