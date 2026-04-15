Ls = [10,20,30,9]
target_sum = 59
n = len(Ls)
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if Ls[i]+Ls[j]+Ls[k] == target_sum:
                print("Triplet sum is found: ", Ls[i],",",Ls[j],",",Ls[k])
                print("total sum",target_sum)
            