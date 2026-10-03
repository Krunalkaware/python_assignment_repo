seconds = int(input("Enter time in seconds: "))

hours = seconds // 3600
remaining_seconds = seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print("Hours =", hours)
print("Minutes =", minutes)
print("Seconds =", seconds)
