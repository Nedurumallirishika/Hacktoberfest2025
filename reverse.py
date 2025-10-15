# Reverse an array in Python
arr = [10, 20, 30, 40, 50]
print("Original array:", arr)

# Find length
n = len(arr)

# Reverse using loop
for i in range(n // 2):
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

print("Reversed array:", arr)
