

def sum_of_numbers(*numbers):


    """To add all numbers provided in the function call."""
    result = 0
    for num in numbers:
        result += num
    print(result)


sum_of_numbers(100, 100, 100, 100, 100)