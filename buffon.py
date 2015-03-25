#!/usr/bin/env python3

import math
import random

def buffon(needlesNbr, groovesLen, needlesLen):
	"""Simulates Buffon's needle experiments."""

	intersects = 0
	for i in range(needlesNbr):
		y = random.random() * needlesLen / 2
		angle = random.random() * math.pi
		z = groovesLen / 2 * math.sin(angle)

		if y <= z:
			intersects += 1

	expFreq = intersects / needlesNbr
	thFreq = 2 * needlesLen / (math.pi * groovesLen)

	return (intersects, expFreq, thFreq)

def runBuffon(needlesNbr, groovesLen, needlesLen):
	print('Distance between grooves:', groovesLen)
	print('Number of needles:', needlesNbr)
	print('Length of needles:', needlesLen)
	print('Starting simulation...')

	intersects, expFreq, thFreq = buffon(needlesNbr, groovesLen, needlesLen)

	piEst = 2 * needlesLen / (expFreq * groovesLen)

	print('Done.')
	print('Intersections:', intersects)
	print('Experimental frequency:', expFreq)
	print('Theorical frequency:', thFreq)
	print('PI estimation:', piEst)
	print('Relative error:', (piEst - math.pi) / math.pi * 100, '%')

def runTests(maxNeedlesNbr, testsNbr):
	print('Starting', testsNbr, 'simulations...')

	needlesStep = maxNeedlesNbr // testsNbr
	needlesNbr = needlesStep
	o = 'Needles;Experimental;Theorical;PI;Error\n'
	for i in range(testsNbr):
		print('Simulating '+str(needlesNbr)+' needles...')
		intersects, expFreq, thFreq = buffon(needlesNbr, 10, 10)
		piEst = 2 * 10 / (expFreq * 10)
		o += str(needlesNbr)+';'+str(expFreq)+';'+str(thFreq)+';'+str(piEst)+';'+str(abs((expFreq - thFreq) / thFreq))+'\n'

		needlesNbr += needlesStep

	print('Done.')

	f = open('tests.csv', 'w+')
	f.write(o)
	f.close()

if __name__ == '__main__':
	runTests(500000, 5000)
	#runBuffon(100000, 10, 10)