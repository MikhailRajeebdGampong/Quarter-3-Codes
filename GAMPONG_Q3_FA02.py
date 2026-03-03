#steps = [
    [4500, 5200, 4800, 5000, 5300],  
    [4000, 4100, 3900, 4200, 4600],  
    [6000, 5800, 5900, 6100, 6200]  
]

names = ["Me", "Lia", "Jake"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Display step counts
for i in range(len(steps)):
    print(f"\n{name s[i]}'s Steps:")
    total = 0
    for j in range(len(steps[i])):
        print(f"{days[j]}: {steps[i][j]} steps")
        total += steps[i][j]
    
    average = total / len(steps[i])
    print(f"Total steps: {total}")
    print(f"Average steps: {average:.2f}")
