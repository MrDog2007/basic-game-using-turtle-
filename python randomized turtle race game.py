import turtle
import random

game_over = False

bob = turtle.Turtle()
mike  = turtle.Turtle()
target = turtle.Turtle()

bob.color('green')
mike.color('purple')
target.color('cyan')

bob.speed('fast')
mike.speed('fast')

print('the first one in the cyan box wins')

target.penup()
target.left(random.randint(90,180))
target.forward(random.randint(200,400))
target.right(random.randint(90,180))
target.forward(random.randint(50,150))
target.pendown()
target.setheading(90)
target.forward(50)
target.left(90)
target.forward(50)
target.left(90)
target.forward(50)
target.left(90)
target.forward(50)


mike.penup()
mike.left(90)
mike.forward(100)
mike.pendown()

randforward = random.randint(20, 50)
randright = random.randint(0, 360)
randleft = random.randint(0, 360)



while game_over == False:

    bob.forward(randforward)
    randforward = random.randint(20, 50)
    bob.right(randright)
    randright = random.randint(0, 360)
    bob.forward(randforward)
    bob.left(randleft)
    randleft = random.randint(0, 360)
    bob.forward(randforward)

    bob_y = bob.ycor()
    if bob_y >= 400:
        bob.setheading(270)
        bob.forward(100)
    if bob_y <= -400:
        bob.setheading(90)
        bob.forward(100)

    bob_x = bob.xcor()
    if bob_x >= 473:
        bob.setheading(180)
        bob.forward(100)
    if bob_x <= -400:
        bob.setheading(0)
        bob.forward(100)
    
    mike.forward(randforward)
    randforward = random.randint(20, 50)
    mike.right(randright)
    randright = random.randint(0, 360)
    mike.forward(randforward)
    mike.left(randleft)
    randleft = random.randint(0, 360)
    mike.forward(randforward)

    mike_y = mike.ycor()
    if mike_y >= 400:
        mike.setheading(270)
        mike.forward(100)
    if mike_y <= -400:
        mike.setheading(90)
        mike.forward(100)

    mike_x = mike.xcor()
    if mike_x >= 473:
        mike.setheading(180)
        mike.forward(100)
    if mike_x <= -400:
        mike.setheading(0)
        mike.forward(100)
    
    if game_over == True:
        break
else:
    game_over = True


turtle.done()
