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


for n in mN:
    for iid in range(0, 110):
        tempResults = []
        for w in range(0, n):
            tempResults.append((n,
                                math.sqrt((-2*math.log10(1-uVal.pop(0))) / ((1/57)**2))))
        results.append((n, sum([pair[1] for pair in tempResults]) / n))  # M_n

mean = np.mean([pair[1] for pair in results])
print("Average: ", mean)

plt.title('Monte-Carlo Simulation')
plt.scatter(*zip(*results))
plt.axhline(mean, color='black')
plt.ylabel('mn (in inches)')
plt.xlabel('n')
plt.show()

# Print out all results
# count = 0
# for i in results:
#     print(str(count) + ": " + str(i))
#     count += 1
