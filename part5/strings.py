# s = "Hello"
# print(s)
# print(s[0])
# print(s[-2])

# s = "*Sad "
# s1 = "Ora"
# s2 = " Noises*"
# s3 = s + s1 + s2  # s3 = "*Sad " + "Ora" + " Noises*"
# s4 = s3 * 3  # 3 * s2
#
# print(s3)

# s = "*Sad Ora Noises*"
#
# if "Ora" in s:
#     print("It's Star Platinum")
# else:
#     print("It's not Star Platinum")

# if "Polnareff" < "Iggy":
#     print("Smaller")
# else:
#     print("Bigger")

# if "Jotaro" != "jotaro":
#     print("yes")
# else:
#     print("no")

# s = "*Sad Ora Noises*"
# s1 = s[1:4]
# s2 = s[-4:-1]
# print(s1)
# print(s2)

# s = "*Sad Ora Noises*"
# s1 = s[:]
# print(s1)

# s = "*Sad Ora Noises*"
# s1 = s[0:5:3]
# print(s1)

# s = "*Sad Ora Noises*"
# s1 = s[::-1]
# print(s1)

# s = "jotaro"
# print(s.capitalize())

# s = input("Enter string: ")
# for i in range(0, len(s)):
#     print(s[i])

s = input("Enter string: ")
ncount = 0
acount = 0
scount = 0

for ch in s:
    if ch.isdigit():
        ncount = ncount + 1
    elif ch.isalpha():
        acount = acount + 1
    elif ch.isspace():
        scount = scount + 1
    else:
        continue

print(ncount)
print(acount)
print(scount)
