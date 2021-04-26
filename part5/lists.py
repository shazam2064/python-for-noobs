# list1 = [1, 2, 3, 4, 5, "JOTARO"]
# # l = list(1, 2, 3, 4, 5)
# list1[6] = "Polnareff"
# print(list1[6])

# list1 = [1, 2, 3, 4, 5, "JOTARO", ['a', 'b', 'c']]
# # l = list(1, 2, 3, 4, 5)
# list1.append("Star Platinum")
# print(list1)

list1 = [1, 2, 3, 4, 5, "JOTARO", ['a', 'b', 'c']]
list1.extend(("Star Platinum", "Silver Chariot"))
print(list1[6])
