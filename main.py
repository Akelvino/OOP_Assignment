class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age= age
        self.gender = gender

    def introduce(self):
        return (f'My name is {self.name}. I am {self.age} and I am a {self.gender}')
    

intro = Person("kelvin", 30, "male")
print(intro.introduce())
