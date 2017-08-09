def run(Ac,Aj,C,D,J,K):
  # print(Ac)
  # print(Aj)
  # print(C)
  # print(D)
  # print(J)
  # print(K)
  schedule = list('X'*1440) # Extra char at the end to check for crossover
  for i in range(len(C)):
    schedule[C[i]:D[i]] = list('J'*(D[i]-C[i])) # Jamie does the job while Cameron is away
  for i in range(len(J)):
    schedule[J[i]:K[i]] = list('C'*(K[i]-J[i])) # Cameron does the job while Jamie is away
  # schedule[1440] = schedule[1439]
  X = C + J
  Y = D + K
  X,Y = (list(t) for t in zip(*sorted(zip(X,Y),reverse=False))) # result is large to small
  # print(schedule)
  print(X)
  print(Y)
  gaps = []
  state = []
  count = 0
  head,tail = '',''
  for i in range(len(schedule)):
    if schedule[i] == 'X':
      count += 1
    else:
      if count == 0: # counting non 'X'
        if i == 0:
          gaps.append(0)
          state.append(schedule[i])
          head = schedule[i]
        else:
          head = schedule[i]
      else:
        gaps.append(count)
        tail = schedule[i]
        state.append(head+tail)
        count = 0 # reset count
        head = schedule[i]
  gaps.append(count)
  state.append(head)
  gaps.append(gaps.pop(len(gaps)-1)+gaps.pop(0))
  state.append(state.pop(len(state)-1)+state.pop(0))

  gaps,state = (list(t) for t in zip(*sorted(zip(gaps,state),reverse=False))) # result is large to small

  rC,rJ = 720,720
  for i in range(len(gaps)):
    if state[i] == 'CC' and rC >= gaps[i]:
      rC -= gaps[i]
      gaps[i] = 0
    elif state[i] == 'JJ' and rJ >= gaps[i]:
      rJ -= gaps[i]
      gaps[i] = 0

  result = 0
  for i in range(len(gaps)):
    if gaps[i] > 0:
      result += 1

  print(gaps)
  print(state)


  # print(schedule)

  return result


T = int(input())  # read a line with a single integer
for i in range(1, T + 1):
  Ac, Aj = input().split()
  Ac = int(Ac)
  Aj = int(Aj)
  C = []
  D = []
  J = []
  K = []
  for j in range(Ac):
    Ci, Di = input().split()
    C.append(int(Ci))
    D.append(int(Di))
  for j in range(Aj):
    Ji, Ki = input().split()
    J.append(int(Ji))
    K.append(int(Ki))
  result = run(Ac,Aj,C,D,J,K)
  print("Case #{}: {}".format(i, result))
  # check out .format's specification for more formatting options