import math

def run(N,R,O,Y,G,B,V):
  # print(N,R,O,Y,G,B,V)

  n = math.floor(N/2)
  if R > n or O > n or Y > n or G > n or B > n or V > n:
    return 'IMPOSSIBLE'

  if O > 0 and O == B and O+B == N:
    return 'OB'*(n)
  if O > 0 and O == B and O+B < N:
    return 'IMPOSSIBLE'
  if O > 0 and O+1 > B:
    return 'IMPOSSIBLE'

  if G > 0 and G == R and G+R == N:
    return 'GR'*(n)
  if G > 0 and G == R and G+R < N:
    return 'IMPOSSIBLE'
  if G > 0 and G+1 > R:
    return 'IMPOSSIBLE'

  if V > 0 and V == Y and V+Y == N:
    return 'VY'*(n)
  if V > 0 and V == Y and V+Y < N:
    return 'IMPOSSIBLE'
  if V > 0 and V+1 > Y:
    return 'IMPOSSIBLE'

  result = []

  secondary = ''
  if G > 0:
    secondary = secondary + 'RG'*G + 'R'
    R = R - (G+1)
  if O > 0:
    secondary = secondary + 'BO'*O + 'B'
    B = B - (O+1)
  if V > 0:
    secondary = secondary + 'YV'*V + 'Y'
    Y = Y - (V+1)

  primary = 'R'*R + 'Y'*Y + 'B'*B
  # print(primary)
  for i in range(1,len(primary)):
    if primary[i] == primary[i-1]:
      for j in range(i+1,len(primary)):
        if primary[j] != primary[i]:
          tmp = list(primary)
          tmp[i],tmp[j] = tmp[j],tmp[i]
          primary = ''.join(tmp)
          break
  primary=primary[::-1]
  for i in range(1,len(primary)):
    if primary[i] == primary[i-1]:
      for j in range(i+1,len(primary)):
        if primary[j] != primary[i]:
          tmp = list(primary)
          tmp[i],tmp[j] = tmp[j],tmp[i]
          primary = ''.join(tmp)
          break
  # print(primary)
  return secondary+primary


T = int(input())  # read a line with a single integer
for i in range(1, T + 1):
  N,R,O,Y,G,B,V = input().split()
  N = int(N)
  R = int(R)
  O = int(O)
  Y = int(Y)
  G = int(G)
  B = int(B)
  V = int(V)
  result = run(N,R,O,Y,G,B,V)
  print("Case #{}: {}".format(i, result))
  # check out .format's specification for more formatting options