import turtle

def draw_circle(turtle, color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_rectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.goto(x - width / 2, y - height / 2)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_triangle(turtle, color, x, y, size):
    turtle.penup()
    turtle.goto(x - size / 2, y + size / 4)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(x + size / 2, y + size / 4)
    turtle.goto(x, y - size / 2)
    turtle.goto(x - size / 2, y + size / 4)
    turtle.end_fill()

def draw_face_outline(turtle, x, y, radius, color):
  turtle.penup()
  turtle.goto(x, y-radius)
  turtle.pendown()
  turtle.color(color)
  turtle.circle(radius)


def draw_smiley_face():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("white")

    artist = turtle.Turtle()
    artist.speed(0)
    artist.hideturtle()

    center_x = 0
    center_y = 0
    face_radius = 200

    draw_face_outline(artist, center_x, center_y, face_radius, "green")

    eye_radius = 40
    eye_offset_x = 80
    eye_y = 80

    draw_circle(artist, "red", center_x - eye_offset_x, eye_y, eye_radius)

    draw_circle(artist, "blue", center_x + eye_offset_x, eye_y, eye_radius)

    mouth_width = 150
    mouth_height = 30
    mouth_y = -20
    draw_rectangle(artist, "yellow", center_x, mouth_y, mouth_width, mouth_height)

    nose_size = 60
    nose_y = -90

    draw_triangle(artist, "black", center_x, nose_y, nose_size)

    turtle.done()

draw_smiley_face()