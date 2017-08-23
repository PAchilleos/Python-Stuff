import turtle
turtle.speed(2)
turtle.hideturtle()

I=str(input('what shape to you want to draw?: Options: Circle Square Triangle '))

if I == "Circle" :
        x=input('What radius circle would you like?: ')
        x=int(x);
        turtle.circle(x)
                
elif I == "Square" :
        x=input('How big do you want the sides of the square?: ');
        x=int(x);
        turtle.fd(x);
        turtle.rt(90);
        turtle.fd(x);
        turtle.rt(90);
        turtle.fd(x);
        turtle.rt(90);
        turtle.fd(x);
        turtle.rt(90);

elif I == "Triangle" :
        x=input('How big do you want the sides of the triangle?: ');
        x=int(x);

        turtle.fd(x);
        turtle.rt(120);
        turtle.fd(x);
        turtle.rt(120);
        turtle.fd(x);
