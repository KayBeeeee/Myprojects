#The Turtle Crossing Game
import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Crossing")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the player
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.goto(0, -250)
player.setheading(90)

# Create the cars
cars = []
colors = ["red", "yellow", "blue", "green", "purple"]
for i in range(5):
    car = turtle.Turtle()
    car.shape("square")
    car.color(random.choice(colors))
    car.penup()
    car.goto(random.randint(-300, 300), random.randint(-250, 250))
    cars.append(car)

# Move the player
def move_up():
    y = player.ycor()
    y += 10
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= 10
    player.sety(y)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")

# Game loop
game_is_on = True
while game_is_on:
    screen.update()

    # Move the cars
    for car in cars:
        car.setx(car.xcor() - 10)
        if car.xcor() < -300:
            car.goto(random.randint(300, 600), random.randint(-250, 250))

    # Check for collisions
    for car in cars:
        if player.distance(car) < 20:
            game_is_on = False
            print("Game Over!")

    time.sleep(0.1)

screen.exitonclick()