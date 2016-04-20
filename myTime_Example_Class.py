class myTime():
    def __init__(self, hour, minute, second):
        self.h = hour
        self.m = minute
        self.s = second
    def getTime(self):
        return (h, m, s)
    def __str__(self):
        return str(self.h) + ":" + str(self.m) + ":" + str(self.s)
        
t = myTime(13, 5, 23)

print(t)
