class cat:
    def __init__(self,name, age):
        self.name=name
        self.age=age

    def info(self):
        print("I am a cat, and my name is", self.name, "I am ",self.age, "years old" )
    def sound(self):
        print("Meow Meow")

class dog:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def info(self):
          print("I am a dog, and my name is", self.name, "I am ",self.age, "years old")
    def sound(self):
        print("Woof Woof")
obj=cat("Suzie", 2)
obj2=dog("Fluffy",5)

#Itrate for loop
for animal in(obj,obj2):
        animal.sound()
        animal.info()