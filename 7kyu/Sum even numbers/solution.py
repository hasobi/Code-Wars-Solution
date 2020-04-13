def sum_even_numbers(seq): 
    # your code here
    num = 0
    for i in seq:
        if i%2==0:
            num += i
    return num
