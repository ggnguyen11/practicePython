# FizzBuzz game project from udemy
# program should print each number from 1 to 100 in turn and include 100
# if number is divisible by 3 print "Fizz" instead of the number
# if number is divisible by 5 print "Buzz" instead of the number
# if number is divisible by both 3 and 5 print "FizzBuzz" instead of number

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    elif i % 5 == 0 and i % 3 != 0:
        print("Buzz")
    else:
        print(i)