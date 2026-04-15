Ls = [10,20,50,66,89,20,50,10]
minimum_vale = Ls[0]
for x in Ls:
    if x<minimum_vale:
        minimum_vale=x
        break
print("the minimum value is: ",minimum_vale)