# practicepython.org | exercise 7 | 01/27/2024
# prompt: with given list a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100], write
# one line that makes a new list with only the even elements of a in it
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# list comprehension w/ conditional
evens = [num for num in a if num % 2 == 0]

# alt solution using lambda() & filter() functions
even_filter = lambda num: num % 2 == 0

# applies even_filter conditional specified above to the list a w/ filter()
# then turns it into a list to be stored in evens_only
evens_only = list(filter(even_filter, a))

print(evens)
print(evens_only)