with open("d05/data.txt", "r") as f:
    data = f.read().splitlines()

split = data.index("")
ranges = data[:split]
count = 0

ranges = [[int(num) for num in bounds.split("-")] for bounds in ranges]
ranges.sort()

merged = [ranges[0]]

for lb, ub in ranges[1:]:
    last = merged[-1]

    if lb <= last[1]:
        last[1] = max(last[1], ub)

    else:
        merged.append([lb, ub])
    

for lb, ub in merged:
    count += ub - lb + 1

print(count)