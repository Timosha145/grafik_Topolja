from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np

def glasses():
    x1=np.arange(-9,-0.5,0.5)
    y1=(-1/16)*(x1+5)**2+2
    x2=np.arange(1,9.5,0.5)
    y2=(-1/16)*(x2-5)**2+2
    x3=np.arange(-9,-0.5,0.5)
    y3=1/4*(x3+5)**2-3
    x4=np.arange(1,9.5,0.5)
    y4=1/4*(x4-5)**2-3
    x5=np.arange(-9,-6.5,0.5)
    y5=-(x5+7)**2+5
    x6=np.arange(6,9.5,0.5)
    y6=-(x6-7)**2+5
    x7=np.arange(-1,1.5,0.5)
    y7=-0.5*x7**2+1.5
    fig=plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,color="black",linestyle="dashed",linewidth=2,marker='x',markersize=5)
    plt.title("glasses")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()
def umbrella():
    x1=np.arange(-12,12.5,0.5)
    y1=(-1/18)*x1**2+12
    x2=np.arange(-4,4.5,0.5)
    y2=(-1/8)*x2**2+6
    x3=np.arange(-12,-3.5,0.5)
    y3=(-1/8)*(x3+8)**2+6
    x4=np.arange(4,12.5,0.5)
    y4=(-1/8)*(x4-8)**2+6
    x5=np.arange(-4,0.3,0.5)
    y5=2*(x5+3)**2-9
    x6=np.arange(-4,1,0.5)
    y6=1.5*(x6+3)**2-10
    fig=plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,color="green",linestyle="solid",linewidth=3,marker='*',markersize=5)
    plt.title('umbrella')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
def fish():
    x1 = np.arange(0, 9.5, 0.5)
    y1=(2/27)*x1*x1-3
    x2 = np.arange(-10, 0.5, 0.5)
    y2=0.04*x2*x2-3
    x3 = np.arange(-9, -2.5, 0.5)
    y3=(2/9)*(x3+6)**2+1
    x4 = np.arange(-3, 9.5, 0.5)
    y4=(-1/12)*(x4-3)**2+6
    x5 = np.arange(5, 9, 0.5)
    y5=(1/9)*(x5-5)**2+2
    x6 = np.arange(5, 8.5, 0.5)
    y6=(1/8)*(x6-7)**2+1.5
    x7 = np.arange(-13, -8.5, 0.5)
    y7=(-0.75)*(x7+11)**2+6
    x8 = np.arange(-15, -12.5, 0.5)
    y8=(-0.5)*(x8+13)**2+3
    x9 = np.arange(-15, -10, 0.5)
    y9=[1]*len(x9)
    x10 = np.arange(3, 4, 0.5)
    y10=[3]*len(x10)
    fig = plt.figure()
    plt.plot(x1, y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,color="blue",linestyle="dashdot",linewidth=3,marker='o',markersize=5)
    plt.title('fish')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

def whichFigure():
    global var
    choice=var.get()
    if choice==1:
        glasses()
    elif choice==2:
        fish()
    elif choice==3:
        umbrella()
    else:
        umbrella()

window=Tk()
window.geometry("650x260")
window.title("BuildTheGraph")

var=IntVar()
r1=Radiobutton(text="glasses",variable=var,value=1, font="Calibri 26",command=whichFigure)
r2=Radiobutton(text="fish",variable=var,value=2, font="Calibri 26",command=whichFigure)
r3=Radiobutton(text="umbrella",variable=var,value=3, font="Calibri 26",command=whichFigure)
r1.pack()
r2.pack()
r3.pack()

window.mainloop()    