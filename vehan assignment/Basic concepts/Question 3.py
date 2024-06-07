def sum_of_squares(lst):
    sum_squares = 0
    for i in lst:
        sum_squares += i ** 2
    return sum_squares

print(sum_of_squares([1, 2, 3, 4]))