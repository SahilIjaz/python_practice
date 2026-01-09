class Student:
    def __init__(a, name, age):
        a.name = name
        a.age = age

    def great(a):
        return f"Hello, i am {a.name} and age is {a.age}."


std_1 = Student('Alice', 20)

print(std_1.great())
