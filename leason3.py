"""
This script demonstrates the use of a list comprehension to filter elements from a list based on a specified condition.

The script processes a list of names and creates a new list containing only the names that have more than three characters.

Variables:
    names (list): A list of names to be filtered.
    new_names (list): A new list containing names from the original list that have more than three characters.

    new_names = [n for n in names if len(n) > 3]
    # new_names will be ['Alice', 'Charlie', 'David']
This function uses a list comprehension to generate a list of elements based on a specified condition or transformation.

Returns:
    list: A new list containing the transformed or filtered elements.

Example:
    # Example of a list comprehension that squares each number in the input list
    input_list = [1, 2, 3, 4]
    output_list = [x**2 for x in input_list]
    # output_list will be [1, 4, 9, 16]
"""
names = ['Alice', 'Bob', 'Charlie', 'David']
new_names =[n for n in names if len(n) > 3]
print(new_names)

names = ['Alice', 'Bob', 'Charlie', 'David']
new_names = {n:len(n) for n in names if len(n) > 3}
print(new_names)

numbers = [1, 2, 3, 4]
squared_numbers = {x:x**2 for x in numbers if x % 2 == 0}
print(squared_numbers)

numbers = [1, 2, 3, 4, -2]
squared_numbers = {x**2 for x in numbers}
print(squared_numbers)

string = 'helloajsjhuejnc'
new_set ={n for n in string if n  not in 'aeiou'}
print(new_set)

a = (x for x in range(1,10))
print(tuple(a))

x = b"10"
print(x)

x2 = b"test"
print(x2)


x3= bytes("hello", encoding="utf-8")
x4 = x3[1:3]
print(x4)

z = x2+x4
print(z)