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
			s += ": {0}\n\t".format(values)
		return s

# 是不是病人以及碱基对
class DoubleAndIsPatient(object):
	"""docstring for DoubleAndIsPatient"""
	def __init__(self, jianjidui):
		self.patientNum = 0
		self.nonPatientNum = 0
		self.jianjidui = jianjidui
	def __str__(self):
		return "碱基对：" + self.jianjidui + "\n\t\t" + "病人数：" + str(self.patientNum) + "\t非病人数：" + str(self.nonPatientNum)


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
		if attrs[j] not in arr[j].dict:
			arr[j].dict[attrs[j]] = DoubleAndIsPatient(attrs[j])
		else:
			arr[j].dict[attrs[j]].patientNum += (isPatient == 1)
			arr[j].dict[attrs[j]].nonPatientNum += (isPatient == 0)

for i in range(0, len(weidians) - 1):
	w = arr[i]
	for keys,values in w.dict.items():
		if abs(values.patientNum - values.nonPatientNum) > 50:
			print(w)
