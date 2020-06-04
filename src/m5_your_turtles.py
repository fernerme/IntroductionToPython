"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Melina Ferner.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()

leftie = rg.SimpleTurtle()
leftie.pen = rg.Pen('red', 2)
leftie.speed = 10
rightie = rg.SimpleTurtle()
rightie.pen = rg.Pen('blue', 2)
rightie.speed =10

rightie.pen_up()
rightie.forward(150)
rightie.left(90)
rightie.pen_down()

leftie.pen_up()
leftie.left(180)
leftie.forward(150)
leftie.right(90)
leftie.pen_down()
r1 = 1
r2 = 2

for k in range(20):
    leftie.draw_circle(r1)
    leftie.pen_up()
    leftie.right(90)
    leftie.forward(20)
    leftie.left(90)
    leftie.pen_down()
    rightie.draw_circle(r2)
    rightie.pen_up()
    rightie.right(90)
    rightie.forward(30)
    rightie.left(90)
    rightie.pen_down()
    r1 = r1+20
    r2 = r2+30



window.close_on_mouse_click()