# practicepython.org | exercise 12 | 01/29/2024
# prompt: write a program that takes a list of numbers and makes a new list
# of only the first and last elements of the given list, use a function
# ex: use a = [5, 10, 15, 20, 25]
a = [5, 10, 15, 20, 25]
b = []

def heads_tails(list, new_list):
    new_list.append(list[0])
    new_list.append(list[-1])
    print(new_list)

heads_tails(a, b)

# sample solution:
# def list_ends(a_list):
#   return [a_list[0], a_list[len(a_list)-1]]