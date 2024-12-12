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
