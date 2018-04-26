import math
import numpy as np
import scipy.stats as st
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
    # print("Average: ", np.mean(ycord))
    # print("Sqrt of Standard Deviation: ", math.sqrt(np.std(ycord)))

    points = [0, 0, 0, 0, 0, 0, 0]
    zValues = [1.4, 1, 0.5, 0, -0.5, -1, -1.4]

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

    empericalCDF = []
    for i in range(0, len(points)):
        print("The probability of " +
              str(zValues[i]) + " is: " + str(points[i]))
        empericalCDF.append((zValues[i], points[i]))

    madnValues = []
    cdfValue = [0.9192, 0.8413, 0.6915, 0.5, 0.3085, 0.1587, 0.0808]
    for i in range(0, len(points)):
        madnValues.append(np.abs(points[i] - cdfValue[i]))

    MADn = np.amax(madnValues)
    MADnPlot = (zValues[np.argmax(madnValues)], MADn)
    print("The max value for MADn = " + str(MADn))

    # Calculate the z score for -2.5 to 2.5
    # z = []
    # cdf = []
    plotCDF = []
    start = -2.5
    while start <= 2.5:
        # cdf.append(st.norm.cdf(start))
        # z.append(start)
        plotCDF.append((start, st.norm.cdf(start)))
        start += 0.01

    # for i in range(0, len(z)):
    #     print("The z score for " + str(z[i]) + " is " + str(cdf[i]))

    plt.title('Goodness of fit of standard normal CDF for n = ' + str(n))
    plt.plot(*zip(*plotCDF), label='Standard Normal CDF')
    plt.scatter(*zip(*empericalCDF), color='red', label='Emperical CDF')
    plt.scatter(*MADnPlot, color='orange', label=r'$MAD_n$')
    # plt.axhline(np.mean(ycord), color='black')
    plt.ylabel(r'$M_n(x)$')
    plt.xlabel(r'$n$')
    plt.legend()
    plt.show()

# Print out all results
# count = 0
# for i in results:
#     print(str(count) + ": " + str(i))
#     count += 1
