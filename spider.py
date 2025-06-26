import turtle

# --- Setup ---
screen = turtle.Screen()
screen.bgcolor("deepskyblue")
t = turtle.Turtle()
t.speed(3)         # Slower speed (1-10, 3 is 'slow')
t.hideturtle()

# 1. Draw the web thread the spider is hanging from
t.pencolor("white")
t.pensize(3)
t.penup()
t.goto(0, 300)
t.pendown()
t.goto(0, 50)

# 2. Draw a cleaner body
t.pensize(1)
t.color("black")
t.penup()
t.goto(0, 0)
t.begin_fill()
t.circle(70)        # Large abdomen
t.end_fill()
t.goto(0, 80)
t.begin_fill()
t.circle(45)        # Smaller, overlapping head
t.end_fill()

# 3. Draw funnier, googly eyes
t.penup()
t.color("white")
t.goto(-20, 135)
t.dot(40)
t.goto(20, 135)
t.dot(40)
t.color("black")
t.goto(-15, 145)
t.dot(15)
t.goto(25, 145)
t.dot(15)

# 4. --- FIXED: Draw organized, jointed legs ---
t.pensize(10)
# Symmetrical angles for 4 pairs of legs
leg_angles = [30, 60, 120, 150, 210, 240, 300, 330]
for angle in leg_angles:
    t.penup()
    t.goto(0, 70)  # Start all legs from the "neck" area
    t.setheading(angle)
    t.pendown()
    
    # Draw the two segments of the leg
    t.forward(60)
    # Bend the knee based on which side the leg is on
    if angle < 180:
        t.right(45)
    else:
        t.left(45)
    t.forward(50)

# --- Finish ---
screen.exitonclick()