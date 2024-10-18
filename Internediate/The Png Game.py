#The Pong  Game
# Import the necessary modules
import turtle

# Create the screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Create the left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Create the right paddle
right_paddle = turtle.Turtle() # Create the right paddle
right_paddle.speed(0) # Set the speed of the paddle
right_paddle.shape("square") # Set the shape of the paddle to a square
right_paddle.color("white") # Set the color of the paddle to white 
right_paddle.shapesize(stretch_wid=5, stretch_len=1) # Stretch the paddle to be 5 times the normal size 
#in the width and 1 time in the length
right_paddle.penup() # Prevent the paddle from drawing lines as it moves
right_paddle.goto(350, 0) # Set the initial position of the paddle
ball = turtle.Turtle() # Create the ball
ball.speed(0) # Set the speed of the ball
ball.shape("circle") # Set the shape of the ball to a circle
ball.color("white") # Set the color of the ball to white
ball.penup() # Prevent the ball from drawing lines as it moves
ball.goto(0, 0) # Set the initial position of the ball
ball.dx = 0.2 # Set the horizontal speed of the ball
ball.dy = 0.2 # Set the vertical speed of the ball
# Create the score board
score_a = 0 # Set the initial score for player A
score_b = 0 # Set the initial score for player B
score = turtle.Turtle() # Create the score object
score.speed(0) # Set the speed of the score
score.color("white") # Set the color of the score to white
score.penup() # Prevent the score from drawing lines as it moves
score.hideturtle() # Hide the score
score.goto(0, 260) # Set the initial position of the score
score.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal")) # Write the initial score
# Function to move the left paddle up
def move_left_paddle_up():
    y = left_paddle.ycor() # Get the current y-coordinate of the left paddle
    y += 20 # Increase the y-coordinate by 20
    left_paddle.sety(y) # Set the new y-coordinate of the left paddle
    # Function to move the left paddle down
def move_left_paddle_down():
    y = left_paddle.ycor() # Get the current y-coordinate of the left paddle
    y -= 20 # Decrease the y-coordinate by 20
    left_paddle.sety(y) # Set the new y-coordinate of the left paddle
    # Function to move the right paddle up
def move_right_paddle_up():
    y = right_paddle.ycor() # Get the current y-coordinate of the right paddle
    y += 20 # Increase the y-coordinate by 20
    right_paddle.sety(y) # Set the new y-coordinate of the right paddle
    # Function to move the right paddle down
def move_right_paddle_down():
    y = right_paddle.ycor() # Get the current y-coordinate of the right paddle
    y -= 20 # Decrease the y-coordinate by 20
    right_paddle.sety(y) # Set the new y-coordinate of the right paddle
    # Bind the functions to the keyboard
screen.listen()
screen.onkeypress(move_left_paddle_up, "w") # Bind the "w" key to move the left paddle up
screen.onkeypress(move_left_paddle_down, "s") # Bind the "s" key to move the left paddle down
screen.onkeypress(move_right_paddle_up, "Up") # Bind the "Up" arrow key to move the right paddle up
screen.onkeypress(move_right_paddle_down, "Down") # Bind the "Down" arrow key to move the right paddle down
while True:
    screen.update() # Update the screen
    ball.setx(ball.xcor() + ball.dx) # Move the ball horizontally
    ball.sety(ball.ycor() + ball.dy) # Move the ball vertically
    # Check for collisions with the top and bottom walls
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    # Check for collisions with the left and right walls
    if ball.xcor() > 390:
        ball.goto(0, 0)
        score_a += 1
        score.clear()
        score.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        score_b += 1
        score.clear()
        score.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    # Check for collisions with the paddles
    if ball.xcor() < -340 and ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50:
        ball.dx *= -1
    elif ball.xcor() > 340 and ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50:
        ball.dx *= -1
        # Move the paddles
left_paddle.sety(left_paddle.ycor() + 20)
right_paddle.sety(right_paddle.ycor() + 20)
left_paddle.sety(left_paddle.ycor() - 20)
right_paddle.sety(right_paddle.ycor() - 20)
turtle.done()
