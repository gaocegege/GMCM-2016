#!/usr/local/bin/python3

filename = 'genotype.dat'

outputfilename = 'snp.map'

class Weidian(object):
	def __init__(self, weidian):
		self.weidian = weidian
		self.chro = 1
		self.dis = 0
		self.position = 1234555

	def __str__(self):
		return "{0} {1} {2} {3}\n".format(self.chro, self.weidian, self.dis, self.position)

handle = open(filename, "r")
outputHandle = open(outputfilename, 'w')

all_text = handle.read()
lines = all_text.split('\n')
weidians = lines[0].split(' ')

for i in range(0, len(weidians)):
	outputHandle.write(str(Weidian(weidians[i])))
