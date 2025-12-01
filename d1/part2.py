password = 0
state = 50

with open("d1/data.txt", "r") as data:
    while True:
        line = data.readline().strip()
        if not line:
            break

        part = [line[0], int(line[1:].strip())]

        if part[0] == "L":
            while part[1] > 99:
                part[1] -= 100
                password += 1
            if state < part[1] and state != 0:
                part[1] -= 100
                password += 1
            elif state < part[1]:
                part[1] -= 100
            state -= part[1]
        elif part[0] == "R":
            state += part[1]

        while state > 199:
            state -= 100
            password += 1

        if state > 99 and state <= 199:
            state -= 100
            password += 1

        elif state == 0:
            password += 1
    print(password)