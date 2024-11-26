# Part1
# Task1
def print_task1():
    print("“Don’t compare yourself with anyone in this world…")
    print("\tif you do so, you are insulting yourself.”")
    print("\t\t\t\tBill Gates")
print_task1()

#Task2
def display_numbers(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    even_numbers = [i for i in range(num1, num2 + 1) if i % 2 == 0]

    print("Even numbers between {} and {}:".format(num1, num2))
    print(even_numbers)
display_numbers(10, 20)

#Task3
def print_square(side_length, symbol, is_solid):
    if not isinstance(side_length, int) or side_length <= 0:
        raise ValueError("Side length must be a positive integer")

    if not isinstance(symbol, str) or len(symbol) != 1:
        raise ValueError("Symbol must be a single character")

    if not isinstance(is_solid, bool):
        raise ValueError("is_solid must be a boolean")
    # Print the square
    for i in range(side_length):
        for j in range(side_length):
            #solid square
            if is_solid:
                print(symbol, end=' ')
            #empty square
            else:
                if i == 0 or i == side_length - 1 or j == 0 or j == side_length - 1:
                    print(symbol, end=' ')
                else:
                    print(' ', end=' ')
        print()


print_square(5, '*', True)
print_square(5, '*', False)

#Task4
def find_smallest(a, b, c, d, e):
    return min(a, b, c, d, e)
print(find_smallest(1, 6, 9, 4, 2))  # Output: 5

#Task5
def product_of_range(start, end):
#swap
    if start > end:
        start, end = end, start
# Calculate product
    product = 1
    for i in range(start, end + 1):
        product *= i
    return product
print(product_of_range(1, 5))
print(product_of_range(5, 1))

#Task6
def count_digits(number):
    number_as_string = str(abs(number))
    digit_count = len(number_as_string)
    return digit_count
number = 3456
print(count_digits(number))

#Task7
def is_palindrome(number):
    number_as_string = str(abs(number))
    reversed_string = number_as_string[::-1]
    if number_as_string == reversed_string:
        return True
    else:
        return False
number = 123321
#True
print(is_palindrome(number))
number = 421987
#False
print(is_palindrome(number))


#Part2
#Task1
def product_of_elements(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product
numbers_list = [1, 2, 3, 4]
print(product_of_elements(numbers_list))

#Task2
def find_minimum(numbers):
    if len(numbers) == 0:
        return None

    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum
print(find_minimum([3, 1, 4, 1, 5]))

#Task3
def prime(k):
    if k <= 1:
        return False
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return True
def count_primes(numbers):
    prime_count = 0
    for num in numbers:
        if prime(num):
            prime_count += 1
    return prime_count
print(count_primes([2, 3, 4, 5, 6, 7]))

#Task4
def remove_number(numbers, target):
    removed_count = 0
    while target in numbers:
        numbers.remove(target)
        removed_count += 1
    return removed_count
numbers = [1, 2, 3, 2, 4, 2, 5]
print(remove_number(numbers,2))
print(numbers)

#Task5
def both_lists(list1, list2):
    return list1 + list2
list_a = [1, 2, 3]
list_b = [4, 5, 6]
both_list = both_lists(list_a, list_b)
print(both_list)