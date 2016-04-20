class myTime():
    def __init__(self, hour, minute, second):
        self.h = hour
        self.m = minute
        self.s = second
    def getTime(self):
        return (h, m, s)
    def __str__(self):
        return str(self.h) + ":" + str(self.m) + ":" + str(self.s)
        
    def __add__(self, other):
        hour = self.h + other.h
        minute = self.m + other.m
        second = self.s + other.s
        return myTime(hour, minute, second)
        
    def __lt__(self, other):
        if self.h < other.h:
            return True
    
t = myTime(13, 5, 23)

print(t)
