class machine():
	time = 0
	working_time = 0
	num = 0
	def __init__(self, time, working_time, num):
		self.time = time
		self.sec = time
		self.working_time = working_time
		self.num = num
	
	def isBroken(self):
		self.sec = self.sec - 1
#		print ("Machine ", self.num, " sec ", self.sec, " working time: ", self.working_time)
		if (self.sec == 0):
			return True
		return False
