with open("d03/test.txt", "r") as f:
    data = f.read().splitlines()
    data = [[int(digit) for digit in str(num)] for num in data]

total = 0

for num in data:
    max1 = max(num[:-1])
    index = num.index(max1)
    num.remove(max1)

    max2 = max(num[index:])
    total += int(str(max1) + str(max2))

print(total)
