###############################################
# Name: Vamshider Reddy,Dasari
# Class: CMPS 5363 Cryptography
# Date: 04 August 2015
# Program 3 - Elliptical Curve.
###############################################
##including header files
import argparse
import sys
import elliptical as sl
import math
from fractions import Fraction
import graph as g

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", dest="a", help="Part 'a' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-b", dest="b", help="Part 'b' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-x1",dest="x1", help="X-Coordinate of the first point")
    parser.add_argument("-y1",dest="y1", help="Y-Coordinate of the first point")
    parser.add_argument("-x2",dest="x2", help="X-Coordinate of the second point")
    parser.add_argument("-y2",dest="y2", help="y-Coordinate of the second point")
    args = parser.parse_args()
    # Assingning the input values to the local variables
    a = Fraction(args.a)
    b = Fraction(args.b)
    x1 = Fraction(args.x1)
    y1 =Fraction(args.y1)
    x2 = Fraction(args.x2)
    y2 = Fraction(args.y2)
    x3 = int()
    y3 = int()
    slope = int()
    print("a=",args.a," b=",args.b,"x1=",args.x1," y1=",args.y1," x2=",args.x2," y2=",args.y2)
    #passing the values to the function
    x3,y3=sl.checkPoint(a,b,x1,y1,x2,y2,slope)
    m= sl.findSlope(x1,y1,x2,y2,a)
    #ploting the points in the graph.
    g.createGraph(a,b,x1,y1,x2,y2,x3,y3,m)
    print("x3 = ",x3,"y3 = ",y3)
   

if __name__ == '__main__':
    main()
