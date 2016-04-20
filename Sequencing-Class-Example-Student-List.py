class student():
	def __init__(self, lst = []):
		self.stdList = lst
	def __repr__(self):
		returnStr = ""
		for i in self.stdList:
			returnStr = returnStr + i
		return returnStr
	
	def __str__(self):
		returnStr = ""
		for i in self.stdList:
			returnStr = returnStr + i
		return returnStr
		
s = student()
s2 = student(['Amy', 'Betty'])
  
