import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("🎄 Merry Christmas 🎄")

tree = turtle.Turtle()
tree.speed(0)
tree.hideturtle()

# Draw tree layers
def draw_tree():
    tree.color("green")
    tree.penup()
    tree.goto(0, -250)
    tree.pendown()

    width = 200
    height = 80

    for i in range(5):
        tree.begin_fill()
        tree.forward(width)
        tree.left(120)
        tree.forward(width)
        tree.left(120)
        tree.forward(width)
        tree.left(120)
        tree.end_fill()

        tree.penup()
        tree.goto(-(width//2), -250 + (i+1)*height)
        tree.pendown()
        width -= 30

# Draw trunk
def draw_trunk():
    tree.penup()
    tree.goto(-20, -250)
    tree.pendown()
    tree.color("brown")
    tree.begin_fill()
    for _ in range(3):
        tree.forward(40)
        tree.left(90)
        tree.forward(60)
        tree.left(90)
    tree.end_fill()

# Create blinking lights
lights = []
light_colors = ["red", "yellow", "blue", "white", "pink"]


for _ in range(30):
    light = turtle.Turtle()
    light.shape("circle")
    light.shapesize(0.5)
    light.penup()
    light.color(random.choice(light_colors))
    light.goto(random.randint(-100, 100), random.randint(-200, 100))
    lights.append(light)

# Blink lights animation
def blink_lights():
    while True:
        for light in lights:
            light.color(random.choice(light_colors))
        time.sleep(0.5)

# Draw everything
draw_tree()
draw_trunk()
blink_lights()


# # Screen setup
# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.title("🎄 Merry Christmas 🎄")
# screen.setup(800, 600)  # Set a reasonable window size
# tree = turtle.Turtle()
# tree.speed(0)
# tree.hideturtle()

# # Draw tree layers (fixed: centered, proper spacing with overlap)
# def draw_tree():
#     tree.color("green")
#     tree.penup()
#     width = 250  # Starting width for bottom layer
#     num_layers = 5
#     overlap = 30  # Pixels of overlap between layers
#     y = -300  # Starting y for bottom layer
    
#     for i in range(num_layers):
#         # Calculate triangle height
#         tri_height = (math.sqrt(3) / 2) * width
        
#         # Position at bottom center
#         tree.goto(-width // 2, y)
#         tree.setheading(0)  # Face right
#         tree.pendown()
        
#         tree.begin_fill()
#         tree.forward(width)
#         tree.left(120)
#         tree.forward(width)
#         tree.left(120)
#         tree.forward(width)
#         tree.left(120)
#         tree.end_fill()
        
#         # Update for next layer (up and smaller)
#         y += tri_height - overlap
#         width -= 35  # Taper the tree

# # Draw trunk (adjusted position)
# def draw_trunk():
#     tree.penup()
#     tree.goto(-25, -340)  # Adjusted to align with tree base
#     tree.setheading(0)
#     tree.pendown()
#     tree.color("brown")
#     tree.begin_fill()
#     for _ in range(2):
#         tree.forward(50)  # Slightly wider trunk
#         tree.left(90)
#         tree.forward(70)  # Taller trunk
#         tree.left(90)
#     tree.end_fill()

# # Create blinking lights (positions more constrained to tree area)
# lights = []
# light_colors = ["red", "yellow", "blue", "white", "pink", "orange", "gold"]
# num_lights = 100
# for _ in range(num_lights):
#     light = turtle.Turtle()
#     light.shape("circle")
#     light.shapesize(0.5)  # Smaller lights
#     light.penup()
#     # Random position within approximate tree bounds (-120 to 120 x, -300 to 50 y)
#     x = random.randint(-120, 120)
#     y = random.randint(-300, 40)
#     light.goto(x, y)
#     light.color(random.choice(light_colors))
#     lights.append(light)

# # Blink lights animation (non-blocking with ontimer)
# def blink_lights():
#     for light in lights:
#         light.color(random.choice(light_colors))
#     # Schedule next blink
#     screen.ontimer(blink_lights, 400)  # Blink every 400ms

# # Draw everything
# draw_tree()
# draw_trunk()

# # Start the animation
# blink_lights()

# # Keep window open until click
# screen.exitonclick()