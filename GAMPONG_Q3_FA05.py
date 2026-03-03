names = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],  # Me
    [4000, 4100, 3900, 4200, 4600],  # Lia
    [6000, 5800, 5900, 6100, 6200]   # Jake
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

daily_totals = []

for j in range(len(days)):
    total = steps[0][j] + steps[1][j] + steps[2][j]
    daily_totals.append(total)
    print(f"{days[j]} - Total Steps: {total}")

max_total = max(daily_totals)
max_index = daily_totals.index(max_total)
print(f"\nMost active day overall: {days[max_index]} ({max_total} steps)")
