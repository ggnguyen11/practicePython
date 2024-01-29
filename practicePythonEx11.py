# practicepython.org | exercise 11 | 01/29/2024
# prompt: ask user for number and test whether number is prime or not
# (prime numbers have no divisors) / function practice

def prime_test(n):
    if n % 2 != 0 and n != 2 and n != 1:
        print("Your number is prime!")
    elif n == 2:
        print("Your number is prime!")
    elif n % 2 == 0 and n != 2:
        print("Your number is not prime!")
    elif n == 1:
        print("Your number is not prime!")
    else:
        print("Your number is not prime!")
    
num = int(input("Give me a number that I can test for its primality: "))
prime_test(num)