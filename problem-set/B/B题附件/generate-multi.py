#!/usr/local/bin/python3

filename = 'prepass-for-rt.dat'

multifilename = 'multi_phenos.txt'

outputTemplate = 'multi-antdant-{0}.txt'

class SNP(object):
	"""docstring for weidian"""
	def __init__(self, pheo):
		self.pheo = pheo

	def __str__(self):
		s = "{0} {1} {2} {3} {4} {5}".format(self.familyID, self.ID, self.pID, self.mID, self.sex, self.isAffected)
		for e in self.arr:
			s += " {0} {1}".format(e[0], e[1])
		s += "\n"
		return s

handle = open(filename, "r")
multiHandle = open(multifilename, 'r')
lines = handle.read().split('\n')
healthyLines = multiHandle.read().split('\n')

for index in range(0, 10):
	outputfilename = outputTemplate.format(index)
	outputHandle = open(outputfilename, 'w')
	weidians = lines[0].split(' ')

	arr = []

	buf = ""
	for i in range(1, len(weidians)):
		buf += weidians[i]
		buf += ","
	buf += "healthy"
	buf += "\n"
	outputHandle.write(buf)

	for i in range(1, len(lines)):
		attrs = lines[i].split(' ')
		healthyAttrs = healthyLines[i - 1].split(' ')
		buf = ""
		for j in range(1, len(weidians)):
			buf += attrs[j] + ","
		buf += "{0}\n".format(healthyAttrs[index])
		outputHandle.write(buf)
