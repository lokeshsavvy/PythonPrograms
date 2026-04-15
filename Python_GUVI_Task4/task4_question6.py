Ls1 = [10,20,50,66,89,100,143]
Ls2 = [23,69,143,66,58,20,102]
Ls3 = [100,20,650,69,143]
Duplicates = []
for item in Ls1:
    if item in Ls2 and item in Ls3:
        if item not in Duplicates:
            Duplicates.append(item)
print("Duplicates in 3 lists: ", Duplicates)