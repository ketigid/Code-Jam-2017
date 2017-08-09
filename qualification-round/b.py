def isTidy(x):
	tmp = x % 10
	x = x // 10
	while x > 0:
		tmp2 = x % 10
		if tmp2 > tmp:
			return False
		else:
			tmp = tmp2
			x = x // 10
	return True

def findLargestTidy(x):
	while x > 0:
		if isTidy(x):
			return x
		else:
			x = x - 1

def isGEXXX(x):
	x_str = str(x)
	for i in range(1,len(x_str)):
		x_str = list(x_str)
		x_str[i] = x_str[0]
		x_str = ''.join(x_str)
	x_new = int(x_str)
	return x >= x_new

def findFast(x):
	if isTidy(x):
		return x

	x_str = str(x)
	x_out = x_str
	numof_digits = len(x_str)

	if x_str[0] == '1' and not isGEXXX(int(x_str)):
		x_out = list(x_out)
		x_out[0] = '0'
		for i in range(1,numof_digits):
			x_out[i] = '9'
		x_out = ''.join(x_out)
		return int(x_out)

	largest_sofar = int(x_str[0])
	for i in range(numof_digits):
		x_out = list(x_out)
		if isGEXXX(int(x_str[i:])):
			x_out[i] = x_str[i]
			x_out = ''.join(x_out)
			# print(x_out)
		else:
			x_out[i] = str(int(x_str[i])-1)
			for j in range(i+1,numof_digits):
				x_out[j] = '9'
			x_out = ''.join(x_out)
			# print(x_out)
			return int(x_out)

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n = int(input())
  # print("Case #{}: {}".format(i, findLargestTidy(n)))
  print("Case #{}: {}".format(i, findFast(n)))
  # check out .format's specification for more formatting options

