import turtle as trtl
import random as rand

#variables
num_walls = 20
width = 20
color = "black"
length = width

#initiate stuff
painter = trtl.Turtle()
painter.speed(0)
painter.pencolor(color)
painter.pensize(3)
painter.hideturtle()

# Procedural Abstraction
def draw_door(pos):
  painter.forward(pos)
  painter.penup()
  painter.forward(width*2)
  painter.pendown()

def draw_bar(pos):
  painter.forward(pos)
  painter.left(90)
  painter.forward(width*2)
  painter.backward(width*2)
  painter.right(90)

#draw maze
for w in range(num_walls):
  length += width
  if (w > 4): 
    painter.left(90)
    door_loc = rand.randint(width*2, (length-width*2))
    bar_loc = rand.randint(width*2, (length-width*2))


    while (abs(door_loc-bar_loc)<width):
      door_loc = rand.randint(width*2, (length-width*2))
    if (door_loc < bar_loc):
      #draw doors
      draw_door(door_loc)
      #draw barriers
      draw_bar(bar_loc-door_loc-width*2)
      # Finish side
      painter.forward(length-bar_loc)
    else:
      #draw barriers
      draw_bar(bar_loc)
      #draw door
      draw_door(door_loc - bar_loc)
      # Finish side
      painter.forward(length - door_loc - width*2)
  else:
    painter.left(90)
    painter.forward(length)



wn = trtl.Screen()
wn.screensize()
wn.setup(width=1.0, height=1.0)
wn.mainloop()
