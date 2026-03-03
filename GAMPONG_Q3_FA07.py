names = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],  # Me
    [4000, 4100, 3900, 4200, 4600],  # Lia
    [6000, 5800, 5900, 6100, 6200]   # Jake
]


for i in range(len(steps)):
    print(f"\n{names[i]}'s daily steps: {steps[i]}")
    total = sum(steps[i])
    average = total / len(steps[i])
    print(f"Total steps: {total}")
    print(f"Average steps: {average:.2f}")


all_steps = [step for person in steps for step in person]
max_steps = max(all_steps)
min_steps = min(all_steps)
print(f"\nMaximum steps in dataset: {max_steps}")
print(f"Minimum steps in dataset: {min_steps}")

Using a 2D array made organizing and analyzing the step counts much easier because all the data was stored in a structured way
, with rows for each person and columns for each day.
Calculating totals and averages was straightforward using loops and built-in functions.
The easy part was using sum() and max()/min() to summarize the data.
The more challenging part was making sure to access the correct row and column while iterating.
