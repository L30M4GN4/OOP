import numpy as np
from math import sqrt
class statistic():
	stat_obj = 0
	def __init__(self, obj):
		self.stat_obj = obj
		
	def expected_value(self, diapason):
		self.tmp = self.stat_obj.exp_calculating(diapason)
		return sum(self.tmp)/len(self.tmp)
	
	def dispersion(self, diapason):
		self.tmp = self.stat_obj.exp_calculating(diapason)
#		return expected_value((tmp[i]-expected_value(diapason))**2)
		return np.var(self.tmp)
		
	def standard_deviation(self, diapason):
		return sqrt(self.dispersion(diapason))
