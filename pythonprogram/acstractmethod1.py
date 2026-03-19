from abc import ABC, abstractmethod

#Abstract class
class Vehicle(ABC):

	@abstractmethod
	def start(self):
		pass

	@abstractmethod
	def stop(self):
		pass

#child class1
class Car(Vehicle):
	
	def start(self):
		print("Car starts with key")


	def stop(self):
		print("Car stops with break")


#child class2
class Bick(Vehicle):

	def start(self):
		print("Bick starts with self-start button")

	def stop(self):
		print("Bick stops with break")


#object creation
c=Car()
c.start()
c.stop()

b=Bick()
b.start()
b.stop()