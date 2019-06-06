from collections import deque	
class Que():
	que = 0
	sec = 0
	workers = []
	def __init__(self, que):
		Que.que = que
		
	def check(self, masters_list, machines_list, workers_and_times, _udp):	
		for i in machines_list:
			if (i.isBroken()):
				if i.num not in self.que: 
					self.que.append(i.num)
					_udp.send("+")	
		for masterI in masters_list:
			if masterI not in Que.workers:
				while (self.que):
					print (self.que)
					if masterI.isBusy == False:
						machineID = masterI.pop(self.que)
						_udp.send("-" + str(masterI.ID))
						print ("Master", masterI.ID, "took machine", machineID)	
						masterI.changeState()
						Que.workers.append(masterI)
						workers_and_times.append((masterI,machines_list[machineID].working_time))
						break
		return workers_and_times
