class Employee:
	def __init__(self,eno,ename,esal):
		self.eno=eno
		self.ename=ename
		self.esal=esal
	def display(self):
		print("The employee name is:",self.ename)
		print("The employee no	is:",self.eno)
		print("The employee salary:" ,self.esal)
class Increment():
	def modify(self):
		self.esal=self.esal+10000
		self.display()

print("Hi")
		
e=Employee(10,"durga",50000)
Increment.modify(e)