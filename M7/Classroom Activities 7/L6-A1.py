import turtle
turtle.Screen().bgcolor("red")
sc = turtle.Screen()
sc.setup(600, 600)
turtle.title("You are allowed to enter here!")
board = turtle.Turtle()
n = 9
for i in range(n):
    board.forward(100)
    board.left(360/n)