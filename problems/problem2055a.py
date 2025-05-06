"""
https://codeforces.com/problemset/problem/2055/A
"""

import random

n = random.randint(2,500)
a = random.randint(1,n)
b = random.randint(1,n)

while a == b:
    b = random.randint(1,n)

#pads = list(range(1,n + 1))
#print(pads)

print(f'n = {n}, a = {a}, b = {b}')

x = a
y = b

# This fucntion makes the moves for A
def moveA(numa,numb):

    done = False

    if not done and numa - numb > 1 and numa - 1 >= 1: 
        numa = numa - 1
        done = True       
    
    if not done and numb - numa > 1 and numa + 1 <= n:
        numa = numa + 1
        done = True

    if not done and numa > numb and numa - 1 == numb and numa + 1 <= n:
        numa = numa + 1
        done = True
    
    if not done and numa < numb and numa + 1 == numb and numa - 1 >= 1:
        numa = numa - 1
        done = True
    
    return numa

# This fucntion makes the moves for B
def moveB(numa,numb):
    return moveA(numb,numa)

count = 0

# Initial conditions
print(f'a = {a}, b = {b}, move = {count}')

# Iterations for the movements 
while a != moveA(a,b) and b != moveB(a,b):
    a = moveA(a,b)
    b = moveB(a,b)
    count = count + 1
    print(f'a = {a}, b = {b}, move = {count}')


print('-------------')

print(f'n = {n}, a = {x}, b = {y}')

if a == moveA(a,b):
    print('NO')

if b == moveB(a,b):
    print('YES')

