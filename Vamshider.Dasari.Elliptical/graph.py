import numpy as np
import matplotlib.pyplot as plt

def createGraph(a,b,x1,y1,x2,y2,x3,y3,m):
    allPoints=[x1,x2,x3,y1,y2,y3]
    z = max(allPoints)
    #Determines width and height of plot.
    w = z+5
    h = z+5

    # Annotate the plot with your name using width (w) and height (h) as your reference points.
    an1 = plt.annotate("Vamshider Reddy Dasari", xy=(-w+2 , h-2), xycoords="data",
                  va="center", ha="center",
                  bbox=dict(boxstyle="round", fc="w"))

    # This creates a mesh grid with values determined by width and height (w,h)
    # of the plot with increments of .0001 (1000j = .0001 or 5j = .05)
    y, x = np.ogrid[-h:h:1000j, -w:w:1000j]

    # Plot the curve (using matplotlib's countour function)
    # This drawing function applies a "function" described in the
    # 3rd parameter:  pow(y, 2) - ( pow(x, 3) - x + 1 ) to all the
    # values in x and y.
    # The .ravel method turns the x and y grids into single dimensional arrays
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - ( pow(x, 3) + a*x + b ), [0])



    # Plot the points ('ro' = red, 'bo' = blue, 'yo'=yellow and so on)
    plt.plot(x1, y1,'ro')

    # Annotate point 1
    plt.annotate('x1,y1', xy=(x1, y1), xytext=(x1+1,y1+1),
            arrowprops=dict(arrowstyle="->",
            connectionstyle="arc3"),
            )

    plt.plot(x2, y2,'ro')

    # Annotate point 2
    plt.annotate('x2,y2', xy=(x2, y2), xytext=(x2+1,y2+1),
            arrowprops=dict(arrowstyle="->",
            connectionstyle="arc3"),
            )

    # Use a contour plot to draw the line (in pink) connecting our point.
    plt.contour(x.ravel(), y.ravel(), (y-y1)-m*(x-x1), [0],colors=('pink'))

    # I hard coded the third point, YOU will use good ol mathematics to find
    # the third point
    plt.plot(x3,y3,'yo')

    # Annotate point 3
    plt.annotate('x3,y3', xy=(x3,y3), xytext=(x3+1,y3+1),
            arrowprops=dict(arrowstyle="->",
            connectionstyle="arc3"),
            )

    # Show a grid background on our plot
    plt.grid()

    # Show the plot
    plt.show()
