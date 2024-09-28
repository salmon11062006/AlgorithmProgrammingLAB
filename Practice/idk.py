class Person:
    name = 0
    age = 0
    hobby = 0
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
   
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_hobby(self):
        return self.hobby

p1 = Person('Salomo', 18, 'Volleyball')
p2 = Person('Chris', 20, 'Basketball')
p3 = Person('Bradley', 19, 'Cycling')

print(p1.get_name(), p1.get_age(), p1.get_hobby())