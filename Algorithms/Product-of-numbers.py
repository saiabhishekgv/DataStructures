'''
Question :
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Do not use division in your solution.You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
'''

'''
Solution :

Brute Force : 
        A brute force approach would use two loops to multiply the integer at every index by the integer at every nested_index, unless index == nested_index.

Time Complexity : O(n^2)

Greedy : 
    - Create a output list.
    - For each iteration in given input list : 
        - Get the product before the index and put it in output list
    - For each iteration in given input list (Reverse Order) : 
        - Get the product after the index and put it in output list
    - return list    
Time Complexity : O(n)
Space Complexity : O(1)
'''

def productOfNumbers(list_of_numbers):
    '''
    :param list_of_numbers: list of numbers like [1,4,6,9]
    :return: list with product of all number except at index i.
    '''
    if len(list_of_numbers) < 2:
        raise IndexError("Length of input list is atleast 2")

    l = len(list_of_numbers)
    product_of_numbers = [None]*l

    left_product = list_of_numbers[0]
    for i in xrange(1,l):
        product_of_numbers[i] = left_product
        left_product = left_product * list_of_numbers[i]

    left_product = list_of_numbers[l-1]
    for i in xrange(l-2, -1, -1):
        product_of_numbers[i] = product_of_numbers[i]*left_product if product_of_numbers[i]!=None else left_product
        left_product = left_product * list_of_numbers[i]

    return product_of_numbers

print productOfNumbers([1,4,6,9])