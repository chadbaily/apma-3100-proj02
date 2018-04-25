import math
import numpy as np
import matplotlib.pyplot as plt

x = 1000
a = 24693
c = 1753
K = 2**17

uVal = []
count = 0
itterations = 300000
while count < itterations:

    x = (a * x + c) % K
    uVal.append(x / K)

    count = count + 1

# for i in uVal:
#     print(i)

mN = [5, 10, 30, 50, 100, 150, 250, 500]
results = []
mean = 71.15437313155435  # mean
sigma = 2.762189518228876  # sqrt of var


def zscore(mn, n):
    global mean
    global sigma
    return ((mn - mean) / (sigma * math.sqrt(n)))


for n in mN:
    for iid in range(0, 110):
        count = 0
        tempResults = []
        while count < n:
            count += 1
            tempResults.append((n,
                                math.sqrt((-2 * math.log(1 - uVal.pop(0))) / ((1 / 57)**2))))
        results.append(
            (n, zscore(sum([pair[1] for pair in tempResults]) / n, n)))  # M_n

ycord = [pair[1] for pair in results]
print("Average: ", np.mean(ycord))
print("Sqrt of Standard Deviation: ", math.sqrt(np.std(ycord)))


points = [0, 0, 0, 0, 0, 0, 0]

for point in ycord:
    if(point <= 1.4):
        points[0] += 1
    if(point <= 1.0):
        points[1] += 1
    if(point <= 0.5):
        points[2] += 1
    if(point <= 0):
        points[3] += 1
    if(point <= -0.5):
        points[4] += 1
    if(point <= -1):
        points[5] += 1
    if(point <= -1.4):
        points[6] += 1

for i in range(0, len(points)):
    points[i] = points[i] / 880  # getting probability

for point in points:
    print("The probability of 1.4, ... is: " + str(point))

plt.title('Monte-Carlo Simulation')
plt.scatter(*zip(*results))
plt.axhline(np.mean(ycord), color='black')
plt.ylabel('mn')
plt.xlabel('n')
plt.show()

# Print out all results
# count = 0
# for i in results:
#     print(str(count) + ": " + str(i))
#     count += 1
