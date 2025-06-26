import turtle

# --- Configuration ---
SPIDER_COLOR = "black"
EYE_COLOR = "red"
BACKGROUND_COLOR = "lightgray"
PEN_SIZE = 5
DRAW_SPEED = 0  # 0 is the fastest, 10 is fast, 1 is slowest

# --- Main Drawing Functions ---

def draw_body(spider_turtle):
    """Draws the spider's two-part body (abdomen and cephalothorax)."""
    print("Drawing body...")
    spider_turtle.penup()
    
    # Abdomen (the larger, back part)
    spider_turtle.goto(0, -60)
    spider_turtle.pendown()
    spider_turtle.begin_fill()
    spider_turtle.circle(60)
    spider_turtle.end_fill()
    
    # Cephalothorax (the smaller, front part where legs attach)
    spider_turtle.penup()
    spider_turtle.goto(0, 0)
    spider_turtle.pendown()
    spider_turtle.begin_fill()
    spider_turtle.circle(40)
    spider_turtle.end_fill()
    
    spider_turtle.penup()

def draw_legs(spider_turtle):
    """Draws the spider's eight legs, attached to the cephalothorax."""
    print("Drawing legs...")
    # These are the angles for each of the 8 legs, starting from the right side
    leg_angles = [15, 45, 135, 165, 195, 225, 315, 345]
    leg_length1 = 120  # Length of the first segment of the leg
    leg_length2 = 90   # Length of the second segment
    joint_angle = 45   # How much the leg bends at the joint
    
    for angle in leg_angles:
        # Go to the center of the cephalothorax to start each leg
        spider_turtle.goto(0, 40)
        spider_turtle.setheading(angle)
        
        # Draw the leg
        spider_turtle.pendown()
        spider_turtle.forward(leg_length1)
        
        # Create the joint bend
        # Legs on the right side bend right, legs on the left bend left
        if angle < 180:
            spider_turtle.right(joint_angle)
        else:
            spider_turtle.left(joint_angle)
            
        spider_turtle.forward(leg_length2)
        spider_turtle.penup()

def draw_eyes(spider_turtle):
    """Draws the spider's eyes on its head."""
    print("Drawing eyes...")
    eye_size = 8
    # Positions for the 8 eyes in two rows
    eye_positions = [
        (-20, 65), (-10, 70), (10, 70), (20, 65),
        (-18, 55), (-8, 58), (8, 58), (18, 55)
    ]
    
    for pos in eye_positions:
        spider_turtle.goto(pos)
        # The dot() command is perfect for small filled circles
        spider_turtle.dot(eye_size, EYE_COLOR)

# --- Main Program Execution ---

if __name__ == "__main__":
    # 1. Setup the screen and turtle
    screen = turtle.Screen()
    screen.title("Spider Drawer")
    screen.bgcolor(BACKGROUND_COLOR)
    
    # Create our spider turtle
    spider = turtle.Turtle()
    spider.shape("turtle")
    spider.color(SPIDER_COLOR)
    spider.pensize(PEN_SIZE)
    spider.speed(DRAW_SPEED)

    # 2. Draw the parts of the spider
    draw_body(spider)
    draw_legs(spider)
    draw_eyes(spider)
    
    # 3. Finish up
    spider.hideturtle()  # Hide the turtle arrow when drawing is done
    print("Done! Click the window to close.")
    screen.exitonclick()  # Wait for a click on the screen to close the window