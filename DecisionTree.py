from __future__ import print_function
import numpy as np
import sys
import math
import inspect

class Node:
	def __init__(self, attri, leftBranch, rightBranch, depth, datay, dataa, classy):
		self.left = leftBranch
		self.right = rightBranch
		self.label = attri
		self.depth = depth
		self.datay = datay
		self.dataa = dataa
		self.classy = classy

class Leaf:
	def __init__(self, nparray):
		self.decison = majorityVote(nparray[..., -1])


def printInorder(root):
	if root:
		printInorder(root.left)
		print(root.label, end = '\t')
		printInorder(root.right)

def printPostorder(root):
	if root:
		printPostorder(root.left)
		printPostorder(root.right)
		print(root.label, end = '\t')

def countY(lstY, classy):
	comp1 = lstY[0]
	cnt1 = 0
	cnt2 = 0
	for ele in lstY:
		if ele == comp1:
			cnt1 += 1
		else:
			comp2 = ele
			cnt2 += 1
	if cnt2 == 0:
		copy = classy.copy()
		copy.remove(comp1)
		comp2 = copy[0]
	return [cnt1, comp1, cnt2, comp2]

def printPreorder(root):
	if (root) and (not isinstance(root, Leaf)):
		for a in range(len(root.dataa)):
			print(root.depth * '|\t', end = ' ')
			print(root.label, end = ' = ')
			print(root.dataa[a], end = ': [')
			data = countY(root.datay[a], root.classy)
			print(data[0], end = ' ')
			print(data[1], end = '/')
			print(data[2], end = ' ')
			print(data[3], end = ']\n')
			# print(root.datay[a]., end = ' ')
			# print(root.datal, end = ' ')
			# print(root.datar, end = '\n')
			if a == 0:
				printPreorder(root.left)
			else:
				printPreorder(root.right)

def majorityVote(lstY):
	comp1 = lstY[0]
	cnt1 = 0
	cnt2 = 0
	for ele in lstY:
		if ele == comp1:
			cnt1 += 1
		else:
			comp2 = ele
			cnt2 += 1

	if cnt1 >= cnt2:
		return comp1
	else:
		return comp2



def decisionNode(nparray):
	length = nparray.shape[1]
	mi = []
	for i in range(length - 1):
		mi.append(mutualInformationCal(nparray[..., -1], nparray[..., i]))

	if mi == []:
		return None
	temp = mi.copy()

	mi.sort()


	if mi[-1] > 0:
		decision_index = temp.index(mi[-1])

		return decision_index
	return None

def partitionArray(nparray, attriIndex, attri):
	comp = nparray[..., attriIndex][0]
	indexTrue = []
	indexFalse = []

	trueRows = []
	falseRows = []
	for i in range(len(nparray[..., attriIndex])):
		if nparray[..., attriIndex][i]== comp:
			indexTrue.append(i)
		else:
			indexFalse.append(i)
	for a in indexTrue:
		trueRows.append(nparray[a])
	for b in indexFalse:
		falseRows.append(nparray[b])
	trueRows = np.array(trueRows)
	falseRows = np.array(falseRows)
	trueRows = np.delete(trueRows, attriIndex, axis = 1)
	falseRows = np.delete(falseRows, attriIndex, axis = 1)
	newattri = attri.copy()
	newattri.pop(attriIndex)
	return [trueRows, falseRows, newattri]

def buildTree(nparray, maxDepth, attri, classy, depth):
	if maxDepth < 1:
		return None
	attriIndex = decisionNode(nparray)
	if (attriIndex is not None) and (depth < maxDepth):
		depth += 1
		leftRows, rightRows, newattri= partitionArray(nparray, attriIndex, attri)
		# print(newattri, end = '\n')
		# print(leftRows, end = '\n')
		# print(rightRows, end = '\n')
		leftBranch = buildTree(leftRows, maxDepth, newattri, classy, depth)
		rightBranch = buildTree(rightRows, maxDepth, newattri, classy, depth)
		datay = [leftRows[..., -1], rightRows[..., -1]]
		
		for ele in nparray[..., attriIndex]:
			comp = nparray[..., attriIndex][0]
			if ele != comp:
				dataa = [comp, ele]
				break
			else:
				dataa = [comp]

		return Node(attri[attriIndex], leftBranch, rightBranch, depth, datay, dataa, classy)
	return Leaf(nparray)






# def testProcess(infile, outfile):

def entropyCal(lst):
	if len(lst) == 0:
		return 0
	pos = 0
	neg = 0
	comp = lst[0]
	for x in lst:
		if x == comp:
			pos += 1
		else:
			neg += 1

	if neg == 0:
		return 0

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

def classifyRow(row, root, attri):
	if isinstance(root, Leaf):
		return root.decison

	check = attri.index(root.label)
	if row[check] == root.dataa[0]:
		return classifyRow(row, root.left, attri)
	else:
		return classifyRow(row, root.right, attri)


def makeDecision(nparray, root, attri):
	lines = []
	if root is None:
		decison = majorityVote(nparray[..., -1])
		for i in range(shape(nparray)[1]):
			lines.append(decision)
			return lines

	for line in nparray:
		lines.append(classifyRow(line[:-1], root, attri))
	return lines

def train(inp, outp, maxDepth):
	fin = open(inp, "r")
	fout = open(outp, "w")
	lines = fin.readlines()

	attri = lines[0].strip().split('\t')

	lst = []
	for a in lines[1:]:
		lst.append(a.strip().split('\t'))
	nparray = np.array(lst)

	trainOrigin = nparray[..., -1]

	classy = list(set(nparray[..., -1]))
	root = buildTree(nparray, maxDepth, attri, classy, depth = 0)

	trainLines = makeDecision(nparray, root, attri)
	for a in trainLines:
		fout.writelines(a + '\n')

	fin.close()
	fout.close()

	return [root, trainLines, trainOrigin]

def test(inp, outp, decisionTree):
	fin = open(inp, "r")
	fout = open(outp, "w")
	lines = fin.readlines()

	attri = lines[0].strip().split('\t')

	lst = []
	for a in lines[1:]:
		lst.append(a.strip().split('\t'))
	nparray = np.array(lst)

	testOrigin = nparray[..., -1]

	testLines = makeDecision(nparray, decisionTree, attri)
	for a in testLines:
		fout.writelines(a + '\n')

	fin.close()
	fout.close()
	return [testLines, testOrigin]

def metrics(outp, trainLines, trainOrigin, testLines, testOrigin):
	fout = open(outp, "w")
	lengthTrain = len(trainLines)
	lenthTest = len(testLines)
	errorTrain = 0
	errorTest = 0
	for x in range(lengthTrain):
		if trainLines[x] != trainOrigin[x]:
			errorTrain += 1
	for y in range(lenthTest):
		if testLines[y] != testOrigin[y]:
			errorTest += 1

	rateTrain = errorTrain / lengthTrain
	rateTest = errorTest / lenthTest
	fout.writelines('error(train): ' + str(rateTrain) + '\n' + 'error(test): ' + str(rateTest))
	fout.close()


if __name__ == "__main__":

	trainInput = sys.argv[1]
	testInput = sys.argv[2]
	maxDepth = int(sys.argv[3])

	trainOut = sys.argv[4]
	testOut = sys.argv[5]
	metricsOut = sys.argv[6]

	decisionTree, trainLines, trainOrigin = train(trainInput, trainOut, maxDepth)
	testLines, testOrigin = test(testInput, testOut, decisionTree)
	metrics(metricsOut, trainLines, trainOrigin, testLines, testOrigin)

	print('\n')
	printPreorder(decisionTree)
