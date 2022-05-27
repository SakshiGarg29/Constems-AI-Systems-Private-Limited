import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# 1. function to generate random numbers from scratch without
# using any libraries in python

def random1(m=2**32, a=1103515245, c=12345, size =1):
    random1.current = (a*random1.current + c) % m
    return random1.current/m

# setting the seed
random1.current = 1
n_iter = 100
ls = []
ls1 = []
for i in range(n_iter):
    x = float(random1())
    y = float(random1())
    ls.append(x)
    ls1.append(y)
print("List of random numbers generated:",ls)

# 3. Predicting the Value of Pi
circle_points = 0
square_points = 0

for i in range (n_iter ** 2):
    rand_x = float(random1())
    rand_y = float(random1())

    # Distance between (x, y) from the origin
    origin_dist = rand_x ** 2 + rand_y ** 2

    # Checking if (x, y) lies inside the circle
    if origin_dist <= 1:
        circle_points += 1

    square_points += 1

    # Estimating value of pi
    pi = 4 * circle_points/square_points

print("Final Estimation of Pi:", pi)

# 2. Visualizinf the randomness of generated values
plt.scatter(ls,ls1, color = 'green')
plt.title('Randomness of Generated Function')
plt.xlabel('Number Range')
plt.ylabel('Range')
plt.show()
