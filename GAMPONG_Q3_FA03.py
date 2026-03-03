steps = [
    [4500, 5200, 4800, 5000, 5500],  # Friend 1
    [4000, 4100, 3900, 4200, 4600],  # Friend 2
    [6000, 5800, 5900, 6100, 6200]   # Friend 3
]

for i in range(len(steps)):
    total = sum(steps[i])
    average = total / len(steps[i])
    minimum = min(steps[i])
    maximum = max(steps[i])
    
    print(f"Friend {i+1} - Total Steps: {total} | "
          f"Average: {average:.1f} | "
          f"Min: {minimum} | "
          f"Max: {maximum}")

Using a 2D array made organizing and analyzing the step data easier and faster. It reduced repetitive code and allowed simple calculations using built-in functions.
Although working with the rows and columns took some getting used to, the overall process of summarizing the data was straightforward and efficient.
