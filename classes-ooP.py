class Student:
    counter = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Student.counter += 1

    
    def get_student(self):
        return f"Name: {self.__name}, Age:{self.__age}."


student1 = Student('Sahil', 20)

print(student1.get_student())


class Employee(Student):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender

    def get_gender(self):
        return self.gender

    def get_employee(self):
        return f'{self.get_student()} Gender:{self.get_gender()}'


class Ilumanai(Student):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

    def get_role(self):
        return self.role

    def get_ilumanai(self):
        return f'{self.get_student()} Role:{self.get_role()}'
    




employee1 = Employee('Ali', 25, 'Male')
print(employee1.get_employee())

print(Student.counter)


Ilumanai1 = Ilumanai('Sara', 30, 'Developer')
print(Ilumanai1.get_ilumanai())

