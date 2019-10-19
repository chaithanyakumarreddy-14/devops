class Test():
	def setname(self,name):
		self.name=name
	def getname(self):
		return self.name
	def setmarks(self,marks):
		self.marks=marks
	def getmarks(self):
		return self.marks
s=Test()
s.setname("durga")
print(s.getname())
s.setmarks(90)
print(s.getmarks())
s1=Test()
s.setname("chaithanya")
print(s.getname())
s.setmarks(80)
print(s.getmarks())
	