#simple class
class student:
        grade=10
        name="pegiun"
        def intro(self): 
                print("hi i am a student")
        def detail(self):
                print("My name is",self.name)
                print("i study in",self.grade)

ob=student() 
ob.intro()
ob.detail()
