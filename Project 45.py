turtle.colormode(255)
radius = 140
for i in range(6):
    habib.fillcolor(random.randint(1,255 ), random.randint(1,255 ), random.randint(1,255 ))
    habib.begin_fill()
    habib.circle(radius)
    habib.end_fill()
    radius -= 20
