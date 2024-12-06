class fruit:
    #Taste = sweet is a class variable
    taste="sweet"
    #instance variable
    def _init_(self, name, color):
        self.name=name
        self.color=color
#object creation
a=fruit("apple","red")
banana=fruit("banana","yellow") 
print(a.taste)
print(a.name,a.color)
print(banana.name,banana.color)       
