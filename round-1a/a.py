# def above

import copy

def run(cake_in):
	rows = len(cake_in)
	cols = len(cake_in[0])
	# cake_flat = [elem for row in cake_in for elem in row]
	print('cake_in')
	for item in cake_in:
		print(item)

	cake_out = copy.deepcopy(cake_in)
	for i in range(rows):
		for j in range(cols):
			# print(i,j)
			if cake_in[i][j] != '?': # contains a letter
				# print('found a letter')
				# go right
				m = j + 1
				while m < cols:
					if cake_out[i][m] == '?':
						cake_out[i][m] = []
					if type(cake_out[i][m]) == list:
						cake_out[i][m].append(cake_in[i][j])
						m += 1
					else:
						break
				# go left
				m = j - 1
				while m >= 0:
					if cake_out[i][m] == '?':
						cake_out[i][m] = []
					if type(cake_out[i][m]) == list:
						cake_out[i][m].append(cake_in[i][j])
						m -= 1
					else:
						break
				# go down
				m = i + 1
				while m < rows:
					if cake_out[m][j] == '?':
						cake_out[m][j] = []
					if type(cake_out[m][j]) == list:
						cake_out[m][j].append(cake_in[i][j])
						m += 1
					else:
						break
				# go up
				m = i - 1
				while m >= 0:
					if cake_out[m][j] == '?':
						cake_out[m][j] = []
					if type(cake_out[m][j]) == list:
						cake_out[m][j].append(cake_in[i][j])
						m -= 1
					else:
						break

				# for m in range(rows):
				# 	# print(m,j,cake_in[m][j])
				# 	if cake_out[m][j] == '?':
				# 		cake_out[m][j] = []
				# 	# print(m,j,cake_out[m][j],type(cake_out[m][j]))
				# 	if type(cake_out[m][j]) == list:
				# 		cake_out[m][j].append(cake_in[i][j])
				# 	# print(m,cake_out)
				# for n in range(cols):
				# 	if cake_out[i][n] == '?':
				# 		cake_out[i][n] = []
				# 	if type(cake_out[i][n]) == list:
				# 		cake_out[i][n].append(cake_in[i][j])
				# 	# print(n,cake_out)
	print('cake_out')
	for item in cake_out:
		print(item)

	indexes = {}
	for i in range(rows):
		for j in range(cols):
			if type(cake_out[i][j]) == list:
				key = ','.join(str(x) for x in [i,j])
				indexes.setdefault(key,0)
				indexes[key] = len(cake_out[i][j])
	index_sorted = sorted(indexes,key=indexes.get)

	while len(index_sorted) > 0:
		print('iterate')
		print(index_sorted)
		ind = index_sorted[0]
		if indexes[ind] == 1:
			i,j = ind.split(',')
			i = int(i)
			j = int(j)
			cake_out[i][j] = ''.join(cake_out[i][j])
			for ind2 in index_sorted:
				if ind == ind2:
					continue
				else:
					m,n = ind2.split(',')
					m = int(m)
					n = int(n)
					try:
						cake_out[m][n].remove(cake_out[i][j])
					except ValueError:
						0
					indexes[ind2] -= 1
					if indexes[ind2] == 0:
						indexes.pop(ind2)
			indexes.pop(ind)
			index_sorted = sorted(indexes,key=indexes.get)
		else:
			i,j = ind.split(',')
			i = int(i)
			j = int(j)
			cake_out[i][j] = ''.join(cake_out[i][j][0])
			# print(cake_out[i][j])
			for ind2 in index_sorted:
				if ind == ind2:
					continue
				else:
					# print(ind2)
					m,n = ind2.split(',')
					m = int(m)
					n = int(n)
					try:
						cake_out[m][n].remove(cake_out[i][j])
					except ValueError:
						0
					indexes[ind2] -= 1
					if indexes[ind2] == 0:
						indexes.pop(ind2)
			indexes.pop(ind)
			index_sorted = sorted(indexes,key=indexes.get)
		for item in cake_out:
			print(item)






	# for i in range(rows):
	# 	for j in range(cols):
	# 		if type(cake_out[i][j]) == list:
	# 			if len(cake_out[i][j]) == 1:
	# 				cake_out[i][j] = ''.join(cake_out[i][j])
	# 				for m in range(rows):
	# 					for n in range(cols):
	# 						if type(cake_out[m][n]) == list:
	# 							if cake_out[i][j] in cake_out[m][n]:
	# 								cake_out[m][n].remove(cake_out[i][j])
	# 			else:

	return cake_out


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  r, c = input().split()
  r = int(r)
  c = int(c)
  cake = []
  for j in range(r):
  	cake.append(list(input()))
  result = run(cake)
  print("Case #{}:".format(i))
  for m in range(r):
  	print(result[m])
  	# print(''.join(result[m]))
  # check out .format's specification for more formatting options