import random
class mathematiq():
	mean = 0
	def __init__(self, mean):
		self.mean = mean
		 
	def exp_calculating(self, diapason):
		y = []
		for i in range(diapason):
#			x = random.randint(0, diapason*2)
#			y.append(1-((exp(-x/mathematiq.mean))/mathematiq.mean))
			y.append(int(random.expovariate(1/self.mean))+1)
		return y
		#F(t) = 1- e^(-t/T)/T
