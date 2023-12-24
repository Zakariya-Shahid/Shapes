import stddraw


#first box
stddraw.line(0.5, 1, 1, 1)
stddraw.line(0.5, 0.5, 1, 0.5)
stddraw.line(0.5, 0.5, 0.5, 1)
stddraw.line(1, 0.5, 1, 1)
stddraw.point(.25,.25)

#second box
stddraw.line(0, 0, 0, 0.5)
stddraw.line(0, 0.5, 0.5, 0.5)
stddraw.line(0.5, 0, 0.5, 0.5)
stddraw.line(0, 0, 0.5, 0)
stddraw.point(.75,.75)
stddraw.show()
