from __future__ import print_function
import sys
import math
import inspect

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def printInorder(root):
	if root:
		printInorder(root.left)
		print(root.val, end = '\t')
		printInorder(root.right)

def printPostorder(root):
	if root:
		printPostorder(root.left)
		printPostorder(root.right)
		print(root.val, end = '\t')

def printPreorder(root):
	if root:
		print(root.val, end = '\t')
		printPreorder(root.left)
		printPreorder(root.right)

def readargs():
	trainInput = sys.argv[0]
	testInput = sys.argv[1]
	maxDepth = int(sys.argv[2])
	trainOut = sys.argv[3]
	testout = sys.argv[4]
	metricsOut = sys.argv[5]

def trainProcess(infile, outfile):
	fin = open(infile, "r")
    fout = open(outfile, "w")
    lines = fin.readlines()



def testProcess(infile, outfile):

def entropyCal(lst):
	pos = 0
	neg = 0
	comp = lst[0]
	for x in lst:
		if x == comp:
			pos += 1
		else:
			neg += 1
	entropy = -((pos / (pos + neg)) * math.log(pos / (pos + neg), 2) + (neg / (pos + neg)) * math.log(neg / (pos + neg), 2))
	return entropy

def mutualCal(lstY, lstX):
	




