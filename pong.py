'''import turtle  #turtle used for basic graphics especially games

wn = turtle.Screen()
wn.title("pingpong by @alexaustin007")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0) #it speeds up the game quite a bit

#score
score_a = 0
score_b = 0

# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0) #This is the speed of animation and not the speed that the paddle moves
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()  #penup doesnt draw lines by moving because if we dont write this turtle will draw lines when paddle moving
paddle_a.goto(-350,0) # X cordinate
paddle_a.shapesize(stretch_wid= 5,stretch_len=1) #it will stretch the shape because bydefault its 20px by 20px

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0) #Right side of screen
paddle_b.shapesize(stretch_wid = 5,stretch_len = 1)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0) # middle of screen 
ball.dx = 0.5 # x movement of the ball
ball.dy = 0.5 # y movement of the ball

#Pen

pen = turtle.Turtle() #for naming scoreboard and counting small 't' for module name capital T for class name
pen.penup()
pen.color('white')
pen.goto(0,260)
pen.hideturtle()
pen.speed(0) #animation speed not the movement speed
pen.write("Rohan :0 Austin: 0", align = 'center' , font = ("Courier", 24,"normal"))

#Functions

def paddle_a_up():
    y = paddle_a.ycor() #ycor is a turtle module which returns the y cor
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)



#keyboard binding

wn.listen() #this tells  to listen to keyboard inputs
wn.onkeypress(paddle_a_up,"w") #when pressed w in keyboard it will call the function
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")







# main game loop

while True:
    wn.update()

    #Ball moving
    ball.setx(ball.xcor() + ball.dx) #The ball moves with the delta speed as set
    ball.sety(ball.ycor() + ball.dy) #The ball moves with the delta speed as set

    #border checking

    if ball.ycor() > 290:
        ball.sety(290) #if its greater than 290 it will set the ball at 290
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        pen.clear()
        score_a += 1 #if ball touches the right side player 'a' get points
        pen.write("rohan:{} austin:{}".format(score_a,score_b), align = 'center' , font = ("Courier", 24,"normal")) # format is used to store score values in specific player name
        
        
    
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        score_b += 1 #if ball touches the left side player 'b' get points
        pen.clear()
        pen.write("rohan:{} austin:{}".format(score_a,score_b), align = 'center' , font = ("Courier", 24,"normal"))
       


    #paddle and ball collision

    if (ball.xcor() > 340  and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+ 40 and ball.ycor() > paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340  and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+ 40 and ball.ycor() > paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1'''


'''string = input("Enter the string: ")
liststring = list(string)
len_liststring = list(liststring)

for i in range(len_liststring-1):
    for j in range(len_liststring-i-1):
        if liststring[j] > liststring[j+1]:
            liststring[j],liststring[j+1] = liststring[j+1],liststring[j]

for m in liststring:
    new_string += m
print(new_string)'''

'''number = [212,-3837,20,23,5,33,67,3,5,5244,-83]
for i in range(len(number)):
    for j in range(i+1,len(number)):
        if number[i] > number[j]:
            number[i],number[j] = number[j],number[i]
print(number)'''

'''def quick_sort(sequence):
    if len(sequence) <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    greater = []
    lower = []

    for item in sequence:
        if item > pivot:
            greater.append(item)
        else:
            lower.append(item)
    return quick_sort(lower) + [pivot] + quick_sort(greater)

print(quick_sort([2,4,1,1,1,11,2,5335,122,3,112,-727,0,-26726]))'''

'''def binary_search(sequence,item):
    begin_index = 0
    end_index = len(sequence)-1

    while begin_index <= end_index:
        midpoint = (begin_index+end_index) // 2
        midpoint_value = sequence[midpoint]

        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint-1
        else:
            begin_index = midpoint+1
    return None

    
sequence_a = [1,2,3,4,5,7,9,16,500]
item_a = 16 
print(binary_search(sequence_a,item_a))'''









        


    