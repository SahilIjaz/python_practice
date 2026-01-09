print("Hello, World!")


print('Functions in Python.')


def greet(name):
    return f"Hello,{name}!"


def sum(a, b):
    return f"Sum is{a+b}."


name = input('Enter your name:')
print(greet(name))
a = int(input('Enter first number:'))
b = int(input("Enter seconf number:"))
print(sum(a, b))


print('Practice questions regarding functions.')


a = int(input('Enter first number:'))
b = int(input("Enter seconf number:"))
print(sum(a, b))


def is_even_or_odd(num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'


num = int(input('Enter a number:'))
print(is_even_or_odd(num))


def max_3(num_1, num_2, num_3):
    return max(num_1, num_2, num_3)


num_1 = int(input('Enter first number:'))
num_2 = int(input('Enter second number:'))
num_3 = int(input('Enter third number:'))
print(f"Maximum number is", max_3(num_1, num_2, num_3))


def factNum(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * 1

    return fact


num = int(input('Enter a number:'))
print(f"Factorial of {num} is", factNum(num))


def vowels_string(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1

    return count


print('Count vowels in a string.')
string = input('Enter a string:')
print(f"Number of vowels in the string is", vowels_string(string))


def is_prime(num):
    if num > 1:
        for i in range(2, num):
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
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    return fib_sequence[:n]


n = int(input('Enter the number of terms:'))
print(f"Fibonacci sequence up to {n} terms is:", fibonacci(n))


def is_palindrome(string):
    if string == string[::-1]:
        return 'Palindrome'
    else:
        return 'Not a palindrome'


string = input('Enter a string:')
print(is_palindrome(string))


print('Lists now')

list_1 = [1, 2, 3, 4, 5]

print('List of numbers', list_1)

lust_2 = ['apple', 'banana', 'cherry']

print('List of fruits', lust_2)

mixed_list = [1, 'apple', 3.14, True]
print('Mixed list', mixed_list)

print('Accessing elements in a list')
print('First element of list_1:', list_1[0])
print('Last element of lust_2:', lust_2[-1])

print('Slicing list_1 from index 1 to 3:', list_1[1:4])
print('Adding element to list_1')
list_1.append(6)
print('Updated list_1:', list_1)
print('Removing element from lust_2')
lust_2.remove('banana')
print('Updated lust_2:', lust_2)


for item in mixed_list:
    print('Item:', item)


print('Length of list_1:', len(list_1))
print('Length of lust_2:', len(lust_2))
print('Length of mixed_list:', len(mixed_list))

print(f"Hello,{name}")

students = {

    'std_1': {
        "name": 'Sahil',
        'age': 20},
    'std_2': {
        'name': 'Ali',
        'age': 25
    }
}

print('Students list of dictionaries:', students)
print('Accessing student 1 name:', students['std_1'])

employees = {
    1,
    2
}

print('Employees set:', employees)
