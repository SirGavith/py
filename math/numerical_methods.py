import numpy as np
import math
import matplotlib.pyplot as plt
import sympy as sp
from tabulate import tabulate


#Enter the value of y at x=2 here:
# v=2.406005

def equation1(x,y):
	return -y+2*x


def euler(f,initialy,initialx,stepsize,endpoint):
	counter = 1
	yi=[initialy]
	xi=[initialx]
	x,y = initialx,initialy
	while x < endpoint - stepsize / 2:
		#print (x,y)
		counter += 1
		y = y+stepsize*f(x,y)
		x = x+stepsize
		yi.append(y)
		xi.append(x)
	e = None #y-v
	return (stepsize,x,y,e,xi,yi)
# Improved Euler's Method and table sumarizing results

def printEval(method):
	table=[]
	output = []
	steps = [10.0, 20.0, 40.0, 80.0, 160.0, 320.0]
	#steps = [10.0, 20.0, 40.0]
	ei = 1
	for i in range(len(steps)):
		(stepsize,x,y,e,valx,valy) = method(equation1,1.0,0.0,2.0 / steps[i],2.0)
		r=e/ei
		ei=e
		output.append([i+1,steps[i],stepsize,x,y,e,r])
	print(output)

	table.append(['i', 'n(i)', 'dx(i)', 'x(i)', 'y_i(2)', 'e(i)', 'r(i)'])
	for i in range(len(output)):
		table.append(output[i])
	print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

def eulerimproved(f,initialy,initialx,dx,endpoint):
  yi=[]
  xi=[]
  x,y = initialx,initialy

  while x < endpoint - dx / 2:
    #estimate new y by Euler's method
    estNewY = y+dx * f(x,y)
    #re-estimate new y by trapezoid method
    y += dx * (f(x,y) + f(x+dx,estNewY)) * 0.5
    x += dx
    yi.append(y)
    xi.append(x)
  e = y-v
  return (dx,x,y,e,xi,yi)


# (stepsize,x,y,e,valx,valy) = eulerimproved(equation1,1.0,0.0,0.1,2.0)

# print(y)


# Runge-Kutta Method and table sumarizing results

def rungekutta(f,initialy,initialx,dx,endpoint):
  yi=[]
  xi=[]
  x,y = initialx,initialy

  while x < endpoint - dx/2:
    #defining k values per Runge Kutta
    k1 = dx * f(x,y)
    k2 = dx * f(x+(dx/2), y+(k1/2))
    k3 = dx * f(x+(dx/2), y+(k2/2))
    k4 = dx * f(x+dx, y+(k3))
    #estimate new y by Runge Kutta Method
    y += (k1+(2*k2)+(2*k3)+k4) / 6
    x += dx

    yi.append(y)
    xi.append(x)
    e = y-v
  return (dx,x,y,e,xi,yi)

# printEval(rungekutta)



# Code to implmenent Euler's Method over various invertals and plot the results

def equation2(x,y):
	return 2-2*x+2*y

print(euler(equation2,0,1,0.25,2))

# final_values = [10,20,25,30,35,40]
# y0 = 1
# x0 = 0
# xi,yi = [0]*6,[0]*6

# for i in range(len(final_values)):
#   endpoint = final_values[i]
#   (stepsize,x,y,e,xi[i],yi[i])=euler(equation1,y0,x0,endpoint/20,endpoint)
#   plt.figure(i)
#   plt.title('Eulers Method on the interval [0,%i]' %endpoint)
#   plt.xlabel('X')
#   plt.ylabel('Y')
#   plt.plot(xi[i],yi[i],'-o')