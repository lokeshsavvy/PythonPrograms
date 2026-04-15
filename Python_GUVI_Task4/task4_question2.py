def is_prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True
Ls = [10,501,22,37,100,999,87,351]
prime_list = []
for n in Ls:
    if is_prime(n):
        prime_list.append(n)
print("prime numbers:",prime_list)
print("total count: ",len(prime_list))