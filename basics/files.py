"""
Python Files
"""

# with open("./files/test_read.csv", mode="r") as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line)

#     try:
#         f.write("trying to write")
#     except Exception as e:
#         print("Error:", e)


# with open("./files/test_write.csv", mode="w") as f:
#     f.write("Line 1")
#     f.write("\n")
#     f.write("Line 2")

#     try:
#         f.readlines()
#     except Exception as e:
#         print("Error:", e)


"""
1,2,3,4,5
6,7,8,9,10
11,12,13,14,15
16,17,18,19,20
"""


# numbers = []
# with open("./files/test_readwrite.csv", mode="r") as f:
#     lines = f.readlines()
#     for line in lines:
#         numbers.append(line.split(","))


# new_numbers = []
# for num in numbers:
#     l_num = [int(n)**2 for n in num]
#     new_numbers.append(l_num)


# with open("./files/test_readwrite.csv", mode="w") as f:
#     for num in new_numbers:
#         i = 0
#         for n in num:
#             if i:
#                 f.write(",")
#             f.write(str(n))
#             i = 1
#         f.write("\n")
