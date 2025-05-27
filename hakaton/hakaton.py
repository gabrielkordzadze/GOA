from turtle import*
#ფონის დაყენება
bgcolor("lightgreen")

# ფუნჯის სიჩქარე
speed(0)

# ტანის დახატვა
penup()
goto(-50, -100)
pendown()
fillcolor("lightgray")
begin_fill()
for _ in range(2):
    forward(100)
    left(90)
    forward(200)
    left(90)
end_fill()

# თავის დახატვა
penup()
goto(0, 120)
pendown()
fillcolor("tan")
begin_fill()
circle(60)
end_fill()

# მარცხენა ყურის დახატვა
penup()
goto(-30, 230)
pendown()
fillcolor("tan")
begin_fill()
circle(20)
end_fill()

# მარჯვენა ყურის დახატვა
penup()
goto(30, 230)
pendown()
fillcolor("tan")
begin_fill()
circle(20)
end_fill()

# თვალების დახატვა
penup()
goto(-20, 180)
pendown()
fillcolor("black")
begin_fill()
circle(10)
end_fill()

penup()
goto(20, 180)
pendown()
fillcolor("black")
begin_fill()
circle(10)
end_fill()

# ცხვირის დახატვა
penup()
goto(-60, 150)
pendown()
fillcolor("black")
begin_fill()
circle(20)
end_fill()



# შარვლის დახატვა
penup()
goto(-50, -100)
pendown()
fillcolor("lightblue")
begin_fill()
for _ in range(2):
    forward(100)
    left(90)
    forward(80)
    left(90)
end_fill()

# ფეხსაცმლის დახატვა
penup()
goto(-50, -180)
pendown()
fillcolor("red")
begin_fill()
for _ in range(2):
    forward(50)
    left(90)
    forward(30)
    left(90)
end_fill()

penup()
goto(0, -180)
pendown()
fillcolor("red")
begin_fill()
for _ in range(2):
    forward(50)
    left(90)
    forward(30)
    left(90)
end_fill()

# პროგრამის დასრულება
exitonclick()


