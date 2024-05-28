# practicepython.org | exercise 35 | 05/27/2024
# pt 3/4 of birthday data series: load JSON file from disk, extract months of
# all birthdays and count how many people have a birthday in each month

# output should be: {
#	"May": 3,
#	"November": 2,
#	"December": 1
#}
import json

# importing Counter (takes list and counts its elements)
from collections import Counter

# ex use case
#sandwiches = ["ham", "cheese", "roast beef", "ham", "cheese", "roast beef", "ham"]
#c = Counter(sandwiches)

# 