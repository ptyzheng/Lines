import os
import cv2
import numpy as numpy

#create a def (similar to method in java)
def example_def():
	#you don't have to declare a variable type for a variable 
	example_var = "example of a variable"
	print("example_var: ", example_var)
	#this means when you re-assign a value, you can assign it to anything!
	example_var = 5
	print("also example_var: ",example_var)


example_def()
#python is pass-by-reference, unlike pass-by-value like Python.
example_list = [[1,2,3,4], [1,2,3]]
print("example_list: ",example_list)

#when you have a list of lists, you have a list of references to the other lists. 
#We make a new list b that is a copy of example_list
b = example_list
print("b at declaration: ", b)
#but because we're storing references to other lists, if those lists change then b will also change.
example_list[1].append(5)

#notice that we did not explicitly edit b, but the values are different!
print("b after editing example_list: ", b)

#now we will show you how this applies to definitions.

def example_reference(ex_list):
	#in Java, what we pass is a copy of ex_list. But in Python, the variable reference is passed.
	ex_list.append([5,4,3])

print("original example_list: ", example_list)
example_reference(example_list)
print("after example_reference: ", example_list)


#creating classes in Python:
class ExampleClass:
	def __init__(self, var1, var2):
		self.var1 = var1
		self.var2 = var2
	#any definitions to be used as a class definition must have "self" as a parameter
	def print_vals(self):
		print("Class var 1: ", self.var1)
		print("Class var 2: ", self.var2)

class1 = ExampleClass(10, 20)
class1.print_vals()
