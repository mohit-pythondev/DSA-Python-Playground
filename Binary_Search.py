def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2 # to avoid overflow replace mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

    """
    Time Complexity: O(log n)
    Space Complexity: O(1)
    Best Case: O(1)
    Worst Case: O(log n)
    
    """

try:
    arr = list(map(int, input("Enter the sorted array: ").split())) #eg: 2 4 6 8 10
    target = int(input("Enter the target element: ")) 
    result = binary_search(arr, target)
    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found.")
except ValueError:
    print("Invalid input. Please enter valid integers.")


