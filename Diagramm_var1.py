from turtle import Turtle, Screen
from itertools import cycle


lst = ['C++', 'Python', 'Python', 'C#', 'C#', 'Js']
lst2 = set(lst)
lst3 = dict()

for lst_item in lst:
    lst3[lst_item] = lst.count(lst_item)

print(lst3)
result = dict()

for x in lst3:
    result[x] = 360 / len(lst) * lst3[x]

print(result)
letter_frequencies = result.items()


COLORS = cycle(['yellow', 'black', 'red', 'pink'])

RADIUS = 150
LABEL_RADIUS = RADIUS * 1.4
FONTSIZE = 23
FONT = ("Times New Roman", FONTSIZE, "bold")


total = sum(fraction for _, fraction in letter_frequencies)

brain = Turtle()
brain.screen.bgcolor("silver")
brain.speed(6)
brain.penup()
brain.sety(-RADIUS)
brain.pendown()
brain.pensize(2)

for _, fraction in letter_frequencies:
    brain.fillcolor(next(COLORS))
    brain.begin_fill()
    brain.circle(RADIUS, fraction * 360 / total)
    position = brain.position()
    brain.goto(0, 0)
    brain.end_fill()
    brain.setposition(position)


brain.penup()
brain.sety(-LABEL_RADIUS)

for label, fraction in letter_frequencies:
    brain.circle(LABEL_RADIUS, fraction * 360 / total / 2)
    brain.write(label, align="center", font=FONT)
    brain.circle(LABEL_RADIUS, fraction * 360 / total / 2)


brain.hideturtle()

screen = Screen()
screen.exitonclick()
