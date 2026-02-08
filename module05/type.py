# def infos(b):
# 	print(f"my name is {b.name}")
# Test = type("Test",(),{"name":"test","pnt":infos}) 


# b = test()
# b.pnt()

class custom(type):
	def __new__(self, name, b, attributes):
		print("hilllow")
		super().__new__(self, name, b, attributes)

class Dog(metaclass=custom):
    def bark(self):
        print("woof")

# d = Dog()
# print(type(Dog))


