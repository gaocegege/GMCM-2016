#!/usr/local/bin/python3

filename = 'genotype.dat'

outputfilename = 'snp.ped'

class Individual(object):
	"""docstring for weidian"""
	def __init__(self, i, isAffected):
		self.arr = []
		self.ID = i
		self.familyID = i
		self.isAffected = isAffected
		self.pID = 0
		self.mID = 0
		self.sex = "other"

	def __str__(self):
		s = "{0} {1} {2} {3} {4} {5}".format(self.familyID, self.ID, self.pID, self.mID, self.sex, self.isAffected)
		for e in self.arr:
			s += " {0} {1}".format(e[0], e[1])
		s += "\n"
		return s

handle = open(filename, "r")
outputHandle = open(outputfilename, 'w')

all_text = handle.read()
lines = all_text.split('\n')
weidians = lines[0].split(' ')

arr = []

for i in range(1, len(lines)):
	if i <= 500:
		arr.append(Individual(i, 0))
	else:
		arr.append(Individual(i, 1))

for i in range(1, len(lines)):
	attrs = lines[i].split(' ')
	if len(attrs) < 9445:
		continue
	for j in range(0, len(weidians)):
		arr[i - 1].arr.append(attrs[j])

for i in range(0, len(lines) - 1):
	outputHandle.write(str(arr[i]))
