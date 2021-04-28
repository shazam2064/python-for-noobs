# n = int(input("Enter n: "))
# list1 = []
#
# for i in range(0, n):
#     val = int(input("Enter element: "))
#     list1.append(val)
# print(list1)

n = int(input("Enter n: "))
list1 = [int(input("Enter element: ")) for i in range(0, n)]
print(list1)
