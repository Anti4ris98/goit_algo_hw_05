def binary_search_with_bounds(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2
        if arr[mid] == target:
            upper_bound = arr[mid]
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    # Якщо елемент не знайдено і верхня межа не встановлена, значить всі елементи менші за target
    if upper_bound is None and left >= len(arr):
        upper_bound = None  # Можна встановити специфічне значення або залишити None
    return (iterations, upper_bound)

arr = [1, 3, 5.5, 8, 10, 12, 15.5, 18, 20.5, 22, 24]
x = 15.5
result = binary_search_with_bounds(arr, x)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")