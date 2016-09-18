#!/usr/local/bin/python3

filename = 'genotype.dat'

outputfilename = 'prepass-genotype.dat'

class Weidian(object):
	"""docstring for weidian"""
	def __init__(self, weidian):
		self.arr = []
		self.weidian = weidian

	def __str__(self):
		s = "SNPs: " + self.weidian + "\n\t"
		for e in self.arr:
			s += "\t\t: {0}\n".format(e)
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
outputHandle = open(outputfilename, 'w')

all_text = handle.read()
lines = all_text.split('\n')
weidians = lines[0].split(' ')
outputHandle.write(lines[0] + '\n')

arr = []
# 最小字母
weidiansLeast = []

for i in range(0, len(weidians)):
	arr.append(Weidian(weidians[i]))
	weidiansLeast.append('a')

for j in range(0, len(weidians)):
	for i in range(1, len(lines)):
		attrs = lines[i].split(' ')
		if attrs[j][0] != attrs[j][1]:
			if (attrs[j][0] < attrs[j][1]):
				weidiansLeast[j] = attrs[j][0]
			else:
				weidiansLeast[j] = attrs[j][1]
			break

print(weidiansLeast)

for i in range(1, len(lines)):
	attrs = lines[i].split(' ')
	line = ''
	if len(attrs) < 9445:
		continue
	for j in range(0, len(weidians)):
		if attrs[j][0] != attrs[j][1]:
			line += '1 '
		elif attrs[j][0] == weidiansLeast[j]:
			line += '0 '
		else:
			line += '2 '
	line = line[:-1]
	line += '\n'
	outputHandle.write(line)
