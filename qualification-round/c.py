import re
import math
import timeit

class TreeNode(object):
	Ls,Rs = -1,-1
	debug = False
	def __init__(self,spaces):
		self.left = None
		self.right = None
		self.empty_spaces = spaces
		self.max_spaces_left = -1
		self.max_spaces_right = -1

	def occupy(self):
		if TreeNode.debug:
			print('running occupy')
		self.left = TreeNode(math.floor(((self.empty_spaces-1)/2)))
		self.right = TreeNode(math.ceil(((self.empty_spaces-1)/2)))
		self.max_spaces_left = self.left.empty_spaces
		self.max_spaces_right = self.right.empty_spaces
		if TreeNode.debug:
			print(self.max_spaces_left, self.max_spaces_right)
		self.empty_spaces = -1
		TreeNode.Ls = self.max_spaces_left
		TreeNode.Rs = self.max_spaces_right
		if TreeNode.debug:
			print('Ls',TreeNode.Ls,'Rs',TreeNode.Rs)
		return max(self.max_spaces_left,self.max_spaces_right)

	def find(self):
		if TreeNode.debug:
			print('running find')
			self.print()
		if self.max_spaces_left == 1 and self.max_spaces_right == 1:
			TreeNode.Ls = 0
			TreeNode.Rs = 0
			return 0
		# reached a leaf node
		if self.max_spaces_left < 0 and self.max_spaces_right < 0:
			if TreeNode.debug:
				print('reached a leaf node')
			return self.occupy()
		# go right
		elif self.max_spaces_left < 0 or self.max_spaces_right > self.max_spaces_left:
			if TreeNode.debug:
				print('going right')
			self.max_spaces_right = self.right.find()
			return max(self.max_spaces_left,self.max_spaces_right)
		# go left
		elif self.max_spaces_right < 0 or self.max_spaces_right <= self.max_spaces_left:
			if TreeNode.debug:
				print('going left')
			self.max_spaces_left = self.left.find()
			return max(self.max_spaces_left,self.max_spaces_right)

	def print(self):
		print(TreeNode.Ls,TreeNode.Rs,self.left,self.right,self.empty_spaces,self.max_spaces_left,self.max_spaces_right)

def run2(n,k):
	# if k > n//2+1:
	# 	return 0,0
	root_node = TreeNode(n)
	# print(root_node.empty_spaces)
	for i in range(k):
		# print('person',i)
		root_node.find()
		# print('run2:',TreeNode.Ls,TreeNode.Rs)

	return max(TreeNode.Ls,TreeNode.Rs),min(TreeNode.Ls,TreeNode.Rs)

def run3(n,k):
	# if k > n//2+1:
	# 	return 0,0

	table = [0]*(n+1)
	table[n] = 1
	# index = n
	f,c = -1,-1
	for i in range(k):
		# m = max(table)
		index = max([i for i,j in enumerate(table) if j>0])
		if index == 3:
			if table[3] >= k-i:
				return 1,1
			elif table[3] + table[2] >= k-i:
				return 1,0
			else:
				return 0,0
		if index == 2:
			if table[index] >= k-i:
				return 1,0
			else:
				return 0,0
		table[index] = table[index]-1
		if table[index] == 0:
			table[index:] = []
		tmp = (index-1)/2
		f = math.floor(tmp)
		c = math.ceil(tmp)
		table[f] = table[f] + 1
		table[c] = table[c] + 1
		# index = max(table[index],table[f],table[c])

	return max(f,c),min(f,c)

def run4(n,k):
	# if k > n//2+1:
	# 	return 0,0

	# table = [0]*(n+1)
	table = {}
	table[0] = 0
	table[1] = 0
	table[2] = 0
	table[3] = 0
	table[n] = 1
	index = n
	f,c = -1,-1
	# for i in range(k):
	i = 0
	while i < k:
		remaining = k-i
		# print(i,k)
		# m = max(table)
		# index = max([i for i,j in table.items() if j>0])
		# print(len(table))
		if index in table:
			index = index
		elif index-1 in table:
			index = index - 1
		elif c+1 in table:
			index = c + 1
		else:
			index = c
			# print(table[index])
		if index == 3:
			if table[3] >= remaining:
				return 1,1
			elif table[3] + table[2] >= remaining:
				return 1,0
			else:
				# print('here')
				# for k,v in table.items():
				# 	print(k,v)
				return 0,0
		if index == 2:
			if table[index] >= remaining:
				return 1,0
			else:
				return 0,0
		# table[index] -= 1
		# if table[index] == 0:
			# table.pop(index)
		tmp = (index-1)/2
		f = math.floor(tmp)
		c = math.ceil(tmp)
		table.setdefault(f,0)
		table.setdefault(c,0)
		if table[index] >= remaining:
			break
		else:
			table[f] += table[index]
			table[c] += table[index]
			i += table[index]
			table.pop(index)


	return max(f,c),min(f,c)


def run(n,k):
	stalls = '1'+'0'*n+'1'
	# print(stalls)
	# print(matchObj.group(1))
	# for i in range(1,k+1):
	# set1 = {}
	# thres1 = 0
	# for i in range(1,k+1):
	# 	for j in range(n):
	# 		if stalls[j] ~= '0':
	# 			continue
	# 		tmp = list(stalls)
	# 		tmp[j] = '2'
	# 		tmp = ''.join(tmp)
	# 		print(tmp)
	# 		matchObj = re.search('(0*)2(0*)',tmp)
	# 		# print(matchObj.group(0))
	# 		Ls = len(matchObj.group(1))
	# 		Rs = len(matchObj.group(2))
	# 		if min(Ls,Rs) > thres1:
	# 			set1 = {}
	# 			set1[j] = [Ls,Rs]
	# 			thres1 = min(Ls,Rs)
	# 		elif min(Ls,Rs) == thres1:
	# 			set1[j] = [Ls,Rs]
	# 	if len(set1) == 1:
	# 		for k,v in set1.items():
	# 			tmp = list(stalls)
	# 			tmp[j] = '1'
	# 			stalls = ''.join(tmp)
	# 	else:
	# 		for k,v in set1.items():


	return n,k

start = timeit.default_timer()
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n, k = input().split()
  n = int(n)
  k = int(k)
  # a,b = run3(n,k)
  # print("Case #{}: {} {}".format(i, a, b))
  c,d = run4(n,k)
  print("Case #{}: {} {}".format(i, c, d))
  # print("Case #{}: {} {}".format(i, a-c, b-d))
  # check out .format's specification for more formatting options

stop = timeit.default_timer()
# print(stop - start)