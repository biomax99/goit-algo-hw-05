def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0

    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # Якщо елемент не знайдений, повертаємо найближчу "верхню межу"
    if low < len(arr):
        return (iterations, arr[low])
    return (iterations, None)

# Приклад використання
arr = [1.2, 2.4, 3.5, 4.8, 5.6, 6.9]
result = binary_search(arr, 4.5)
print(result)
