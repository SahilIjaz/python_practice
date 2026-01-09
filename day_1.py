print("Hello, World!")


print('Functions in Python.')

def greet(name):
    return f"Hello,{name}!"


def sum(a,b):
    return f"Sum is{a+b}."

name =input('Enter your name:')
print(greet(name))
a = int(input('Enter first number:'))
b = int(input("Enter seconf number:"))
print(sum(a,b))


print('Practice questions regarding functions.')


a = int(input('Enter first number:'))
b = int(input("Enter seconf number:"))
print(sum(a,b))

def is_even_or_odd(num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'
    
num = int(input('Enter a number:'))
print(is_even_or_odd(num))


def max_3(num_1,num_2,num_3):
    return max(num_1,num_2,num_3)

num_1 = int(input('Enter first number:'))
num_2 = int(input('Enter second number:'))
num_3 = int(input('Enter third number:'))
print(f"Maximum number is",max_3(num_1,num_2,num_3))


def factNum(num):
    fact = 1
    for i in range (1,num+1):
        fact = fact *1

    return fact

num = int(input('Enter a number:'))
print(f"Factorial of {num} is",factNum(num))


def vowels_string(string):
    vowels='aeiouAEIOU'
    count=0
    for char in string:
        if char in vowels:
            count +=1
        
    return count

print('Count vowels in a string.')
string = input('Enter a string:')
print(f"Number of vowels in the string is",vowels_string(string))

def is_prime(num):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                return 'Not a prime number'
        return 'Prime number'
    else:
        return 'Not a prime number'

num = int(input('Enter a number:'))
print(is_prime(num))


def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    return fib_sequence[:n]

n = int(input('Enter the number of terms:'))
print(f"Fibonacci sequence up to {n} terms is:",fibonacci(n))


def is_palindrome(string):
    if string == string[::-1]:
        return 'Palindrome'
    else:
        return 'Not a palindrome'
    

string = input('Enter a string:')
print(is_palindrome(string))

