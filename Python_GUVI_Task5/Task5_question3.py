num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
is_even = lambda x: x%2==0
squares_of_even = [n**2 for n in num if is_even(n)]
print(squares_of_even)
