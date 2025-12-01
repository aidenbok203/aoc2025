password = 0
state = 50

with open("d1/data.txt", "r") as data:
    while True:
        line = data.readline().strip()
        if not line:
            break

        part = [line[0], int(line[1:].strip())%100]

        if part[0] == "L":
            if state < part[1]:
                part[1] -= 100
            state -= part[1]
        elif part[0] == "R":
            state += part[1]

        state = state % 100

        if state == 0:
            password += 1
    print(password)