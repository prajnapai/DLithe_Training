Q = int(input())
S = ''
Operations = []
for _ in range(Q):
    ops = input()
    if ops[0] == '1':
        Operations.append(S)
        S += ops[2:]
    if ops[0] == '2':
        Operations.append(S)
        ind = int(ops[2:])
        S = S[:len(S)-ind]
    if ops[0] == '3':
        ind = int(ops[2:])
        print(S[ind-1])
    if ops[0] == '4':
        S = Operations.pop()