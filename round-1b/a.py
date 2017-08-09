def run(D,N,K,S):
  K,S = (list(t) for t in zip(*sorted(zip(K, S),reverse=True))) # result is small to large

  time = [(D-k)/s for k,s in zip(K,S)]

  t = time[0]
  for i in range(1,len(time)):
    if time[i] > t:
      t = time[i]

  # print(D)
  # print(N)
  # print(K)
  # print(S)
  # print(time)

  return D/t

T = int(input())  # read a line with a single integer
for i in range(1, T + 1):
  D, N = input().split()
  D = int(D)
  N = int(N)
  K = []
  S = []
  for j in range(1, N + 1):
    Ki, Si = input().split()
    K.append(int(Ki))
    S.append(int(Si))
  result = run(D,N,K,S)
  print("Case #{}: {}".format(i, result))
  # check out .format's specification for more formatting options