import turtle


def Line(dot1=(0, 0), dot2=(0, 0)):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(dot1)
    t.pensize(SIZE)
    t.pendown()
    t.goto(dot2)
    t.penup()


def Cir(dot=(0, 0), radius=5, Flag=1, heading=0):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(dot)
    t.pendown()
    t.pensize(SIZE)
    t.setheading(heading)
    t.circle(radius, 180 * Flag)
    t.penup()
def Cir1(dot=(0, 0), radius=5, Flag=1, heading=0):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(dot)
    t.pendown()
    t.pensize(SIZE)
    t.setheading(heading)
    t.circle(radius, 270 * Flag)
    t.penup()

TIMES, RADIUS, SIZE = 20, 10, 2
LINES = [[(0, 0), (6, 0)],
         [(0, 1), (6, 1)],
         [(0, 2), (6, 2)],
         [(0, 3), (6, 3)],
         [(0, 4), (6, 4)],
         [(0, 5), (6, 5)],
         [(0, 6), (6, 6)],
         # [(0, 0), (0, 6)],
         # [(1, 0), (1, 6)],
         # [(2, 0), (2, 6)],
         # [(3, 0), (3, 6)],
         # [(4, 0), (4, 6)],
         # [(5, 0), (5, 6)],
         # [(6, 0), (6, 6)],
         [(6, 0), (6, 6)],
         [(5, 0), (5, 6)],
         [(4, 0), (4, 6)],
         [(3, 0), (3, 6)],
         [(2, 0), (2, 6)],
         [(1, 0), (1, 6)],
[(0, 0), (0, 6)],
         ]

for i, dot in enumerate(LINES):
    dot1, dot2 = list(map(lambda x: x * TIMES, dot[0])), list(map(lambda x: x * TIMES, dot[1]))
    # print(dot1)
    # print(dot2)
    # Line(dot1, dot2)
    if i < 7:
        if i==6:
            Line(dot1,(dot2[0]+10,dot2[1]) )
            Cir1((dot2[0]+10, dot2[1]), RADIUS, 1)
        elif i == 5:
            Line(dot2,dot1 )
            Cir((dot1[0], dot1[1]), RADIUS, -1)
        elif i == 0:
            Line((dot1[0]-10,dot1[0]),dot2)
            Cir((dot2[0], dot2[1]), RADIUS, 1)
        elif i % 2 == 0:
            Line(dot1, dot2)
            Cir((dot2[0], dot2[1]), RADIUS, 1)
        else:
            Line(dot2,dot1 )
            Cir((dot1[0], dot1[1]), RADIUS, -1)
    else:
        if i % 2 != 1:

                Line(dot1,dot2 )
                Cir((dot2[0], dot2[1]), RADIUS, 1, -270)
        elif i == 7:
            Line((dot2[0], dot2[1] + 10), dot1)
            Cir((dot1[0], dot1[1]), RADIUS, -1, 90)
        elif i == len(LINES) - 1:
            Line(dot2,(dot1[0],dot1[1]-10))
        else:
            Line(dot2,dot1 )
            Cir((dot1[0], dot1[1]), RADIUS, -1, 90)

turtle.mainloop()