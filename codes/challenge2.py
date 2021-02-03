numbers = 0
valid = 0
numips = list()

numbers = int(input("Enter the number of numbers: "))
for i in range(numbers):
    numips.append((input('')))

# # to be cleared
# numbers = 5
# numips = ['172.16']

num = ""
j = 0
m = 0


# ip -> num[(.num)3]?
# num ->[0-255]

for numip in numips:
    # checking for num
    if numip == 0 or numip[0] == '.':
        continue
    if numip[-1] != '.':
        numip = numip + "."
    else:
        continue
    num = ""
    j = 0
    # while j < len(numip) and j < 4 and numip[j] != '.':
    #     num += numip[j]
    #     j += 1

    # # num is okay and we didn't check more than the required
    # if j == 4 or not (0 <= int(num) <= 255):
    #     continue

    # # num exists by itself
    # if len(numip) == j:
    #     valid += 1
    #     continue

    j += 1

    for m in range(3):
        num = ""
        l = 0
        while j < len(numip) and l < 4 and numip[j] != '.':
            num += numip[j]
            l += 1
            j +=1

        if num == '':
            break

        if l == 4 or not (0 <= int(num) <= 255):
            continue

        if (len(numip)<= j):
            valid += 1
            break

        j += 1  # skip the .

    # if we reach here, the address is invalid
print("Valid:", valid)
