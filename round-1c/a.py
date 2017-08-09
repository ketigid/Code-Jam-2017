import math

def top(radius):
  return math.pi * radius * radius

def side(radius, height):
  # print(radius,height)
  return 2 * math.pi * radius * height

def run(N,K,R,H):
  # print(N)
  # print(K)
  # print(R)
  # print(H)
  T = [top(r) for r in R]
  S = [side(r,h) for r,h in zip(R,H)]
  # print(T)
  # print(S)
  # print(T)
  # print(S)
  result = 0
  for i in range(N):
    # print('i',i)
    tmp = T[i] + S[i]
    S2 = S[:]
    T2 = T[:]
    S2.pop(i)
    T2.pop(i)
    if len(T2) > 0:
      S2,T2 = (list(t) for t in zip(*sorted(zip(S2,T2),reverse=True))) # result is large to small
    for j in range(K-1):
      # print('j',j)
      tmp += S2[j]
    if tmp > result:
      result = tmp
  return result

T = int(input())  # read a line with a single integer
for i in range(1, T + 1):
  N, K = input().split()
  N = int(N)
  K = int(K)
  R = []
  H = []
  for j in range(1, N + 1):
    Ri, Hi = input().split()
    R.append(int(Ri))
    H.append(int(Hi))
  result = run(N,K,R,H)
  print("Case #{}: {}".format(i, result))
  # check out .format's specification for more formatting options