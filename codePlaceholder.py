# placeholder file for test code
import math

# mean
count = 0
sum = 0
for i in range(55, 84):
    count += 1
    sum += i

print("sum: " + str(sum))
print("count: " + str(count - 1))
print("mean: " + str(sum / (count - 1)))

# variance
var = 0
for i in range(55, 84):
    var += (i - 71.46) ** 2

var = var / 28

print("variance: " + str(var))
# SD
print("standard deviation: " + str(math.sqrt(var)))