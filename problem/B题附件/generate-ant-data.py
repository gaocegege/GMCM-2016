#!/usr/local/bin/python3

filename = 'prepass-for-rt.dat'

outputfilename = 'antdata.txt'

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
outputHandle = open(outputfilename, 'w')

all_text = handle.read()
lines = all_text.split('\n')
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
	buf = ""
	for j in range(1, len(weidians)):
		buf += attrs[j] + ","
	if i <= 500:
		buf += "0\n"
	else:
		buf += "1\n"
	outputHandle.write(buf)
