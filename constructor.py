class construct:
    def __init__(self,name ,color):
        self.name=name
        self.color=color

ob=construct("watermelon","red")
print(ob.name)
print(ob.color)

class fruit:
 def __del__(self):
    print("desctructor called delete.")
ob=fruit()
del ob