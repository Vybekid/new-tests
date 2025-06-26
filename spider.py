import turtle

# --- Configuration ---
SPIDER_COLOR = "black"
HOURGLASS_COLOR = "#b71c1c"  # A dark, blood-red color
WEB_COLOR = "gray"
BACKGROUND_COLOR = "white"
DRAW_SPEED = 0  # 0 is the fastest, 10 is fast, 1 is slowest

# --- Helper and Drawing Functions ---

def draw_web_thread(t):
    """Draws the single thread the spider is hanging from."""
    t.hideturtle()
    t.pencolor(WEB_COLOR)
    t.pensize(2)
    t.penup()
    # Go to the top of the screen, slightly off-center from the spider's body
    t.goto(0, 300)
    t.pendown()
    # Draw down to the spinneret area of the abdomen
    t.goto(0, -100)
    t.penup()

def draw_body(t):
    """Draws the spider's two-part body."""
    t.color(SPIDER_COLOR)
    
    # Abdomen (the large, back part)
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.begin_fill()
    t.circle(80)
    t.end_fill()
    
    # Cephalothorax (the smaller, front part)
    t.penup()
    t.goto(0, 20)
    t.pendown()
    t.begin_fill()
    t.circle(45)
    t.end_fill()

def draw_hourglass(t):
    """Draws the red hourglass symbol on the abdomen."""
    t.penup()
    # Position in the center of the abdomen
    t.goto(0, -25)
    t.color(HOURGLASS_COLOR)
    t.begin_fill()
    
    # Draw two triangles pointing at each other
    # Top triangle
    t.goto(15, -15)
    t.goto(-15, -15)
    t.goto(0, -40)
    
    # Bottom triangle
    t.goto(15, -65)
    t.goto(-15, -65)
    t.goto(0, -40)
    
    t.end_fill()

def draw_curved_tapered_leg(t, start_pos, angle, length, segments, start_width, end_width, curve_direction):
    """
    Draws a single leg that is curved and tapers from thick to thin.
    - curve_direction: 1 for curving left, -1 for curving right.
    """
    t.penup()
    t.goto(start_pos)
    t.setheading(angle)
    t.pencolor(SPIDER_COLOR)

    # Calculate how much the pen size and angle should change per segment
    width_decrement = (start_width - end_width) / segments
    segment_length = length / segments
    turn_angle = 70 / segments  # Total curve of 70 degrees spread over segments

    for i in range(segments):
        current_width = start_width - (i * width_decrement)
        # Ensure width doesn't go below 1
        t.pensize(max(1, current_width))
        t.pendown()
        t.forward(segment_length)
        # Turn slightly to create the curve
        if curve_direction == 1:
            t.left(turn_angle)
        else:
            t.right(turn_angle)
    t.penup()

def draw_all_legs(t):
    """Defines and draws all eight legs."""
    # Define properties for each of the 8 legs
    # [angle, length, curve_direction (1=left, -1=right)]
    leg_properties = [
        # Right side legs (curve "outward" which is to the right)
        [30, 180, -1],
        [60, 190, -1],
        [110, 160, 1], # Top back leg curves "inward"
        [140, 150, 1], # Bottom back leg curves "inward"
        # Left side legs (mirror images)
        [330, 180, 1],
        [300, 190, 1],
        [250, 160, -1], # Top back leg curves "inward"
        [220, 150, -1], # Bottom back leg curves "inward"
    ]
    
    for props in leg_properties:
        angle, length, curve_dir = props
        draw_curved_tapered_leg(
            t=t,
            start_pos=(0, 60), # All legs start from the cephalothorax
            angle=angle,
            length=length,
            segments=20,      # More segments = smoother curve
            start_width=12,   # Thickest part of the leg
            end_width=1,      # Thinnest part of the leg
            curve_direction=curve_dir
        )

# --- Main Program Execution ---

if __name__ == "__main__":
    # 1. Setup the screen and turtle
    screen = turtle.Screen()
    screen.title("Black Widow Spider")
    screen.bgcolor(BACKGROUND_COLOR)
    # Use a bigger window size for this larger drawing
    screen.setup(width=600, height=800)
    
    spider_turtle = turtle.Turtle()
    spider_turtle.speed(DRAW_SPEED)

    # 2. Draw the parts in the correct order (from back to front)
    print("Drawing web thread...")
    draw_web_thread(spider_turtle)
    
    print("Drawing body...")
    draw_body(spider_turtle)

    print("Drawing hourglass marking...")
    draw_hourglass(spider_turtle)
    
    print("Drawing legs...")
    draw_all_legs(spider_turtle)
    
    # 3. Finish up
    spider_turtle.hideturtle()
    print("Done! Click the window to close.")
    screen.exitonclick()