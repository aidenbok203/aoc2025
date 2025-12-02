password = 0

with open("d02/data.txt", "r") as data:
    id = data.read().split(",")
    id = [[int(element) for element in word.split("-")] for word in id]

for word in id:
    for num in range(word[0], word[1] + 1):
        currentID = str(num)
        if currentID in (currentID * 2)[1:-1]:
            password += num

print(password)