from collections import deque
import random
from classes.udp import UDP
from classes.master import master
from classes.machine import machine
from classes.Que import Que
from classes.mathematiq	import mathematiq
from classes.statistic import statistic	

class main():
	def __parsing_cfg(self, path_to_file):
		f = open(path_to_file, 'r')
		a = [line for line in f]
		dictry = {}
		for i in a[2:]:
				tmp = i.strip('\n')
				tmp = tmp.strip(';')
				tmp = tmp.split("=")
				for j in tmp:
					tmp[tmp.index(j)] = j.strip(' ')
				for j in tmp:
					tmp[tmp.index(j)] = j.strip("\"")
				a[a.index(i)] = tmp
		b = list.copy(a[2]+a[3])
		dictry = dict(zip(b[::2], b[1::2]))
		host = dictry["sHost"]
		port = int(dictry["sPort"])
		return ((host,port))

	def __init__(self):
		path_to_file = "/home/leo/shara/6_sem/oop/config.cfg"
		sock_addr = self.__parsing_cfg(path_to_file)
		_recv_arr = bytes("", encoding = 'utf-8')
		_udp = UDP(sock_addr)
		print('waiting data...')
		while(1):
			if ("exit" in _recv_arr.decode('utf-8')):
					_udp.stop_listening()
					break
			if ("stop" in _recv_arr.decode('utf-8')): 
				_udp.send(str(_machine_stat.expected_value(_num_of_machines)) + ";" + str(_machine_stat.standard_deviation(_num_of_machines)) + ";" + str(_master_stat.expected_value(_num_of_machines)) + ";" + str(_master_stat.standard_deviation(_num_of_machines)))	
				while(1):
					_recv_arr = _udp.recv()
					if (_recv_arr != bytes("", encoding = 'utf-8')):
						break
				if ("exit" in _recv_arr.decode('utf-8')):
					break
			random.seed()
			sec = 0
			que = deque()
			myQue = Que(que)

			if _recv_arr == bytes("", encoding = 'utf-8'):
				_recv_arr = _udp.recv()
			if _recv_arr == bytes("", encoding = 'utf-8'): continue

			_position_array = _udp.pos_array(_recv_arr)
			_env_time = 0 
		
			_num_of_masters = int(_recv_arr[0:_position_array[0]].decode('utf-8'))
			_num_of_machines = int(_recv_arr[_position_array[0]+1:_position_array[1]].decode('utf-8'))
			_crash_seq = int(_recv_arr[_position_array[1]+1:_position_array[2]].decode('utf-8'))
			if (len(_position_array) == 4):
				_mean_working_time = int(_recv_arr[_position_array[2]+1:_position_array[3]].decode('utf-8'))
				_env_time = int(_recv_arr[_position_array[3]+1:].decode('utf-8'))
			else:
				_mean_working_time = int(_recv_arr[_position_array[2]+1:].decode('utf-8'))

			_machines_math = mathematiq(_crash_seq) 
			_masters_math = mathematiq(_mean_working_time)
		
			_machine_stat = statistic(_machines_math)
			_master_stat = statistic(_masters_math)

			_working_time = _masters_math.exp_calculating(_num_of_machines)
			_crash_times = _machines_math.exp_calculating(_num_of_machines)
			masters_list = [master() for i in range (_num_of_masters)]
			machines_list = [machine(_crash_times[i], _working_time[i], i) for i in range (_num_of_machines)]	
		
			workers_and_times = []
	
			if (_env_time == 0):
				while (1):
					_recv_arr = _udp.recv()
					if ((_recv_arr != bytes("", encoding = 'utf-8')) and ("pause" not in _recv_arr.decode('utf-8'))): break
					elif ("pause" in _recv_arr.decode('utf-8')):
						print ("Paused...")
						while (1):
							_recv_arr = _udp.recv()
							if "pause" in _recv_arr.decode('utf-8'):
								_recv_arr = bytes("", encoding = 'utf-8')
								print ("Contining...")
								break 
					_working_time = _masters_math.exp_calculating(_num_of_machines)
					_crash_times = _machines_math.exp_calculating(_num_of_machines)
					#			print ("Crash_times: ", _crash_times)
					#			print ("Working_times: ",_working_time)
					for i in machines_list:
						if i.sec == 0:
							i.sec = _crash_times[i.num]
							i.working_time = _working_time[i.num]

					workers_and_times = myQue.check(masters_list, machines_list, workers_and_times, _udp)
					for i in workers_and_times:
						if i[0].time == i[1]:
							i[0].changeState()
							workers_and_times.remove(i)
							myQue.workers.remove(i[0])
							print (i[0].ID , "FINISHED")
						i[0].time = i[0].time + 1
					#			sleep(3)
			else:
				for I_env_time in range (_env_time): 
					_recv_arr = _udp.recv()
					if ((_recv_arr != bytes("", encoding = 'utf-8')) and ("pause" not in _recv_arr.decode('utf-8'))): break
					elif ("pause" in _recv_arr.decode('utf-8')):
						print ("Paused...")
						while (1):
							_recv_arr = _udp.recv()
							if "pause" in _recv_arr.decode('utf-8'):
								_recv_arr = bytes("", encoding = 'utf-8')
								print ("Contining...")
								break 
					_working_time = _masters_math.exp_calculating(_num_of_machines)
					_crash_times = _machines_math.exp_calculating(_num_of_machines)
					#			print ("Crash_times: ", _crash_times)
					#			print ("Working_times: ",_working_time)
					for i in machines_list:
						if i.sec == 0:
							i.sec = _crash_times[i.num]
							i.working_time = _working_time[i.num]

					workers_and_times = myQue.check(masters_list, machines_list, workers_and_times, _udp)
					for i in workers_and_times:
						if i[0].time == i[1]:
							i[0].changeState()
							workers_and_times.remove(i)
							myQue.workers.remove(i[0])
							print (i[0].ID , "FINISHED")
						i[0].time = i[0].time + 1
					#			sleep(3)
			print('waiting data...')
			for i in range (5):
				if _recv_arr == bytes("", encoding = 'utf-8'):
					_recv_arr = _udp.recv()
			if ("exit" in _recv_arr.decode('utf-8')):
					break
