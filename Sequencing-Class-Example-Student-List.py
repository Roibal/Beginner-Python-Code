class student():
	"""
	The purpose of this class python program is to show 'sequencing', which treats an object as a list and can be indexed.
	"""
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
		
	def __getitem__(self, key):
		return self.stdList[key]
	
	def __setitem__(self, key, content):
		self.stdList[key] = content
		
#s = student()
s = student(['Amy', 'Betty'])
s[1] = "Cindy"
print(s[1])
  
