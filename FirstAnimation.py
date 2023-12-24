import stddraw

# draw a vertically centered triangle
stddraw.line(0.25, 0.25, 0.5, 0.75)
stddraw.line(0.5, 0.75, 0.75, 0.25)
stddraw.line(0.25, 0.25, 0.75, 0.25)

# draw a point in the middle of the triangle
x_coord = 0.5
y_coord = 0.5
velocity = .01

stddraw.point(x_coord, y_coord)
while True:
    # Clear the canvas (so that only one dot appears)
    stddraw.clear()
    stddraw.line(0.25, 0.25, 0.5, 0.75)
    stddraw.line(0.5, 0.75, 0.75, 0.25)
    stddraw.line(0.25, 0.25, 0.75, 0.25)

    stddraw.point(x_coord, y_coord)

    # creating animation such that the dot moves to and fro on y axis with in triangle
    if y_coord >= 0.75:
        velocity = -0.01
    elif y_coord <= 0.25:
        velocity = 0.01
    y_coord += velocity
    stddraw.show(10)

stddraw.show()


