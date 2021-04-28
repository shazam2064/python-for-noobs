# n = int(input("Enter n: "))
# list1 = []
#
# for i in range(0, n):
#     val = int(input("Enter element: "))
#     list1.append(val)
# print(list1)

# n = int(input("Enter n: "))
# list1 = [int(input("Enter element: ")) for i in range(0, n)]
# print(list1)

# n = int(input("Enter n: "))
# list1 = [int(input("Enter element: ")) for i in range(0, n)]
# print(list1)
# for ele in list1:
#     print(ele)

def linesearch(k, lst):
    for val in lst:
        if k == val:
            return True
    else:
        return False


n = int(input("Enter n: "))
list1 = [int(input("Enter element: ")) for i in range(0, n)]
key = int(input("Enter key: "))
res = linesearch(key, list1)
print(res)
