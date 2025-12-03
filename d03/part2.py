with open("d03/data.txt", "r") as f:
    data = f.read().splitlines()
    data = [[int(digit) for digit in str(num)] for num in data]

total = 0

for num in data:
    index = 0
    jolt = []
    for i in range(12):
        remaining = 11 - i
        if remaining == 0:
            max1 = max(num[index:])
        else:
            max1 = max(num[index:-remaining])
        index = num.index(max1, index)
        jolt.append(str(max1))
        index += 1
    total += int("".join(jolt))

print(total)
