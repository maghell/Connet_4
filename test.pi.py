from turtle import *
def setup (): 
    speed (1000)
    pu()
    goto (-300,150)
    pd()
    #her tinger jeg firkanten
    for i in range(2):
        fd (600)
        rt (90)
        fd (400)
        rt (90)
    speed (1000)
    #her setter jeg hvor den skal tainge fra
    for i in range (5):
        pu ()
        rt (90)
        fd (75)
        lt (90)
        fd (50)
        pd ()
    #her tinger jeg selve cirklarne
        for i in range(10):
            circle(25,360,30)
            pu ()
            fd (55)
            pd()
    #her venner jeg tilbage
        pu ()
        rt (180)
        fd (600)
        rt(180)

    column = []
    for i in range (10):
        row = []
        for i in range (5):
            row.append(0)
        column.append(row)

def coulor(column,coulor):
    fillcolor (coulor) 
    fd (75)
    circle(25,360,30)
    


setup ()    

coulor (8,"red")

