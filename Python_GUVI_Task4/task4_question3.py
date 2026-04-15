Ls = [10,501,22,37,100,999,87,351]
Happy_list = []
for n in Ls:
    temp = n
    past_numbers = []
    while temp !=1 and temp not in past_numbers:
        past_numbers.append(temp)
        total = 0
        for digit in str(temp):
            total += int(digit)**2
            temp = total
    if temp ==1:
        Happy_list.append(n)
print("Happy Numbers :",Happy_list)
print("count of happy numbers",len(Happy_list))