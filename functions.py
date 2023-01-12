"""
Python Functions
"""

# def function():
#     print("This is a function.")

# function()

# def str_split_counter(string):
#     s = string.split(",")
    
#     l = len(s)
    
#     return l

# string1 = "This, is, a, string, separated, by, commas"

# len1 = str_split_counter(string1)

# print(len1)


# def sum_lists(listA, listB):
#     listC = []
    
#     if len(listA) != len(listB):
#         print("Prints do not have the same size")
#         return listC

#     for i in range(len(listA)):
#         c = listA[i] + listB[i]
#         listC += [c]

#     return listC

# la = [1, 2, 3, 4, 5, 6]
# lb = [7, 8, 9, 10, 11, 12]

# lc = sum_lists(la, lb)

# print(lc)
# print()

# def sum_lists_2(listA, listB):
#     if len(listA) != len(listB):
#         print("Prints do not have the same size")
#         return []
    
#     return [listA[i] + listB[i] for i in range(len(listA))]

# lc = sum_lists_2(la, lb)

# print(lc)
# print()

# def func(arg: float = 2.5) -> float:
#     return int(arg)

# print(func(1.5))
# print(func())