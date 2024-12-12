class mother:
    def __init__(self,eyes, hair_texture):
        self.eyes=eyes
        self.hair_texture=hair_texture
    def display(self):
        print("Your eye color is", self.eyes)
        print("Your hair texture is",self.hair_texture)
class daughter(mother):
    def __init__(self,eyes,hair_texture):
        mother.__init__(self,eyes,hair_texture)

obj=daughter("hazel","curly")
obj.display()

class teacher:
    def __init__(self, name, closs, school):
        self.name=name
        self.closs=closs
        self.school=school
    def display(self):
        print("Hi,", self.name)
        print("You are in class", self.closs)
        print("You go to ", self.school)

class student(teacher):
        def __init__(self,name,closs, school):
            super().__init__(name,closs, school)

    
obj=student("Emilia","10D", "ISGR")
obj.display()