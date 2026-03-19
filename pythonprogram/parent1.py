#parent class
class person:
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def show(self):
		print("Name:", self.name)
		print("Age:",self.age)
#child class1
class Teacher(person):
		def __init__(self, name, age, subject):
			super().__init__(name,age)
			self.subject = subject

		def display(self):
			self.show()
			print("subject:",self.subject)

#Child class2
class Student(person):
	def __init__(self,name,age,marks):
		super().__init__(name,age)
		self.marks = marks

	def display(self):
		self.show()
		print("marks:",self.marks)

		
#object creation
t1 = Teacher("anubhab",23,"python")
s1 = Student("susmita",20,88)

print("-----Teacher details-----")
t1.display()


print("-----Student details-----")
s1.display()






