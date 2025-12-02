password = 0

with open("d02/data.txt", "r") as data:
    id = data.read().split(",")
    id = [[int(element) for element in word.split("-")] for word in id]

for word in id:
    for num in range(word[0], word[1] + 1):
        currentID = str(num)
        mid = int(len(currentID) / 2 - 1)
        part = [currentID[:mid+1], currentID[mid+1:]]
        
        if part[0] == part[1]:
            password += int(str(part[0]) * 2)

print(password)