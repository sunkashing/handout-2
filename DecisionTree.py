from __future__ import print_function
import numpy as np
import sys
import math
import inspect

# class Node:
# 	def __init__(self, attri, leftBranch, rightBranch):
# 		self.left = leftBranch
# 		self.right = rightBranch
# 		self.label = attri
# 		self.depth = 0
# 		self.prediction = None

# def printInorder(root):
# 	if root:
# 		root.depth += 1
# 		printInorder(root.left)
# 		print(root.val, end = '\t')
# 		printInorder(root.right)

# def printPostorder(root):
# 	if root:
# 		root.depth += 1
# 		printPostorder(root.left)
# 		printPostorder(root.right)
# 		print(root.val, end = '\t')

# def printPreorder(root):
# 	if root:
# 		root.depth += 1
# 		print(root.val, end = '\t')
# 		printPreorder(root.left)
# 		printPreorder(root.right)

# def majorityVote(lstY):
# 	comp1 = lstY[0]
# 	cnt1 = 0
# 	cnt2 = 0
# 	for ele in lstY:
# 		if ele == comp1:
# 			cnt1 += 1
# 		else:
# 			comp2 = ele
# 			cnt2 += 1

# 	if cnt1 >= cnt2:
# 		return comp1
# 	else:
# 		return comp2



# def decisionNode(nparray):
# 	length = nparray.shape[1]
# 	mi = []
# 	for i in range(length - 1):
# 		mi.append(mutualInformationCal(nparray[..., -1], nparray[..., i]))
# 	if mi.sort()[-1] > 0:
# 		decision_index = mi.index(mi.sort()[-1])
# 		return decision_index
# 	return None

# def partitionArray(nparray, attriIndex):
# 	comp = nparray[..., attriIndex][0]
# 	indexTrue = []
# 	indexFalse = []

# 	trueRows = []
# 	falseRows = []
# 	for i in range(len(nparray[..., attriIndex])):
# 		if nparray[..., attriIndex][i]== comp:
# 			indexTrue.append(i)
# 		else:
# 			indexFalse.append(i)
# 	for a in indexTrue:
# 		trueRows.append(nparray[a])
# 	for b in indexFalse:
# 		falseRows.append(nparray[b])
# 	trueRows = np.array(trueRows)
# 	falseRows = np.array(falseRows)
# 	trueRows = np.delete(trueRows, attriIndex, axis = 1)
# 	falseRows = np.delete(falseRows, attriIndex, axis = 1)
# 	return (trueRows, falseRows)

# def buildTree(nparray):
# 	attriIndex = decisionNode(nparray)
# 	if attriIndex is None:
# 		return leafNode(nparray)

# def trainProcess(infile, outfile):
# 	fin = open(infile, "r")
#     fout = open(outfile, "w")
#     lines = fin.readlines()

#     attri = lines[0].strip().split('\t')[:-1]
#     kind = lines[0].strip().split('\t')[-1]

#     lst = []
#     for a in lines[1:]:
#     	lst.append(a.strip().split('\t'))
#     nparray = np.nparray(lst)

#     while 





# def testProcess(infile, outfile):

def entropyCal(lst):
	if lst == []:
		return 0
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

def mutualInformationCal(lstY, lstX):
	compx1 = lstX[0]
	lstY1 = []
	lstY2 = []

	for x in lstX:
		if x != compx1:
			compx2 = x
			break
		else:
			compx2 = None

	px1 = len(selectValIndex(lstX, compx1)) / (len(selectValIndex(lstX, compx1)) + len(selectValIndex(lstX, compx2)))
	px2 = 1 - px1

	for x in selectValIndex(lstX, compx1):
		lstY1.append(lstY[x])

	for y in selectValIndex(lstX, compx2):
		lstY2.append(lstY[y])

	ylxv1 = entropyCal(lstY1)
	ylxv2 = entropyCal(lstY2)

	ylxv = px1 * ylxv1 + px2 * ylxv2
	mutualinformation = entropyCal(lstY) - ylxv

	return mutualinformation


	


def selectValIndex(lst, val):
	if val == None:
		return []
	comp = val
	newlst = []
	for i in range(len(lst)):
		if lst[i] == val:
			newlst.append(i)
	return newlst

# if __name__ == "__main__":

# 	trainInput = sys.argv[0]
# 	testInput = sys.argv[1]
# 	maxDepth = int(sys.argv[2])
# 	trainOut = sys.argv[3]
# 	testout = sys.argv[4]
# 	metricsOut = sys.argv[5]

# 	fin = open(infile, "r")
#     fout = open(outfile, "w")
#     lines = fin.readlines()

#     attri = lines[0].strip().split('\t')[:-1]
#     kind = lines[0].strip().split('\t')[-1]

#     lst = []
#     for a in lines[1:]:
#     	lst.append(a.strip().split('\t'))
#     nparray = np.array(lst)

# 	if (maxDepth == 0) or (decisionNode(nparray) == None):
# 		prediction = majorityVote(nparray[..., -1])


# lst = [[1,2,3],[4,5,6],[7,8,9]]
# lst = np.array(lst)
# lst = lst[...,1]
# print(lst)
print(mutualInformationCal([1,2,2,1,2], [1,2,2,1,1]))
