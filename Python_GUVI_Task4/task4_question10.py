Ls = [4, 2, -3, 1, 6]
n = len(Ls)
for i in range(n):
    total = 0
    for j in range(i,n):
        total = total + Ls[j]
        if total == 0:
            print("Sub list with sum equal to Zero is found: ")
            print(Ls[i:j+1])
            exit()