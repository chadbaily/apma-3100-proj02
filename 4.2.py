import math

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
        count = 0
        tempResults = []
        while count < n:
            count += 1
            tempResults.append(
                math.sqrt(uVal.pop(0)**2 + uVal.pop(0)**2))
        results.append(sum(tempResults) / n)  # M_n

count = 0
for i in results:
    print(str(count) + ": " + str(i))
    count += 1
