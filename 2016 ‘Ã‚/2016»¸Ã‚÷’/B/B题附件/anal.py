#!/usr/local/bin/python3

filename = 'genotype.dat'

class Weidian(object):
	"""docstring for weidian"""
	def __init__(self, weidian):
		self.dict = {}
		self.weidian = weidian

	def __str__(self):
		s = "SNPs: " + self.weidian + "\n\t"
		for keys,values in self.dict.items():
			s += keys
			s += ": {0}\n\t".format(values)
		return s
		

handle = open(filename, "r")

all_text = handle.read()
lines = all_text.split('\n')
weidians = lines[0].split(' ')

arr = []

for i in range(0, len(weidians) - 1):
	arr.append(Weidian(weidians[i]))

for i in range(1, len(lines)-1):
	attrs = lines[i].split(' ')
	isPatient = 0
	if i > 501:
		isPatient = 1
	for j in range(0, len(weidians) - 1):
		if {attrs[j], isPatient} not in arr[j].dict:
			arr[j].dict[{attrs[j]] = 1
		else:
			arr[j].dict[attrs[j]] += 1

for i in range(0, len(weidians) - 1):
	print(arr[i])