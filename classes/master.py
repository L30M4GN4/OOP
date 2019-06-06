from collections import deque
class master():
	time = 0
	isBusy = False
	ID = 0
	
	def __init__(self):
		master.isBusy = False
		self.ID = master.ID + 1
		master.ID = master.ID + 1
		self.time = master.time
		
	def changeState(self):
		self.isBusy = not self.isBusy
		self.time = 0
		
	def pop(self, que):
		tmp = que.popleft()
		return tmp
