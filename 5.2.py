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
mean = 0.7633496513793749  # mean
sigma = 0.246349662499206  # sqrt of var


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
                                zscore(math.sqrt(uVal.pop(0)**2 + uVal.pop(0)**2), n)))
        results.append((n, sum([pair[1] for pair in tempResults]) / n))  # M_n

ycord = [pair[1] for pair in results]
print("Average: ", np.mean(ycord))
print("Sqrt of Standard Deviation: ", math.sqrt(np.std(ycord)))


# plt.title('Monte-Carlo Simulation')
# plt.scatter(*zip(*results))
# plt.axhline(0.7633496513793749, color='black')
# plt.ylabel('mn')
# plt.xlabel('n')
# plt.show()

# Print out all results
count = 0
for i in results:
    print(str(count) + ": " + str(i))
    count += 1
