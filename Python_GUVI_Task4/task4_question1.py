Ls = [10,501,22,37,100,999,87,351]
Even_list = []
Odd_list = []
for num in Ls:
    if num%2 == 0:
        Even_list.append(num)
    else:
        Odd_list.append(num)
print("Even Numbers:",Even_list)
print("Odd Numbers:",Odd_list)

