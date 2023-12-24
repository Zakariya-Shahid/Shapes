import stddraw


#first box
stddraw.line(0.5, 1, 1, 1)
stddraw.line(0.5, 0.5, 1, 0.5)
stddraw.line(0.5, 0.5, 0.5, 1)
stddraw.line(1, 0.5, 1, 1)
x1 = 0.25
y1 = 0.25
stddraw.point(x1,y1)

velocity1 = 0.01

#second box
stddraw.line(0, 0, 0, 0.5)
stddraw.line(0, 0.5, 0.5, 0.5)
stddraw.line(0.5, 0, 0.5, 0.5)
stddraw.line(0, 0, 0.5, 0)

x2 = 0.75
y2 = 0.75
stddraw.point(x2,y2)

velocity2 = 0.01

# moving the points one vertical direction and then other in horizontol direction
while True:
    stddraw.clear()
    stddraw.line(0.5, 1, 1, 1)
    stddraw.line(0.5, 0.5, 1, 0.5)
    stddraw.line(0.5, 0.5, 0.5, 1)
    stddraw.line(1, 0.5, 1, 1)
    stddraw.point(x1,y1)

    stddraw.line(0, 0, 0, 0.5)
    stddraw.line(0, 0.5, 0.5, 0.5)
    stddraw.line(0.5, 0, 0.5, 0.5)
    stddraw.line(0, 0, 0.5, 0)
    stddraw.point(x2,y2)

    if y1 >= 0.5:
        velocity1 = -0.01
    elif y1 <= 0:
        velocity1 = 0.01
    y1 += velocity1

    if x2 >= 1:
        velocity2 = -0.01
    elif x2 <= 0.5:
        velocity2 = 0.01
    x2 += velocity2

    stddraw.show(10)


