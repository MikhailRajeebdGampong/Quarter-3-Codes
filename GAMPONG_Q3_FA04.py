names = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],  # Me
    [4000, 4100, 3900, 4200, 4600],  # Lia
    [6000, 5800, 5900, 6100, 6200]   # Jake
]

totals = []
for i in range(len(steps)):
    totals.append(sum(steps[i]))
    print(f"{names[i]} - Total Steps: {totals[i]}")

max_total = max(totals)
max_index = totals.index(max_total)
print(f"\nPerson with highest total steps: {names[max_index]} ({max_total} steps)")

min_total = min(totals)
difference = max_total - min_total
print(f"Difference between highest and lowest total steps: {difference}")
