# Bubble Sort Program

arr = [64, 34, 25, 12, 22, 11, 90]

n = len(arr)

# Bubble Sort
for i in range(n - 1):
    for j in range(n - i - 1):

        # Compare adjacent elements
        if arr[j] > arr[j + 1]:

            # Swap elements
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Display sorted array
print("Sorted Array:")
print(arr)