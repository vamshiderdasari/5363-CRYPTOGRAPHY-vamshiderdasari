###############################################
# Name: Vamshider Reddy,Dasari
# Class: CMPS 5363 Cryptography
# Date: 04 August 2015
# Program 3 - Elliptical Curve.
###############################################
##including header files
import string
import argparse
import random
import sys
from pprint import pprint
import math
from fractions import Fraction

##This function will check weather the points are on the curve and find the third.
#@parameters: both the points,slope, and also the co-efficents are given as parameters. 
def checkPoint(a,b,x1,y1,x2,y2,m):
    m= findSlope(x1,y1,x2,y2,a)
    print("slope =",m)
    x3=0.0
    y3=0.0
    checkp1=x1**3+a*x1+b-y1**2
    checkp2=x2**3+a*x2+b-y2**2
    if checkp1==0 and checkp2==0 :
        print("Both the points exist on the curve.")
        x3 =Fraction( m**2-x1-x2).limit_denominator(1000)
        y3 =Fraction(m*(x3-x1)+y1).limit_denominator(1000)
    else:
        print("The Points does not exist on curve")
    return (x3,y3)

##this function is used to find the slope
##@parameters : the two points are given as input and also the a value.
def findSlope(x1,y1,x2,y2,a):
    m=0.0
    if x1==x2 and y1==y2:
        print("Tthe two points are similar")
        m = float(3*x1**2+a)/float(2*y2)
    elif (x1==x2 and y1!= y2):
        print("The Slope cannot be found ")
    else:
        m=float(y2-y1)/float(x2-x1)
    return m
    
def main():
    slope= findSlope(x1,y1,x2,y2,a)
    x3,y3= checkPoint(a,b,x1,y1,x2,y2,slope)
    
    

if __name__ == '__main__':
    main()
        
