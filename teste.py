import math

n,m = map(int,raw_input().split())

aux = m
count = 0
presses = 0

while aux % 2 == 0:
    aux = aux / 2
    count += 1

if n >= aux: 
    x = 1
    y = 1
else: 
    x = 2
    y = 2
while n != m:
    while n > math.ceil(aux/x):
        n -= 1
        presses += 1
    while n < math.ceil(aux/x):
        n = n * 2
        presses += 1
    if n == math.ceil(aux / x): 
        presses += y + count
print presses
