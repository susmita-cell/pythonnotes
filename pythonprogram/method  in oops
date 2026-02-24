method  in oops 
_____________________
instance method 
static method 
class maethod 



class Demo:
	#instance method call by object
	def show(self):
		print("hi")
d=Demo()# object create
d.show() #object refrence (d) call 
#Demo.show()  #not call by class




class Demo:
	#staticmethod  it call by classname  
	@staticmethod
	def show():
		print("hi")
Demo.show() #it call by classname
d=Demo()
d.show()



class Demo:
	#classmethod  it call by classname  but  it call  by object
	@classmethod
	def show(cls):
		print("hi")
Demo.show() #it call by classname  better
d=Demo()
d.show() # it call by object





class Demo:
	def show(self):
		print("instance show method")
	@classmethod
	def look(cls):
		print("class look method")
	@staticmethod
	def disp():
		print("disp static method")
d=Demo()
Demo().show() # by object call
d.show()  # it call by object  refernce 
d.look()
d.disp()
#Demo.show()  error
Demo.look()
Demo.disp()

constructor 
_________________
__init__   constructor special method 



class Rectangle:
	def __init__(self):   #constrcutor
		self.length=5
		self.breadth=7
	def show(self):
		print("rectangle lenegth=",self.length)
		print("rectangle breadth=",self.breadth)
	def area(self):
		print("area of rectangle=",self.length*self.breadth)
	def perimeter(self):
		return 2*(self.length+self.breadth)
r=Rectangle()
r.show()
r.area()
print("perimeter of rectangle=",r.perimeter())




class Rectangle:
	def __init__(self):   #constrcutor
		self.length=5
		self.breadth=7
	def show(self):
		print("rectangle lenegth=",self.length)
		print("rectangle breadth=",self.breadth)
	def area(self):
		print("area of rectangle=",self.length*self.breadth)
	def perimeter(self):
		return 2*(self.length+self.breadth)
r=Rectangle()
r.show()
r.area()
print("perimeter of rectangle=",r.perimeter())
r1=Rectangle()
r1.show()
r1.area()
print("perimeter of rectangle=",r1.perimeter())




class Rectangle:
	def __init__(self):   #constrcutor
		self.length=5
		self.breadth=7
	def show(self):
		print("rectangle lenegth=",self.length)
		print("rectangle breadth=",self.breadth)
	def area(self):
		print("area of rectangle=",self.length*self.breadth)
	def perimeter(self):
		return 2*(self.length+self.breadth)
r=Rectangle()
r.show()
r.area()
print("perimeter of rectangle=",r.perimeter())
r1=Rectangle()
r1.show()
r1.area()
print("perimeter of rectangle=",r1.perimeter())