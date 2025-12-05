with open("d05/data.txt", "r") as f:
    data = f.read().splitlines()

split = data.index("")
ranges = data[:split]
values = data[split + 1:]

fresh = 0

ranges = [[int(num) for num in bounds.split("-")] for bounds in ranges]
values = [int(num) for num in values]

for lb, ub in ranges:
    for num in list(values):
        if lb <= num <= ub:
            values.remove(num)
            fresh += 1

print(fresh)